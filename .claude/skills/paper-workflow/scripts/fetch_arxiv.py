#!/usr/bin/env python3
"""
Fetch recent papers from arXiv API with retry and rate limiting
"""
import sys
import json
import time
import urllib.request
import urllib.parse
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET

def fetch_arxiv(category, days=7, max_results=100, retry=3):
    """Fetch papers from arXiv with retry mechanism"""
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days)

    date_from = start_date.strftime('%Y%m%d')
    date_to = end_date.strftime('%Y%m%d')

    query = f'cat:{category} AND submittedDate:[{date_from}0000 TO {date_to}2359]'
    params = {
        'search_query': query,
        'sortBy': 'submittedDate',
        'sortOrder': 'descending',
        'max_results': str(max_results)
    }

    url = f"https://export.arxiv.org/api/query?{urllib.parse.urlencode(params)}"

    for attempt in range(retry):
        try:
            # Add User-Agent to avoid blocking
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (compatible; PaperWorkflow/1.0)'
            })

            with urllib.request.urlopen(req, timeout=30) as response:
                xml_data = response.read().decode('utf-8')

            root = ET.fromstring(xml_data)
            ns = {'atom': 'http://www.w3.org/2005/Atom'}

            papers = []
            for entry in root.findall('atom:entry', ns):
                arxiv_id = entry.find('atom:id', ns).text.split('/')[-1].split('v')[0]
                title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
                summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
                published = entry.find('atom:published', ns).text[:10]

                authors = [a.find('atom:name', ns).text for a in entry.findall('atom:author', ns)]
                author_str = ', '.join(authors[:3])
                if len(authors) > 3:
                    author_str += ' et al.'

                papers.append({
                    'arxivId': arxiv_id,
                    'title': title,
                    'authors': author_str,
                    'summary': summary,
                    'published': published,
                    'category': category
                })

            # Respect rate limit: wait 3 seconds before next request
            if attempt < retry - 1:
                time.sleep(3)

            return papers

        except urllib.error.HTTPError as e:
            if e.code == 503:
                wait_time = (attempt + 1) * 5  # Exponential backoff
                print(f"503 error, retrying in {wait_time}s... (attempt {attempt + 1}/{retry})", file=sys.stderr)
                time.sleep(wait_time)
            else:
                print(f"HTTP Error {e.code}: {e.reason}", file=sys.stderr)
                if attempt == retry - 1:
                    return []
        except Exception as e:
            print(f"Error fetching {category} (attempt {attempt + 1}/{retry}): {e}", file=sys.stderr)
            if attempt < retry - 1:
                time.sleep(3)
            else:
                return []

    return []

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--category', default='hep-ex')
    parser.add_argument('--days', type=int, default=7)
    parser.add_argument('--max-results', type=int, default=100)
    parser.add_argument('--retry', type=int, default=3)
    args = parser.parse_args()

    papers = fetch_arxiv(args.category, args.days, args.max_results, args.retry)
    print(json.dumps(papers, indent=2, ensure_ascii=False))
