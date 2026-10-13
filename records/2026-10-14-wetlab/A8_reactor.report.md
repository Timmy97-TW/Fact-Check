# A8 — Bioreactor runs, timeline, runs 1-4, batch forecasting (65 facts)

**8 confirmed, 2 conflict, 55 skipped.**

As expected, the wet lab folder is not the hardware folder. The only reactor material in the
whole corpus is three notebook entries: 2026-06-06 plus its 2026-06-07 continuation (run 1),
2026-06-14 (run 2), and 2026-09-02 "Bioreactor Sampling" with the 2026-09-05 SDS-PAGE that
follows it (run 4 blot). Run 3 (21 July to 8 August) does not appear in the wet lab notebook at
all, and no pressure, flow, shear, probe or membrane number is anywhere in these files.

## Settled

| id | what the notebook settled |
|---|---|
| WW-046 | 0.304 is the 27 h reactor reading; 0.480 is labelled "Sampling from medium" |
| WH-008 | both the 0.304 and the 0.480 are in the wet lab record, not only the hardware notebook |
| WH-005 | 30 min steps to 390 min, then 24/25/26/27 h, 27 h reactor only — hardware notebook wrong |
| WH-001 | run 1 is dated 20260606 in the notebook (the raw workbook had hours only) |
| WH-015 | 25 rows, 11:00 to 18:10 on 14 June — the "2.5 hours" in the Dry Lab Notebook is wrong |
| WH-012 | 14 June, 200 rpm stir, 37 °C all on the record; sampling point is not |
| WW-051 | the missing flask details: 500 mL flask, 20 mL culture medium, 200 rpm orbital shaker |
| WH-049 | three fractions confirmed, 44 h confirmed; times are 16/18/20/22/24/40/42/44 h |
| WH-045 | **conflict stands** — the 2 Sep SOP adds a fifth flow number, ~385 mL/min |
| WH-235 | **conflict** — the wet lab side of run 1 ends 7 June at 27 h, not 10 June |

## Not settled — needs the hardware team's own logs

These are engineering measurements with no counterpart in the wet lab folder. Noah, Anton,
Joshua or Chars's own rig logs are the only source.

- **Pump, pressure and flow:** WW-001 (pump calibration table, no date anywhere),
  WW-098 (0.0327 bar zero-flow intercept), WW-099 (the threefold spread at 405 mL/min),
  WW-104 (jumper test, 46-55 % vs 43-56 %), WW-108 (magnetic pump rejected at 263 mL/min),
  WW-128 (1,132.2 L cumulative), WW-129 (feed/retentate/permeate pressures),
  WW-130 (0 % bubble rejection), WH-004 (94 mL/min in run 1 — how was it measured?),
  WH-250 (the 14 August manual series; the page's table stops at dial 22).
- **Membrane and module:** WW-002 (0.2 µm vs 50 kDa), WW-065 (2,000-6,000 s−1 wall shear),
  WW-066 (scale-up vs scale-down), WW-105 (150 cm²/8 fibres vs 200 cm²/11 fibres).
- **Probes:** WW-092 (DO and pH probes not autoclavable), WH-245 (first probe tests 5 Aug).

## Not settled — fits and models (no fit output in the corpus)

The raw OD series for runs 1 and 2 *are* now in hand (June notebook), so these can be
recomputed rather than asked about, but the notebook states no fitted value:
WH-009 (run 1 flask r = 0.309 /h), WH-016 (run 2 reactor 1.195 /h — the notebook series
reproduces roughly 1.18 /h between 12:02 and 13:25, so the figure is plausible),
WW-135 and WH-040 (perfusion model R² 0.991 — which model gives 0.991 is still open, and
numbers.json has 0.9875/0.9557), WH-117 and WH-118 (Kalman walk-forward; needs
walkforward_0902_results.csv, which is not in the wiki repo), WH-027 ("28 times slower at
22 °C" — no source file and no 37 °C/22 °C pair in the notebook to derive it from).

## Not settled — run 3 (21 July to 8 August)

Nothing. The July and August notebooks contain no bioreactor, photometer or OD-run entry at
all; July 21-31 is wholly cloning, gels and plants. Only Chars's photometer log can settle
WH-019 (22 °C incubator setting), WH-022 (2,132 points at 336 h vs the 243 h usable window),
WH-024 (the 7 d 21 h 28 m dashboard snapshot), WH-243 (pump failure at ~217 h) and
WH-244 (3 Aug, reactor + photometer + plants in one incubator). WH-032 is the one that
*should* have been in the wet lab notebook and is not: there is no four-quadrant streak of the
reactor culture logged in July or August, so the "168 colony morphology" claim has no plate
record — ask whoever streaked it for the plate photo.

## Not settled — run 4 (1 to 6 September)

- WH-034 (chassis) and WH-036 (37 °C): the 2 Sep sampling entry never names the strain or the
  incubator temperature. Its blot uses an anti-His-tag antibody, which is consistent with a
  tagged construct but names nothing. Only Chars knows what was inoculated on 1 September.
- WH-120 (three log pieces, 3.2 h / 10.2 h gap / 102.4 h), WH-126 (102.4 h vs 53 h 22 min),
  WH-039 ("longest run" 102.4 h vs 434 h), WH-042 (0.84 vs 0.1738 start OD): all live in the
  photometer CSVs and the page prose, not the wet lab notebook. There is no 1 September
  inoculation entry of any kind.

## Not settled — timeline and wiki questions (not mine)

WH-233, WH-234, WH-238, WH-241, WH-248, WH-252, WH-253, WH-255, WH-256, WH-258, WH-259,
WH-260, WH-261, WH-262 are hardware-notebook or human-practices dates with no wet lab
counterpart; WW-003 (which versions have DBTL entries), WH-134 (which run scores the
registered forecast), WH-136 (whether leftover 1008 file names count), WH-011 (was run 1's
22 °C measured or assumed — the 6 June entry records no temperature at all) and WH-002
(see below) are judgement calls or need a person.

## Things worth raising

1. **Run 1 ends 7 June, not 10 June.** The notebook's last reactor reading is 27 h on the
   7 June continuation, and there is no bioreactor entry again until 14 June. The Milestone
   "6 to 10 Jun" window and the `260610 test1 no stir.xlsx` filename are both unexplained by
   the wet lab record. (Patched as a conflict on WH-235.)
2. **The 0.480 is not a serum-bottle control.** The notebook line is literally
   "Sampling from medium : 0.480". Engineering's "medium reservoir" is right; the Results page
   wording should change.
3. **The only strain designation for the June reactor runs is "Bacillus subtilis 169"**
   (14 June entry). No such strain exists; it is near-certainly a typo for 168, and the 6 June
   entry names no strain number at all. So the wiki's change from WB800 to 168 for runs 1 and 2
   still has no wet lab support — WH-002 stays open, and this typo is what to ask about.
4. **Run 1's first day actually goes down, not up.** Reactor OD600 runs 0.172, 0.108, 0.101,
   0.194, 0.130, 0.178, 0.166, 0.112, 0.123, 0.136, 0.126, 0.125, 0.083, 0.131 over 0 to
   390 min, while the incubator arm climbs 0.172 to 0.987. The "reactor 0.17 to 0.37" on the
   Digital Twin page quietly splices the 24-26 h readings onto a first day that ends at 0.131.
   Worth saying so on the page.
5. **Five different numbers for run 4 loop flow:** 94 (Bioreactor 2.5), 263 (operating point),
   300 (stated ceiling), ~371 (raw CSV) and ~385 mL/min (the 2 Sep sampling SOP, PWM 100).
   The SOP number is the one written by the person doing the sampling during the run.
6. **Blot caption says 14 to 44 h; the notebook's earliest sample is 16 h.** The "nine points"
   is nine lanes per gel (three fractions at three times), not nine timepoints.
7. **A date typo in the notebook itself:** the run 1 continuation entry is dated "20200607"
   while its title says "Continuous from 20260606". Harmless, but the wet lab may want to fix it.
8. **"Add 20 mL on culture medium to bioreactor & flask (volume 500mL)"** is ambiguous — 20 mL
   of inoculum into a 500 mL working volume, or 20 mL total in a 500 mL flask? WW-051 and the
   run 2 growth rates depend on which. Worth one question to whoever ran it on 14 June (that
   entry carries no "Done by" line).
