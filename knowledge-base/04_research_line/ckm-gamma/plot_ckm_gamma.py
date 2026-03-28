import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Data points
measurements = [
    {
        'year': 2013, 'value': 69.0, 'err_plus': 17.0, 'err_minus': 16.0,
        'experiment': 'BaBar', 'label': 'BaBar legacy combination',
        'category': 'legacy_combination'
    },
    {
        'year': 2024, 'value': 66.5, 'err_plus': 2.8, 'err_minus': 2.9,
        'experiment': 'LHCb', 'label': 'LHCb-quoted world average',
        'category': 'world_average_reference'
    },
    {
        'year': 2024, 'value': 75.2, 'err_plus': 7.6, 'err_minus': 7.6,
        'experiment': 'Belle+Belle II', 'label': 'Belle + Belle II combination',
        'category': 'combined_result'
    },
    {
        'year': 2025, 'value': 66.4, 'err_plus': 2.7, 'err_minus': 2.8,
        'experiment': 'HFLAV', 'label': 'HFLAV Summer 2025',
        'category': 'world_average'
    },
]

milestones = [
    {'year': 1991, 'title': 'GLW method proposed', 'type': 'theory_method'},
    {'year': 1997, 'title': 'ADS method proposed', 'type': 'theory_method'},
    {'year': 2002, 'title': 'Bondar Dalitz-based method', 'type': 'theory_method'},
    {'year': 2003, 'title': 'GGSZ formalism', 'type': 'theory_method'},
    {'year': 2009, 'title': 'CLEO-c strong-phase inputs', 'type': 'external_input'},
    {'year': 2020, 'title': 'BESIII improved inputs', 'type': 'external_input'},
]

# Set up figure with two rows
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[2, 1],
                                 sharex=True, gridspec_kw={'hspace': 0.08})

# ============ Top panel: Measurements ============
# Style definitions
category_styles = {
    'legacy_combination': {'marker': 's', 'color': '#1f77b4', 'markersize': 8, 'label': 'B factory (legacy)'},
    'combined_result': {'marker': 's', 'color': '#ff7f0e', 'markersize': 8, 'label': 'B factory (combined)'},
    'world_average_reference': {'marker': 'D', 'color': '#2ca02c', 'markersize': 8, 'label': 'LHCb-quoted WA'},
    'world_average': {'marker': 'D', 'color': '#d62728', 'markersize': 9, 'label': 'HFLAV world average'},
}

for m in measurements:
    style = category_styles[m['category']]
    ax1.errorbar(m['year'], m['value'],
                 yerr=[[m['err_minus']], [m['err_plus']]],
                 fmt=style['marker'], color=style['color'],
                 markersize=style['markersize'],
                 capsize=4, capthick=1.2, elinewidth=1.2,
                 markeredgecolor='white', markeredgewidth=0.5)

    # Annotation: experiment name and value
    offset_x = 0.3
    offset_y = m['err_plus'] + 0.8
    if m['category'] in ['world_average_reference', 'world_average']:
        offset_y = m['err_plus'] + 1.2

    ax1.annotate(f"{m['experiment']}\n${m['value']:.1f}^{{{m['err_plus']:+.1f}}}_{{{m['err_minus']:+.1f}}}$°",
                 xy=(m['year'], m['value']),
                 xytext=(m['year'] + offset_x, m['value'] + offset_y),
                 fontsize=8, ha='left', va='bottom',
                 bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor='gray', alpha=0.8))

ax1.set_ylabel(r'$\gamma$ / $\phi_3$ [deg]', fontsize=12)
ax1.set_ylim(30, 115)
ax1.set_xlim(1988, 2027)
ax1.grid(True, linestyle='--', alpha=0.4)

# Create legend from category styles
legend_handles = [
    plt.Line2D([0], [0], marker=category_styles[cat]['marker'], color='w',
                markerfacecolor=category_styles[cat]['color'], markersize=8,
                label=category_styles[cat]['label'])
    for cat in ['legacy_combination', 'combined_result', 'world_average_reference', 'world_average']
]
ax1.legend(handles=legend_handles, loc='upper left', fontsize=9, framealpha=0.9, ncol=2)

# ============ Bottom panel: Milestones ============
milestone_styles = {
    'theory_method': {'color': '#9467bd', 'marker': '|', 'label': 'Theory method'},
    'external_input': {'color': '#8c564b', 'marker': '|', 'label': 'External input (charm factory)'},
}

y_milestone = {'theory_method': 0.7, 'external_input': 0.3}

for ms in milestones:
    style = milestone_styles[ms['type']]
    ax2.scatter(ms['year'], y_milestone[ms['type']],
                marker=style['marker'], s=200, color=style['color'],
                zorder=5, linewidths=2)
    ax2.annotate(ms['title'], xy=(ms['year'], y_milestone[ms['type']]),
                 xytext=(0, 15), textcoords='offset points',
                 fontsize=7.5, ha='center', va='bottom', rotation=0,
                 bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor=style['color'], alpha=0.85))

ax2.set_ylim(0, 1)
ax2.set_yticks([])
ax2.set_xlabel('Year', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.3, axis='x')

# Milestone legend
legend_patches = [
    mpatches.Patch(color='#9467bd', label='Theory method proposal'),
    mpatches.Patch(color='#8c564b', label='Charm-factory input'),
]
ax2.legend(handles=legend_patches, loc='upper right', fontsize=8, framealpha=0.9)

# Shared title
fig.suptitle(r'CKM Angle $\gamma$ / $\phi_3$ Measurements and Method Development', fontsize=14, fontweight='bold', y=0.98)

plt.subplots_adjust(top=0.93, hspace=0.08)

# Export
output_path = '/Users/xueting/Claude/CKM-Gamma/ckm_gamma_measurements'
plt.savefig(output_path + '.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.savefig(output_path + '.pdf', bbox_inches='tight', facecolor='white')
print(f"Saved: {output_path}.png and {output_path}.pdf")

plt.show()
