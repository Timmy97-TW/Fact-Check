# A6 — hydroponics and soil (49 facts)

**18 confirmed, 4 conflict (notes added, Timmy decides), 27 skipped.**

Primary evidence used: `Electronic Lab Notes/Plant notebook.docx`, the April/June/July/August/September
ELNs, `Protocol/Hydroponic medium preparation.docx` and `Protocol/Soil Application of Protectant.docx`.

## The big win: the Soil Application of Protectant protocol

Nobody seems to have read this file against the fact list. It holds **two dated versions of the
23 August soil ACCD trial** (an "initial plan" and an "altered version"), and between them they
settle four facts that were marked "only Alex knows":

- **PS-030 (150 vs 100 mM)** — initial plan 150 mM with pretreatment on 0823/0824; a note at the
  top says those pretreatment groups were invalid because the western blot showed no ACCD in
  *B. subtilis*, and the altered version drops the salt to 100 mM from 0825. Both numbers are real;
  150 mM is the 23 August trial, 100 mM the restart the wiki indexes on 29 August.
- **PS-031 (n per group)** — "1 pot->3 plants" for pretreatment, cotreatment, posttreatment and the
  salt-only control; "3 pots->3 plants" for the unsalted control.
- **PS-033 (spray or drench)** — answers Dr. Kyle's 25 August question: **3 foliar sprays of ACCD**,
  in both versions, and the altered version adds "do protein dialysis before spraying", which is
  where the daily log's "ACCD (dialysis)" label comes from. The wiki's "sprayed" is right.
- **PS-035 (4 September)** — the altered timeline ends "0904: collect data(chlorophyll, freshweight,
  seeds?)" then "0905: demonstrate results at green forum event". 4 September was the planned last day.

Also in that protocol, the altered version pours NaCl **on the soil** (25 mM, then 200 mM on 0901 and
300 mM on 0903 "until NaCl flows out"), where the initial plan sprayed 25 mM NaCl on the leaves —
useful if the Plants page describes the dosing route.

## Numbers on the wiki that the raw files contradict

- **Plants page, hydroponic heat set D at 37 °C → the ELN says 35 °C.** 20 and 21 August both read
  "heat box(setting 50℃, actual temp 35℃)". The only 37 °C in the hydroponic record is set C's
  *setting* on 15–16 August, whose actual was 33 °C. (PS-112)
- **Plants page, 10-day-old plants at heat → 12 days.** Set C sown 30 July, 4 days at 4 °C (so out of
  the cold 3 August), heat on 15 August = 12 days. The record sheet is right. (PS-107)
- **Plants page, 2.1 mL and Experiments page, 2 mL per well → 2.2 mL in all five entries**
  (1 Jun, 19 Jul, 30 Jul, 12 Aug, 17 Aug). (PS-069)
- **Plants page, "at least 48 hours" stratification → 4 days** in every hydroponic entry from July on
  (27 April was 3 days). 48 hours appears nowhere in the corpus. (PS-071)
- **Experiments page, 0.1x MS for the salinity protocol → the salinity set (19 July) used ½ MS.**
  0.1x MS first appears 12 August, i.e. the heat sets. (PS-070)
- **Results page, "no file names the protectant" → it is named a dozen times**: "CH biotech
  protectant" (25 July), "CH protectant" (28 July and 14–21 August), "CH biopeptide" / 正瀚 / 正翰
  on the agar plates, diluted 1/500. This also fixes the status note on **WW-091**, which repeats the
  "agent unknown" claim. (PS-083)
- **Plants page, 0.6% agar in the seed lids → all three numbers are real and 0.6% is the newest.**
  1% on 19 July (250 µL), 0.8% from 30 July (270 µL) and on 12/17 August (250 µL), then the
  20 August entry "Prepare 420 mL 0.6% ½ MS agar / Purpose: Add agar into lids for new set of
  seeds". So the Plants page is quoting the last version, not an error. (PS-068)

## Two internal contradictions inside the team's own files

- **The 3 M NaCl autoclave time (PS-073) is a copy error, not a wiki error.** The July ELN entry says
  "Autoclave for 20 minutes at 127°C" and so does the Hydroponic medium preparation protocol; it is
  the duplicate of that same entry inside `Plant notebook.docx` that says "127C for 30min". The
  Plant notebook copies of the plant entries have drifted from the month ELNs in at least this one
  place — worth a spot check if any other fact cites the Plant notebook copy.
- **The 26 August entry (PS-037)** is titled "Cotreatment + NaCl on soil" but its purpose says
  "agar grown Arabidopsis" and the procedure is 75/100 mM NaCl + 1:500 正翰 on agar plates. The soil
  protocol *does* schedule 0826 as the soil cotreatment day, but with ACCD poured on soil — a
  different agent and route. Most likely the title belongs to the soil ACCD schedule and the
  procedure recorded is the agar CH run. **Ask Abigail**, she did both.

## Still unsettled

### Needs the hardware files (not in the wet lab corpus at all) — ask Anton
`WW-029`, `WW-030`, `WW-031`, `WH-214`, `WH-215`, `WH-216`, `WH-217`, `WH-218`, `WH-219`, `PS-078`.
The corpus has no STL, 3MF or G-code and no `Hydroponic system/` folder, so no plate geometry
(42.27 cm³, 3.51 cm³/mm, 3.5 g/mm, 54.2 g, 111.9 g, 117.50 × 92.50 × 25.08 mm, 74.72 cm³,
21.59 mm spacing, 15% gyroid, the 180 g draft case) can be checked here.
- Useful partial: **the 13 seed positions have notebook support.** The 22 July entry "Issue of Box BI"
  says "8 out of 13 plants are not growing", i.e. that board carried 13 lids. The rows-of-4-5-4
  layout and the 21.59 mm spacing still need the STL. (`WW-031`, `WH-214`)
- `PS-078`: the first raw mention of 3D printed boards anywhere in the corpus is **20 July**
  ("3 3D printer boards"). Nothing records a 25 June print; the Hardware page's date has no wet lab
  source. The 17 June weekly note only says "We have four prototypes now".
- `WW-041`: 24, 25 and 26 April are logged as "(empty)" in the April ELN. No record of the fixed
  plates being cut for 300 mL / 1.5 L / 2 L boxes.

### Needs `Hydroponic system/Chlorophyll content for hydroponic system.xlsx` — ask Alex
`PS-099` (0.7933 vs 0.714, n=9 vs n=10), `PS-125` (which heat run the sheet is), `PS-143` (missing
fresh weights, #DIV/0!), `PS-146` (four sheets vs three sets). The workbook is not in the corpus.
For `PS-125` the ELN does give the two candidates cleanly: boxes **C1–C4 at 33 °C from 15 August**
(protectant into C2 on 14 Aug, C3 on 15 Aug, C4 on 16 Aug) and **D1–D4 at 35 °C from 20 August**
(D2 on 19 Aug, D3 on 20 Aug, D4 on 21 Aug) — so whoever reads the cut-off tab name only has to match
the harvest date to one of those.

### Needs `Soil planting/` (daily logs, the progression deck, the ACCD salinity deck, the 23 Sep photos)
`PS-012` (7 trays vs 4), `PS-017` (3 vs 7 days old on the slides), `PS-040`, `PS-045`, `PS-048`,
`PS-049`, `PS-052`. None of these files are in the corpus. What the ELN adds:
- The August ELN names **tray 5 and tray 6 on 10 August** (8 pots) and **4 more pots on 17 August**
  with no tray number. No tray 7 anywhere. (`PS-012`)
- **There is no September soil entry of any kind**, and no 23/24/25 August soil ACCD entry either —
  the 23 August trial was never written up in the ELN, only planned in the protocol. So the
  12 September ACCD dose (`PS-049`), the salt-schedule comparison (`PS-040`) and the soil heat trial
  (`PS-052`) have no notebook record at all. Only Alex can supply these.
- **Alarming for `PS-052`:** the wiki's soil heat conditions (37 °C, 5 days of heat, 5 days of
  recovery) are almost word for word the literature recipe in `Protocol/Stress Literature Review.docx`
  — "Plates with 10-day-old seedlings held at 37 °C for 1, 3, or 5 days, then returned to 22 °C for
  5 days of recovery" (Zhang et al. 2022). Note the paper says **22 °C** recovery, the wiki says 25 °C.
  Please check that these are our conditions and not a copied protocol.

### Needs a person, not a file
- `PS-009` **light and photoperiod**: I searched every ELN. There is **no light intensity and no
  photoperiod anywhere in the corpus**, for soil or for hydroponics — so the wiki's 16 h / 8 h is
  also unsourced, not just the soil side. The only chamber settings written down are "growth chamber
  at 22.2%" (20 July, probably a humidity typo) and "incubator (22℃ for 17hr)" for agar plates
  (17 August). Ask Alex / Dr. Kyle.
- `PS-010` **ecotype**: I grepped the whole corpus. "columbia-0 kyle seeds" (27 July) is the only
  ecotype mention in any notebook; every other Columbia/Col-0 hit is in the literature review. So the
  fact's wording is accurate, but whether the soil and hydroponic plants are the same lot is still a
  question for Dr. Kyle.
- `PS-015` (25 vs 26 July) and `PS-021` (0809 labels): the ELN dates are firm (20260725 by Alex;
  20260810 by Sophie H) and nothing in the ELN explains the 0726 / 0809 photo labels. I confirmed
  PS-021 on the ELN date and left PS-015 as a conflict since there the label disagreement is the
  whole fact.
- `PS-081` / `PS-085` **box numbering**: left as conflicts. The ELN is unambiguous (Box 4 got
  600 µL on 25 July, Box 1 got 600 µL on 28 July), the record sheet is unambiguous the other way
  (Box 2 on 25 July, Box 3 on 28 July, Box 1 = control). Nothing in the corpus says which numbering
  survived, so this is a renumbering only Alex / Abby T / Audrey H can confirm.
- `PS-076` **aeration**: no air stone, pump, bubbler or darkness is mentioned in any ELN or protocol —
  the boxes are closed tip boxes. The **only** mention of aeration in the whole corpus is the
  literature review ("Refresh medium every 3–5 days ... maintain O₂ (gentle aeration if possible)"),
  which reads like the source of any aeration claim on the wiki. Left unpatched because a negative
  cannot be confirmed, but Timmy can treat it as answered: we did not aerate.
- `PS-110` **set C duration**: the last set C entry is 16 August (protectant into C4). No end date,
  no harvest, no chlorophyll entry for set C. The wiki's "seven days" has no source.
- `WW-091` four-box photos: 28 July records "take test pictures of the 4 boxes" and 4 August records a
  hydroponic fresh-weight harvest, which fits the 25 Jul / 28 Jul / 4 Aug span, but the
  control / pre / co / post labelling comes from the record sheet, not the ELN. Left unpatched.

## One more date oddity
The 19 July entry sows set A and says to wait 4 days at 4 °C, yet the **20 July** entry transfers
"the tube rack with 41 plants" into boxes 1–3. Those have to be two different racks, and the sowing of
the older one is not in any ELN. If any fact dates set A's plant age from 19 July (e.g. the timeline
sheet's "Day 10" on 25 July), it is dating the wrong rack.
