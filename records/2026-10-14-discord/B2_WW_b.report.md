# B2_WW_b — fact-check against the Discord record

## Counts
- Facts in batch: 71
- Verdicts written: 31
- confirmed: 12 (WW-106, WW-115, WW-120, WW-126, WW-128, WW-129, WW-160, WW-161, WW-162, WW-201, WW-205, WW-254)
- conflict: 1 (WW-130)
- annotate: 18 (WW-105, WW-108, WW-116, WW-119, WW-131, WW-134, WW-141, WW-142, WW-163, WW-168, WW-203, WW-207, WW-242, WW-251, WW-255, WW-262, WW-263, WW-264)
- No evidence, left alone: 40, including every Registry-accession fact (WW-187 to WW-199, WW-192, WW-211), the protocol facts (WW-145, WW-149, WW-151, WW-169, WW-170, WW-176, WW-177, WW-180), the 23 August TiO2 calibration numbers (WW-110 to WW-113), WW-118, WW-135, WW-164, WW-165, WW-230, WW-245, WW-246, WW-259 and the ELISA milestone M-001.

## Channels read end to end
Teams/🧬wetlab, Teams/wetlab-progression, 🧬wetlab/Cloning Constructs, Phase2/part-development, Phase2/dry-bioreactor, Phase2/dry-lpa, and the back half of Teams/📐-drylab (August to October). Phase2/stress-protectant, Phase2/plant-model-establishing, Teams/wetlab-notice, Teams/🧍-human-practice and the whole research server were searched by grep on many spellings.

Two attachments were opened and read as data: the two raw bioreactor logs Chars posted on 9 October as "Experiment 4", and the 16 August pressure-to-flow spreadsheet. These settle seven facts on their own.

## Most important findings

1. **The raw logs for run 4 exist in Discord and settle five facts at once.** Chars posted `record_20260902_020658.csv` and `record_20260906_090304.csv` on 9 October labelled "Experiment 4". File 1 runs 2026-09-01T13:06Z to 16:16Z (3.12 h, OD600 0.008 to 0.238); file 2 starts 10.24 h later and runs 102.44 h unbroken (OD600 0.831 to 3.770). That is WW-120 exactly.
2. **Results and Engineering describe one run, not two (WW-126).** Engineering's "53 h 22 min" window ends at window index 6400 of file 2, elapsed 192,148 s, OD600 2.4474, on 4 September. Its quoted start OD600 of 0.1738 comes from file 1. The instructor's 13 October answer is correct.
3. **WW-128 and WW-129 are exact.** Window 6400 carries cumulative flow 1,132,192 mL and TMP −0.00045 bar; window 171 of file 1 carries feed/retentate/permeate 0.2412 / 0.1874 / 0.2133 bar with TMP −0.000703. Every published pressure is in the logs.
4. **WW-130 is wrong.** Bubble rejection did not stay at 0 % — `od600_bubble_pct` is non-zero in 4,374 of 12,259 windows, maximum 42.9 %, mean 4.6 %, and the first window already reads 35.7 %. What did stay clean is `od600_valid`, true in every window.
5. **The hollow-fibre module is 150 cm² over 8 fibres (WW-160, WW-105).** Timmy's 4 July "authoritative hardware parameters" post on the research server gives model HF-E-MI-M020-10-60-P, 0.2 µm, 150 cm², 8 fibers, 1.0 mm bore, and says in its own heading that it "replaces M+/200 cm²/11-fiber record". The same post confirms the LEIRONG ZP4000-N79H pump and its 230–2600 mL/min range (WW-161) and the BP8G-AGA transducer at 1.0 % FS over 0–1 MPa (WW-162).
6. **WB800 was electroporated (WW-205).** Chars on 14 September: "We never success electroporation on WB800 yet" — an attempt, not an absence. chloe's 26 September letter to the SubtiToolKit donor: the team "successfully electroporate our 10k+ bp Level 2 multi-gene circuit assembly into Bacillus subtilis WB800 and begin Light Plate Apparatus (LPA) testing". The Experiments page's "168 only" is wrong.
7. **S15A and G17A are sequence-confirmed, not merely designed (WW-201).** Sophie Chen's 26 September post gives successful Level 0 reads for S15A, G17A and WT.
8. **LEA14 is the team's own word (WW-254).** It is absent from wet lab construct labels but used constantly by the protectant and dry lab side from May onwards, and chloe's donor letter lists "output constructs (LEA14, ACCD, BoPep4)". The wiki prose is traceable after all.
9. **DiOPAL appears nowhere in either Discord server (WW-263).** The team says LPA or Light Plate Apparatus throughout, including in a letter to an external donor.
10. **The reactor was "version 4" / "prototype 4" in early September (WW-264, WW-262).** Chars and jacquelyn both use that numbering for the run Engineering calls cycle 5 on prototype VIII, and Chars labels the run itself Experiment 4.
11. **The 16 August sweep really was paired (WW-242).** The spreadsheet has Background and HFM columns over the same eight pump settings (10 to 24 by twos). The background fraction computes to 37 % at the lowest setting and 52–56 % at the other seven, matching neither published range.

## Came closest without settling
- **WW-119**: Discord carries the exact phrase "Western blot (J in WB800)" — but in Sophie Chen's 29 August progression post, not in the notebook. The wiki's wording was taken from Discord, so the event is real and the citation is wrong. Logged as annotate because the claim is about the notebook.
- **WW-115 / WW-116**: Noah Tau's own figure caption states the 3.8 % median, the R² above 0.999 and the no-transform decision word for word, and names the mg 5 monotonicity exclusion. It does not give the per-instrument R² digits (0.9999, 0.9998) or the second exclusion at mg 37.
- **WW-168**: the only logged LPA run uses two wavelengths at three intensity tiers, which fits, but lists units 01 to 12 only, not twenty-four positions with four replicates.
- **WW-141**: ABDI clone V7 was sequenced successfully on 4 September, well before the 23 September snapshot that says the Level 2 sequencing date is blank. The blank is a record gap.
- **WW-108**: Chars rejected the magnetic pump on 16 August, not 23 August, and no message gives the sub-200 mL/min figure; 263 mL/min is confirmed as the selected operating point from a separate figure.
- **M-001**: the string ELISA does not occur once in either server. Nothing to report.
