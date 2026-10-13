# A2_protein — 48 facts

**6 confirmed, 7 conflict, 35 skipped.**

Confirmed: WW-039, WW-040, WW-086, WW-093, WW-094, WW-117.
Conflict (raw file contradicts, or contradicts in part): WW-038, WW-095, WW-119, WW-131, WH-054, WH-055, WM-159.

---

## Things worth knowing before the office

**No raw wet lab file anywhere states a kDa value for an ACC deaminase band.** Every western-blot
table in the gel-label files (20260802, 20260807, 20260824, 20260929) has its "Expected Size (kDa)"
column left empty, and no notebook entry gives a band size. The only kDa numbers in the archive are
the 20260802 protein-marker slide marks (180, 130, 100, 75, 63, 48, 35, 28). So all four wiki figures
— 35–40, 41, 42 and 36 kDa — are reads off photographs. The fusion's computed mass appears nowhere in
the wet lab files either. One question to Chars/Gabriel settles WW-038, WW-086, WW-117, WW-118,
WW-132 and WH-050 at once: *what mass do you read for the ACCD band, and against which marker mark?*

**The 6 and 7 August blots look like one blot, not two.** The sample list on the gel-label image
"20260807 western blot" (S1–S6 = 25, 10, 150, 250 mM from 0805 and 25, 150 mM from 0806) is
character-for-character the "Gel one" loading of the 20260806 SDS-PAGE entry — the gel the 20260806
Western Blotting entry transferred and left in antibody overnight. There is no western blot entry at
all on 7 August. So WW-094 and WW-095 are probably the same membrane photographed the next morning,
and the Dry Lab Notebook's "third August blot" may be a double count. Also the salt series is
10 to 250 mM, not 25 to 250 mM.

**The reactor time course is three gels over two days and has no 14 h point.** 20260902 (Chars):
lumen cell lysate / lumen medium / shell medium at 16, 18, 20 h. 20260905 Gel 1 (Sophie C): the same
three fractions at 20, 22, 24 h. Gel 2: 40, 42, 44 h. Eight time points, nine lanes per gel, nothing
dated 4 September, and no 14 h sample in the archive. The wiki's "sampled every two hours at 14, 16,
18, 20, 22, 24, 40, 42 and 44 h" fuses three gels and invents the 14 h point.

**There is no 29 August "Western blot (J in WB800)" entry.** The blot ticked off on 29 August is the
20260828 SDS-PAGE entry by Chars (gel cut in half, left half to PVDF with anti-His CST, right half
Coomassie), loaded with the cell lysate and medium from the 20260827 extraction. That entry names
neither the construct nor the strain, so "J in WB800" is an addition made downstream.

**The only shell-side plating in the whole wet lab archive is one line.** 20260902 Bioreactor
Sampling, by Chars: "Sample the shell side medium at 16hr and 24hr. Spread on the LB plate overnight
antibiotics". That line says the 24 h is a *run* time point and the plates were incubated *overnight*
with no temperature — so Measurement's Figure 23 caption is right and "read after 24 h at 37 °C" is
not. It plates two samples from one session, which may be where "two platings" comes from. No volume,
no result, no lumen plate, and no June / run-1 plating entry exists in any monthly notebook.

**No activity assay exists, and no data file for one exists.** DNPH appears exactly once in the whole
archive — 20260902, as the planned future use of frozen samples ("for ELISA and DNPH assay").
"Berthelot" appears nowhere. `_FILE_LISTING.txt` has no activity, ELISA or DNPH data file of any kind.
The October notebook stops at 8 October and its 7 October entries are transformation, golden gate and
colony PCR only — there is no 7 October permeate assay in the wet lab record at all (WH-051).

**The His-tag position really is both ways, in the team's own files.** The 2026 primer list carries
two reverse primers for the same peptide: `Bopep4` reverse appends a C-terminal His6, and
`NHis-Bopep4` reverse ends the peptide at a free …GGHN + stop. In the cloning products,
pSTK-0C-SamyQ-Bopep4-v2t1 and -v2t2 (SnapGene-created 2026.8.19, i.e. *after* 16 August) are
C-terminally tagged; only Bopep4-1-23-WT (2026.9.26), Bopep4-G17A (2026.9.26) and
SamyQ-Bopep4-S15A (2026.9.28) put the 6xHis upstream of the mature peptide. Every ACCD and LEA
construct in the folder is C-terminally tagged. So Peptide Design's "every construct ordered after
16 August" is wrong as written, but the N-terminal design is real. The three late-September files
match D-03, D-02 and D-06 of the WM-172 order list residue for residue (SamyQ signal + HHHHHH +
mature 1-23 / G17A / S15A, +1 residue H, no spacer).

---

## Could not settle, grouped

### Band reads — needs Chars or Gabriel to read the images (one conversation)
- **WW-118** (eight ladder bands, 180–28 kDa, on 24 Aug): the eight marker marks are written down
  only for the 20260802 blot; the 20260824 entries list "ladder (5 µL); ladder (2 µL)" with no marks.
- **WW-132** (two opposite readings of the reactor blot) and **WH-050** (shell-side band at ~42 kDa,
  run 4): no raw file reads any lane of the 9/2 or 9/5 gels, and the shell supernatant lanes exist but
  carry no annotation. "Run 4" does not appear in the wet lab files at all — that numbering is the
  hardware notebook's.

### Activity assays — needs the data file; only Chars/Gabriel know where it is
- **WH-051** (7.25 mU/mL permeate, 7 Oct): no assay entry on 7 October, no permeate sample, no data
  file. Needs the raw export behind 7.2514 mU/mL and which batch it came from.
- **WH-052** (DNPH vs Berthelot): no purchase record, no assay entry for either method. Needs Chars
  to say when DNPH arrived and which runs used which method.

### Hardware / reactor records — not in the wet lab folder
- **WH-053** (run 1, 2 mL shell side, 6 June): the June notebook has bioreactor growth tests (OD600
  only) and no plating. Lives in the hardware notebook — ask Gabriel / abby.
- **WH-056** (leak reported 4 Sep), **WH-057** (0.2 µm pore vs 0.25–1.0 µm cell), **WH-058** (breach
  and leak alarms untested): nothing in the wet lab archive. WH-057 needs a citation from Timmy;
  WH-056 needs Chars.

### Dry lab / modelling — outside this corpus by design
- **WM-160 to WM-171, WM-173, WM-174, WM-176 to WM-186** (24 facts): HADDOCK, AlphaFold3, ViennaRNA,
  Pearce/Tang/Yamaguchi literature, the audit and the pre-registered re-run. None of this is in the
  wet lab files. Two partial corroborations worth noting: WM-174's "sequence-verified AmilCP construct
  uses the same signal peptide" — a SamyQ-TAT-HA-AmilCP construct does exist at Level 0 and Level 1
  Expression, alongside several Csn-AmilCP ones; and WM-177's homopolymer run is in the *codon
  optimisation* source, not the cloning products (the mature CDS in pSTK-0C-Bopep4-1-23-WT has no
  A-run longer than 4).
- **WM-172** (six cassettes to synthesis on 20 Aug): no order sheet in the wet lab folder. The
  20 August notebook entry is "Level 1 Golden Gate Assembly of Bopep4", not a synthesis order. Three
  of the six cassette architectures do exist as SnapGene files, but created 26–28 September — design
  files, so they do not date the order.

---

## Alarming

1. **WW-131 is marked critical and the time course on the wiki is not the experiment that was run.**
   Three gels became one, eight time points became nine, and 14 h exists nowhere in the archive.
2. **The 7 August blot may not exist as a separate experiment** (see above). If it is the 6 August
   membrane, the wiki counts one August blot twice and the "not usable" verdict has no written source.
3. **Peptide Design's "every construct ordered after 16 August"** is contradicted by the team's own
   SnapGene files dated 19 August, which are C-terminally tagged.
4. **The 7 October ACCD activity number has no trace in the wet lab archive** — no entry, no sample,
   no file. The October notebook ends on 8 October.
5. **Bioreactor's "two platings of shell-side medium, both of which [grew nothing]"**: the notebook
   records the two plates but records no result for either. The "no colonies" outcome is nowhere in
   the wet lab notebook.
