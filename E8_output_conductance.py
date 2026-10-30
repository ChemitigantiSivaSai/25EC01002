import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("E6_mosfet_output.csv")

# ---- Figure: g_d = dI_D/dV_DS for every gate voltage ----
plt.figure(figsize=(10, 6))

for v_gs, group in df.groupby("V_GS (V)"):
    group = group.sort_values("V_DS (V)")
    g_d = np.gradient(group["I_D (mA)"], group["V_DS (V)"])  # mA/V = mS

    plt.plot(
        group["V_DS (V)"],
        g_d,
        marker="s",
        linestyle="--",
        linewidth=2,
        label=f"$V_{{GS}}$ = {v_gs} V",
    )

plt.title("MOSFET Differential Output Conductance")
plt.xlabel("Drain-to-Source Voltage, $V_{DS}$ (V)")
plt.ylabel("Conductance, $g_d$ (mS)")
plt.legend(title="Gate-Source Voltage", loc="upper right")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.savefig("E8_gd_vds.png", dpi=300)

# ---- Table: g_d and r_o at the highest V_GS ----
group = df[df["V_GS (V)"] == df["V_GS (V)"].max()].copy()
group = group.sort_values("V_DS (V)")

group["g_d (mS)"] = np.gradient(group["I_D (mA)"], group["V_DS (V)"])
group["r_o (kΩ)"] = 1 / group["g_d (mS)"]  # 1/mS = kΩ

print(f"V_GS = {group['V_GS (V)'].iloc[0]} V\n")
print(
    group[["V_DS (V)", "I_D (mA)", "g_d (mS)", "r_o (kΩ)"]].to_string(
        index=False,
        formatters={
            "V_DS (V)": "{:.2f}".format,
            "I_D (mA)": "{:.3f}".format,
            "g_d (mS)": "{:.3f}".format,
            "r_o (kΩ)": "{:.3f}".format,
        },
    )
)

plt.show()
