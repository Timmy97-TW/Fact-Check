# A1 Cloning — 74 facts

**36 confirmed, 7 conflict, 31 skipped.**

Conflicts: WW-006, WW-008, WW-010, WW-075, WW-125, WW-180, WW-201.

## Could not settle

### No sequencing records exist anywhere in the wet lab folder (7 facts)
There is no sequencing-report file in `_FILE_LISTING.txt` and none of the six monthly
notebooks ever logs a sequencing submission or result — `grep -i sequenc` returns only
protocol boilerplate ("before DNA sequencing", "amplify bacterial sequences"). So every
"sequenced on <date>" claim is unverifiable from these files. For each one the colony PCR
date and the clone IDs *are* confirmed on the gels:

- **WW-060** module D, clones B2 and B4 — confirmed on `20260626 Colony PCR A1-A12 B1-B10`,
  "B: 1C-Pveg-RBS0-CCaR-B0015 … Note: B2, B4 Positive clone". This also answers the item's
  own question: the B2/B4 labels are **lane-group labels on that gel**, not module names, so
  module D's B2 and module B's B2 (from the 24 June `s11` gel, "B: PliaG - RBS0 - CcaSm3 -
  B0015 … Positive clone") are different isolates. Only the 1 Jul sequencing date is open.
- **WW-062** module B, clone B2 — colony PCR 24 June confirmed (same 24 June `s11` gel). 3 Jul open.
- **WW-063** module E, clone G3 — confirmed on `20260624 Colony PCR s12`, "G: pSTK-1D-PcpcG2-veg-EEBD-Csn:AmilCP-B0015 … Note: G3 Positive clone". 3 Jul open.
- **WW-064** module F, clone H10 — H10 is on `20260626 Colony PCR H9-H12` ("H: 1D-Pveg-EEBD-RBS0-Csn:AmilCP-B0015") and is miniprepped on the 6 July gel at 3585 bp. 3 Jul open.
- **WW-069** module K, clones D10 and D14 — confirmed on `20260709 Colony PCR A D`, 1696 bp,
  "Note: D10, D14 positive clone". 14 Jul open.
- **WW-084** module A, clones A1–A3 — confirmed on `20260730 Colony PCR (A, L in E. Coli)`,
  "A1, A2, A3 Liquid culture 7/30 -> sequencing all positive". The 31 Jul date is open **and
  looks too early**: see the date problem below.
- **WW-106** SamyQ-BoPep4 Level 0 sequenced 19 Aug, "clones V4, V19 and V7" — the 14 August
  gels send **Q1-4, Q1-10, Q1-19** (v2t1) and **Q2-5, Q2-7, Q2-13** (v2t2) to liquid culture.
  V4/V19/V7 looks like a shorthand for v2t1 #4, v2t1 #19 and v2t2 #7, but nothing in the
  folder says so, and no 19 August event in the folder is a SamyQ-BoPep4 sequencing.
  **Ask Chars/Gabriel for the Genomics sequencing reports — that one folder would close all seven.**

### Needs the Registry pages, not the wet lab folder (13 facts)
WW-187 to WW-199 (accessions `BBa_K1232004`, `BBa_K823002`, `BBa_K823000`, `BBa_K143012`,
`BBa_K592002`; the 32-row / 6-accession / 8-kit / 18-new counts; and the category + function
one-liners for PtagC+RBS, L3S2P21, RBS0, B0015, ccaS-m3, PcpcG2-veg, EEBD-RBS0) and WW-211
(eight parts from the kit, no kit accession). The wet lab corpus has no part datasheets or
Registry exports. What it does give: the 18 June notebook miniprep lists **20 STK kit parts
in hand**, including `pSTK-0A-Pveg(BBa)`, `pSTK-0A-PlepA`, `pSTK-0A-PliaG`, `pSTK-0AB-PtagC+RBS`,
`pSTK-0B-RBS0`, `pSTK-0D-B0015`, `pSTK-0D-L3S2P21` — so the part identities are real, only the
accessions and the counts need the Parts page. Whoever curates Parts (not wet lab) can close these.

### Only a person can answer (4 facts)
- **WW-004** MoClo 2.0 all unsuccessful. The design premise is in the notebook: 6 June
  "Golden Gate Assembly … Vector (pJUMP29-1A)" with uncloned PCR/pTwist inserts, screened by
  colony PCR on 8 June. But **no results are recorded for that colony PCR and there is no
  8 June gel in the June gel folder at all** — consistent with "data is not shown", which is
  exactly why only Chloe can confirm "all trials were unsuccessful".
- **WW-005** Professor Huang's judgement. The terminator swap itself is in the files
  (`pSTK-1D-PcpcG2-veg-EEBD-RBS0-Csn-LEA-bkdb cold double.dna`, the 1–6 August
  "Csn:LEA-bkdB Cold" gels, then back to B0015), but no date or reasoning is written down.
- **WW-012** nine of thirteen Level 1 modules. The gels name clones construct by construct but
  there is no master build table in the wet lab folder; counting it from gels would be my
  arithmetic, not the team's record.
- **WW-141** no Level 2 sequence end to end. Nothing in the folder records Level 2 sequencing;
  the last Level 2 work is the 19 September junction gel and the 25 September electroporation
  of ACDI into WB800. Confirming a negative from absence is not safe — ask whether anything was sent.

### Partly settled, one piece missing (7 facts)
- **WW-009** second colony PCR after electroporation into B. subtilis. The practice is confirmed
  (30 Jul "Colony PCR (K in B. Sub)" 842 bp; 31 Jul "(J in B. Sub)"; 19 Aug J1–J8 after
  electroporation). But "sharp bands at the expected sizes" is not supportable: **the expected
  size for J in B. subtilis is written three different ways** — `1145(?)` on 31 July (with the
  lab's own question mark), "around 615" on 12 August, and 1195 on 19 August. Ask wet lab which is right.
- **WW-011** clone I6 could not be located. The 27 July gel note reads "I3 and I6: 7/27 Liquid
  culture; 7/28 Miniprep/sequencing?", but from 1 August onward **only I3** appears (1 Aug
  miniprep 165 ng/µL, 1 Aug EcoRI digest at 3757 bp, every later ACDI assembly). Nothing says
  I6 was lost or never stocked.
- **WW-049** the move into the SubtiToolKit. The kit is real and `pSTK-1A`–`1D-sfGFP` are the
  Level 1 destinations (WW-209), but the **11 June date has no support**: the earliest kit entry
  is the 18 June "Collecting miniprep from 20 STK kit parts", the 18 and 21 June sizing gels,
  and the first STK Golden Gate on 22 June. 11 June in the notebook is only "Agar Prep".
- **WW-076** module G unsuccessful, "G2 carried the right band and then failed its digest".
  G2 is real and was digested: 26 July miniprep (PcpcG2-veg-EEBD-RBS0-csn:LEA, 3296 bp) and
  26–27 July BsmbI 2-site digest expecting 1214 bp insert + 2082 bp vector. **No outcome is
  written for that digest** and no repeat count is given.
- **WW-080** 27 vs 28 July for module J sequencing. Unresolvable: J9 was miniprepped 26 July and
  digested 26–27 July "before DNA sequencing", so sequencing was on or after 27 July. No record picks a day.
- **WW-082** eleven of twelve colonies. The 30 July gel gives the twelve lanes A1–A12, the
  1833 bp expected size and "A1, A2, A3 Liquid culture 7/30 -> sequencing all positive", but the
  **band count 11/12 exists only in the photograph** — no text in the folder states it.
- **WW-102** (patched confirmed) — same caveat: "every lane banded except Q1-6" is only in the photo.

## Things worth flagging

1. **A sequencing date that cannot be right.** Module A clones A1–A3 and module C clones C6/C9
   were first miniprepped on **1 August** ("Miniprep (liquid culture 0731)", BioDrop A1 107,
   A2 89, A3 94, C6 98, C9 78 ng/µL) and EcoRI-checked the same day "before moving on to golden
   gate". The wiki has module A sequenced 31 July and module C sequenced 24 July — both before
   any plasmid existed. Either the wiki dates are submission dates for something else, or they
   are wrong.
2. **1,145 bp is module J, not module A.** Results attributes 1,145 bp to module A
   (PtagC+RBS-Ho1:PcyA-L3S2P21). In the raw files `1145(?)` appears exactly twice, both times as
   "J: Pveg-EEBD-RBS0-Csn:ACCD-B0015 | Csn F | ACCD R | 1145(?)" on the 31 July B. subtilis gel.
   Module A's two real sizes are 2,231 bp (Pveg version) and 1,833 bp (PtagC rebuild). (WW-081)
3. **Module C's clone is C10 on the gel, C9 everywhere after.** The 22 July gel note says
   "(C6, C10)"; the 1 August miniprep, the 1 August EcoRI digest and the August figure deck all
   say C6 and C9. One of the two labels is a typo and the wiki follows C9. (WW-075)
4. **Module H is not a no-clone module.** H3, H7 and H1 exist, were miniprepped, digested and
   sent for sequencing, and there is a gel literally titled `20260813_PCR_of_H_after_sequencing.jpg`.
   The build record's "No clone and no date on record" is wrong. (WW-010)
5. **The Level 2 junction sizes changed with the primers.** On 30 August the three junctions were
   ccaR F/Csn R **760**, CcaSm3 F/CcaR R **632**, pcyA F/CcaSm3 R **411**. From 1 September they are
   **661**, **632**, **375** with `L2`-prefixed primers and `csn rv-seq`. The wiki's 375/632/661 are the
   September set; the August numbers are a different primer generation, not errors. None of the
   `L2 …` primers are in `2026 primer list.docx`.
6. **The ratio sweep was three ratios, not two.** The 26 August Golden Gate built ACDI at
   **1:3, 1:5 and 1:7**; only 1:5 and 1:7 reached the 1 September junction gel. The wiki never mentions 1:3.
7. **Csn R has no Golden Gate tail.** Every other conversion primer carries the
   spacer–BpiI–overhang–BsaI–overhang tail; `Csn R` in the primer list is a plain 19-mer,
   `CAAGTAATGAGATCGCTGC`, and is used as a screening/junction primer. The "thirteen primers"
   count also does not match the list, which has 27 "Convert MoClo to STK" primers. (WW-180, WW-181)
8. **The His tag is C-terminal, and two constructs have none.** Across every annotated SnapGene
   product the 6xHis sits at the 3' end of the CDS and the secretion signal (SamyQ/Csn) at the 5'
   end. The exceptions are the AmilCP cargoes, which carry no 6xHis at all, and the BoPep4
   variants, which are built as `…_1-23_NHis` with an **N-terminal** His matching the
   `NHis-Bopep4` reverse primer. That is three different answers to open item 37, each true of a
   different construct family. (WW-200, WW-008, WW-201)
9. **Constructs on the wiki that the cloning products do not have:** there is no `ACDE`/`ABDE`
   device file although both were assembled and screened on 3–4 August (`W: ABDE`, `V: ACDE`,
   1045 bp, all failed). Conversely the folder has products the wiki never mentions:
   `pSTK-EXP1-PtagC+RBS-GanA-Gala-L3S2P21`, `Pveg-RBS0-mCherry-B0015`, `Pveg-RBS0-mScarlet-B0015`
   (screened 25 July at 1164 and 1149 bp), and `pSTK-EXP1-Pveg-Bopep4-15-23`.
