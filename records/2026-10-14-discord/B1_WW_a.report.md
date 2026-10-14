# B1_WW_a — fact-check against the Discord record

71 facts in the batch, 25 with a verdict.

| verdict | count |
|---|---|
| confirmed | 5 (WW-002, WW-024, WW-065, WW-069, WW-075) |
| conflict | 4 (WW-010, WW-025, WW-027, WW-074) |
| annotate | 16 |
| no evidence | 46 |

Confidence: 15 high, 10 medium.

## Channels read end to end
- `Teams/🧬wetlab` (708 msgs) and its threads `Cloning Constructs`, `Regrouping`
- `Teams/wetlab-progression` (205 msgs)
- `Phase2/dry-bioreactor` (327 msgs)
- `Phase2/part-development`, `Phase2/kill-switch-design`, `Phase2/dry-lpa`
- `Phase2/stress-protectant` and `Phase2/plant-model-establishing` (searched plus read in part)
- Research server: `🧪-bioreactor/Part info`, `📈-math-model/AmilCP Prediction`, the three `⚫-lpa` threads, `🧪-bioreactor/Notebook`, `regulations/Bioreactor laws`
- `Teams/wetlab-notice` searched only; it is scheduling traffic with no experimental content.

## Most important findings

1. **WW-002 confirmed.** The written withdrawal exists. Timmy's 4 July hardware specification, posted as the parameters that supersede the earlier design spec, says the pore size is 0.2 um microfiltration and not 50 kDa, and asks that the "50 kDa MWCO" and "blocks OMV" wording be revised because 0.2 um passes small OMVs and debris.

2. **WW-025 conflict, and the biggest one in the batch.** The claim that the light-plate array never ran a CcaS/CcaR experiment on a live culture is wrong. On 19 September Timmy posted the layout of "LPA test1 ACCD lv2" with green at 100, 12 and 2 per cent and red at the same levels sampled from two hours; Chloe Wu posted the resulting gels on 21 September loaded as green 100 and green 12 at 2, 4, 6 and 8 hours; an OD results workbook from that run went up on 3 October. Dose, duration and an expression readout were paired.

3. **WW-074 conflict.** The "no OD600 time series of any kind" claim is wrong. The running log `od600_log_20260721_034533` was posted in instalments on 28 July, 4 August and 8 August, and Chars posted two June bioreactor OD600 workbooks as experiments 1 and 2 plus two September records as experiment 4. What was in the loop is still unrecorded, so only half the fact falls.

4. **WW-024 confirmed at 520 / 660 nm.** The authoritative build spec gives those two wavelengths. 535 and 670 nm appear nowhere in either server, so the Engineering page carries the wrong pair.

5. **WW-075 confirmed, and it names which wiki wording is wrong.** Olivia Lin's readout of the 24 July sequencing batch lists C6 and C9 successful and C1, C3, C8 and C10 unsuccessful. The gel note's "(C6, C10)" is the error; C9 is the second clone.

6. **WW-010 and WW-027 conflict.** Module H does have named clones and dates (H1 sequenced 12 August, a 740 bp H band on 14 September). And the hydroponic boxes' agent is named all through the progression posts: "CH bio peptide" / "CH protectant", added to pre, co and post arms on 14, 20 and 21 August.

7. **WW-021 annotate.** The duty cycles the status note calls unrecorded are in Anton Lin's 16 July sketch: 80, 160 and 255, annotated as roughly 31, 63 and 100 per cent.

8. **WW-065 confirmed with a caveat worth carrying.** 0.02 m², 11 fibres, 129 and 388 mL/min are verbatim in Timmy's 27 June table — but the 4 July spec explicitly replaces that record with 150 cm², 8 fibres, 94 and 282 mL/min, and Chars had already said 2000 s⁻¹ is only a recommended industrial minimum, not a requirement.

9. **WW-104 annotate.** Chars said in the same message that posted the 16 August pressure data that the PDF analysis was produced by Claude. Both percentage ranges on the wiki are downstream of an automated pass over one spreadsheet, so the spreadsheet is what needs recomputing.

10. **WW-003 annotate.** Through September the team worked with four prototypes, not seven: diagrams labelled P1 (6 June), P2 (14 June), P3 (10 July), and prototype 4 for the September integration run. Joshua says P3 was never drawn because it was not marked as a DBTL cycle at the time — which explains the bare headings.

## Came closest without settling

- **WW-096 (434 h).** The log file is named `od600_log_20260721_034533` and its last instalment went up at 14:06 on 8 August, which is about 442 hours of wall clock and fits 434 h far better than "past 400 hours". No verdict written: the evidence is a filename in an attachment field, not quotable message text.
- **WW-080 (J sequenced 27 vs 28 July).** The J9 result was announced on 30 July from a file carrying the order code SD260728019. Suggestive of 28 July, but the order code is not a statement by a person.
- **WW-084 (A sequenced 31 July).** Colony PCR on 30 July and the A1–A3 success are both confirmed, but the miniprep of A1, A2 and A3 is logged on 1 August, after the stated sequencing date.
- **WW-071 (19 July photometer).** Discord records that session in detail — TiO2 seen, four-fold overestimate, blank suspected, then 0.100 against the Bio-Drop's 0.149 — but gives neither the 20-to-8 per cent improvement nor the 6.4 per cent reference shift.
- **WW-089 (trehalose doses).** Alex Li names 1 mM and 10 mM as the set-5 best doses where the status note has 5 mM and 10 mM.
- **WW-088 (seven measurable seedlings).** Nothing in Discord about the 3 August salt-ladder plate counts. The only "nine plants per plate" line is from 22 September and belongs to a different trial.

## Nothing found
WW-004, 005, 008, 009, 011, 014, 016, 017, 018, 019, 020, 022, 029, 030, 031, 032, 033, 034, 035, 036, 037, 041, 043, 044, 048, 060, 062, 063, 064, 070, 072, 076, 077, 085, 088, 090, 091, 092, 095, 097, 098, 099, 103. The LED sorting track (018–020), the float plate (029–031), the photometer arithmetic (032–037) and the containment platings (014, 048) leave no trace in either server; that work lived in spreadsheets and the lab notebook, not in chat.
