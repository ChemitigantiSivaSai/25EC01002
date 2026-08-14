import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the ID-VGS sweep data
df = pd.read_csv("E9_mosfet_transfer.csv")

# Create plot
fig, ax = plt.subplots(figsize=(8, 5))

# Process each VDS value
for v_ds, group in df.groupby("V_DS (V)"):

    # Sort data by VGS
    group = group.sort_values("V_GS (V)")

    v_gs = group["V_GS (V)"].to_numpy()
    i_d = group["I_D (mA)"].to_numpy()

    # Select the approximately linear region
    linear = (v_gs >= 2.5) & (v_gs <= 5.0)

    v_gs_linear = v_gs[linear]
    i_d_linear = i_d[linear]

    # Linear fit: ID = m*VGS + c
    m, c = np.polyfit(v_gs_linear, i_d_linear, 1)

    # Threshold voltage from x-intercept
    v_t = -c / m

    # Generate extrapolated line
    v_gs_fit = np.linspace(v_t, 5.0, 100)
    i_d_fit = m * v_gs_fit + c

    # Plot original ID-VGS data
    ax.plot(
        v_gs,
        i_d,
        marker="o",
        linewidth=2,
        label=f"$V_{{DS}}$ = {v_ds} V"
    )

    # Plot linear extrapolation
    ax.plot(
        v_gs_fit,
        i_d_fit,
        "--",
        linewidth=2
    )

    # Mark threshold voltage
    ax.plot(
        v_t,
        0,
        marker="x",
        markersize=10,
        markeredgewidth=2
    )

    # Print result
    print(f"V_DS = {v_ds} V")
    print(f"Slope = {m:.3f} mA/V")
    print(f"Intercept = {c:.3f} mA")
    print(f"Estimated V_T = {v_t:.3f} V")
    print()

# Graph formatting
ax.set_title("Threshold Voltage Extraction")
ax.set_xlabel("$V_{GS}$ (V)")
ax.set_ylabel("$I_D$ (mA)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()

plt.tight_layout()

# Save E10 result
plt.savefig("E10_threshold.png", dpi=300)

plt.show()
