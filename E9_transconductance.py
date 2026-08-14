import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the ID-VGS sweep data
df = pd.read_csv("E9_mosfet_transfer.csv")

# Create two plots side by side
fig, ax = plt.subplots(1, 2, figsize=(11, 4.5))

# Process each VDS value
for v_ds, group in df.groupby("V_DS (V)"):

    # Sort the data by VGS
    group = group.sort_values("V_GS (V)")

    v_gs = group["V_GS (V)"]
    i_d = group["I_D (mA)"]

    # Calculate transconductance
    gm = np.gradient(i_d, v_gs)

    # ID-VGS plot
    ax[0].plot(
        v_gs,
        i_d,
        marker="o",
        linewidth=2,
        label=f"$V_{{DS}}$ = {v_ds} V"
    )

    # gm-VGS plot
    ax[1].plot(
        v_gs,
        gm,
        marker="s",
        linewidth=2,
        label=f"$V_{{DS}}$ = {v_ds} V"
    )

    # Find peak gm
    peak_index = np.argmax(gm)
    peak_gm = gm[peak_index]
    peak_vgs = v_gs.iloc[peak_index]

    # Mark peak gm
    ax[1].plot(
        peak_vgs,
        peak_gm,
        marker="o",
        markersize=8
    )

    # Mark VGS and peak gm on graph
    ax[1].annotate(
        f"Peak gm = {peak_gm:.2f} mS\nVGS = {peak_vgs:.2f} V",
        xy=(peak_vgs, peak_gm),
        xytext=(10, 10),
        textcoords="offset points"
    )

    # Print result in terminal
    print(f"V_DS = {v_ds} V")
    print(f"Peak gm = {peak_gm:.3f} mS")
    print(f"V_GS at peak gm = {peak_vgs:.3f} V")
    print()

# ID-VGS graph
ax[0].set_title("Transfer Characteristics")
ax[0].set_xlabel("$V_{GS}$ (V)")
ax[0].set_ylabel("$I_D$ (mA)")
ax[0].grid(True, linestyle="--", alpha=0.6)
ax[0].legend()

# gm-VGS graph
ax[1].set_title("Transconductance")
ax[1].set_xlabel("$V_{GS}$ (V)")
ax[1].set_ylabel("$g_m$ (mS)")
ax[1].grid(True, linestyle="--", alpha=0.6)
ax[1].legend()

plt.tight_layout()

# Save E9 result
plt.savefig("E9_gm_vgs.png", dpi=300)

plt.show()
