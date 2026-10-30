# EC2L104: Introduction to EDA Tools

Roll number: `25EC01002`

## How to run the scripts

Open the repository folder in VS Code (or `cd` into it) and run each script from that folder, because all data files are read using relative paths.

```
pip install numpy pandas matplotlib openpyxl scipy

python E1_check_setup.py
python E6_read_data.py
python E7_output_characteristics.py
python E8_output_conductance.py
python E9_transconductance.py
python E10_threshold.py
python E11_diode_characteristics.py
python E12_Level1.py
python E12_Level3.py
python diode_iv.py
```

Each script reads its input file from the same folder and saves its figure(s) next to it.

## E1: Setup Output

Terminal output of `E1_check_setup.py` (the date-of-birth line added in E5 is omitted here):

```
EDA Tools Environment Ready
numpy version: 2.5.1
pandas version: 3.0.5
matplotlib version: 3.11.1
scipy version: 1.18.0
Roll Number: 25EC01002
```

File: `E1_check_setup.py`

## E2: Git Log History

The repository was initialized with the roll number `25EC01002`.

The `.gitignore` file contains:

```
*.log
*.out
__pycache__/
.venv/
```

Git log (`git log --oneline --graph --decorate --all`), snapshot taken at commit `a88b723` (later commits are not listed here):

```
* bd2bdd5 (HEAD -> main, origin/main, origin/HEAD) Ignore Python cache and virtual environment
* 521c2e9 Update E3 notes and git log in README
* 4d01c8e Refresh git log in README
*   81c4a3c Merge branch_check into main; keep both lines
|\  
| * e6eace3 (branch_check) Add comment on branch_check
* | 7edecb2 Add small README comment on main
* | 74dbc73 Update README: list all .gitignore entries
* | e9e04df Update README: corrected results, E12 parameters, run instructions
* | ddf6c57 Report final V_T from linear-region fits in E10
* | 14e8dcc Plot g_d vs V_DS for all V_GS in E8 script
* | d775ca0 Rename bonus script to match naming pattern
* | 91f3f94 Add Bonus Shockley diode analysis
* | 655038a Clarify E12 README heading
* | c451254 Update README with E1-E12 results
* | b673a91 Complete E12 Level 3 MOSFET simulation
* | 16afaf5 Complete E12 Level 1 MOSFET simulation
* | 70f6ff9 Complete E11 diode characteristics
* | 676f683 Complete E10 threshold voltage extraction
* | eb48bf2 Complete E9 MOSFET transconductance
* | 7113415 Complete E8 output conductance
* | fc16d9b Complete E7 MOSFET output characteristics
* | 03a6211 Complete E6 MOSFET data reading
* | 4346f89 Complete E1 setup verification
* | 55e08a9 Document GitHub round trip commit
* | 0dbca99 Add date of birth information
* |   61ed12c Resolve README merge conflict
|\ \  
| * | 39812e6 (branch_demo) Add branch demonstration note
* | | 7e46af8 Add master branch update
* | | e4eaf7c Add branch demonstration note
|/ /  
* / 6558cc0 Update README for branching exercise
|/  
* 15f3bc9 Add roll number information
* 1f54d33 Add git history details to README
* 69704c1 Refine EDA environment status message
* ecd6e8d Update EDA setup confirmation message
* 80bd28f Add EDA setup files and gitignore
```

## E3: Branching

- Created branch `branch_check` from `main`.
- The roll-number print line in `E1_check_setup.py` had already been added on `main` earlier (commit `15f3bc9`), so the change committed on `branch_check` (commit `e6eace3`) is only a one-line comment (`# branch_check demo`) at the top of that file.
- Meanwhile `main` received further commits, so the two branches diverged.
- Merged `branch_check` into `main` with a merge commit (`81c4a3c`); the divergence and merge are visible in Git Graph.

## E4: Conflict Resolution

- Created a deliberate merge conflict by editing the same place in `README.md` on `main` and on `branch_demo` (the `## Branch Demo Commit` heading).
- Merged `branch_demo` into `main` (merge commit `61ed12c`). The leftover conflict markers were cleaned out of `README.md` in commit `55e08a9`.

Explanation (two sentences):

The conflict was on the `## Branch Demo Commit` heading: `main` had that heading plus a new `## Master Branch Update` section, while `branch_demo` only had the heading. I kept the `main` (HEAD) version because it already contained the branch's line and also the extra update, so no change from either side was lost.

### E4 (second attempt): conflict on an axis-label line

To follow the exercise exactly, a second conflict was created on the same `plt.ylabel(...)` line of `E7_output_characteristics.py` on two branches, `conflict_a` and `conflict_b`, both created from the same commit of `main`.

- `conflict_a`: `plt.ylabel('Drain Current $I_D$ (mA)')`
- `conflict_b`: `plt.ylabel('$I_D$ (mA)')`

Merging `conflict_b` after `conflict_a` stopped with a conflict; the markers were removed **before** committing the merge (merge commit `<fill in: git log --oneline -1>`).

Explanation (two sentences):

I kept the `conflict_a` version, `Drain Current $I_D$ (mA)`, because it is the more descriptive label and still contains the mathematical symbol that the `conflict_b` version used. Keeping one complete line also meant no leftover text from the other side, so the file runs without edits.

## E5: GitHub Round Trip

- Published the repository to GitHub.
- Cloned the repository into a different folder.
- Added a line to print my date of birth in the setup file.
- Committed and pushed the change from the cloned repository.
- Pulled the changes back into the original repository.
- Verified that the changes were correctly reflected in the original repository.

Round-trip commit hash:

```
0dbca99
```

## E6: Reading Data

Loaded the MOSFET ID-VDS sweep data using pandas.

Data file: `E6_mosfet_output.csv`

Python script: `E6_read_data.py`

Output:

```
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

Reproduced the family of MOSFET ID-VDS output characteristics for four gate-source voltages (2, 3, 4 and 5 V).

Python script: `E7_output_characteristics.py`

Input data: `E6_mosfet_output.csv`

Output graph: `E7_id_vds.png`

The graph includes:

- ID versus VDS curves
- Multiple VGS values
- Axis labels
- Legend
- Grid

Image properties:

```
Size: 3000 x 1800 pixels
Resolution: 300 dpi
```

## E8: Output Conductance

Calculated the differential output conductance using `np.gradient`.

Python script: `E8_output_conductance.py`

Input data: `E6_mosfet_output.csv`

Output graph: `E8_gd_vds.png`

The differential output conductance was calculated using:

```
g_d = np.gradient(I_D, V_DS)
```

The output resistance was calculated using:

```
r_o = 1 / g_d
```

For the highest gate-source voltage:

```
V_GS = 5.0 V
```

Calculated values:

```
V_DS (V) I_D (mA) g_d (mS) r_o (kOhm)
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

```
g_d ~ 0.66 mS

r_o = 1 / g_d
    ~ 1 / 0.66
    ~ 1.515 kOhm
```

Therefore:

```
r_o ~ 1.515 kOhm
```

Image properties:

```
Size: 3000 x 1800 pixels
Resolution: 300 dpi
```

## E9: Transconductance

Loaded the ID-VGS sweep data and calculated the transconductance.

Python script: `E9_transconductance.py`

Input data: `E9_mosfet_transfer.csv`

Output graph: `E9_gm_vgs.png`

Peak transconductance results (first point within 0.1 % of the maximum is reported):

```
V_DS = 0.1 V
Peak gm = 0.380 mS
V_GS at peak gm = 2.000 V

V_DS = 1.0 V
Peak gm = 3.800 mS
V_GS at peak gm = 3.000 V

V_DS = 3.0 V
Peak gm = 11.400 mS
V_GS at peak gm = 5.000 V

V_DS = 5.0 V
Peak gm = 12.720 mS
V_GS at peak gm = 5.000 V
```

Maximum transconductance:

```
Maximum gm = 12.720 mS
V_DS = 5.0 V
V_GS = 5.0 V
```

Note: for V_DS = 0.1 V and 1.0 V the device is in the linear region, where g_m is constant (0.38 mS and 3.8 mS) once strong inversion is reached, so there is a plateau instead of a peak; the reported V_GS is the first point of that plateau. For V_DS = 3 V and 5 V, g_m keeps increasing with V_GS (I_D is quadratic in saturation), so the maximum lies at the end of the sweep (V_GS = 5 V) and is not a true peak.

Image properties:

```
Size: 3300 x 1350 pixels
Resolution: 300 dpi
```

## E10: Threshold Extraction

Estimated the threshold voltage using the linear extrapolation method with `np.polyfit`.

Python script: `E10_threshold.py`

Input data: `E9_mosfet_transfer.csv`

Output graph: `E10_threshold.png`

Method: in the linear region (small V_DS) a straight line is fitted to the strong-inversion part of the ID-VGS curve (V_GS = 2.5 to 5 V) and extrapolated to I_D = 0:

```
x-intercept = -Intercept / Slope
```

Output of `E10_threshold.py`:

```
V_DS = 0.1 V
Slope = 0.380 mA/V
Intercept = -0.550 mA
x-intercept = 1.447 V
V_T = x-intercept - V_DS/2 = 1.397 V   (linear region: used)

V_DS = 1.0 V
Slope = 3.800 mA/V
Intercept = -7.220 mA
x-intercept = 1.900 V
V_T = x-intercept - V_DS/2 = 1.400 V   (linear region: used)

V_DS = 3.0 V
Slope = 8.654 mA/V
Intercept = -20.572 mA
x-intercept = 2.377 V
Saturation: not used for V_T

V_DS = 5.0 V
Slope = 9.253 mA/V
Intercept = -22.071 mA
x-intercept = 2.385 V
Saturation: not used for V_T

Final threshold voltage V_T = 1.399 V (mean of V_DS = [0.1, 1.0] V)
```

In the linear region the x-intercept equals V_T + V_DS/2, which is why V_DS/2 is subtracted. The two linear-region values agree, giving V_T of about 1.4 V. The V_DS = 3 V and 5 V intercepts (about 2.38 V) are not used: in saturation the ID-VGS curve is quadratic, so a straight-line extrapolation does not give V_T.

Image properties:

```
Size: 2400 x 1500 pixels
Resolution: 300 dpi
```

## E11: Diode Characteristics

Loaded and plotted the diode I-V characteristics at different ambient temperatures.

Python script: `E11_diode_characteristics.py`

Input data: `E11_Diode_IV_Temperature.csv`

Data columns:

```
V (V)
T (C)
I (mA)
```

Data size:

```
108 rows
3 columns
```

Output graph: `E11_diode_IV.png`

The graph contains:

- Diode voltage on the x-axis
- Diode current on the y-axis
- Curves for different ambient temperatures
- Axis labels
- Legend
- Grid

Image properties:

```
Size: 2800 x 1750 pixels
Resolution: 350 dpi
```

## E12: MOSFET ID-VDS Characteristics

An n-channel silicon MOSFET was analyzed using the following parameters:

```
tox = 10 nm
NA = 1 x 10^16 cm^-3
QF = 1 x 10^12 cm^-2
W = 4 um
L = 0.18 um
Aluminum metal gate = 4.1 eV
mu_n = 400 cm^2/Vs
```

The ID-VDS characteristics were plotted for:

```
V_GS = 1 V
V_GS = 2 V
V_GS = 3 V
```

for:

```
0 V <= V_DS <= 4 V
```

Simulator used: ngspice (batch `.control` scripts with `dc` sweeps and `wrdata` output).

SPICE model parameters derived from the given data (as used in the `.cir` files):

```
Level 1: .model NMOS1 NMOS LEVEL=1 VTO=-0.476 KP=1.381e-4 GAMMA=0.16685 PHI=0.7142 LAMBDA=0
Level 3: .model NMOS3 NMOS LEVEL=3 VTO=-0.476 KP=1.381e-4 GAMMA=0.16685 PHI=0.7142
Devices: W = 4u, L = 0.18u
```

How these follow from the given data (C_ox = eps_ox/t_ox = 3.45e-7 F/cm^2):

```
KP    = mu_n * C_ox = 400 * 3.45e-7 = 1.38e-4 A/V^2
GAMMA = sqrt(2 q eps_si N_A) / C_ox ~ 0.167 V^0.5
PHI   = 2 * phi_F ~ 0.714 V
VTO   = phi_ms - Q_F/C_ox + PHI + GAMMA*sqrt(PHI) ~ -0.47 V
        (phi_ms ~ -0.86 V for the 4.1 eV Al gate on p-Si, Q_F/C_ox ~ 0.46 V)
```

The negative V_T means this device is depletion-mode, so it conducts even at V_GS = 0 V.

### E12(a): SPICE Level 1

Python script: `E12_Level1.py`

SPICE circuit: `E12_Level1.cir`

Output graph: `E12_Level1.png`

Simulation output:

```
Plot created: E12_Level1.png
Total data points: 1203
```

Data files:

```
E12_VGS1.csv
E12_VGS2.csv
E12_VGS3.csv
```

Image properties:

```
Size: 2800 x 2100 pixels
Resolution: 350 dpi
```

### E12(b): SPICE Level 3

Python script: `E12_Level3.py`

SPICE circuit: `E12_Level3.cir`

Output graph: `E12_Level3.png`

Simulation output:

```
Plot created: E12_Level3.png
Total data points: 1203
```

Data files:

```
E12_Level3_VGS1.csv
E12_Level3_VGS2.csv
E12_Level3_VGS3.csv
```

Image properties:

```
Size: 2800 x 2100 pixels
Resolution: 350 dpi
```

### Level 1 vs Level 3

With the same VTO, KP, GAMMA and PHI, the saturation currents are 3.34 / 9.41 / 18.54 mA (Level 1) against 3.19 / 8.96 / 17.67 mA (Level 3) at V_GS = 1 / 2 / 3 V, so Level 3 gives about 5% less current and the knee occurs at a slightly lower V_DS. Both plots stay flat in saturation because Level 1 has LAMBDA = 0 and no Level-3 short-channel parameters (THETA, VMAX, ETA, ...) were set. Hence the two models are close here; the short-channel effects expected at L = 0.18 um would only show up once those parameters are specified.

## Bonus Exercise: Shockley Diode Analysis

Generated synthetic diode data using the Shockley diode equation in Python with NumPy.

The parameters used were:

```
IS = 1 x 10^-12 A
VT = 0.02585 V
VD = 0 V to 0.8 V
VD step = 0.01 V
Ideality factors: n = 1.0, 1.5, 2.0
```

Python script: `diode_iv.py`

Output graphs:

```
Bonus_Diode_IV.png
Bonus_Diode_IV_Log.png
Bonus_Diode_Conductance.png
```

Why the log plot is useful (one sentence): on a log axis each curve becomes a straight line with slope 1/(n V_T ln 10), so the exponential behaviour over many decades of current, and the value of n, can be read directly, whereas on the linear plot every curve looks flat near zero and then shoots up.

The conductance g_d = dI_D/dV_D was computed with `np.gradient(ID, VD)` and compared with the exact derivative (I_D + I_S)/(n V_T) (dashed lines in `Bonus_Diode_Conductance.png`). They agree to within about 2.5 % at interior points; the two end points are less accurate (up to about 20 %) because `np.gradient` uses a one-sided difference there.

## Repository File Structure

```
25EC01002/
|
|-- .gitignore
|-- README.md
|
|-- E1_check_setup.py
|
|-- E6_read_data.py
|-- E6_mosfet_output.csv
|
|-- E7_output_characteristics.py
|-- E7_id_vds.png
|
|-- E8_output_conductance.py
|-- E8_gd_vds.png
|
|-- E9_transconductance.py
|-- E9_mosfet_transfer.csv
|-- E9_gm_vgs.png
|
|-- E10_threshold.py
|-- E10_threshold.png
|
|-- E11_diode_characteristics.py
|-- E11_Diode_IV_Temperature.csv
|-- E11_diode_IV.png
|
|-- E12_Level1.py
|-- E12_Level1.cir
|-- E12_Level1.png
|-- E12_VGS1.csv
|-- E12_VGS2.csv
|-- E12_VGS3.csv
|
|-- E12_Level3.py
|-- E12_Level3.cir
|-- E12_Level3.png
|-- E12_Level3_VGS1.csv
|-- E12_Level3_VGS2.csv
|-- E12_Level3_VGS3.csv
|
|-- diode_iv.py
|-- Bonus_Diode_IV.png
|-- Bonus_Diode_IV_Log.png
|-- Bonus_Diode_Conductance.png
```
<!-- main update -->