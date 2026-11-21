"""Render the design comparison from the two executable Paper B fixtures."""

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

from ocp_batch_ownership_case import run
from ocp_case import check_cases


legacy = {(r["design"], r["demand"]): len(r["changed_protected_paths"]) for r in check_cases()}
batch = {(r["layout"], r["placement_rule"]): len(r["changed_existing_files"]) for r in run()}

plt.rcParams.update({"font.family": "DejaVu Sans", "svg.fonttype": "none", "font.size": 10})
fig, axes = plt.subplots(1, 2, figsize=(9.2, 3.65), sharey=True)
fig.subplots_adjust(left=.095, right=.985, bottom=.205, top=.75, wspace=.25)
colors = ("#236379", "#ab541b")
layouts = ("dispatch", "methods")
labels = ("Operation files", "Shape files")
panels = (
    ("A  Different requests", legacy, ("triangle", "label"), ("Add a triangle", "Add a labeling\noperation")),
    ("B  Same batch request", batch, ("layout_ownership", "shared_adapter"), ("Keep ownership\nby layout", "Allow a shared\nadapter")),
)
for ax, (title, data, columns, captions) in zip(axes, panels):
    ax.set_title(title, loc="left", fontweight="bold", pad=9)
    for j, (color, layout, label) in enumerate(zip(colors, layouts, labels)):
        slots = [i + (-.17 if j == 0 else .17) for i in range(len(columns))]
        values = [data[layout, col] for col in columns]
        bars = ax.bar(slots, values, width=.29, color=color, label=label, zorder=3)
        ax.bar_label(bars, padding=4, color=color, fontweight="bold")
    ax.set_xticks(range(len(columns)), captions)
    ax.set_ylim(0, 2.45)
    ax.set_xlim(-.47, 1.47)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(axis="y", color="#d4dde3", linewidth=.8, zorder=0)
    ax.spines[["top", "right", "left"]].set_visible(False)
    ax.spines["bottom"].set_color("#a9b5bc")
    ax.tick_params(axis="both", length=0, pad=6)

axes[0].set_ylabel("Existing source files changed", labelpad=10)
handles, legend_labels = axes[0].get_legend_handles_labels()
fig.legend(handles, legend_labels, loc="upper right", bbox_to_anchor=(.993, .988), frameon=False, ncol=2)
fig.text(.095, .952, "Existing-file edits across two layouts", fontsize=14, fontweight="bold", va="top")
fig.text(.095, .052, "Published fixture candidates. Each batch candidate adds one new file and passes the same behavior checks.", fontsize=8, color="#3d515c")

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("output_directory", type=Path)
out = parser.parse_args().output_directory
out.mkdir(parents=True, exist_ok=True)
for extension in ("png", "svg"):
    fig.savefig(out / f"Paper_B_Figure_1_Edit_Boundaries.{extension}", dpi=250, facecolor="white")
