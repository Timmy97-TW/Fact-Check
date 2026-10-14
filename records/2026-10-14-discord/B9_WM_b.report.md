# B9_WM_b — fact-check against the Discord record

## Counts
- Facts in batch: 72
- Verdicts written: 24 (confirmed 1, conflict 1, annotate 22)
- Confidence: 20 high, 4 medium
- No evidence found, nothing written: 48

## Channels read end to end
- Phase2/data-physicalization, Phase2/dry-protectant-mutation, Phase2/part-development, Phase2/stress-protectant (main server)
- Teams/📐-drylab from August onward, Teams/🧬wetlab and Teams/wetlab-progression by keyword, outreach/9-5 Public Forum Event
- Research server: every 🦾-protectant thread (all 40+ files), all codon-opt threads
- Everything else swept with grep on numbers, residue names, tool names, dates and Chinese spellings

## Most important findings
1. **WM-112 conflict.** The wiki says the DisVis feasibility check never produced a result and that a WeNMR account is still needed. Felix posted two DisVis runs on the WeNMR server on 15 August (BoPEP4 WT active residues; BAK1 active residues) and reported results from them four hours later. He held WeNMR accounts all through August for HADDOCK, WHISCY and DisVis.
2. **WM-089.** The 14 July per-residue contact table gives position 18 one partner list: Glu324, Lys345, Asn347, Asp348, Phe371. Peptide Design and the MD pages each quote a subset, so the two pages do not actually contradict each other. The Asp320 / Glu296 numbering appears nowhere in Discord.
3. **WM-148.** The K18R entry on the run list is a docking job: HADDOCK run "BoPEP4-PEPR1_T1-2_K18R_DockTest" (23 July). The MD record is first BoPep4 WT (18 Aug), six jobs (20 Aug), three more (30 Aug), with no K18R MD anywhere.
4. **WM-107 confirmed.** 8 August: PEPR1 from 5GR8, BAK1 from 4MN8 (FLS2-flg22-BAK1), PEPR2 with no experimental structure, modelled with AlphaFold2/ColabFold and SWISS-MODEL. Files posted: PEPR1_template_5GR8_chainA.pdb, BAK1_chainB.pdb.
5. **WM-108 / WM-128.** Felix's "Finalized Inputs from Methodology" of 18 August carries the 41 active and 9 passive PEPR1 restraints and the apoplast pH estimate of 5.7–6.3 verbatim. The derivation (4.5 Å cutoff, both crystal copies) is not in Discord, and nothing addresses the pH 5.5 used by MD.
6. **WM-119.** The LEA14 boundary was never decided: both truncation 1-16 and 1-23 went onto the September send lists. Liviiii's ColabFold run (19 Sep, pLDDT 86 over the core) says the floppy front end stops around 20–23.
7. **WM-104.** The ACC deaminase runs the earlier pass could find no numbers for do exist — Sara posted five HADDOCK run links plus the ACCD active-residue list on 26 September under "ACCD: Sprints and Results". Ask Sara for the values.
8. **WM-173 / WM-159.** Wet lab sequence-verified pSTK-0C-SamyQ-Bopep4_1-23 in WT, S15A and G17A on 26 September, and N-His BoPep4 constructs appear in the 30 September cloning record. The N-terminal tag move is dated by the dry lab lead's 20 August message, right after the C-His MD job.
9. **WM-168.** The 16 August order decision exists as two PDFs posted that afternoon, but the lead says the six-hour docking analysis had just finished and he had not read the report yet — the fourteen-claim audit is machine output reviewed afterwards, not a team deliberation record.

## Came closest without settling
- **WM-114**: Asn23–Arg487 is given as 2.40 Å (with Asn23–Asp441 2.71 Å), but only one copy, so the 2.59 Å second copy and the Arg491 distance stay open.
- **WM-110 / WM-111**: the US-align transfer and the Kabsch refit are confirmed to have happened, by itz_bruce on 1 August, but no TM-score, identity or RMSD number was ever posted.
- **WM-096**: the two truncation designs appear as "2truncation mutation" and "3truncation mutation" (21 July) and neither reached the 27 July order; the Delta-1 / Delta-1-2 / Delta-1-3 names are never used in Discord.
- **WM-194**: the LED-per-stress idea and the paper-plus-styrofoam build are both in the planning record, but no colour scheme or flashing-frequency encoding.

## Silence worth noting
- Every data physicalization survey number (WM-187 to WM-193) is absent. The team ran a separate "GIS + Data physicalization" Discord server from 1 July (invite posted in General), which is not in this corpus; the Public Forum survey lives in a Google Doc. That server or the doc is where those numbers are.
- No MD number from the batch (98.7% occupancy, 2.81 Å, 30 ns, f-nat, ipTM, pLDDT 90.8, Spearman values) appears anywhere in either corpus; the MD results were published as GitHub Pages reports and discussed only by link.
- Nothing on AtPP2-B11, Koller and Bent, the eighteen-point mutation panel values, the codon-optimiser adenine run, or the LEA14 GRAVY value.
- The team's dry-lab analysis PDFs (0716/0721/0725/0816 reports, Point_Mutation_Panel.pdf) are in the attachment store but are AI-generated reports of the same lineage as the wiki text, so I did not treat them as independent evidence.
