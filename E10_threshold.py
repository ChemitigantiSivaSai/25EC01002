import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the ID-VGS sweep data
df = pd.read_csv("E9_mosfet_transfer.csv")

fig, ax = plt.subplots(figsize=(8, 5))

# The linear-extrapolation method is valid in the LINEAR region (small V_DS).
# There, the x-intercept of the fitted line equals V_T + V_DS/2.
# V_DS = 3 V and 5 V are in saturation for most of the sweep (ID is quadratic),
# so no straight line is fitted on the plot for them and they are not used for V_T.
LINEAR_VDS = [0.1, 1.0]

vt_values = []

for v_ds, group in df.groupby("V_DS (V)"):
    group = group.sort_values("V_GS (V)")
    v_gs = group["V_GS (V)"].to_numpy()
    i_d = group["I_D (mA)"].to_numpy()

    # Fit window: strong inversion and still in the linear region (V_GS - V_T > V_DS)
    window = (v_gs >= 2.5) & (v_gs <= 5.0)
    m, c = np.polyfit(v_gs[window], i_d[window], 1)   # ID = m*VGS + c
    v_intercept = -c / m                              # x-intercept of the fitted line
    linear = v_ds in LINEAR_VDS

    # Data curve (colour is reused for this curve's fit line and marker)
    (line,) = ax.plot(v_gs, i_d, marker="o", linewidth=2,
                      label=f"$V_{{DS}}$ = {v_ds} V" + ("" if linear else " (saturation, not used)"))
    colour = line.get_color()

    print(f"V_DS = {v_ds} V")
    print(f"Slope = {m:.3f} mA/V")
    print(f"Intercept = {c:.3f} mA")
    print(f"x-intercept = {v_intercept:.3f} V")

    if linear:
        v_t = v_intercept - v_ds / 2
        vt_values.append(v_t)
        print(f"V_T = x-intercept - V_DS/2 = {v_t:.3f} V   (linear region: used)")

        # Extrapolated fit line down to I_D = 0, same colour as the data
        v_fit = np.linspace(v_intercept, 5.0, 100)
        ax.plot(v_fit, m * v_fit + c, "--", linewidth=1.5, color=colour)
        ax.plot(v_intercept, 0, marker="x", markersize=10,
                markeredgewidth=2, color=colour)
    else:
        print("Saturation: not used for V_T")
    print()

v_t_final = np.mean(vt_values)
print(f"Final threshold voltage V_T = {v_t_final:.3f} V "
      f"(mean of V_DS = {LINEAR_VDS} V)")

# Final V_T
ax.axvline(v_t_final, color="k", linestyle=":", linewidth=1.5)
ax.annotate(f"$V_T$ = {v_t_final:.2f} V",
            xy=(v_t_final, 0), xytext=(v_t_final - 0.15, 8),
            rotation=90, ha="right", va="bottom")

ax.set_title("Threshold Voltage Extraction (Linear Extrapolation)")
ax.set_xlabel("$V_{GS}$ (V)")
ax.set_ylabel("$I_D$ (mA)")
ax.grid(True, linestyle="--", alpha=0.6)
ax.legend()
plt.tight_layout()
plt.savefig("E10_threshold.png", dpi=300)
plt.show()
