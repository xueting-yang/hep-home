/* ===========================
   Xueting's HEP HOME — App
   =========================== */

// ──────────────────────────────────
// Header scroll effect
// ──────────────────────────────────

const header = document.getElementById('header');
window.addEventListener('scroll', () => {
  if (window.scrollY > 50) {
    header.classList.add('scrolled');
  } else {
    header.classList.remove('scrolled');
  }
});

// ──────────────────────────────────
// Utility
// ──────────────────────────────────

function escapeHtml(text) {
  if (!text) return '';
  const div = document.createElement('div');
  div.textContent = text;
  return div.innerHTML;
}

// ──────────────────────────────────
// Load projects from JSON
// ──────────────────────────────────

async function loadProjects() {
  const grid = document.querySelector('.grid');
  if (!grid) return;

  try {
    const resp = await fetch('./data/projects.json');
    if (!resp.ok) throw new Error('Failed to load projects');
    const projects = await resp.json();

    grid.innerHTML = projects.map(p => `
      <a href="${p.url}" class="card">
        <div class="card-header">
          <h3>${escapeHtml(p.title)}</h3>
          <span class="tag ${p.status}">${p.status === 'done' ? '已完成' : '进行中'}</span>
        </div>
        <p>${escapeHtml(p.description)}</p>
        <div class="card-footer">
          <span>${p.date}</span>
          <span class="card-link">查看</span>
        </div>
      </a>
    `).join('');
  } catch (e) {
    console.warn('Could not load projects:', e);
  }
}

// ──────────────────────────────────
// HEP-EX Paper Fetcher
// ──────────────────────────────────

const PROXIES = [
  url => `https://corsproxy.io/?${encodeURIComponent(url)}`,
  url => `https://api.allorigins.win/raw?url=${encodeURIComponent(url)}`,
  url => `https://api.codetabs.com/v1/proxy?quest=${encodeURIComponent(url)}`,
];

async function fetchWithProxy(url) {
  // Try direct first (works if served via http, not file://)
  try {
    const resp = await fetch(url);
    if (resp.ok) {
      const text = await resp.text();
      if (text && !text.includes('arxiv.org/api/errors')) return text;
    }
  } catch (_) {}

  // Try proxies
  for (const makeUrl of PROXIES) {
    try {
      const resp = await fetch(makeUrl(url));
      if (!resp.ok) continue;
      const text = await resp.text();
      if (!text || text.includes('arxiv.org/api/errors')) continue;
      return text;
    } catch (_) {}
  }
  return null;
}

function renderHepExCard({ title, authors, summary, published, arxivId, source, physics }) {
  const container = document.getElementById('hep-ex-card');
  if (!container || !arxivId) return;
  const pdfUrl = `https://arxiv.org/pdf/${arxivId}`;
  const sourceLabel = source === 'live' ? '今日精选' : '精选推荐';
  const physicsBlock = physics ? `
    <div class="hep-physics">
      <div class="hep-physics-item">
        <span class="hep-physics-label">🔭 物理问题</span>
        <p class="hep-physics-text">${escapeHtml(physics.question)}</p>
      </div>
      <div class="hep-physics-item">
        <span class="hep-physics-label">📊 核心成果</span>
        <p class="hep-physics-text">${escapeHtml(physics.result)}</p>
      </div>
      <div class="hep-physics-item">
        <span class="hep-physics-label">💡 重要意义</span>
        <p class="hep-physics-text">${escapeHtml(physics.significance)}</p>
      </div>
      ${physics.category ? `<span class="hep-category">${escapeHtml(physics.category)}</span>` : ''}
    </div>
  ` : '';

  const titleHtml = `<a href="${pdfUrl}" target="_blank" class="hep-title-link">${escapeHtml(title)}</a>`;
  container.outerHTML = `
    <div class="hep-ex-container">
      <div class="hep-ex-card">
        <div class="hep-ex-card-header">
          <div class="hep-ex-title-row">
            <h3 class="hep-ex-title">${titleHtml}</h3>
            <span class="hep-ex-badge">${sourceLabel} · ${published}</span>
          </div>
          <p class="hep-ex-authors">${escapeHtml(authors)} · <a href="https://arxiv.org/abs/${arxivId}" target="_blank" class="hep-arxiv-link">arXiv:${arxivId}</a></p>
        </div>
        ${physicsBlock}
        <div class="hep-ex-footer">
          <span class="hep-abstract-label">摘要</span>
          <span><a href="${pdfUrl}" target="_blank" class="hep-ex-link">阅读PDF →</a></span>
        </div>
        <p class="hep-ex-abstract">${escapeHtml(summary)}</p>
      </div>
    </div>
  `;
}

function showOfflineCard(err) {
  const container = document.getElementById('hep-ex-card');
  if (!container) return;
  const msg = err ? `加载失败: ${err.message}` : '暂无论文数据';
  container.outerHTML = `
    <div class="hep-ex-offline" style="max-width:780px;margin:0 auto;">
      <p>${msg}</p>
      <p style="margin-top:0.5rem;font-size:0.8rem;">
        <a href="https://arxiv.org/list/hep-ex/recent" target="_blank">访问 arXiv hep-ex 最近更新 →</a>
      </p>
    </div>
  `;
}

function parseXmlEntries(text) {
  const parser = new DOMParser();
  const xml = parser.parseFromString(text, 'text/xml');
  return Array.from(xml.querySelectorAll('entry')).map(entry => {
    const rawId = entry.querySelector('id')?.textContent || '';
    const arxivId = rawId.includes('arxiv.org')
      ? rawId.split('/').pop().replace('v1', '')
      : rawId.replace('arxiv:', '');
    return {
      title: entry.querySelector('title')?.textContent?.replace(/\s+/g, ' ').trim() || '',
      authors: Array.from(entry.querySelectorAll('author name')).slice(0, 5).map(n => n.textContent).join(', '),
      authorCount: entry.querySelectorAll('author name').length,
      summary: entry.querySelector('summary')?.textContent?.replace(/\s+/g, ' ').trim() || '',
      published: entry.querySelector('published')?.textContent?.slice(0, 10) || '',
      arxivId,
    };
  }).filter(e => e.arxivId && !e.arxivId.includes('errors') && e.title);
}

async function fetchLivePaper() {
  // Live fetch from arXiv - try multiple approaches
  const today = new Date();
  const dateStr = today.toISOString().split('T')[0];
  const yesterday = new Date(today);
  yesterday.setDate(yesterday.getDate() - 1);
  const dateFrom = yesterday.toISOString().split('T')[0];

  const sq = `cat:hep-ex+AND+submittedDate:[${dateFrom}+TO+${dateStr}]`;
  const encodedSq = sq
    .replace(/%/g, '%25')
    .replace(/:/g, '%3A')
    .replace(/\[/g, '%5B')
    .replace(/\]/g, '%5D');
  const apiUrl = `https://export.arxiv.org/api/query?search_query=${encodedSq}&sortBy=submittedDate&sortOrder=descending&max_results=30`;

  // Try direct fetch first
  try {
    const resp = await fetch(apiUrl);
    if (resp.ok) {
      const text = await resp.text();
      if (text && !text.includes('arxiv.org/api/errors')) {
        const entries = parseXmlEntries(text);
        if (entries.length > 0) {
          const idx = Math.floor(Math.random() * Math.min(entries.length, 10));
          const e = entries[idx];
          return {
            title: e.title,
            authors: e.authors + (e.authorCount > 5 ? ' et al.' : ''),
            summary: e.summary,
            published: e.published,
            arxivId: e.arxivId,
            source: 'live',
          };
        }
      }
    }
  } catch (_) {}

  // Try proxy
  const text = await fetchWithProxy(apiUrl);
  if (!text) return null;

  const entries = parseXmlEntries(text);
  if (entries.length === 0) return null;

  const idx = Math.floor(Math.random() * Math.min(entries.length, 10));
  const e = entries[idx];
  return {
    title: e.title,
    authors: e.authors + (e.authorCount > 5 ? ' et al.' : ''),
    summary: e.summary,
    published: e.published,
    arxivId: e.arxivId,
    source: 'live',
  };
}

async function fetchFromPapersJson() {
  try {
    const resp = await fetch('./data/papers.json');
    if (!resp.ok) throw new Error(`HTTP ${resp.status}`);
    const papers = await resp.json();
    if (!Array.isArray(papers) || papers.length === 0) throw new Error('Empty papers list');
    const idx = Math.floor(Math.random() * papers.length);
    const p = papers[idx];
    return {
      title: p.title,
      authors: p.authors,
      summary: p.summary,
      published: p.published,
      arxivId: p.arxivId,
      source: 'static',
      physics: p.physics || null,
    };
  } catch (e) {
    console.error('Failed to load papers.json:', e);
    return null;
  }
}

async function fetchHepExPaper() {
  // Try local papers first (always works when site is deployed)
  const local = await fetchFromPapersJson();
  if (local) {
    renderHepExCard(local);
    return;
  }

  // Fallback: try live arXiv (best-effort, may fail due to CORS)
  const live = await fetchLivePaper().catch(e => ({ error: e }));
  if (live && !live.error) {
    renderHepExCard(live);
    return;
  }

  showOfflineCard(live?.error);
}

// ──────────────────────────────────
// Init
// ──────────────────────────────────

document.addEventListener('DOMContentLoaded', () => {
  loadProjects();
  fetchHepExPaper();
});
