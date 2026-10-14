# B8_WM_a — fact check against Discord

72 facts in the batch. Verdicts written: 22. The other 50 have no Discord evidence and were left alone.

## Counts
- confirmed: 8, all high confidence — WM-003, WM-004, WM-020, WM-021, WM-022, WM-023, WM-026, WM-035.
- annotate: 14 — WM-001, WM-016, WM-017, WM-019, WM-024, WM-025, WM-034, WM-057, WM-058, WM-074,
  WM-078, WM-080, WM-081, WM-083.
- conflict: 0.

## Read in full
corpus-gems: Phase2/dry-math-sims (+ its Member thread), Phase2/dry-protectant-mutation (+ Member),
Teams/📐-drylab (end to end), 📐-drylab/DryLab Notebook, outreach/9_5 Public Forum Event, and targeted
reads of Phase2/plant-model-establishing, Teams/wetlab, Teams/wetlab-progression, Teams/wetlab-notice.
corpus-research: all 📈-math-model threads, 🦾-protectant/ACCD, BoPep4 Design Strategy, Multiple Sequence
Alignment, 0725 Alanine Substitution, 0725 Tandem Repeat Analysis, 0912-1010 Modeling Goals, codon-opt and
big-picture listings. Everything else was grepped with about 90 patterns (numbers with and without
separators, Chinese terms, date spellings).

## The two documents that carry almost everything
Nearly all the evidence is in two PDFs attached in Teams/📐-drylab, not in chat text.

1. **DNPH_ACCD__zh.pdf**, posted by Timmy 2026-10-07 21:21. A full ACC-deaminase activity report dated
   7 October, built from DNPH.xlsx FlexA A540 readings, n = 1. It confirms, verbatim, the whole assay
   block: the A540/OD600/mU table for WB800, csn and samyQ; 7.25 mU/mL; 44.0 mg/L/h and 1.056 g/L/day;
   the standard curve (slope 0.18695, R² 0.99907, residual SD 0.00715, LOD/LOQ from 3.3σ/m and 10σ/m);
   the 110 vs 160.6 µL correction of factor 1.460; the reaction conditions (43.03 mM ACC, pH 8.0, 30 °C,
   30 min, WB800 blank); and the signal-does-not-track-biomass argument.
2. **MERGED_MODEL_REPORT_EN.pdf**, posted by ethanl 2026-09-25 16:30. The Block 1 county yield model
   report. It confirms the permutation result (rain by stage, p = 0.010, +19.8 kg/ha; warm nights and
   humid days cost nothing), the 399 county-seasons / 11 counties / 2007-2025 common row set, the ERA5
   feature source, and the second-crop term list.

These are the archived sources earlier passes could not find. Both should be dropped into the project
folder before the 21 October freeze.

## Most important findings
1. The 32% in WM-001 does not match the headline model: the report gives second-crop MAE 591 → 378
   (36%) under leave-one-year-out, and 400 (32%) with the search nested inside each fold. The page
   should say which number it is quoting.
2. WM-058: the report describes the assayed material as filtered **culture supernatant** from the
   WB800/csn/samyQ cultures and never mentions a reactor or permeate batch. The page's "reactor
   permeate" wording looks wrong, and open question 6 stays open.
3. WM-025: the DNPH report writes that ACCD acts as a **homotrimer** and uses 36,800 g/mol as a
   provisional monomer mass "to be recomputed for the actual construct" — against the page's homotetramer
   of ~144 kDa. Separately, Ryan told Timmy on 7 July that the ordered acdS sequence is most likely from
   *Pseudomonas entomophila*, and that *P. putida* was used only for the structure work.
4. WM-024: the team's own report lists kcat and Km as **not determined** ([待補], ranges 0.5–10 s⁻¹ and
   1.5–17 mM) and says one operating point cannot separate Km from Vmax. The page states 3.4 mM / 146 min⁻¹
   as settled.
5. WM-019: the second-crop term list matches the report's best model term for term; the first-crop list
   adds warm nights and hours ≥ 35 °C, which that model does not contain and which the report explicitly
   recommends dropping.
6. WM-034: the report flags that all three OD600 readings were outside the spectrophotometer's linear
   range (1.319 / 1.529 / 1.661 after a 2× dilution), so absolute biomass is understated; only the
   ranking is safe.
7. WM-023: the 1.460 correction is confirmed but the report says it still needs written confirmation
   from Gabriel; if 110 µL had a reason, every number must be recomputed.
8. WM-081: the "16" traces to Felix's 25 July alanine-scan dossier ("invariant across all 16
   characterized Pep-family peptides"); the "17" traces to the source paper's figure caption, "Alignment
   of nine BoPROPEPs and eight AtPROPEPs". Two different sets, two different counts.
9. WM-074: Phoebe Chen's June message gives the same chlorophyll coefficients and fresh-weight
   normalisation, but writes OD633 where the page writes OD663 — almost certainly a typing slip, worth
   one check against the protocol document.
10. WM-078: the published paper Timmy circulated spells it **BoPEP4**, which is a tiebreaker for the
    site-wide spelling decision.

## Closest misses
- WM-057 / WM-006 (2026 blind test): the 25 September report says "2026 is v3's frozen blind test and
  was left untouched" and proposes the same protocol for the second crop — one day before the claimed
  26 September freeze, but it never states a date or the 7.9% / 8.8% county errors.
- WM-005, WM-007, WM-008, WM-010: the stress-index lookup table exists in Discord
  (ethanl, 2026-08-29, csi_lookup_table.numbers) but that sheet is the **optogenetic** CSI-to-lux chain,
  not the first-crop yield lookup, so it settles none of these.
- WM-012, WM-013, WM-015, WM-039, WM-065, WM-075: plant channels discuss the exact experiments
  (ACCD spray pre/co/post treatment at 75 and 100 mM NaCl, root length, chlorophyll extraction, the
  spreadsheets) but no message carries the fresh-weight, root-length or chlorophyll **values** on the wiki.
- All Block 3 dose and payback numbers (WM-038 to WM-050) and all geospatial numbers (WM-059 to WM-073):
  nothing in this pull. The GIS channel is not in the export, and the fertilizer, parcel-count and payback
  figures appear nowhere else.
