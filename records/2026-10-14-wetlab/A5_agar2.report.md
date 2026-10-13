# A5_agar2 — agar sets #7 to #11, 18 Aug salinity plates, heat pre-test, buffer vs ACCD, Results headline plant numbers

**4 confirmed, 6 conflict, 13 skipped** (23 facts).

Confirmed: PA-151, PA-156, PA-166, PA-173.
Conflict (patched with what the raw files say): WW-027, WW-088, PA-152, PA-155, PA-174, PA-181.

Important scope note: the corpus holds **no** `Agar/` folder — no `Chlorophyll content for Agar plate.xlsx`, no `(for wiki)` workbook, no `All agar salinity tests_.xlsx`, no decks. Every fact whose value lives only in those files is unsettleable here; the notebooks and protocols were the only evidence available.

## Could not settle

### Numbers that exist only in the chlorophyll workbooks
No notebook anywhere carries an OD or a mg/g value for an agar plate. The only agar chlorophyll **extraction** entries in the whole corpus are 10 Aug (set 7 trial 1), 22 Aug (heat pre-test) and 5 Aug (set 6, flagged below) — and none of them records a result, only the plate layout.
- **PA-155** (set 7 "trial 3" 24 Aug, original vs for-wiki) — needs the two workbooks side by side; only Abby K can say which column was pasted. (Patched with the run's identity, which the notes do settle.)
- **PA-169 / WW-103** (heat pre-test, three versions) — needs the workbook; see the arithmetic below, which narrows it but does not close it. Abby T / Abby K.
- **PA-176, WW-134** (set 8 ACCD chlorophyll, the 0.106 / 0.830 / 1.092 triplicate) — needs the workbook. Abby K.
- **WW-133** (set 7 trial 4, 5 Sep, the 3.5-fold claim) — the 5 Sep reading has no notebook entry at all; needs the workbook plus whoever ran that plate.
- **WW-089** (six trehalose sets, root lengths 11.00 → 14.71 mm, SE ~2.3) — the notebooks log fresh weight for sets 5 and 6, never root length. Needs the root-length measurement sheet.
- **WW-090** (hydroponic salinity set 1, 0.0828 mg/g vs 1.251 per plant) — the 4 Aug hydroponic fresh-weight entry is headed "Hydroponic experiment set ?" and stops mid-procedure with no results. Needs the hydroponic sheet; Alex ran the boxes.

### Runs with no notebook record at all
The Plant notebook's last agar entry is 19 Aug; the August lab notes' last plant entry is 26 Aug (soil); the September and October lab notes contain **zero** plant entries.
- **PA-170** (18 Aug salinity concentration plates, "no vernalize" vs stratified 18 Aug, Day 1 before the incubator date) — there is no plant entry on 18 Aug in any notebook, and 50 mM NaCl appears nowhere after May. Only Abigail / Naomi / Audrey H can date these plates.
- **PA-178** (buffer vs ACCD sown 7 Sep), **PA-180** (set 9 official ACCD), **PA-193** (set 10 BoPEP4), **PA-198** (set 11 LEA) — nothing in the notebooks or protocols. The plant model team is the only source.
- **PA-174** is patched, but the judgement it needs (does the "data we can use" comparison still stand?) is still the team's.

### Not mine to decide
- **WW-103** (whether to publish the 15 Aug heat numbers) and **WW-088**'s second half (which n the statistics used) are editorial/statistical calls.

## Alarming things in the raw files

1. **WW-027 is wrong as written.** The wiki says "No file in the archive names what went into the boxes". The notebooks name it precisely: 600 µL CH protectant into box C2 (14 Aug, pre), C3 (15 Aug, co), C4 (16 Aug, post), the same for D2/D3/D4 on 19–21 Aug, and 600 µL into box 4 (25 Jul) and box 1 plus 10 mL 3M NaCl into boxes 1–4 (28 Jul). The heat conditions are logged too: incubator **set 37 °C, actual 33 °C** (15 Aug) and **set 50 °C, actual 35 °C** (20 Aug). Alex did all of it. This sentence should come off the Results page.
2. **There were four CH peptide agar runs, not three.** Pre-treatments on 4 Aug (trial 1), 13 Aug ("trial #2"), 17 Aug ("set #7 trial 3") and the batch sown 19 Aug. The run pre-treated 13 Aug has no chlorophyll extraction entry, which is exactly why no "trial 2" sheet exists. The wiki line "trial 2 and trial 3: dates not recorded" is contradicted by the notebook, and "three trials, 1 August to 5 September" undercounts.
3. **The 9 Aug fresh-weight table is entered twice, with different labels and a different control.** Plant notebook: control 0.1537 g, salted rows labelled "w/ 100mM NaCl". August lab notes, same day, same three people: control **0.1587** g, the same rows labelled "without 100mM NaCl". The salt/no-salt swap that PA-151 blames on the chlorophyll sheet is also a disagreement inside the notebook. Someone has to say which labelling is real before the set 7 trial 1 figure can be trusted.
4. **Set 7 plates held 23–25 plants, not 9.** The 9 Aug table gives plant counts of 23, 24, 23, 25, 25, 25, 24. Any per-plant normalisation of set 7 that assumes nine is wrong.
5. **The heat pre-test plates had ants in them.** 21 Aug: "Ants climbing inside the incubator ... ants climbing into the heat stress pretest agar plates". That is the run behind PA-169 / WW-103.
6. **The heat pre-test was read on 21–22 Aug, not 15 Aug.** Fresh weight 21 Aug, chlorophyll extraction 22 Aug; 15 Aug is only the pre-treatment spray date. Both wiki pages date the numbers 15 August.
7. **Arithmetic on PA-169, as far as it goes.** Using the control's layout-block ODs (mean A663 = 0.8717, A645 = 0.3940), fw = 0.1219 g and V = 4 mL (the volume both the protocol and the 22 Aug entry use): as labelled → **0.49 mg/g**; with the two wavelengths swapped → **0.68 mg/g**. The workbook says 0.6263, so neither reproduces it exactly, but only the swapped reading is anywhere near it — weak support for the team's transposition inference, not proof. Note also that the 22 Aug entry lists the wavelengths in the order "663, 645" while the equation takes OD645 first, which is a plausible way for the swap to have happened.
8. **The for-wiki heat numbers are internally inconsistent by a factor of four.** 35.48 / 2.9557 = **12.00** for the control, while the three treated rows give 20.19 / 6.6358 = 3.04, 17.32 / 5.8083 = 2.98 and 16.42 / 5.5588 = 2.95. The control row alone is divided by about four times as much as every treated row, and that single factor is what flips the ranking between the two versions of the sheet.
9. **The acetone volume V in the chlorophyll equation changes between runs.** 1 mL on 13 July, 4 mL in the agar protocol and in every August run, 2 mL in the current `Chlorophyll Extraction.docx`. Every mg/g figure scales with it, so cross-run comparisons on the wiki are only valid if V was the same.
10. **Set 6 chlorophyll was read at the wrong wavelength and the notebook says so.** 5 Aug: "A633 -> used the wrong wavelength this time, it should be 663". Set 6 is one of the six trehalose sets quoted in WW-089.
11. **No LEA14 or BoPep4 plant protocol was ever written.** All three application protocols (agar, hydroponic, soil) end with bare "LEA" and "Bopep4" headings and nothing under them, and no notebook entry in the corpus applies either to a plant. This is consistent with WW-028 ("never applied to a plant") but sits badly against PA-193, which reports a set 10 BoPEP4 deck with twelve plates photographed 3 Oct and a chlorophyll sheet dated 20261010. One of those two is wrong, and only the plant model team can say which. I did not patch WW-028 (critical) because absence of a record is not proof of absence of an experiment.
12. **The ACCD used around 23–26 Aug had no enzyme in it.** Soil protocol: "western blotting results show no ACCD in b. subtilis so the pretreatment groups that we have done for 0823 and 0824 were not valid(no rescue effectiveness)". The set 8 agar pretest was tested from 26 Aug and the protocol marks it "WITHOUT ENZYME ACTIVITY ASSAY TESTING".
13. **The formal ACCD protocol and the one actually used disagree on how the dose is delivered** (NaCl baked into the agar + 0.1 mL of 50 mU/mL pipetted and reapplied every 3–4 days, versus three sprays of both NaCl and ACCD onto the leaves). Both observe for 10 days, so the deck's Day 20 timeline is in neither. See PA-181.
