import numpy as np
import matplotlib.pyplot as plt

# Constants
IS = 1e-12          # Reverse saturation current (A)
VT = 0.02585        # Thermal voltage (V)

# Diode voltage sweep
VD = np.arange(0, 0.8 + 0.01, 0.01)

# Ideality factors
ideality_factors = [1.0, 1.5, 2.0]

# Store currents and conductances
currents = {}
conductances = {}

# Calculate diode current and small-signal conductance
for n in ideality_factors:
    ID = IS * (np.exp(VD / (n * VT)) - 1)
    gd = np.gradient(ID, VD)

    currents[n] = ID
    conductances[n] = gd


# --------------------------------------------------
# Figure 1: Diode I_D-V_D characteristics
# Linear y-axis
# --------------------------------------------------

plt.figure(figsize=(8, 6), dpi=350)

for n in ideality_factors:
    plt.plot(
        VD,
        currents[n],
        label=rf"$n = {n}$"
    )

plt.xlabel(r"$V_D$ (V)")
plt.ylabel(r"$I_D$ (A)")
plt.title(r"Diode $I_D$-$V_D$ Characteristics")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("Bonus_Diode_IV.png", dpi=350)
plt.close()


# --------------------------------------------------
# Figure 2: Diode I_D-V_D characteristics
# Logarithmic y-axis
# --------------------------------------------------

plt.figure(figsize=(8, 6), dpi=350)

for n in ideality_factors:
    ID = currents[n]
    positive = ID > 0

    plt.semilogy(
        VD[positive],
        ID[positive],
        label=rf"$n = {n}$"
    )

plt.xlabel(r"$V_D$ (V)")
plt.ylabel(r"$I_D$ (A)")
plt.title(r"Diode $I_D$-$V_D$ Characteristics (Log Scale)")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

plt.savefig("Bonus_Diode_IV_Log.png", dpi=350)
plt.close()


# --------------------------------------------------
# Figure 3: Small-signal diode conductance
# Logarithmic y-axis
# --------------------------------------------------

plt.figure(figsize=(8, 6), dpi=350)

for n in ideality_factors:
    gd = conductances[n]
    positive = gd > 0

    (line,) = plt.semilogy(
        VD[positive],
        gd[positive],
        label=rf"$n = {n}$ (np.gradient)"
    )
    # exact derivative of the Shockley equation, for comparison
    plt.semilogy(
        VD,
        (IS * (np.exp(VD / (n * VT)) - 1) + IS) / (n * VT),
        linestyle="--",
        color=line.get_color(),
        label=rf"$n = {n}$ (analytic)"
    )

plt.xlabel(r"$V_D$ (V)")
plt.ylabel(r"$g_d$ (S)")
plt.title(r"Small-Signal Diode Conductance $g_d$")
plt.grid(True, which="both")
plt.legend()
plt.tight_layout()

plt.savefig("Bonus_Diode_Conductance.png", dpi=350)
plt.close()


print("Bonus Exercise completed.")
print("Generated:")
print("  Bonus_Diode_IV.png")
print("  Bonus_Diode_IV_Log.png")
print("  Bonus_Diode_Conductance.png")