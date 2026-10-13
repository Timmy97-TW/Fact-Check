# A7_terms — resolution report

**18 confirmed, 5 conflict, 18 skipped** (41 facts in the slice).

The house-style source the brief pointed at turned out to be real but partial. A "Common mistakes"
list sits at the head of the **May, July, August and September** notebook sections; **April, June and
October have none**, and the REFERENCE template has none. Two kinds of entry appear in it: explicit
corrections written with an arrow (`Csn:ACCD->Csn::ACCD`, `ul-> µL`, `ddH2O->ddH₂O`,
`23444xg->23444 g`, `degrees Celsius->℃`) and bare words to get right (`chloramphenicol`,
`Bacillus subtilis`, `pNW33N-L2 (sfGFP)`, `OD600`, `Q-Amp`, `PcpcG2`, `ccaR ccaS-m3`). Only the July
section carries the construct-name items; the other months carry only units and species.

I treated an arrow entry as a decision, and for the bare-word entries I cross-checked against the two
other team-authored naming artefacts — **`2026 primer list.docx`** and the **`Cloning Products__*.dna`
file names and SnapGene feature labels**. Where all of those agree I confirmed; where the
Common-mistakes list and the primer list disagree I left it a conflict rather than pick.

## Confirmed (18)

Notebook milestones: WW-219, WW-225, WW-227, WW-229, WW-239, WW-240, WW-241.
Naming and spelling: WW-252 (ACCD), WW-253 (Bopep4), WW-256 (PcpcG2-veg), WW-257, WW-258, WW-260,
WW-261 (Csn::ACCD).
Names and numbering: WH-292 (inline photometer), WH-293 (BioDrop), WH-294 (WB800), WH-299 (Chars Hsieh).

Three of these answer questions the wiki had flagged as open rather than merely checking a number:

- **WW-257** — the ACDI/ABDI convention is written out in full in the **2 August** transformation
  entry. Each Level 2 device is the sum of its lettered Level 1 modules:
  `ABDI = A(PtagC+RBS-Ho1:PcyA) + B(PliaG-RBS0-CcaSm3) + D(Pveg-RBS0-ccaR) + I(PcpcG2-veg-EEBD-RBS0-csn:AccD)`,
  and `ACDI` the same with `C(PlepA-RBS0-CcaSm3)` for B. The convention does not need to be asked, it
  needs to be copied onto Engineering §c6.
- **WW-260** — the clone letters are the **plate letter of that day's colony PCR**, reassigned every
  run, not module letters. On 24 June plate B was PliaG-CcaSm3; on 26 June plate B was 1C-Pveg-ccaR,
  whose positives are B2 and B4. Module D's B2 and module B's B2 are definitely different isolates.
- **WW-241** — not a conflict at all. The notebook writes both numbers in one line:
  "Put all boxes into the incubator(setting 37℃, actual temperature 33℃)" on 15 August, and
  "heat box(setting 50℃, actual temp 35℃)" for the second run on **20 August**. Setpoint vs measured.

## Conflict (5) — Timmy decides, but the evidence is now on the page

- **WW-246** — the August notebook does **not** end on 29 August. It has a `2026/8/30` marker with six
  entries and a `2026/8/31` marker with three, so the month runs 1–31 August over 32 dated days.
  (The wiki's other August-notebook figure does check out: counting `Date:` headings gives
  11 + 41 + 103 + 177 + 233 = **565** entries for April–August, exactly the number on the abstract.)
- **WW-245** — the plant notebook snapshot is stale. It now holds 23 July and 10 August entries, not
  nineteen and eight, plus four dated after the 27 August snapshot (3, 11, 25, 28 September).
- **WW-254** — **LEA14 appears nowhere in the wet lab corpus.** Not in any notebook, gel sheet,
  protocol, the primer list or any SnapGene file. The team writes `Lea`, `Csn:LEA`, `Csn-LEA`,
  `LEA v2t1`. Whoever wrote LEA14 on Parts got the gene identity from outside the lab record, so the
  wet lab cannot confirm that every construct carries LEA14 — that one still needs a person.
- **WW-255** — two team sources disagree. The July list says `ccaS-m3`; the primer list rows are
  `ccaSm3 / ccaSm3 F / ccaSm3 R` and every SnapGene file name is `ccaSm3`. `ccaS-m3` occurs exactly
  once in the whole corpus, against 214 `CcaSm3` and 71 `ccaSm3`. I did not pick for them.
- **WW-259** — all four protectant names are the team's own words straight from the entries
  (CH protectant 26, CH bio peptide 10, CH biotech protectant 5, 正瀚 protectant 11, zhenhen 5,
  zhenhan 2). `CH protectant` is the house term by a wide margin. The product name **富肽二號** that
  Experiments gives appears **nowhere** in the wet lab files.

## Could not settle (18) — what is missing and who would know

**Hardware and dry-lab items with no wet-lab trace at all** — the corpus is the wet lab folder, so
these were never going to be in it. Each needs the hardware/dry-lab files, not Chars or Gabriel:

- **WW-230** DiOPAL third iteration, 17 July — needs the hardware notebook. The only LPA document in
  the wet lab folder is `Protocol/Optogenetic LPA Assay.docx`, which calls it "the LPA device" and
  never DiOPAL.
- **WW-242** jumper pressure sweep, 16 August — "jumper", "pressure sweep" and "pump setting" return
  zero hits. Needs the 16 Aug pressure log. Timmy.
- **WW-251** silica calibration, 10 October — the October notebook stops at **8 October**, so the run
  is not logged. The SOP exists (`Protocol/SiO2_OD600_Experiment_SOP.pdf`) but see the flag below.
  Needs the 10 Oct photometer export. Timmy.
- **WW-262 / WW-264 / WH-286 / WH-287 / WH-297** run, cycle, prototype and reactor-unit numbering —
  the wet lab notebook says only "the bioreactor", never BR-01, never a prototype number, never a run
  or cycle number. There is one bioreactor entry in the early-September window, **"Bioreactor
  Sampling" dated 2 September, done by Chars**, sampling at 16/18/20/22/24 and 40/42/44 h — which
  leans towards Engineering's "2 to 4 September" over Results' "started 1 September", but it is a
  sampling entry, not a start. Timmy / Jacquelyn.
- **WW-263 / WH-290** names of the light plate — wet lab only ever writes LPA. Anton / Timmy.
- **WH-289** R1–R3 arm labels — the Optogenetic LPA protocol labels its arms by colour and lux
  (`Red 220 lux`, `Green 510 lux`, …), never R1/R2/R3, so the R1–R3 arm names are a dry-lab addition.
  Timmy.
- **WH-291** photometer build names — the SOP adds a *sixth* scheme, "inline photometer 1" and
  "inline photometer 2". It never says complex/slim or V1/V2. Joshua / Jacquelyn still have to map
  the names.
- **WH-295** port names — the 2 September bioreactor sampling entry uses **"lumen side"** and
  **"shell side"** (9 hits); `feed`, `retentate` and `permeate` appear **zero** times in the wet lab
  corpus. So the hardware-page vocabulary is the one with no lab-record support. Chars Hsieh.
- **WH-296** hollow fibre spelling — `hollow` and `TFF` return zero hits. The only term the wet lab
  uses is **HFM**, in the SiO2 SOP ("high-cell-density perfusion bioreactor (HFM) system"). Timmy.
- **WH-298** Prof. Chang's romanisation — no "Prof. Chang", no 張嘉修, no Jo-Shu, no Chia-Hsiu anywhere
  in the wet lab files. The only professor named is "Professor Kyle" (plant team). Only the professor
  can settle this one.
- **WH-300 / WH-301** digital twin vs shadow, green light on the reactor — "digital twin" returns zero
  hits. Green light appears only in the Optogenetic LPA Assay protocol (220/510/3850 lux on the LPA);
  no reactor entry mentions light at all. That is consistent with the Digital Twin page's claim, but
  silence is not a statement, so I did not confirm it. Chars Hsieh / Timmy.
- **WH-302** mU/mL of supernatant vs permeate — `Protocol/Agar Application of Protectant.docx` fixes
  the working concentration at 50 mU/mL and defines mU/mL as "nmol product formed per minute per mL
  of stock", and the 2 September sampling entry stores lumen- and shell-side samples "for ELISA and
  DNPH assay". Which matrix the 7.25 mU/mL figure came from is not written down. Wet lab.

## Things worth flagging

1. **The August notebook goes to 31 August, not 29.** Nine entries on 30–31 August are currently
   outside what the wiki says the month covers.
2. **September and October are written up.** The September file has 110 dated entries to 30 September
   and October 11 to 8 October. The gap is the PDF export, not the writing.
3. **Same entry, two expected sizes.** The 16 July colony PCR for `Csn:ACCD` gives the product as
   **1596 bp** in the reaction step and **1696 bp** in the gel table, a few lines apart. Nothing on
   the wiki depends on it yet, but one of them is wrong.
4. **The silica SOP does not describe the run the wiki describes.** `SiO2_OD600_Experiment_SOP.pdf`
   is a 100 mL beaker recirculating loop in **DI water**, titrated in 2/5/10/20 mg steps
   (80/200/400/800 µL of stock). WW-251 describes 2.5 mg steps to 100 mg in **500 mL of 1 % SDS**.
   Those are different experiments, not a simplification of the same one.
5. **The LPA protocol contradicts its own figure.** The plate map puts red at 220, 510 and 3850 lux;
   Figure 1's caption says "The red lights are all at a light level of 168 lux while the green lights
   vary, at 220, 510, and 3850 lux". Whichever is right, the memory note about the LPA arms should be
   checked against it.
6. **Two Level 2 devices the wiki never mentions.** The 2 August entry builds `ACDE` and `ABDE`
   alongside ACDI and ABDI (E being the csn:AmilCP module in place of I). Only ABDI and ACDI have
   SnapGene files (`ABDI.dna`, `pSTK-EXP2-CcaSR-CsnACCD (ACDI).dna`), so ACDE/ABDE may have been
   abandoned — but they were transformed.
7. **Four wiki spellings have no raw-file support at all:** `WB800N` (0 hits), `LEA14` (0),
   `Bio-Drop` (0), `富肽二號` (0). The first three are patched; the fourth is in WW-259's note.
8. **`Bacillus subtilis 169`** in the 18 June bioreactor growth test (June notebook, line 1340) —
   every other mention is 168. Almost certainly a typo in the original entry, but it is the strain
   line of a growth-curve experiment.
