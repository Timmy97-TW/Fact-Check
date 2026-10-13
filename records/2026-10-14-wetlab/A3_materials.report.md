# A3 — Materials (50 facts): 26 confirmed, 12 conflict, 12 skipped

Slice: media and antibiotics, enzymes/antibodies/consumables, strains, instruments, vessel/volumes.
Everything below is from the wet lab corpus only. Patch file: `A3_materials.jsonl`.

---

## 1. What could not be settled, and who would know

### Hardware instruments — nothing about them is in the wet lab corpus (7 facts)

The wet lab folder has no hardware files at all. I grepped for every identifier and got
zero hits across all notebooks, protocols and gel sheets: `Biophsep`, `LEIRONG`, `ZP4000`,
`Arduino`, `DiOPAL`, `hollow`, `transducer`, `beam splitter`, `MPa`, `amber`, `600 nm LED`.

- **WW-160** hollow fibre module HF-E-MI-M020-10-60-P (0.2 µm, 150 cm², 8 fibres) —
  needs the vendor datasheet and the 16 Aug module measurement. Timmy / Noah.
- **WW-161** pump ZP4000-N79H rated 230 to 2,600 mL/min — needs the vendor sheet and the
  Results §7 calibration raw data. Timmy.
- **WW-162** pressure transducer 1.0 % of 0 to 1 MPa full scale — needs the transducer
  datasheet; "never zeroed against atmosphere" is a judgement only the builder can confirm. Timmy / Anton.
- **WW-163** Arduino UNO Q photometer / Uno R4 WiFi DiOPAL — needs the firmware repo or
  the hardware notebook. Timmy.
- **WW-164** photometer optics (600 nm amber LED, 2 mm slit, 90:10 splitter) — needs the
  optics BOM. Timmy.
- **WW-168** DiOPAL twenty-four positions, two wavelengths × three tiers × four replicates —
  needs the DiOPAL build record. The only adjacent raw file is
  `Protocol/Optogenetic LPA Assay.docx`, which lists six light conditions
  (red/green at 220, 510 and 3850 lux) and does **not** mention 24 tubes or 4 replicates.
  Worth checking whether the wiki's "three intensity tiers" are those 220/510/3850 lux steps.
- **WW-165** BioDrop as reference instrument — **half settled.** The SiO2 SOP confirms
  "Benchtop spectrophotometer | BioDrop or equivalent, capable of a 1 mL sample at 1 cm
  pathlength, 600 nm" as the external reference anchor. The **OD 2.5 saturation figure is
  not in the corpus**: the SOP mentions 2.5 only as the *theoretical* concentration target
  around cycle 30, not as an instrument ceiling. The 10 Oct silica run is a hardware record
  and the October wet lab notebook has no entry for it. Needs the 10 Oct run log. Timmy.

### Vessel, volumes and culture conditions — a hardware question, not a wet lab one (5 facts)

- **WH-161** 300 mL vs 1 L working volume — not in the wet lab corpus. Jacquelyn / Timmy.
- **WH-162** lumen volume 200 mL vs 7.0 to 7.2 mL — not in the wet lab corpus. The 200 mL
  figure is three orders of magnitude off the weighed holdup, so one of the two is a typo.
  Noah / Anton.
- **WH-164** reactor medium LB — **cannot be settled, and the corpus makes it worse.** The
  wet lab uses both: LB and LBA/LBC/LBE plates and 5 mL LB cultures, *and* TB for every
  overnight liquid culture ("3 mL TB medium and 3 µL ampicillin"). The 14 August entry is
  even titled "Make LB medium" while the recipe inside is "11.g of TB powder". Which medium
  run 4 used is nowhere in these files. Wet lab / Jacquelyn.
- **WH-165** chassis on the Bioreactor page — see WW-203 below; the strain question is real
  but which page should say what is editorial. Jacquelyn / wet lab.
- **WH-166** BPT tubing — not in the wet lab corpus. Noah / Anton.

### Things I confirmed but with a named gap Timmy may still want to close

- **WW-151 (filed as conflict)** The antibody *dilution* is now recoverable — 1:1000 in 5 %
  milk, 4 °C overnight — so "As required" can go. But the **vendor does not match**: see §2.
- **WW-156** the dialysis regime is confirmed to the hour; the cassette's "Slide-A-Lyzer G3
  10K MWCO" identity is on the wiki sheet only, the notebook just says "dialysis cassette".
- **WW-173** the 750 mL / 15-plate batch itself is not in the corpus; it is the 500 mL
  protocol scaled 1.5× exactly. Only confirm-able as arithmetic, not as a recorded batch.
- **WW-159** no Bradford result exists anywhere in the raw files, which matches the wiki.

---

## 2. Things I would flag as alarming

### a. The Golden Gate "PCR program" on Experiments is the colony PCR program (WW-145)

The wiki prints, under Golden Gate assembly, 95 °C 2 min → 30 cycles of
95 °C 30 s / 65 °C 40 s / 72 °C 2.5 min → 72 °C 1 min. That is, line for line,
the thermocycler table from `Protocol/Protocol from iGEM 2025/Colony PCR.docx`
(95 °C 2 min, 95 °C 30 s, 65 °C 40 s, 72 °C 30 s, 72 °C 1 min, 30 cycles) with the
extension stretched to 2.5 min. No Golden Gate reaction in the raw files is cycled at
95 °C at all — Golden Gate is digestion/ligation cycling:

- BsaI route (SOP, and 1 Aug notebook): 37 °C 1.5 min / 16 °C 3 min × 25–45, then
  37 °C 5 min, then 60 °C 10 min inactivation.
- BsmBI route (15 Sep notebook): 42 °C 5 min / 16 °C 5 min × 45, then 42 °C 10 min,
  then 80 °C 20 min.

This is the single worst error I found in the slice. **Both** the Golden Gate table and the
colony PCR table on Experiments carry this same wrong program.

### b. The colony PCR cycling on the wiki is also not what was run (WW-147)

The *reaction* (20 µL, 10 µL Q-Amp, 1 µL + 1 µL primers, 8 µL water, gridded backup plate)
is confirmed dozens of times. But the wiki's cycling beside it — 30 cycles, anneal 65 °C,
extend 2.5 min — is the inherited 2025 program. Every Q-Amp screening run in 2026 is
**35 cycles** of 95 °C 20 s, 20 s annealing at 55, 60 or 65 °C and a 72 °C extension scaled
to the product (30 sec to 5 min), bracketed by 95 °C 5 min and 72 °C 5 min — about forty
entries from 4 August to 8 October, with no exceptions. (The 25-cycle 98 °C program on the
PCR amplification page is a different reaction, the Ex Taq amplification, and that one is
confirmed.)

### c. The Golden Gate formula on Experiments has vector and insert swapped

The wiki's reagent table reads "Vector (10 fmol) / Inserts (20 fmol)", which matches the
notebook (7 Sep: `=> 0.01 pmol : 0.02 pmol`, vector first). But the equation immediately
below it reads `Vector: 0.02 = ...` and `Insert: 0.01 = ...` — the two are the wrong way
round relative to the table and to the notebook. One-line fix.

### d. Western blot antibody vendor (WW-151)

The wiki sheet names the primary as His-Tag Antibody AD1.1.10, sc-53073, Santa Cruz
Biotechnology. The notebook names a **CST (Cell Signaling Technology)** anti-His-tag mAb:
"Incubate in conti His-tag mouse antibody(CST) in 4℃ overnight" (2 Sep) and "Incubate the
PVDP in 1:1000 anti-His-tag mAb (CST) in 2% BSA overnight" (26 Aug). The strings
`AD1.1.10`, `sc-53073`, `Santa Cruz`, `Jackson`, `LumiDura` and `T-Pro` do not occur
anywhere in the corpus. Either the sheet lists a reagent that was ordered but not used, or
the notebook's "(CST)" is wrong. Abigail / Chars.

### e. Ampicillin stock is 50 mg/mL in the notebook, not 25 mg/mL (WW-170)

The Liquid bacterial culture sheet on the wiki says "Ampicillin (25 mg/mL)". The June
notebook says 50 mg/mL twice: "12 mL of TB medium and 12 µL of 50mg/mL Ampicillin" (6 Jun)
and "35 ml of TB medium and 35 µL of 50 mg/ml Ampicillin" (11 Jun). The two blank
concentration cells on that sheet **can be filled in from the raw files**:
chloramphenicol 25 mg/mL stock to 25 µg/mL final, erythromycin 1 mg/mL
(0.01 g in 10 mL of 100 % alcohol, 23 Jul), LBE plates 5 µg/mL. A **fourth** antibiotic,
kanamycin, is also in use (25 µL per 250 mL batch, 24 Aug) and is not on the wiki's list.

### f. Two autoclave times on the wiki do not match the notebook

- **WW-169** Culture agar preparation says "Autoclave 30 min". Every LB agar batch in the
  notebook says 20 minutes at 127 °C (7 Aug, 14 Aug, 30 Jul, 24 Aug). The only 30-minute
  autoclaves in the corpus are the ½ MS hydroponic agar (30 May), the 3 M NaCl stock
  (25 Jul) and Lu's EP buffer (13 Sep).
- **WW-176** the 3 M NaCl stock page says 20 min; the 25 Jul entry says
  "Autoclave the medium at 127C for 30min". The two are exactly swapped.
- Also on WW-169: "250 µL of antibiotics" is the chloramphenicol volume only. The 24 Aug
  batch adds 500 µL ampicillin / 25 µL kanamycin / 1250 µL erythromycin / 250 µL
  chloramphenicol into the same 250 mL.

### g. Ni-NTA: the wiki is right and the kit document in the Protocol folder is not (WW-155)

I expected this to break the other way. The 5 and 6 Aug purifications use the team's own
50 mL buffer formulation — equilibrate 10 mM, wash 25 mM, **elute 150 mM**, spun at
**175 g for 2 min** — exactly as the wiki says. It is
`Protocol/HisTag Protein Purification w_ HisPur™ Ni-NTA Purification Kit.docx` that gives
the manufacturer's **250 mM** elution and **700 × g** spins. That document is where the
"10 to 250 mM" range on the Notebook page comes from. The wiki needs no change; the
Protocol folder has two incompatible versions of the same step.

### h. 1/20 and 1/40 may be swapped between the two electroporation columns (WW-206)

The Experiments electroporation table gives 168 → resuspend in 1/20, WB800 → 1/40.
The raw files give the reverse pattern: the only 168 prep (4 May, Gabriel) resuspends in
**1/40**, and the 2 Sep **WB800** prep resuspends in **1/20** — and that 2 Sep WB800 entry
is also where the wiki's "cool on ice 5 min" and "5,000 × g for 10 min" come from, both of
which differ from the SOP (ice 10 min, 5000 rpm 5 min). The OD 0.85–0.95 window itself is
genuine, it is in the SOP, but no 168 prep was ever harvested in it — the 4 May one was
harvested at OD600 **0.7**.

### i. WB800 competent cells were never harvested at OD600 2.2 (WW-207)

Four WB800 preps are recorded: OD600 0.907 (18 Aug), 0.91 (31 Aug), 0.926 (2 Sep) and the
Lu-method prep of 13 Sep, which logs 2.082 at 14:20 and **2.346** at 14:45. "2.2" is not
any of them. The trehalose buffer (0.5 M), the four washes and the 1/40 resuspension are
all confirmed on 13 Sep.

### j. "Electroporation ran on strain 168 only" is false (WW-205)

WB800 was electroporated at least twice: 15 Sep (ACCD and ABDI, 2.1/2.3/2.5 kV at 250 Ω)
and 1 Oct (`pSTK-Exp2-CcaSRv1-SamyQ:Acds-V2t1 / LBE WB800 2.5kV 25µF 250Ω 20261001`,
screened by colony PCR on 3 Oct). The September gel sheet has a lane
"V: ACDI electroporation in WB800". Also, 15 Sep tested ABDI at **200 Ω**, a resistance the
wiki's table does not list.

### k. 168 was pulsed at 2.0 to 2.2 kV, not 2.1 to 2.3 kV (WW-208)

The 10 May trials are 2.0, 2.2 and 2.1 kV at 300 Ω and 25 µF (plus two arced trials at
∞ Ω), and the 12 May gel note says "2.2 kv, 300Ω". Recovery volume and time are
inconsistent across the files: 1 mL SOC-RM for 4 h at 200 rpm (10 May), 1 mL for 3 h at
225 rpm (SOP), 2 mL (19 Sep). The wiki's "2 mL SOC, 3 h, 200 rpm" is a blend of all three.

### l. The DNA gel is not always 20 mL (WW-149)

Everything else on that page checks out — 100 V for 30 min and 5 µL per well in every gel
entry from July to October, safety dye always 1 µL per 20 mL (so 1:20,000 is right), and
0.8 %, 1 % and 2 % gels all cast. But August alone casts 20, 40, 60, 80, 100 and 120 mL
batches. "20 mL agarose in 1X TAE" should become "per 20 mL" or lose the number.

### m. Hydroponic rig: 270 µL and 2.2 mL ½ MS, not 250 µL and 2 mL 0.1x MS (WW-177)

The 30 Jul entry: "Add 0.8% agar into 48 lids (270 µL each)" and "Add 2.2 mL of ½ MS medium
into 48 tube racks". The string **`0.1x MS` does not appear anywhere in the raw files** —
the hydroponic medium protocol is ½ MS at 2.3 g/L. The 48 positions, the punched lids
(3 mm holes) and the 4 °C stratification are all right.

### n. The chlorophyll conflict resolves toward Experiments, with a caveat (WW-178)

`Protocol/Chlorophyll Extraction.docx`, headed "updated procedure", is the 80 % acetone /
A663 / A645 / Arnon version, with 10 stainless steel (304) balls and 200 µL into 3 wells
per sample. **95 % acetone, 649 nm, 665 nm and Lichtenthaler do not occur anywhere in the
corpus**, so the Results §7 trial-4 description has no raw-file support and should be
checked with whoever wrote it. Two caveats on the protocol itself: it freezes at −80 °C
**overnight**, not for 10 min (the wiki says 10 min), and it adds 4 mL of acetone while the
equation takes V = 2 mL — an internal inconsistency in the team's own file.

### o. Minor: the 19 September Level 2 gel confirms, but check the 1 September one too

WW-150 is confirmed by the 19 Sep entry ("M: 3kb ladder", X:ACDI, 375/632/661 bp). Note
there is a near-identical Level 2 gel on **1 September** with a 3 Kb ladder and the same
three expected sizes, tested at 1:5 and 1:7 — if the wiki figure caption means that one,
the date on it is wrong.

### p. Minor: the seed count differs by plate shape (WW-175)

"18 seeds in two rows of nine" on the 3 cm / 5 cm / 4 cm template is verbatim in
`Protocol/Agar Application of Protectant.docx`, so it is confirmed. But the circular-plate
runs in the notebook plant 25 seeds (5 × 5 template) or 40 seeds per plate, and that same
protocol section says 7 days in the growth chamber where section A and the wiki both say 4.

### q. Known notebook hygiene problems, for whoever does the unit pass

The September notebook's own "Common mistakes" header asks for `degrees Celsius -> ℃`,
`ul -> µL`, `23444g -> 23444 g`. The raw files still carry: `25 kv` for 2.5 kV (8 Aug),
`23kv` for 2.3 kV (July), `capacity: 25 ul` for 25 µF (SOP), `2.5nM dNTP` for 2.5 mM,
`2.5 µm dNTP mix` for mM (23 Jul), `1,7900 g` for 17,900 g (2 Sep), `0.5µg` of restriction
enzyme where µL is meant (20 Aug), `Date: 2026919` (19 Sep), `TEB buffer` for TAE (1 Aug),
and `WN800` for WB800 (8 Aug). None of these changes a fact, but any script that parses the
notebook will trip on them.
