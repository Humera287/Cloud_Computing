import matplotlib.pyplot as plt
import numpy as np
import os

# Create output directory
os.makedirs('images', exist_ok=True)

# Set style
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
fig_dpi = 300

# Hypervisor names
hypervisors = [
    'Proxmox VE\n(Type-1 Bare-Metal)',
    'VMware Workstation\n(Type-2 Hosted)'
]

# -------------------------------------------------------------------------
# Latest Experimental Results
# -------------------------------------------------------------------------

# Events Per Second
eps_values = [1716.69, 684.51]

# Total Events
events_values = [17169, 6846]

# Latency values
proxmox_lat = [0.57, 0.58, 0.65, 2.78]
vmware_lat = [1.31, 1.46, 1.58, 6.16]

# Average and 95th percentile latency
avg_lats = [0.58, 1.46]
p95_lats = [0.65, 1.58]

# Percentage improvement
pct_diff = ((1716.69 - 684.51) / 684.51) * 100

# Event difference
diff_events = 17169 - 6846


# -------------------------------------------------------------------------
# Plot 1: Events Per Second (Throughput)
# -------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 6), dpi=fig_dpi)

bars = ax.bar(
    hypervisors,
    eps_values,
    color=['#0052cc', '#e65100'],
    width=0.45,
    edgecolor='black',
    linewidth=1.2
)

ax.set_ylabel(
    'Events per Second (EPS)',
    fontsize=12,
    fontweight='bold'
)

ax.set_title(
    'CPU Throughput Comparison (Sysbench 20k Primes)',
    fontsize=14,
    fontweight='bold',
    pad=15
)

ax.set_ylim(0, 2100)

for bar in bars:
    height = bar.get_height()

    ax.annotate(
        f'{height:,.2f} eps',
        xy=(bar.get_x() + bar.get_width() / 2, height),
        xytext=(0, 6),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontsize=11,
        fontweight='bold'
    )

# Percentage annotation
ax.text(
    0.5,
    0.85,
    f'Proxmox VE is +{pct_diff:.2f}% higher\nin CPU Throughput',
    transform=ax.transAxes,
    fontsize=12,
    fontweight='bold',
    ha='center',
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor='#e8f4f8',
        edgecolor='#0052cc',
        alpha=0.9
    )
)

plt.tight_layout()

plt.savefig(
    'images/events_per_second_comparison.png',
    dpi=fig_dpi,
    bbox_inches='tight'
)

plt.close()


# -------------------------------------------------------------------------
# Plot 2: Latency Comparison
# -------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 6), dpi=fig_dpi)

metrics = [
    'Minimum Latency',
    'Average Latency',
    '95th Percentile',
    'Maximum Latency'
]

x = np.arange(len(metrics))
width = 0.35

rects1 = ax.bar(
    x - width / 2,
    proxmox_lat,
    width,
    label='Proxmox VE (Type-1)',
    color='#0052cc',
    edgecolor='black',
    linewidth=1
)

rects2 = ax.bar(
    x + width / 2,
    vmware_lat,
    width,
    label='VMware Workstation (Type-2)',
    color='#e65100',
    edgecolor='black',
    linewidth=1
)

ax.set_ylabel(
    'Latency (milliseconds)',
    fontsize=12,
    fontweight='bold'
)

ax.set_title(
    'Sysbench CPU Latency Metrics Comparison (Lower is Better)',
    fontsize=14,
    fontweight='bold',
    pad=15
)

ax.set_xticks(x)
ax.set_xticklabels(
    metrics,
    fontsize=11,
    fontweight='bold'
)

ax.legend(
    fontsize=11,
    loc='upper left'
)

ax.set_ylim(0, 7.0)

# Proxmox labels
for rect in rects1:

    h = rect.get_height()

    ax.annotate(
        f'{h:.2f} ms',
        xy=(
            rect.get_x() + rect.get_width() / 2,
            h
        ),
        xytext=(0, 4),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold',
        color='#003399'
    )

# VMware labels
for rect in rects2:

    h = rect.get_height()

    ax.annotate(
        f'{h:.2f} ms',
        xy=(
            rect.get_x() + rect.get_width() / 2,
            h
        ),
        xytext=(0, 4),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontsize=9,
        fontweight='bold',
        color='#b33c00'
    )

plt.tight_layout()

plt.savefig(
    'images/latency_comparison.png',
    dpi=fig_dpi,
    bbox_inches='tight'
)

plt.close()


# -------------------------------------------------------------------------
# Plot 3: Total Events Comparison
# -------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(8, 6), dpi=fig_dpi)

bars = ax.bar(
    hypervisors,
    events_values,
    color=['#0052cc', '#e65100'],
    width=0.45,
    edgecolor='black',
    linewidth=1.2
)

ax.set_ylabel(
    'Total Events Processed (in 10 seconds)',
    fontsize=12,
    fontweight='bold'
)

ax.set_title(
    'Total Sysbench Prime Calculation Events',
    fontsize=14,
    fontweight='bold',
    pad=15
)

ax.set_ylim(0, 21000)

for bar in bars:

    height = bar.get_height()

    ax.annotate(
        f'{height:,.0f} events',
        xy=(
            bar.get_x() + bar.get_width() / 2,
            height
        ),
        xytext=(0, 6),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontsize=11,
        fontweight='bold'
    )

ax.text(
    0.5,
    0.85,
    f'Proxmox VE processed +{diff_events:,} more events\n'
    f'({pct_diff:.2f}% higher throughput)',
    transform=ax.transAxes,
    fontsize=12,
    fontweight='bold',
    ha='center',
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor='#e8f4f8',
        edgecolor='#0052cc',
        alpha=0.9
    )
)

plt.tight_layout()

plt.savefig(
    'images/total_events_comparison.png',
    dpi=fig_dpi,
    bbox_inches='tight'
)

plt.close()


# -------------------------------------------------------------------------
# Plot 4: Comprehensive Performance Dashboard
# -------------------------------------------------------------------------

fig, axs = plt.subplots(
    2,
    2,
    figsize=(14, 10),
    dpi=fig_dpi
)

fig.suptitle(
    'Performance Analysis Dashboard: '
    'Type-1 (Proxmox VE) vs Type-2 (VMware Workstation)',
    fontsize=16,
    fontweight='bold',
    y=0.98
)


# -------------------------------------------------------------------------
# Subplot 1: EPS
# -------------------------------------------------------------------------

axs[0, 0].bar(
    hypervisors,
    eps_values,
    color=['#0052cc', '#e65100'],
    width=0.4,
    edgecolor='black'
)

axs[0, 0].set_title(
    'Events per Second (Higher is Better)',
    fontsize=12,
    fontweight='bold'
)

axs[0, 0].set_ylabel(
    'Events / sec',
    fontsize=10
)

axs[0, 0].set_ylim(0, 2000)

for bar in axs[0, 0].patches:

    axs[0, 0].annotate(
        f'{bar.get_height():,.2f}',
        (
            bar.get_x() + bar.get_width() / 2,
            bar.get_height()
        ),
        xytext=(0, 4),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontweight='bold'
    )


# -------------------------------------------------------------------------
# Subplot 2: Total Events
# -------------------------------------------------------------------------

axs[0, 1].bar(
    hypervisors,
    events_values,
    color=['#0052cc', '#e65100'],
    width=0.4,
    edgecolor='black'
)

axs[0, 1].set_title(
    'Total Events in 10s (Higher is Better)',
    fontsize=12,
    fontweight='bold'
)

axs[0, 1].set_ylabel(
    'Total Events',
    fontsize=10
)

axs[0, 1].set_ylim(0, 20000)

for bar in axs[0, 1].patches:

    axs[0, 1].annotate(
        f'{int(bar.get_height()):,}',
        (
            bar.get_x() + bar.get_width() / 2,
            bar.get_height()
        ),
        xytext=(0, 4),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontweight='bold'
    )


# -------------------------------------------------------------------------
# Subplot 3: Average Latency
# -------------------------------------------------------------------------

axs[1, 0].bar(
    hypervisors,
    avg_lats,
    color=['#0052cc', '#e65100'],
    width=0.4,
    edgecolor='black'
)

axs[1, 0].set_title(
    'Average Latency (Lower is Better)',
    fontsize=12,
    fontweight='bold'
)

axs[1, 0].set_ylabel(
    'Latency (ms)',
    fontsize=10
)

axs[1, 0].set_ylim(0, 1.8)

for bar in axs[1, 0].patches:

    axs[1, 0].annotate(
        f'{bar.get_height():.2f} ms',
        (
            bar.get_x() + bar.get_width() / 2,
            bar.get_height()
        ),
        xytext=(0, 4),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontweight='bold'
    )


# -------------------------------------------------------------------------
# Subplot 4: 95th Percentile Latency
# -------------------------------------------------------------------------

axs[1, 1].bar(
    hypervisors,
    p95_lats,
    color=['#0052cc', '#e65100'],
    width=0.4,
    edgecolor='black'
)

axs[1, 1].set_title(
    '95th Percentile Latency (Lower is Better)',
    fontsize=12,
    fontweight='bold'
)

axs[1, 1].set_ylabel(
    'Latency (ms)',
    fontsize=10
)

axs[1, 1].set_ylim(0, 2.0)

for bar in axs[1, 1].patches:

    axs[1, 1].annotate(
        f'{bar.get_height():.2f} ms',
        (
            bar.get_x() + bar.get_width() / 2,
            bar.get_height()
        ),
        xytext=(0, 4),
        textcoords="offset points",
        ha='center',
        va='bottom',
        fontweight='bold'
    )


plt.tight_layout(
    rect=[0, 0, 1, 0.95]
)

plt.savefig(
    'images/overall_performance_dashboard.png',
    dpi=fig_dpi,
    bbox_inches='tight'
)

plt.close()


print('All plots generated successfully in images/ folder.')
print()
print('Latest experimental values used:')
print('Proxmox VE    : 1716.69 EPS, 17169 events')
print('VMware        : 684.51 EPS, 6846 events')
print('Proxmox Avg   : 0.58 ms')
print('VMware Avg    : 1.46 ms')
print('Proxmox 95th  : 0.65 ms')
print('VMware 95th   : 1.58 ms')
print('Proxmox Max   : 2.78 ms')
print('VMware Max    : 6.16 ms')
