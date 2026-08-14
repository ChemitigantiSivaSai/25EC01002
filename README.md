# EC2L104: Introduction to EDA Tools

## E1: Setup Output

EDA Setup Successful

numpy version: 2.5.1
pandas version: 3.0.5
matplotlib version: 3.11.1
scipy version: 1.18.0

File:
`E1_check_setup.py`

## E2: Git Log History

The repository was initialized with the roll number `25EC01002`.

The `.gitignore` file contains:

```text
*.log
*.out
```

Git log:

```text
* 61ed12c Resolve README merge conflict
|\
| * 39812e6 Add branch demonstration note
* | 7e46af8 Add master branch update
|/
* 6558cc0 Update README for branching exercise
* 15f3bc9 Add roll number information
* 1f54d33 Add git history details to README
* 69704c1 Refine EDA environment status message
* ecd6e8d Update EDA setup confirmation message
* 80bd28f Add EDA setup files and gitignore
```

## E3: Branching

- Created branch `branch_check`
- Added roll number print statement in `E1_check_setup.py`
- Committed the change on the branch
- Merged the branch into `main`
- Verified branch divergence and merge using Git Graph

## E4: Conflict Resolution

- Created a deliberate merge conflict by modifying the same section in two branches.
- Resolved the conflict by keeping the required changes and removing conflict markers.

Explanation:

Both versions were useful, so I combined the changes into one final version while removing the conflict markers.

## E5: GitHub Round Trip

- Published the repository to GitHub.
- Cloned the repository into a different folder.
- Added a line to print my date of birth in the setup file.
- Committed and pushed the change from the cloned repository.
- Pulled the changes back into the original repository.
- Verified that the changes were correctly reflected in the original repository.

Round-trip commit hash:

```text
0dbca99
```

## E6: Reading Data

Loaded the MOSFET ID-VDS sweep data using pandas.

Data file:

`E6_mosfet_output.csv`

Python script:

`E6_read_data.py`

Output:

```text
Columns:
Index(['V_GS (V)', 'V_DS (V)', 'I_D (mA)'], dtype='str')

Shape:
(44, 3)

Description:
       V_GS (V)   V_DS (V)   I_D (mA)
count  44.00000  44.000000  44.000000
mean    3.50000   2.500000   7.841591
std     1.13096   1.599418   7.904722
min     2.00000   0.000000   0.000000
25%     2.75000   1.000000   0.557500
50%     3.50000   2.500000   4.605000
75%     4.25000   4.000000  12.255000
max     5.00000   5.000000  24.150000
```

## E7: Output Characteristics

Reproduced the family of MOSFET ID-VDS output characteristics for multiple gate-source voltages.

Python script:

`E7_output_characteristics.py`

Input data:

`E6_mosfet_output.csv`

Output graph:

`E7_id_vds.png`

The graph includes:

- ID versus VDS curves
- Multiple VGS values
- Axis labels
- Legend
- Grid

Image properties:

```text
Size: 3000 × 1800 pixels
Resolution: 300 dpi
```

## E8: Output Conductance

Calculated the differential output conductance using `np.gradient`.

Python script:

`E8_output_conductance.py`

Input data:

`E6_mosfet_output.csv`

Output graph:

`E8_gd_vds.png`

The differential output conductance was calculated using:

```python
g_d = np.gradient(I_D, V_DS)
```

The output resistance was calculated using:

```python
r_o = 1 / g_d
```

For the highest gate-source voltage:

```text
V_GS = 5.0 V
```

Calculated values:

```text
V_DS (V) I_D (mA) g_d (mS) r_o (kΩ)
    0.00    0.000   12.400    0.081
    0.50    6.200   11.500    0.087
    1.00   11.500    9.600    0.104
    1.50   15.800    7.700    0.130
    2.00   19.200    5.700    0.175
    2.50   21.500    3.600    0.278
    3.00   22.800    1.650    0.606
    3.50   23.150    0.680    1.471
    4.00   23.480    0.670    1.493
    4.50   23.820    0.670    1.493
    5.00   24.150    0.660    1.515
```

In the saturation region:

```text
g_d ≈ 0.66 mS

r_o = 1 / g_d
    ≈ 1 / 0.66
    ≈ 1.515 kΩ
```

Therefore:

```text
r_o ≈ 1.515 kΩ
```

Image properties:

```text
Size: 3000 × 1800 pixels
Resolution: 300 dpi
```

## E9: Transconductance

Loaded the ID-VGS sweep data and calculated the transconductance.

Python script:

`E9_transconductance.py`

Input data:

`E9_mosfet_transfer.csv`

Output graph:

`E9_gm_vgs.png`

Peak transconductance results:

```text
V_DS = 0.1 V
Peak gm = 0.380 mS
V_GS at peak gm = 5.000 V

V_DS = 1.0 V
Peak gm = 3.800 mS
V_GS at peak gm = 3.500 V

V_DS = 3.0 V
Peak gm = 11.400 mS
V_GS at peak gm = 5.000 V

V_DS = 5.0 V
Peak gm = 12.720 mS
V_GS at peak gm = 5.000 V
```

Maximum transconductance:

```text
Maximum gm = 12.720 mS
V_DS = 5.0 V
V_GS = 5.0 V
```

Image properties:

```text
Size: 3300 × 1350 pixels
Resolution: 300 dpi
```

## E10: Threshold Extraction

Estimated the threshold voltage using the linear extrapolation method with `np.polyfit`.

Python script:

`E10_threshold.py`

Input data:

`E9_mosfet_transfer.csv`

Output graph:

`E10_threshold.png`

Results:

```text
V_DS = 0.1 V
Slope = 0.380 mA/V
Intercept = -0.550 mA
Estimated V_T = 1.447 V

V_DS = 1.0 V
Slope = 3.800 mA/V
Intercept = -7.220 mA
Estimated V_T = 1.900 V

V_DS = 3.0 V
Slope = 8.654 mA/V
Intercept = -20.572 mA
Estimated V_T = 2.377 V

V_DS = 5.0 V
Slope = 9.253 mA/V
Intercept = -22.071 mA
Estimated V_T = 2.385 V
```

The threshold voltage was obtained from the x-intercept:

```text
V_T = -Intercept / Slope
```

Output image:

`E10_threshold.png`

Image properties:

```text
Size: 2400 × 1500 pixels
Resolution: 300 dpi
```

## E11: Diode Characteristics

Loaded and plotted the diode I-V characteristics at different ambient temperatures.

Python script:

`E11_diode_characteristics.py`

Input data:

`E11_Diode_IV_Temperature.csv`

Data columns:

```text
V (V)
T (C)
I (mA)
```

Data size:

```text
108 rows
3 columns
```

Output graph:

`E11_diode_IV.png`

The graph contains:

- Diode voltage on the x-axis
- Diode current on the y-axis
- Curves for different ambient temperatures
- Axis labels
- Legend
- Grid

Image properties:

```text
Size: 2800 × 1750 pixels
Resolution: 350 dpi
```

## E12: MOSFET ID-VDS Using Equations

An n-channel silicon MOSFET was analyzed using the following parameters:

```text
tox = 10 nm
NA = 1 × 10^16 cm^-3
QF = 1 × 10^12 cm^-2
W = 4 µm
L = 0.18 µm
Aluminum metal gate = 4.1 eV
μn = 400 cm^2/Vs
```

The ID-VDS characteristics were plotted for:

```text
V_GS = 1 V
V_GS = 2 V
V_GS = 3 V
```

for:

```text
0 V ≤ V_DS ≤ 4 V
```

### E12(a): SPICE Level 1

Python script:

`E12_Level1.py`

SPICE circuit:

`E12_Level1.cir`

Output graph:

`E12_Level1.png`

Simulation output:

```text
Plot created: E12_Level1.png
Total data points: 1203
```

Data files:

```text
E12_VGS1.csv
E12_VGS2.csv
E12_VGS3.csv
```

Image properties:

```text
Size: 2800 × 2100 pixels
Resolution: 350 dpi
```

### E12(b): SPICE Level 3

Python script:

`E12_Level3.py`

SPICE circuit:

`E12_Level3.cir`

Output graph:

`E12_Level3.png`

Simulation output:

```text
Plot created: E12_Level3.png
Total data points: 1203
```

Data files:

```text
E12_Level3_VGS1.csv
E12_Level3_VGS2.csv
E12_Level3_VGS3.csv
```

Image properties:

```text
Size: 2800 × 2100 pixels
Resolution: 350 dpi
```

## Repository File Structure

```text
25EC01002/
│
├── .gitignore
├── README.md
│
├── E1_check_setup.py
│
├── E6_read_data.py
├── E6_mosfet_output.csv
│
├── E7_output_characteristics.py
├── E7_id_vds.png
│
├── E8_output_conductance.py
├── E8_gd_vds.png
│
├── E9_transconductance.py
├── E9_mosfet_transfer.csv
├── E9_gm_vgs.png
│
├── E10_threshold.py
├── E10_threshold.png
│
├── E11_diode_characteristics.py
├── E11_Diode_IV_Temperature.csv
├── E11_diode_IV.png
│
├── E12_Level1.py
├── E12_Level1.cir
├── E12_Level1.png
├── E12_VGS1.csv
├── E12_VGS2.csv
├── E12_VGS3.csv
│
├── E12_Level3.py
├── E12_Level3.cir
├── E12_Level3.png
├── E12_Level3_VGS1.csv
├── E12_Level3_VGS2.csv
└── E12_Level3_VGS3.csv
```

## .gitignore

```text
*.log
*.out
```