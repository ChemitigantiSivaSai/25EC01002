import pandas as pd
import numpy as np

df = pd.read_csv("E6_mosfet_output.csv")

# Select V_GS = 5 V
group = df[df["V_GS (V)"] == 5.0].copy()

# Sort by V_DS
group = group.sort_values("V_DS (V)")

# Calculate differential output conductance
group["g_d (mS)"] = np.gradient(
    group["I_D (mA)"],
    group["V_DS (V)"]
)

# Calculate output resistance
group["r_o (kΩ)"] = 1 / group["g_d (mS)"]

print("V_GS = 5.0 V\n")

print(
    group[
        ["V_DS (V)", "I_D (mA)", "g_d (mS)", "r_o (kΩ)"]
    ].to_string(
        index=False,
        formatters={
            "V_DS (V)": "{:.2f}".format,
            "I_D (mA)": "{:.3f}".format,
            "g_d (mS)": "{:.3f}".format,
            "r_o (kΩ)": "{:.3f}".format
        }
    )
)
