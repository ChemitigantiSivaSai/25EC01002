import pandas as pd
import matplotlib.pyplot as plt

# Load the diode I-V temperature data
df = pd.read_csv("E11_Diode_IV_Temperature.csv")

# Create the plot
plt.figure(figsize=(8, 5))

# Plot I-V characteristics for each temperature
for temperature, group in df.groupby("T (C)"):

    group = group.sort_values("V (V)")

    plt.plot(
        group["V (V)"],
        group["I (mA)"],
        marker="o",
        linewidth=2,
        markersize=3,
        label=f"{temperature} °C"
    )

# Labels and title
plt.title("Diode I-V Characteristics at Different Temperatures")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")

# Grid and legend
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(title="Ambient Temperature")

# Adjust layout
plt.tight_layout()

# Save as PNG at 350 dpi
plt.savefig("E11_diode_IV.png", dpi=350)

# Display the plot
plt.show()
