import pandas as pd
import matplotlib.pyplot as plt


files = {
    1: "E12_Level3_VGS1.csv",
    2: "E12_Level3_VGS2.csv",
    3: "E12_Level3_VGS3.csv",
}


plt.figure(figsize=(8, 6), dpi=350)


total_points = 0


for vgs, file in files.items():

    df = pd.read_csv(
        file,
        sep=r"\s+",
        header=None,
        usecols=[0, 3],
        names=["VDS", "ID"]
    )

    total_points += len(df)

    plt.plot(
        df["VDS"],
        df["ID"] * -1000,
        label=f"VGS = {vgs} V"
    )


plt.xlabel("VDS (V)")
plt.ylabel("Drain Current ID (mA)")
plt.title("MOSFET ID–VDS Characteristics (SPICE Level 3)")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("E12_Level3.png", dpi=350)


print("Plot created: E12_Level3.png")
print("Total data points:", total_points)