# Wet lab fact-check pass — 14 October 2026

Source: `~/Downloads/Wetlab stuff` (the electronic lab notebook April to October, the plant
notebook, the per-gel label sheets and figure decks May to October, the protocol and SOP folders,
the four SnapGene cloning-product folders, and the 2026 primer list). 122 files, converted to text
and searched in full.

451 of the 901 unresolved facts were worked through, nine areas in parallel. Every `confirmed`
carries a verbatim quote from the raw file and the file path; 180 of the 190 evidence quotes verify
as exact substrings of the corpus and the other 10 are table rows the converter reflowed, each
token checked by hand.

**Counts before → after:** confirmed 414 → **542**, pending 633 → **520**, conflict 248 → **233**.
128 facts moved to confirmed, 26 pendings became conflicts because the raw file contradicts the
page, and 34 existing conflicts got a note that says what the raw data actually shows.
25 critical facts are still unresolved.

---

## 1. Take this to the office: the five asks that pay for the trip

Each of these closes a group of facts at once. Everything else below is smaller.

1. **The Genomics sequencing reports.** No sequencing report exists anywhere in the wet lab folder
   and the notebook never logs a submission, so every "sequenced on <date>" claim is unverifiable.
   One folder closes seven facts (WW-060, WW-062, WW-063, WW-064, WW-069, WW-084, WW-106). The
   clone IDs and colony PCR dates behind all seven are already confirmed on the gels.
   **Chars or Gabriel.**
2. **The `Agar/` folder** — the root-length raw data, both chlorophyll workbooks, the per-set Prism
   decks and `All agar salinity tests_.xlsx`. 28 agar facts are unreachable without it because no
   notebook carries a per-seedling root length or a per-well OD. **Abby K / Abby T.**
3. **The `Hydroponic system/` and `Soil planting/` folders** — the hydroponic chlorophyll workbook,
   the daily soil logs, the progression deck, the 23 September photos. 11 more facts.
   **Alex**, not Chars or Gabriel.
4. **What mass do you read for the ACC deaminase band, and against which marker mark?** Every
   western-blot table in the folder leaves "Expected Size (kDa)" empty, so all four wiki figures
   (35-40, 41, 42, 36 kDa) are reads off photographs. One answer settles WW-038, WW-086, WW-117,
   WW-118, WW-132 and WH-050. **Chars or Gabriel.**
5. **Was the optogenetic plate run 19 September or 29 September?** There is no LPA run in the
   electronic lab notebook on 19 September — the five entries that day are a miniprep, an
   electroporation, a PCR, a gel and a Level 2 assembly, plus Gabriel's supernatant western. A
   candidate light experiment with green/red lanes is dated **29 September**. WH-119, WH-122 and
   WH-128 are currently confirmed on the 19 September date, and the group title plus the Hardware
   and LPA timeline entries move with it. **Chars or Gabriel.**

## 2. Short questions for Chars

- **Run 4, 1 to 6 September:** what was inoculated on 1 September, which strain, and at what
  incubator temperature? The 2 September sampling entry names neither. (WH-034, WH-036)
- **Run 3, 21 July to 8 August:** the July and August notebooks contain no bioreactor entry at all.
  Your photometer log is the only source for WH-019, WH-022, WH-024, WH-243, WH-244.
- **The 7 October permeate activity, 7.25 mU/mL:** no entry, no sample, no data file, and the
  October notebook ends on 8 October. Where is the raw export and which batch was it? (WH-051)
- **DNPH or Berthelot?** DNPH appears once in the whole archive, on 2 September, as a *planned*
  use of frozen samples. When did it arrive and which runs used which method? (WH-052)
- **The 4 September leak** is in no wet lab file. (WH-056)
- **Port names:** the notebook says "lumen side" and "shell side"; `feed`, `retentate` and
  `permeate` appear zero times. The hardware page vocabulary has no lab-record support. (WH-295)
- **Did any Level 2 device go for sequencing?** Nothing records it; the last Level 2 work is the
  19 September junction gel and the 25 September electroporation of ACDI into WB800. (WW-141)
- **Module J's expected size in *B. subtilis* is written three ways** — `1145(?)` on 31 July with
  your own question mark, "around 615" on 12 August, 1195 on 19 August. Which is right? (WW-009)
- **"Bacillus subtilis 169"** in the 18 June growth test is almost certainly a typo for 168, but it
  is the strain line of a growth-curve experiment and it is the only strain designation either June
  reactor run has. The wiki's change from WB800 to 168 for runs 1 and 2 still has no support. (WH-002)
- **The 14 June entry has no "Done by" line** and reads "Add 20 mL on culture medium to bioreactor
  & flask (volume 500mL)" — 20 mL of inoculum into 500 mL, or 20 mL total in a 500 mL flask? Run 2's
  growth rate depends on it. (WW-051)

## 3. Short questions for Gabriel

- **Module H is not a no-clone module.** H3, H7 and H1 were screened, miniprepped and digested, and
  there is a gel named `20260813_PCR_of_H_after_sequencing.jpg`. The build record's "no clone and no
  date on record" is wrong — what happened to H? (WW-010)
- **Module A and module C cannot have been sequenced on 31 July and 24 July.** Both were first
  miniprepped on 1 August ("Miniprep (liquid culture 0731)", BioDrop A1 107, A2 89, A3 94, C6 98,
  C9 78 ng/µL) and EcoRI-checked the same day. Are the wiki dates submission dates for something
  else, or wrong?
- **Clone I6.** The 27 July gel says "I3 and I6: 7/27 Liquid culture; 7/28 Miniprep/sequencing?" but
  from 1 August only I3 ever appears. Was I6 lost, or never stocked? (WW-011)
- **Module C's clone is C10 on the 22 July gel and C9 everywhere after.** One label is a typo and the
  wiki follows C9. (WW-075)
- **Module G.** G2 was miniprepped 26 July and BsmBI-digested 26 to 27 July, but no outcome is
  written for that digest and no repeat count is given. (WW-076)
- **The anti-His antibody vendor.** The notebook says a **CST** mAb at 1:1000 ("anti-His-tag mAb
  (CST)", 26 August and 2 September); the wiki sheet says Santa Cruz sc-53073 / AD1.1.10. None of
  `AD1.1.10`, `sc-53073` or `Santa Cruz` occurs anywhere in the corpus. Which was actually used?
  (WW-151 — Abigail may be the better person)

## 4. Not Chars or Gabriel — do not spend the morning on these

- **Alex:** the hydroponic and soil workbooks (§1.3); box numbering, where the notebook says box 4
  got the protectant on 25 July and box 1 on 28 July while the record sheet says box 2 and box 3
  (PS-081, PS-085); light intensity and photoperiod, which appear **nowhere** in the corpus for
  either platform, so the wiki's 16 h / 8 h is unsourced (PS-009); set C's duration, whose last
  entry is 16 August with no harvest (PS-110); and the 26 August entry titled "Cotreatment + NaCl on
  soil" whose procedure is an agar run (PS-037 — Abigail did both).
- **Abby K / Abby T / Audrey H / Abigail / Naomi:** the agar workbooks; **whether the set 5 salt
  flasks held 200 mL or 250 mL** (see §6.1); which labelling of the 9 August fresh-weight table is
  real; the Prism tests behind the significance stars (PA-070, PA-118); the chamber humidity, which
  is in no file (PA-021); and whether the 11 June rectangular plates are the milestone page's
  "racked the wrong way" batch (PA-050).
- **Anton and Noah:** every LED, duty-cycle, optics, dimension, cost and pressure fact — the wet lab
  folder has no hardware files at all. `LED`, `PWM`, `MOSFET`, `Arduino`, `kLux`, `duty cycle`,
  `520 nm`, `660 nm`, `PPFD` and `µmol` return zero hits.
- **Whoever curates Parts:** WW-187 to WW-199 and WW-211, the accessions and counts. The part
  identities are real — the 18 June miniprep lists 20 STK kit parts in hand — only the Registry
  numbers are missing.
- **Chloe** (WW-004, the MoClo 2.0 trials: the 8 June colony PCR has no recorded result and there is
  no 8 June gel, consistent with "data not shown"), **Professor Huang** (WW-005, the terminator swap
  is in the files but its date and reasoning are not), **Dr. Kyle** (PS-010, the ecotype: "columbia-0
  kyle seeds" on 27 July is the only ecotype mention in any notebook), and **Prof. Chang himself**
  (WH-298 — no romanisation of his name appears anywhere in the wet lab files).
- **You, from the dry lab side:** WH-108 to WH-110, WH-130, WH-131, WW-026, and the fit outputs.

## 5. Settled tonight — stop carrying these

Ninety-four facts no longer need a person. The ones that were explicitly marked as needing an
answer from someone:

- **The ACDI/ABDI naming convention** is written out in the 2 August entry:
  `ABDI = A(PtagC+RBS-Ho1:PcyA) + B(PliaG-RBS0-CcaSm3) + D(Pveg-RBS0-ccaR) + I(PcpcG2-veg-EEBD-RBS0-csn:AccD)`,
  and ACDI the same with C(PlepA-RBS0-CcaSm3) for B. It needs copying onto Engineering §c6, not
  asking. (WW-257)
- **Clone letters are the plate letter of that day's colony PCR**, reassigned each run — module D's
  B2 and module B's B2 are different isolates. (WW-260)
- **Dr. Kyle's spray-or-drench question is answered in the soil protocol:** three foliar sprays of
  ACCD, with "do protein dialysis before spraying" added in the altered version. (PS-033)
- **The 150 vs 100 mM soil salt is not a contradiction:** 150 mM is the 23 August trial, dropped to
  100 mM from 25 August after the blot showed no ACCD. Both numbers are real. (PS-030)
- **n per group in the soil trial:** 1 pot → 3 plants for each treated group, 3 pots → 3 plants for
  the unsalted control. (PS-031)
- **4 September was the planned last day** — "0904: collect data", "0905: demonstrate results at
  green forum event". (PS-035)
- **The trehalose stock is 100 mM** and has been written down since 24 May; the Measurement page's
  "still to be recorded" is stale. (PA-016)
- **The incubator 37/33 °C disagreement was never a conflict:** the notebook writes
  "setting 37℃, actual temperature 33℃" in one line. (WW-241)
- **The purification tag question (open item 37) has three true answers**, one per construct family:
  6xHis at the 3' end in every annotated ACCD and LEA product, no tag at all on the two AmilCP
  cargoes, and an N-terminal tag on the BoPep4 variants built as `…_1-23_NHis`. (WW-008, WW-200,
  WW-201, WM-159)
- **The missing run-1 flask details:** 500 mL flask, 20 mL culture medium, 200 rpm orbital shaker.
  (WW-051, partly — see the ambiguity in §2)
- **The two antibiotic blanks can be filled in:** chloramphenicol 25 mg/mL stock to 25 µg/mL final,
  erythromycin 1 mg/mL, LBE plates 5 µg/mL. A fourth antibiotic, kanamycin, is in use and unlisted.
  (WW-170)

## 6. Numbers on the wiki that the raw files contradict

Ordered by how much depends on them.

1. **Set 5's salt ladder may be 25% over.** 2.192 g is exactly 150 mM in **250 mL**, but the
   notebook pours it into 200 mL flasks, which need 1.7532 g — the value the ACCD protocol gets
   right. 3.652 g and the 7 July remake masses scale the same way. If the flasks were 200 mL, every
   set 5 plate was ~187.5 and ~312.5 mM, and every set 5 value the wiki quotes as 150 or 250 mM is
   mislabelled. **One question to Abby K/T settles it.** (PA-014)
2. **The reactor time course on the wiki is not the experiment that was run.** It is three gels over
   two days — 2 September at 16/18/20 h (Chars), 5 September gel 1 at 20/22/24 h and gel 2 at
   40/42/44 h (Sophie C) — eight time points, nothing dated 4 September, and **no 14 h sample exists
   anywhere in the archive**. The page fuses them into one nine-point series. Marked critical.
   (WW-131)
3. **The Golden Gate "PCR program" on Experiments is the colony PCR program.** No Golden Gate
   reaction in the raw files is cycled at 95 °C at all: it is 37 °C 1.5 min / 16 °C 3 min × 25-45
   then 60 °C 10 min (BsaI), or 42/16 × 45 then 80 °C 20 min (BsmBI). Both the Golden Gate table and
   the colony PCR table carry the same wrong program. (WW-145)
4. **The colony PCR cycling is also the inherited 2025 program.** The reaction is right; every
   Q-Amp run in 2026 — about forty, from 4 August to 8 October, no exceptions — is **35 cycles**
   with 20 s annealing at 55/60/65 °C, not 30 cycles at 65 °C for 2.5 min. (WW-147)
5. **The Golden Gate formula has vector and insert swapped** relative to its own table and to the
   notebook's `0.01 pmol : 0.02 pmol`. One-line fix.
6. **Run 1's first day goes down, not up.** Reactor OD600 runs 0.172 → 0.131 over 0 to 390 min while
   the incubator arm climbs to 0.987. The Digital Twin page's "reactor 0.17 to 0.37" splices the
   24-26 h readings onto it. Also, the 0.480 is labelled "Sampling from medium", so the Results
   page's "serum-bottle control" is the wrong label. (WH-005, WW-046)
7. **Run 1 ends 7 June, not 10 June** — the last reading is 27 h on the 7 June continuation and
   there is no bioreactor entry again until 14 June. The "6 to 10 Jun" window and the
   `260610 test1 no stir.xlsx` filename are both unexplained. (WH-235)
8. **Ampicillin is 50 mg/mL in the notebook, not 25.** (WW-170)
9. **Two autoclave times are exactly swapped:** LB agar is 20 min not 30, the 3 M NaCl stock is
   30 min not 20. (WW-169, WW-176)
10. **The lab autoclaves at 127 °C / 20 min throughout**, not the 121 °C / 15-30 min the safety page
    quotes — that is a standard, not our practice. (WW-016)
11. **Electroporation:** "ran on strain 168 only" is false (WB800 on 15 September and 1 October);
    168 was pulsed at 2.0-2.2 kV not 2.1-2.3; WB800 was never harvested at OD600 2.2 (the four preps
    are 0.907, 0.91, 0.926 and 2.346); and the 1/20 and 1/40 resuspension volumes look swapped.
    (WW-205, WW-208, WW-207, WW-206)
12. **Hydroponics:** heat set D ran at 35 °C actual not 37; the plants were 12 days old at heat, not
    10; wells got 2.2 mL not 2.1 or 2; stratification was 4 days, not "at least 48 hours"; the
    salinity set used ½ MS, not 0.1x (which first appears on 12 August, i.e. the heat sets).
    (PS-112, PS-107, PS-069, PS-071, PS-070)
13. **The Results page's "no file names the protectant" is wrong** — the notebook names it a dozen
    times as CH biotech protectant / CH protectant / CH biopeptide / 正瀚, diluted 1/500, with the
    box and date for each application. That sentence should come off the page, and WW-091's status
    note repeats the same claim. (PS-083, WW-027)
14. **Plate geometry:** "18 seeds in two rows of nine" is verbatim from the *vertical heat-stress*
    tab of the protectant protocol, not from the neutral plates, which are 25 or 40 per plate. Set 7
    plates held 23-25 plants, so any per-plant normalisation assuming nine is wrong. (PA-024, PA-022)
15. **Round plates were 0.8% to 19 August and 0.6% from 20 August**, square verticals 1%. "1% in
    both orientations" is wrong, and the Plants page's 0.6% is right because it quotes the newest
    version. (PA-010, PS-068)
16. **The LPA protocol contradicts itself on red light levels** — Figure 1's caption says the reds
    are all 168 lux, the plate map in the same file says Red 220 / 510 / 3850. The wiki's 390 and
    2,940 lux are in neither. And 31/63/100% duty cannot produce a 220 : 510 : 3850 lux ratio, so one
    of those two sets is wrong. (WH-123, WH-124, WH-205)
17. **The protocol has no 24 h LPA point at all** — 8 to 10 h total, sampling at 2, 4, 6, 8 and 10 h.
    (WH-127)
18. **"Two platings of shell-side medium, both of which grew nothing":** the notebook records the two
    plates (2 September, 16 h and 24 h, incubated *overnight* with no temperature) but records no
    result for either. The "no colonies" outcome is nowhere in the wet lab notebook, and the 24 h is
    a run time point, so Measurement's Figure 23 caption is right and "read after 24 h at 37 °C" is
    not. (WH-054, WH-055, WW-014)
19. **Smaller ones:** 1,145 bp is module J, not module A (module A is 2,231 and 1,833 bp); the August
    notebook runs to 31 August, not 29; the plant-notebook entry counts are stale (23 July and 10
    August entries, plus four dated after the 27 August snapshot); `WB800N`, `LEA14`, `Bio-Drop` and
    `富肽二號` have **zero** support anywhere in the wet lab files; the DNA gel is not always 20 mL
    (August casts 20 to 120 mL); the hydroponic rig uses 270 µL and 2.2 mL of ½ MS, not 250 µL and
    2 mL of 0.1x MS; and the Ni-NTA page is **right** while the HisPur kit document in the Protocol
    folder is the stale one (the runs used 10/25/150 mM at 175 g, exactly as the wiki says).

## 7. Problems inside the team's own files

Not wiki errors — things the lab may want to fix before anyone else reads them.

- **The 9 August fresh-weight table is entered twice with contradictory salt labels and two
  different controls** (0.1537 g in the plant notebook, 0.1587 g in the August lab notes, same three
  people, same 23 plants). The salt/no-salt swap is a notebook-internal disagreement, not only a
  chlorophyll-sheet error.
- **The for-wiki heat numbers are internally inconsistent by a factor of four:** the control row is
  divided by 12.00 while the three treated rows are divided by about 3. That single factor flips the
  ranking between the two versions of the sheet.
- **Set 6 chlorophyll was read at A633 and the notebook says so** ("used the wrong wavelength this
  time, it should be 663"). Set 6 is one of the six trehalose sets the wiki quotes.
- **The acetone volume V in the chlorophyll equation changes between runs** — 1 mL, 2 mL and 4 mL —
  and the SOP itself adds 4 mL while its equation takes V = 2 mL. Every mg/g figure scales with it,
  so cross-run comparisons are only valid if V was the same.
- **The set 7 "trial 4" sheet uses 95% acetone at 665/649 nm with Lichtenthaler coefficients.** Every
  logged extraction all year is 80% acetone at 645/663 nm with Arnon. Someone changed equation
  without recording it, and 95% acetone, 649 nm and Lichtenthaler appear nowhere in the corpus.
- **The ACCD used around 23 to 26 August had no enzyme in it** — the soil protocol says the western
  blot showed no ACCD in *B. subtilis*, so those pretreatment groups were not valid. The set 8 agar
  pretest is marked "WITHOUT ENZYME ACTIVITY ASSAY TESTING".
- **The ants.** 21 August: "ants climbing into the heat stress pretest agar plates". That is the run
  behind the heat pre-test numbers.
- **The heat pre-test was read on 21-22 August, not 15 August** — 15 August is the spray date. Both
  wiki pages date the numbers to 15 August.
- **No LEA14 or BoPep4 plant protocol was ever written:** all three application protocols end with
  bare "LEA" and "Bopep4" headings and nothing under them, and no notebook entry applies either to a
  plant. That supports WW-028's "never applied to a plant" but collides with PA-193's set 10 BoPEP4
  deck. One of the two is wrong and only the plant model team can say which. Left unpatched — absence
  of a record is not proof.
- **The soil heat conditions on the wiki are almost verbatim the Zhang 2022 recipe** in the stress
  literature review, which says 22 °C recovery where the wiki says 25 °C. The only mention of
  aeration anywhere in the corpus is that same literature review — the boxes are closed tip boxes and
  no notebook records aerating them.
- **The 3 M NaCl autoclave discrepancy is a copy error inside the team's notes:** the July ELN and
  the medium protocol both say 20 min; it is the duplicate of that entry inside `Plant notebook.docx`
  that says 30 min. Other facts citing the Plant notebook copy are worth a spot check.
- **Two Level 2 devices the wiki never mentions, ACDE and ABDE, were transformed on 2 August** (all
  failed). Conversely the cloning folder holds products the wiki never mentions:
  `pSTK-EXP1-PtagC+RBS-GanA-Gala-L3S2P21`, `Pveg-RBS0-mCherry-B0015`, `Pveg-RBS0-mScarlet-B0015`,
  `pSTK-EXP1-Pveg-Bopep4-15-23`.
- **The Level 2 junction sizes changed with the primer generation**, not by error: 760/632/411 on
  30 August with the old primers, 661/632/375 from 1 September with the `L2`-prefixed ones. The wiki
  quotes the September set. None of the `L2 …` primers are in the primer list.
- **The ratio sweep was three ratios, not two** — 1:3, 1:5 and 1:7 on 26 August; only 1:5 and 1:7
  reached the junction gel. X5 and X7 are named after the ratios.
- **`Csn R` has no Golden Gate tail** — it is a plain 19-mer screening primer. And the primer list
  holds 27 conversion primers, not the thirteen the wiki counts.
- **The 16 July entry gives the Csn:ACCD product as 1596 bp in one step and 1696 bp a few lines
  later.**
- **The silica SOP describes a different experiment from the one the wiki describes** — a 100 mL
  beaker in DI water titrated in 2/5/10/20 mg steps, versus 2.5 mg steps to 100 mg in 500 mL of 1%
  SDS. Not a simplification of the same run.
- **A date typo in the notebook:** the run 1 continuation is dated "20200607" while its title says
  "Continuous from 20260606". Also `Date: 2026919` on 19 September.
- **Unit hygiene the notebook's own "Common mistakes" header already asks for**, still present in the
  files: `25 kv` for 2.5 kV, `23kv` for 2.3 kV, `capacity: 25 ul` for 25 µF, `2.5nM dNTP` and
  `2.5 µm dNTP mix` for mM, `1,7900 g` for 17,900 g, `0.5µg` of restriction enzyme where µL is meant,
  `TEB buffer` for TAE, `WN800` for WB800. None of these changes a fact, but any script that parses
  the notebook will trip on them.
- **The "Common mistakes" lists exist only in May, July, August and September**; April, June and
  October have none, and only July carries construct-name items. Where that list and the primer list
  disagree — `ccaS-m3` once against 214 `CcaSm3` and 71 `ccaSm3`, every SnapGene name `ccaSm3` — the
  facts were left as conflicts rather than picked. (WW-255)
- **September and October are written up** (110 entries to 30 September, 11 to 8 October). The gap is
  the PDF export, not the writing.

## 8. Wiki edit list

### From this wet lab pass
Every item in §6 is an edit. The ones that are a wrong sentence rather than a wrong number:

- Results: "No file in the archive names what went into the boxes" — delete, it is named a dozen
  times with box and date. (WW-027)
- Results: the reactor blot's "sampled every two hours at 14, 16, 18, 20, 22, 24, 40, 42 and 44 h" —
  three gels, eight points, no 14 h. (WW-131)
- Results: "serum-bottle control" for the 0.480 — the notebook says "Sampling from medium". (WW-046)
- Bioreactor: "two platings of shell-side medium, both of which grew nothing" — the plates are
  recorded, the result is not. (WH-054, WH-055)
- Measurement: "the trehalose stock concentration is still to be recorded" — it is 100 mM and has
  been since 24 May. (PA-016)
- Engineering §c6: add the ACDI/ABDI decomposition, which is already written out in the notebook.
  (WW-257)
- Experiments: the Golden Gate program, the colony PCR program, and the swapped vector/insert
  formula. (WW-145, WW-147)
- Safety: 121 °C / 15-30 min — the lab autoclaves at 127 °C / 20 min. (WW-016)
- Peptide Design: "every construct ordered after 16 August" ends in a free G-G-H-N — false as a
  universal claim; v2t1/v2t2, cloned 19 August, are C-terminally tagged. (WM-159)
- Molecular Dynamics: "the decision to move the purification tag to the C-terminus" has the
  direction backwards. (WM-159)
- Build record: module H's "no clone and no date on record". (WW-010)
- Results: 1,145 bp attributed to module A — it is module J. (WW-081)

### From the dry lab pass (another session, 14 October)
Thirteen more, with page, anchor and the string to grep:
Wiki sentences the dry lab pass found wrong or unsourceable (from the peer session,
evidence on the fact ids given; fuller version in docs/2026-10-14-drylab-consolidation.md section 4).

WRONG, correction has a source file behind it:
1. peptide-design #codon — "a run of seven adenines" -> eight (nt 18-25 of the 69 nt WT mature BoPep4 CDS are GGATC-AAAAAAAA-GACC; optimiser limit is 4). WM-177
2. protein-design/molecular-dynamics #key-findings — the Lys7-Asp129 salt bridge at 98.7% / 2.81 A is the 7-23 trajectory, not the full-length peptide (full length is 44.2%). WM-138
3. protein-design/methodology #engineering-axes — "HADDOCK 2.4" -> 2.5 (haddock2.5-2026-07, 121 production runs); 2.4 is the Honorato 2024 protocol paper, so change the version or reword as a citation. WM-105
4. peptide-design #tag — the exit-channel table's "2" and "111" are n_seeds in exit_channel.json, not free grid points (free points are 694 N-terminus, 1,055 C-terminus with BAK1). Relabel only. WM-162
5. protein-design/methodology #viennarna — "a library of 8,000 random synonymous candidates" exists in no file. Round 2 enumerated 33,395 legal candidates for BoPep4, 34,342 LEA14, 40,899 ACCD, 39,091 AmilCP; the v2 optimiser folded 4,437 structures, v3 110,040. WM-129
6. peptide-design #codon — "roughly 50,000 synonymous draws" per payload, same problem; use the per-group counts above. The rest of that paragraph (0.067 -> 0.528 at CAI 0.78) reproduces exactly. WM-175
7. model — ACC deaminase as "a homotetramer of about 144 kDa", "36.5 kDa per subunit". The team's own 23 Aug ACCD permeate dossier uses 41 kDa and trimer assembly; releaf-model parameters.yaml has our construct's mature protein at 37,636 Da. K_M 3.4 mM and k_cat 146 min-1 are confirmed. Moves the 1.96 mg/L on the same page (2.01 at 37.6 kDa, 2.20 at 41 kDa); the 54 nM is unaffected. WM-025, WM-024

CANNOT BE SOURCED — fix the number or drop the claim:
8. model #dose-and-payback — "A 5-year payback would need an efficacy of 12.8" reproduces from nothing; the printed table gives 7.7 one way and 13.6 the other. The 38.3 y and 64.7 y do reproduce. Ethan has to say which chain produced 12.8. WM-050
9. peptide-design #tag — "scores -155.7, better than untagged wild-type BoPep4 at -125.9"; neither number is in the archived score tables (panel seed gives -173.1 tagged, -144.8 untagged). The -181.9 best seed is right and beats the crystal control's -180.749. Needs the 30-pose panel summary. WM-161

WORTH A CLARIFYING SENTENCE:
10. model #dose-and-payback — the "Ordinary paddy ... 30,000 ... 64.7 y" row only works if NT$30,000 is per unit, but it reads as a total; and the ordinary-paddy annual value moves 1.69x over the efficacy range while salt-affected moves 3.50x, with no stated reason. WM-048
11. model #stress-index — "18 candidate stresses" then "32,767 combinations of 15 candidates"; how 18 became 15 is unexplained and no Block 1 source exists in either project folder. WM-002
12. model #optogenetic-kinetics — 535/672 nm is the source paper's, the hardware runs 520/660 nm; one clause saying which is which closes it. WM-033

REPO FIX, not a page:
13. releaf-wiki/build/model_figures.py:63 — the comment "# Ohlendorf et al. 2019, via the docx" next to K_CCAS, N_CCAS = 4.66, 1.88 should read Castillo-Hair et al. 2019, Nat. Commun. 10:3099. Not done: that repo has an uncommitted tree on finalize/1013.

## 9. Where the detail is

`records/2026-10-14-wetlab/` holds the nine per-area reports with every quote and file path, the
patch files that were applied, and `_applied.json` listing each fact id with its old and new status
and value.

Conversion note: the wet lab files were read as text. Gel *images* were not read, so any fact whose
value exists only in a photograph — band counts, which lanes banded — is marked as such rather than
confirmed.
