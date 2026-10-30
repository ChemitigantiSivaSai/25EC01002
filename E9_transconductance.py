import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the ID-VGS sweep data
df = pd.read_csv("E9_mosfet_transfer.csv")

# Create two plots side by side
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

# Where to put each peak label, so labels do not overlap
label_pos = {0.1: (5.2, 1.0), 1.0: (5.2, 2.9), 3.0: (5.2, 6.2), 5.0: (2.4, 13.2)}  # data coords, free areas

for v_ds, group in df.groupby("V_DS (V)"):
    group = group.sort_values("V_GS (V)")
    v_gs = group["V_GS (V)"].to_numpy()
    i_d = group["I_D (mA)"].to_numpy()

    # Transconductance: g_m = dI_D/dV_GS  (mA/V = mS)
    gm = np.gradient(i_d, v_gs)

    (line,) = ax[0].plot(v_gs, i_d, marker="o", linewidth=2,
                         label=f"$V_{{DS}}$ = {v_ds} V")
    ax[1].plot(v_gs, gm, marker="s", linewidth=2, color=line.get_color(),
               label=f"$V_{{DS}}$ = {v_ds} V")

    # Peak g_m: FIRST point within 0.1 % of the maximum, so a flat plateau
    # (linear region) reports where it starts rather than a rounding-noise winner.
    peak_index = np.flatnonzero(np.isclose(gm, gm.max(), rtol=1e-3))[0]
    peak_gm, peak_vgs = gm[peak_index], v_gs[peak_index]

    ax[1].plot(peak_vgs, peak_gm, marker="o", markersize=9, color=line.get_color(),
               markeredgecolor="k", zorder=5)
    ax[1].annotate(
        f"$V_{{DS}}$={v_ds} V\npeak {peak_gm:.2f} mS at $V_{{GS}}$={peak_vgs:.1f} V",
        xy=(peak_vgs, peak_gm), xytext=label_pos.get(v_ds, (peak_vgs, peak_gm)),
        textcoords="data", fontsize=8, color=line.get_color(), va="center", ha="left" if v_ds == 5.0 else "right",
        arrowprops=dict(arrowstyle="-", color=line.get_color()),
    )

    print(f"V_DS = {v_ds} V")
    print(f"Peak gm = {peak_gm:.3f} mS")
    print(f"V_GS at peak gm = {peak_vgs:.3f} V")
    print()

ax[0].set_title("Transfer Characteristics")
ax[0].set_xlabel("$V_{GS}$ (V)")
ax[0].set_ylabel("$I_D$ (mA)")
ax[0].grid(True, linestyle="--", alpha=0.6)
ax[0].legend()

ax[1].set_title("Transconductance $g_m = dI_D/dV_{GS}$")
ax[1].set_xlabel("$V_{GS}$ (V)")
ax[1].set_ylabel("$g_m$ (mS)")
ax[1].set_ylim(-0.5, 15)
ax[1].grid(True, linestyle="--", alpha=0.6)
ax[1].legend(loc="upper left")

plt.tight_layout()
plt.savefig("E9_gm_vgs.png", dpi=300)
plt.show()
