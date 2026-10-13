# A9 — LPA, DiOPAL, containment, R3 trust layer (43 facts)

**2 confirmed, 6 conflict, 35 skipped.**

The one strong source is `Protocol/Optogenetic LPA Assay.docx`. It settles the plate format
(24-well plate, six columns of four, twelve tubes used), the tube layout (3 red, 9 green),
the strain (CcaSR in *B. subtilis* WB800), the light levels as written (green 220 / 510 / 3850 lux)
and the sampling plan (every 2 h at 2, 4, 6, 8, 10 h; 200 µL per tube, half for OD600, half for
western blot). Everything else in this slice is either hardware/electronics, dry-lab software, or
a 19 September result that the wet lab files do not contain.

## Patched

| id | status | what settled it |
|---|---|---|
| WH-121 | confirmed | Plate map: CcaSR in 3 rows of each green column, 1 row of each red column; step 4 aliquots into twelve tubes. |
| WH-202 | confirmed | "24-well LPA plate", plate map six columns × four rows, "The remaining 12 slots stay empty". |
| WH-123 | conflict | Figure 1 caption says reds are **all** 168 lux; the plate map in the same file labels them Red 220 / 510 / 3850. The wiki's 390 and 2,940 lux appear nowhere. |
| WH-124 | conflict | Protocol plate map gives green 220 / 510 / 3850 lux, corroborating Measurement. No per-LED kLux, duty cycle or measuring position exists in the wet lab files. |
| WH-127 | conflict | The protocol has **no 24 h point at all**: step 7 is 8–10 h total, step 8 samples at 2, 4, 6, 8 and 10 h. The wiki's "24 hour mark" is not in the protocol. |
| WH-132 | conflict | The only 19 Sep western blot in the notebook is "Double check LEA, ACCD in supernatant" (Gabriel), lanes ACCD/LEA under strain headings 168 and WB800 — not LPA samples. Green/red-labelled westerns are dated **29 September**. |
| WH-120 | conflict (note only) | The assay is written up; no execution of it is recorded in any month. |
| WW-025 | conflict (note only) | Same. Absence in the wet lab files, not proof. |

## Could not settle

### Needs the hardware team (Anton, Noah) — no electronics data exists in the wet lab corpus
`LED`, `PWM`, `MOSFET`, `Arduino`, `Bambu`, `kLux`, `duty cycle`, `520 nm`, `660 nm`, `PPFD`
and `µmol` return **zero hits** across every notebook, protocol and gel file. These need the
hardware notebook / Anton's own measurement sheet:

- **WW-018** forty LEDs measured, twenty-four kept — needs Anton's LED measurement sheet.
- **WW-019** 26 % green / 22 % red as-bought spread — same sheet.
- **WW-020** sorted groups hold to 1–2 % — same sheet.
- **WW-021** tiers come from PWM, not LED selection — needs the duty cycles, which are written nowhere.
- **WW-022 / WH-207** snapped post, black holder, 2→4 wall loops, repair not retested — needs Anton; the overnight test is undated.
- **WW-023** readings are lux, not photon flux — *partially supported*: the LPA protocol expresses every light level in lux and no `µmol`/PPFD figure exists anywhere in the corpus. The "has not been computed" half can only be confirmed by Anton.
- **WW-043** well-to-well evenness never measured — needs a 24-position lux map; none exists.
- **WW-070** third iteration assembled 17 July — hardware notebook only.
- **WH-203** 520/660 nm vs ~535/~670 nm — the protocol gives no nm at all. Anton.
- **WH-204** Uno R4 WiFi, three MOSFETs — Anton; the BOM is blank.
- **WH-205** 31 / 63 / 100 % duty — Anton. Note these ratios cannot produce 220 : 510 : 3850 lux (a 3:1 ratio of duty giving a 17:1 ratio of lux), so either the duty figures or the lux figures are wrong.
- **WH-206** 211 × 164 × 108 mm, 18 mm pitch — Anton / the CAD.
- **WH-208** Castillo-Hair half-maximal 4.66 µmol m⁻² s⁻¹ — the protocol **does** cite Castillo-Hair *et al.*, Nat Commun 2019;10:3099 (plus Gerhardt 2016 and Haller 2025), but the 4.66 value is not in any raw file and neither is the lux→PPFD factor. Anton / Timmy.
- **WH-209** NT$355.99 PLA spool — no purchase record in the wet lab files. Anton.
- **WH-211** red LED spread, 20 reds vs "two dead out of the packet" — Anton / Noah.
- **WH-213** LED sorting date (9 vs 17 vs ~4 July) — Anton / Noah.
- **WH-271** 16 May pipeline split; **WH-275** 7 Aug repair — notebook-only dates, no raw record. Anton / Felix.

### Needs the dry lab (Timmy) — software outputs, not wet lab
- **WH-108** 99.5th percentile / 120 h window; **WH-109** alarm shares; **WH-110** step detector 23 % / 0.8 %. None of these numbers exist in the wet lab corpus; they need `out/sentinel.json` and the R3 scripts.
- **WH-130** r = 0.279–0.317 h⁻¹ and **WH-131** held-out error 7 % vs 29–68 % need `lpa_growth_fit_20260919.json`, which is not in the repo.
- **WH-129** which green arm plateaus highest — needs the 19 Sep plate reader export.
- **WW-026** modelled permeate activity 0.039–14.8 mU mL⁻¹ — model output, Timmy's call.

### Needs the 19 September plate reader export
- **WH-125** OD600 0.97–1.08 at 24 h, background 0.059 — no OD600 time course for that plate exists in the notebook; none of 0.97, 1.08, 0.059, 1.056, 1.083, 0.910 or 1.014 appears as an LPA reading anywhere.
- **WH-126** run not repeated — only the person who ran it knows.
- **WH-277** OD readings posted 3 October — no raw trace of the handover.

### Containment — nothing in the wet lab corpus
- **WW-014** no log reduction / no detection limit. The only shell-side plating procedure in the notebook is the 2 September bioreactor sampling by Chars: "Sample the shell side medium at 16hr and 24hr. Spread on the LB plate overnight antibiotics" — one plate per time point, no dilution series, no colony counts, so nothing from which a log reduction or a detection limit could be read. Consistent with the wiki's wording but not stated by it.
- **WW-015** cell dimensions, **WW-016** waste handling, **WW-017** biosafety exam and two-month training: none of membrane pore size, cell size, waste autoclaving, bleach treatment, exam or training appears in any notebook or protocol. These are documentation facts for the safety lead, not wet lab records.
- **WW-048** June plate incubation time/temperature. The June notebook has **no containment plating entry at all**: 6 June and 14 June are bioreactor *growth* tests (OD600 every 30 min, bioreactor vs incubator/flask) with no shell-side plate and no pump leak recorded. The only shell-side plating written down is 2 September.

## Things worth flagging

1. **The protocol contradicts itself on the red light levels.** Figure 1 caption: reds all at 168 lux.
   Plate map in the same file: Red 220 / Red 510 / Red 3850 lux. The wiki took the caption's 168 lux
   for "weak red" and then scaled the other two by the green ratio — a third version that is in no file.
2. **The 31 / 63 / 100 % duty cycles cannot give 220 : 510 : 3850 lux.** One of the two sets is wrong.
3. **No 19 September LPA run exists in the electronic lab notebook.** The five entries dated 20260919
   are miniprep (Chloe), electroporation (Sophie C), PCR (Sophie C), gel electrophoresis and Level 2
   GGA, plus a western blot (Gabriel) on supernatant LEA/ACCD. No lux, no OD600 time course, no LPA
   entry in any month, April to October. The LPA page's "no run under the LPA on record yet" matches
   the wet lab files; Measurement, Digital Twin and Milestone do not.
4. **There is a candidate light experiment, but it is dated 29 September, not 19 September.**
   `GEL photos/2026-09 September` has westerns with lanes VG3 VR3 VG6 VR6 VG20 VR20 VG25 VR25 and
   13G 13R 16G 16R (V-series are the V21/V25/V27 colonies cultured on 27 Sep). Worth asking whether
   this, and not a 19 September plate, is the actual optogenetic run.
5. **The lab autoclaves at 127 °C for 20 minutes, not 121 °C.** Every media-prep entry across May to
   August says 127 °C / 20 min (one hydroponic medium entry says 121 °C / 20 min). The wiki's waste
   figure of 121 °C for 15–30 minutes is not from any raw file, so WW-016 is quoting a standard, not
   the lab's practice.
6. **"168" is also a strain name here.** The 19 Sep western lane block reads "168 ... WB800" —
   *B. subtilis* 168 and WB800, nothing to do with 168 lux. Easy to confuse when searching.
