import pandas as pd
import matplotlib.pyplot as plt

file_path = 'E6_mosfet_output.csv'
df = pd.read_csv(file_path)

plt.figure(figsize=(10, 6))

for v_gs, group in df.groupby('V_GS (V)'):
    group = group.sort_values('V_DS (V)')

    plt.plot(
        group['V_DS (V)'],
        group['I_D (mA)'],
        marker='o',
        linewidth=2,
        label=f'$V_{{GS}}$ = {v_gs} V'
    )

plt.title('MOSFET Output Characteristics ($I_D$ vs $V_{DS}$)')
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)')
plt.ylabel('Drain Current $I_D$ (mA)')
plt.legend(title='Gate-Source Voltage')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.savefig('E7_id_vds.png', dpi=300)
plt.show()
