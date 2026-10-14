# B3_WH_a — hardware facts vs Discord

68 facts checked. Verdicts written: 29 (confirmed 5, annotate 24, conflict 0). 39 facts have no Discord evidence at all.

Confidence: 4 of the 5 confirmations are high (WH-045, WH-076, WH-085, WH-116); WH-039 is medium because Discord settles the direction but not the 434 h figure. Two annotations are medium (WH-009, WH-016).

## Read in full
Phase2/dry-bioreactor, Phase2/dry-fluorometer, Phase2/dry-lpa, 📐-drylab/hardware notebook, 📐-drylab/DryLab Notebook, Teams/📐-drylab (whole channel), research server 🧪-bioreactor/* and od600-spectrophotometer/* and 📈-math-model/Bioreactor Calculations. Teams/🧬wetlab, Teams/wetlab-progression, Teams/wetlab-notice, General/* and the outreach channels were swept by pattern (reactor, membrane, shell, lumen, photometer, blot, kDa, DNPH, plating, pump, pressure, leak, sensor, Kalman) and the hits read in context.

## Most important findings
1. **94 mL/min is a vendor figure.** The 4 July hardware spec gives the module throughput as "94 mL/min @2000 s⁻¹". Run 1's loop flow was almost certainly never measured (WH-004).
2. **The module spec says 8 fibres, 150 cm²**, and says so while explicitly replacing a "200 cm²/11-fiber record". Everything built on 11 fibres — wall shear 4064 s⁻¹, the Hagen-Poiseuille ratio, the computed holdup — rests on a fibre count the team's own authoritative spec contradicts (WH-064, and it bears on WH-062/066/068).
3. **The 16 August pressure analysis was AI-written.** Chars: "The Excel is the data and pdf is the result analysis by claude." That is the likeliest origin of the 0.084 bar / 0.90–0.96× numbers the 25 August report carried, and Noah was still quoting 0.90–0.96× on 5 September (WH-059, WH-062, WH-066).
4. **Biomanufacturing's "longest run 102.4 h" is wrong.** The July run was still logging past 200 h (Ethan, 21 Aug) after Noah started it on 21 July (WH-039).
5. **The 10 October SiO₂ run happened**, watched live by the team. Development, Bioreactor and Measurement still describing it as ongoing or not measured are stale pages (WH-085).
6. **The slim photometer still has a reference channel**, by Noah's own description of the unit measured on 10 October — against Photometer 5.3's single-beam account (WH-095).
7. **3.8 % and the 5 mg exclusion are the team's own**, from Noah's 5 September figure caption, which also says both instruments sat above R² 0.999 over the whole series (WH-076, WH-077, WH-082).
8. **Run 1 was in a 22 °C incubator, not at room temperature** (Timmy's 10 June drylab report), and that report names 168 only for the 1 June flask curves, not for the reactor pair (WH-011, WH-002).
9. **Both ACCD molecular weights are traceable**: ~36 kDa is a line in the 4 July spec note, while Chloe's 21 September blot reading puts the monomer at 38–42 kDa (WH-050).
10. **Leaf temperature and wetness hardware: 2 October confirmed** by Timmy's own announcement (WH-116).

## Came closest without settling
- WH-103 (19 July photometer): three of four claims confirmed verbatim by Chars, but the same thread describes titanium dioxide in the cuvette, not a live culture. Annotated, not confirmed.
- WH-016: Ethan's 21 August survey caps every short test at 0.921 h⁻¹, so the 1.195 h⁻¹ reactor fit sits outside his range — suggestive of a disagreement between two analyses, not proof of one.
- WH-052 / WH-051 (DNPH): a DNPH ACCD protocol was posted on 7 October and DNPH wiki writing was assigned on 12 October, but no assay result of any kind appears in Discord.
- WH-019: 21 July in the incubator is confirmed; the incubator setting never appears, so 22 °C stays unsourced.

## No evidence at all
WH-010 (pump-head leak), WH-022/024/105 (dashboard snapshots), WH-032 (streak plates), WH-036, WH-040, WH-042, WH-051, WH-053/054/055/056 (every shell-side plating and the 4 September membrane-leak remark), WH-058, WH-065, WH-069/071/072/073 (pump and flow-meter calibration series), WH-075, WH-080, WH-081, WH-083, WH-086, WH-089/090/093, WH-096–102, WH-104, WH-108/109/110, WH-117. The wet lab notebook, the Google Sheets and the Prof. Chang meeting notes live outside Discord, which is where most of these would be.
