# Dry lab consolidation, 14 October

What the dry lab actually did, pulled out of
`~/Documents/Claude/Projects/2026 iGEM Project Plant Stress` and written down in one place,
with the codon optimisation and the math model in full detail because those are the two
that carry numbers onto the wiki.

Every number below has a file beside it. Where a number on the wiki does not have a file,
it says so in plain words instead of being smoothed over. The Fact-Check consequences are
in section 5; `Fact-Check/data/facts.json` has been updated to match and rebuilt.

---

## 1. Milestone ledger

Dry lab only. Hardware milestones are already reconstructed in
`2026 iGEM Project Plant Stress/Discord/notebook-build/02_MILESTONE_MAP.md`.

| Date | Milestone | Where it lives |
|---|---|---|
| 2026-06-16 | ViennaRNA translation-initiation analysis, first generation. Four cargos folded in one RS-inclusive window; v2 and v3 order sets drawn and 8 constructs sent to IDT | `Codon Optimization/DNA files/vienna_rs_analysis/` (`REPORT.md`, `round1..6_*.py`), `IDT_order_Gabriel/`, `00_Deliverable_Reports/02_Codon-Optimization_ViennaRNA/` |
| 2026-07-16 → 07-19 | PEPR1 binding and BAK1 activation, PEPR2 dual-receptor selectivity with a pre-registered gate set, consolidated into the master report | `00_Deliverable_Reports/01_DryLab_BoPep4_Modelling/` |
| 2026-07-18 | Secretion design pass: K8 charge handle, signal-peptide short list, N-terminal truncation axis, readout/deconvolution plan | `Haddock/BoPep4-secretion-brief.md`, `by-topic/2026-07-18_Secretion-design_EN.pdf` |
| 2026-07-20 | **Second-generation codon optimiser.** Objective changed from a sum to a bottleneck, random sampling replaced by a certified deterministic descent. v2 / v3 / AprE / K8Q panel | `vienna_rs_analysis/codon_opt_sharp.py`, `run_sharp_opt.py`, `codon_opt_sharp_results.json`, `sharp_opt.log` |
| 2026-07-21 | Engineering-candidate report, the one the wiki is written from: 6 substitutions and 6 truncations, each through both optimiser stages with receptor metrics attached. Top substitutions K18R and K8Q, top truncations Δ1-3 and Δ1-2 | `vienna_rs_analysis/candidates_results.json`, `run_candidates.py`, `02_Codon-Optimization_ViennaRNA/2026-07-21_BoPep4-engineering-candidates_EN.pdf` |
| 2026-07-21 | Receptor-interface map. Both receptors bind the C-terminal 7–23; residues 1–6 make no contact — this is what licenses the truncation axis | `00_Deliverable_Reports/01_DryLab_BoPep4_Modelling/2026-07-21_BoPep4-receptor-interface_EN.pdf` |
| 2026-08-16 | TFF pressure characterisation, and the module of record changes from 150 cm² / 8 fibres to 200 cm² / 11 fibres | `0904_ProfChang_Update/site/assets/js/data.js` key `hyd`, `Math Model/releaf-model/reports/hydraulics.md` |
| 2026-08-23 | ACCD permeate acceptance threshold: the `≥ X` in the 10/5 milestone becomes **≥ 1 mU/mL**, from two independent derivations that land within 1.6× of each other | `00_Deliverable_Reports/28_ACCD_Permeate_Threshold/ACCD_Permeate_Acceptance_Threshold.md` |
| 2026-09-02 | **Level-1 model suite.** Growth refit, cross-flow hydraulics, diffusive transport, instrument audit, secretion scenarios, identifiability, sensitivity, sentinel | `Math Model/releaf-model/` (`reports/`, `out/`, `params/parameters.yaml`) |
| 2026-09-04 | All docking work consolidated into 11 study folders with the methodology audit first | `00_Deliverable_Reports/00_Docking_Analysis/` |
| 2026-09-25 | AIoT stress/control model finished: V1–V7 analyses, technical report EN + ZH, including the negative result | `AIoT Sensors/FINDINGS.md`, `reports/`, `docs/TECHNICAL_REPORT_*.pdf` |
| 2026-09-26 | 2026 first-crop stress-index forecast frozen before any county published | wiki `model/index.html` only — no archived source, see §4.1 |
| 2026-10-07 | DNPH ACC deaminase activity on culture supernatant: samyQ 7.25 mU/mL, csn 3.31, WB800 blank | wiki `model/index.html`; the FlexA raw file is not in the archive |
| 2026-10-12 | Students' own Block 1 / Block 2 / Block 3 conclusions land on the Math Model page | `records/2026-10-12-drylab-round.md` |
| 2026-10-13 | Fact-Check list opened, 1,297 facts | `Fact-Check/` |

---

## 2. Codon optimisation, in full

### 2.1 What was being optimised

The cassette is `PcpcG2-veg – EEBD – MF001 RBS – SamyQ signal peptide – cargo CDS – 6×His – stop`.
The thing being scored is not the protein, it is how open the mRNA is where the ribosome has
to land. Two regions, both read off a ViennaRNA base-pair probability matrix at 37 °C:

* **start+15** — mean unpaired probability of the 15 nucleotides from the SamyQ start codon
* **SD core** — mean unpaired probability of the MF001 Shine-Dalgarno core, `AAGGAGG`

Reference point: **ho1 = 0.681** on start+15, a gene that is known to work in this chassis.
Working threshold ~0.50.

**Window A (RS-inclusive)**, the only window used:
RS (28 nt) + MF001 (24 nt) + A spacer (1 nt) + SamyQ ORF (93 nt) + first 90 nt of the CDS
= 236 nt for the SamyQ groups; 218 nt for BoPep4 because its CDS is only 72 nt; 143 nt for
the Ho1 control. ViennaRNA 2.7.2, 37 °C, MFE + partition function, `noLonelyPairs` on,
`dangles=2`, T→U before folding. Synonymous sampling seeded at 2026, so the run is
reproducible; folding is deterministic.

The honest boundary, stated in `REPORT.md` and worth keeping on the wiki: the RS is excised
by homologous recombination in *B. subtilis*, so Window A is the **pre-recombination transient
mRNA**, not the steady-state functional one. It was chosen deliberately, not by accident.

### 2.2 Generation one, 16 June — rank by the sum

Round 1 diagnostic, wild type, Window A:

| Group | CDS opens | window nt | MFE | ens ΔG | start+15 | SD core |
|---|---|---:|---:|---:|---:|---:|
| BoPep4 | GILIG | 236 | −43.20 | −47.34 | 0.396 | 0.067 |
| LEA14 | ASLLD | 236 | −52.60 | −57.08 | 0.538 | 0.357 |
| ACCD | NLNRF | 236 | −42.10 | −46.63 | 0.563 | 0.088 |
| AmilCP | VIAKQ | 236 | −54.20 | −58.04 | 0.678 | 0.056 |
| Ho1 control | MSVNL | 143 | −20.60 | −23.39 | 0.681 | 0.104 |

Round 2 enumerated every legal synonymous recoding of SamyQ + the first 15 CDS codons and
ranked on `balance = start+15 + SD core`. Legal-candidate counts, from
`round2_tables.txt`: **BoPep4 33,395 · LEA14 34,342 · ACCD 40,899 · AmilCP 39,091**.
Best-by-balance per group:

| Group | start+15 WT → best | SD core WT → best | CAI | SamyQ codons changed | CDS codons changed |
|---|---|---|---:|---:|---:|
| BoPep4 | 0.396 → 0.732 (1.85×) | 0.067 → 0.641 (9.62×) | 0.61 | 26 | 13 |
| LEA14 | 0.538 → 0.841 (1.56×) | 0.357 → 0.534 (1.50×) | 0.69 | 23 | 9 |
| ACCD | 0.563 → 0.860 (1.53×) | 0.088 → 0.657 (7.45×) | 0.59 | 21 | 12 |
| AmilCP | 0.678 → 0.878 (1.30×) | 0.056 → 0.757 (13.45×) | 0.63 | 19 | 11 |

Two controls were run on purpose, and both earn their place in the write-up:

1. **Rank by the sum and you can be fooled.** The top BoPep4 variant on start+15 alone scores
   0.911 — and its SD core is **0.050**, more occluded than the 0.067 wild type it replaces.
   A variant can win the headline and close the ribosome binding site.
2. **The published low-GC / A>U greedy heuristic (Castillo-style) is not safe to copy.** Run as
   a literature control it improved BoPep4 (start+15 0.677, SD core 0.425) but it made **LEA14
   worse than its own wild type**: SD core 0.357 → 0.078, balance 0.895 → 0.747.

Order sets `v2` (SamyQ held at wild-type DNA, CDS recoded) and `v3` (SamyQ codons 2–31 also
editable) were written to GenBank and sent — 8 constructs, `IDT_order_Gabriel/`,
`order_gabriel.json`, `order_rows.json`. v2 versus v3 on the ordered designs,
`v2_v3_comparison.json`:

| Group | WT start+15 / SD | v2 start+15 / SD / CAI | v3 start+15 / SD / CAI |
|---|---|---|---|
| BoPep4 | 0.396 / 0.067 | 0.497 / 0.634 / 0.77 | 0.732 / 0.641 / 0.61 |
| LEA14 | 0.538 / 0.357 | 0.669 / 0.307 / 0.81 | 0.841 / 0.534 / 0.69 |
| ACCD | 0.563 / 0.088 | 0.773 / 0.203 / 0.75 | 0.860 / 0.657 / 0.59 |
| AmilCP | 0.678 / 0.056 | 0.677 / 0.583 / 0.79 | 0.878 / 0.757 / 0.63 |

v3 buys accessibility and pays in CAI. That trade is the whole argument for the second
generation of the optimiser.

### 2.3 Generation two, 20 July — rank by the bottleneck

`codon_opt_sharp.py`. Three changes:

* **Objective**: `J = min(start+15, SD core)`, normalised to the ho1 reference 0.681.
  Ties broken on higher CAI, then on higher `start+15 + SD core`. A design can no longer win
  by sacrificing one region.
* **Search**: max-CAI base sequence, then a block-coordinate descent over the codons that
  actually pair with the initiation region, then a polish pass that certifies a local optimum.
  No random draws.
* **Hard constraints, audited per design**: strictly synonymous · ATG start intact · cleavage
  site intact · no BsaI, EcoRI, XbaI, SpeI, PstI, NotI, HindIII · **no homopolymer ≥ 5** ·
  CAI floor 0.75 · GC between 0.35 and 0.55.

BoPep4 panel, from `sharp_opt.log` and `codon_opt_sharp_results.json`:

| Design | editable | max-CAI base J | best J | start+15 | CAI | GC | structures folded | certified local opt |
|---|---|---:|---:|---:|---:|---:|---:|---|
| **v2** (SamyQ fixed) — headline | 23 CDS codons | 0.054 | **0.528** | 0.757 | 0.779 | 0.421 | 4,437 | yes |
| v3 (SamyQ 2–31 editable) | +30 SP codons | 0.054 | 0.785 | 0.786 | 0.764 | 0.399 | 110,040 | no |
| AprE signal peptide swap | +28 SP codons | 0.054 | 0.715 | 0.719 | 0.798 | 0.446 | 60,390 | yes |
| v2 + K8Q | 23 CDS codons | 0.054 | 0.308 | 0.308 | 0.827 | 0.443 | 786 | yes |

Three readings that belong on the wiki because they are the result, not the method:

* **Optimising codon usage alone closes the ribosome binding site.** The max-CAI base sequence
  scores CAI 0.879 with `J = 0.054` — the SD core is essentially fully occluded. The wild type
  is CAI 0.886, `J = 0.067`. Codon adaptation on its own is not translation optimisation.
* **BoPep4's bottleneck goes 0.067 → 0.528 at CAI 0.779**, which is 0.775 of the ho1 reference,
  and it is a certified local optimum of the bottleneck rather than the best of a sample.
* **The charge handle costs accessibility.** K8Q, the secretion variant, tops out at `J = 0.308`
  — the only design in the panel that fails to clear half the reference. If K8Q is ordered, it
  is ordered knowing it initiates worse.

### 2.4 The 21 July candidate panel

`candidates_results.json`, 12 candidates, each taken through stage 1 (B. subtilis CAI) and
stage 2 (sharp bottleneck), with AF3/HADDOCK receptor metrics attached:

| Candidate | role | receptor verdict | stage 2 start+15 / SD / CAI |
|---|---|---|---|
| WT | reference | iptm 0.74, iPAE 2.96, 8/8 anchors | 0.674 / 0.614 / 0.761 |
| **K18R** | affinity, both receptors | PASS, lRMSD 1.03, 7/8 | 0.569 / 0.502 / 0.783 |
| **K8Q** | secretion, −1 charge | PASS, iptm 0.75, lRMSD 0.73 | 0.509 / 0.496 / 0.752 |
| K8E | secretion, −2 charge | PASS, iptm 0.73 | 0.509 / 0.494 / 0.758 |
| K8S | secretion, −1 polar | PASS, lRMSD 1.88 | 0.635 / 0.635 / 0.768 |
| K8A | negative control | **FAIL**, lRMSD 4.07, 5/8 anchors | 0.521 / 0.516 / 0.751 |
| Δ1-1 … Δ1-6 | N-terminal length ladder | receptor-safe (1–6 non-contacting; AF3 iptm 0.80–0.88 where run) | 0.590–0.687 / 0.606–0.646 |
| **Δ1-3**, **Δ1-2** | selected truncations | as above | 0.664 / 0.614 and 0.651 / 0.646 |

The ladder is also where the greedy heuristic falls apart hardest: its objective drops from
0.478 at Δ1-1 to 0.187 at Δ1-6, and it fails the manufacturing audit on 6 of the 12
candidates. The sharp optimiser passes all 12.

Separately, `truncation_codon_opt_results.json` carries codon-optimised versions of the
registry truncations **1-23, 7-23, 9-23 and 15-23**, SamyQ held fixed (the v2 setting).

### 2.5 Two things the archive settles that the wiki has not

* **The tag moved, and both halves of the story are in the archive.** The June and July
  codon-optimisation designs are C-terminal: `run_sharp_opt.py` builds the CDS as
  `mature + CATCATCATCATCATCAT + TAA`, and every full sequence in `order_rows.json` ends
  `…CATCATCATCATCATCATTAA`. The cassettes that actually shipped are not. The parts list for
  the 20 August order, `0823_Order_Report_Gabriel/BoPep4_0823_parts.csv`, carries the 6×His as
  `6xHis_tag_N_terminal` at nucleotides 489–506, between the SamyQ signal peptide and the
  payload, with the note *"N-terminal only; never fuse His to Asn23"*. So Fact-Check WM-159,
  a critical conflict across three pages, is settled: Peptide Design is right about the
  post-16-August orders, the Molecular Dynamics sentence about a decision to move the tag to
  the C terminus is wrong, and GRAFT Methodology's C-terminal 6×His is true only of the
  June–July design work.
* **The wild type has a run of eight adenines, not seven.** `GGATC` + `AAAAAAAA` + `GACC`,
  nucleotides 18–25 of the 69 nt mature BoPep4 CDS. The optimiser's own limit is four.
  The Peptide Design page says seven.

### 2.6 What this work does and does not prove

Straight from `captions.txt`, and the right language for a judge:

> **Proves**: synonymous recoding measurably changes the modelled accessibility of a fixed
> start region and of the SD core in the pre-recombination transient mRNA — and that the change
> has to be verified, because the published heuristic can make it worse.
>
> **Does not prove**: secretion efficiency, extracytoplasmic HtrA/HtrB quality control,
> steady-state post-recombination mRNA structure, or in-vivo expression.

---

## 3. Math model, in full

Three separate bodies of work carry the name "model". They are not versions of each other and
the wiki currently only shows the first.

### 3.1 Strand A — the wiki's Blocks 1, 2, 3 (`model/index.html`)

**Block 1, stress index.** County rice yields since 2001 (Agriculture and Food Agency), ERA5
for the historical fit, CWA stations live. 18 candidate stresses gathered, 2¹⁵ − 1 = 32,767
combinations of 15 of them fitted and scored out of sample; second crop ends 32% below the
no-weather trend; permuting rain by growth stage costs 19.8 kg/ha (p = 0.010) while warm
nights and humid days cost nothing; 399 county-seasons shared by all models; 2016–2025 county
error 365 against the trend's 419 kg/ha; 2026 forecast frozen 26 September, 4 of 16 counties
in at 7.9% against 8.8%.

**None of this has an archived source.** I searched both project folders on 14 October: there
is no fitting script, no candidate list, no permutation output, no county-season panel behind
these numbers. The nearest thing in the archive is a *different* model — see strand C, which
scores 458 county-seasons on a 671-row panel with ridge and GBM, not 399 on a 32,767-way
subset search. Block 1 therefore stays pending in Fact-Check in full. It is the single largest
unsourced block of numbers on the wiki.

**Block 2, optogenetic kinetics.** This one does have sources, and they check out.
`Math Model/releaf-model/params/parameters.yaml`, section `level2_reserve`, and the 4 July
hardware spec freeze both carry the CcaSR constants from **Castillo-Hair et al. 2019,
Nat. Commun. 10:3099**:

| Constant | Value | Status |
|---|---|---|
| Hill n | 1.88 ± 0.16 | confirmed |
| K½ | 4.66 ± 0.63 µmol m⁻² s⁻¹ at 526 nm | confirmed |
| t½ on | 105.1 ± 1.5 min | confirmed — the wiki's "105 minutes" |
| t½ off | 74.97 ± 0.39 min | confirmed — the wiki's "75 minutes" |
| y0 / Δy | 1,997.6 / 106,740.5 MEFL | the figure on the wiki uses 1,500 and 30,000 instead |
| Wavelengths | paper 535 / 672 nm, our hardware 520 / 660 nm | **offset unreconciled**, the yaml says so |

The attribution comment at `releaf-wiki/build/model_figures.py:63` reads
`# Ohlendorf et al. 2019, via the docx` next to `K_CCAS, N_CCAS = 4.66, 1.88`. The constants
are Castillo-Hair's. That comment is the error, not the page — it is a one-line fix.

Everything downstream of those two constants reproduces exactly. Inverting the Hill function
as `I = K½ · (f/(1−f))^(1/n)` and converting with the photon energy at 526 nm
(3.777 × 10⁻¹⁹ J, 0.2274 J µmol⁻¹) against the photopic efficacy 683 × 0.80 = 546 lm W⁻¹
gives **124 lux per µmol m⁻² s⁻¹**, and then:

| demand f | 0.05 | 0.10 | 0.25 | 0.50 | 0.75 | 0.90 |
|---|---|---|---|---|---|---|
| PPFD µmol m⁻² s⁻¹ | 0.97 | 1.45 | 2.60 | 4.66 | 8.36 | 15.00 |
| lux | 121 | 180 | 322 | 578 | 1,037 | 1,859 |

and the usable band `f = 0.015` (0.50 µmol, under the lamp floor) to `f = 0.94`
(20.1 µmol, over the 20 µmol ceiling) comes out exactly as the page states.

The ACC deaminase kinetics have a better source than the page cites — the team's own
8 August–23 August dossier, `28_ACCD_Permeate_Threshold/`, derived from Hontzeas et al. 2004:
**K_M = 3.4 ± 0.2 mM, k_cat = 146 ± 5 min⁻¹**, pH optimum 8.0 with essentially no activity
below pH 6.5. Two things in that dossier disagree with the wiki:

* **Subunit mass.** The dossier uses 41 kDa; `parameters.yaml` carries 37,636 Da for our own
  construct (Csn-cleaved ACCD + 6×His); the wiki uses 36.5 kDa. The 54 nM active-site figure
  is insensitive to this, the 1.96 mg/L figure is not (2.01 at 37.6 kDa, 2.20 at 41 kDa).
* **Oligomer.** The wiki says homotetramer, ~144 kDa. The dossier says trimer assembly.

And a cross-check nobody has written down: the dossier computes the standard DNPH assay's
limit of quantitation at **3.3 mU/mL for a 30-minute incubation on neat permeate**. The
7 October run was 30 minutes, samyQ read 7.25 mU/mL and csn read 3.31 mU/mL. "Detected,
below LOQ" and "below LOD" on that page are not just plausible, they land exactly where the
dossier predicted. The same dossier sets the permeate acceptance gate at **1 mU/mL**, so the
samyQ result is about 7× the gate — which is a milestone statement the wiki does not make.

**Block 3, dose and payback.** Every arithmetic step reproduces; every input is assumed.
1.67 mL on a plate whose 100 cm² area was reconstructed and never recorded → 1,670 L/ha;
canopy correction = (LAI 4.5 / 0.115) / 16 = **2.444**, hence 4,082 L/ha unrounded and
4,008 L/ha at 2.4 — both numbers are on the page and the 1.8% gap is exactly that rounding;
9 × 4,008 = 36,072, 12 × 4,008 = 48,096, 17 × 4,008 = 68,136, 3.28 × 4,008 = 13,146 all check;
7,251.4 mU per litre ÷ 34,807 mU per reactor-litre-day = 0.2083 reactor-litre-days per litre
checks. The chain is sound and rests on an assumed plate area, an unmeasured protection
lifetime, a provisional trigger and an efficacy (0.28) that disagrees with Block 1's (0.58).
Arithmetic verified, inputs pending — that is the honest status and it is now what Fact-Check
says.

### 3.2 Strand B — the Level-1 bioreactor model (`Math Model/releaf-model/`)

This is the most complete modelling work the project owns and the wiki barely shows it.
Written 2026-09-02, every report generated from code, `fixed | lit | calc | verify` tags on
every parameter and a standing rule that nothing tagged `verify` may be reported as a result.

* **Growth** (`reports/growth.md`). Logistic throughout. 37 °C normoxia r = 1.3057 ± 0.0494 h⁻¹,
  K = 1.5365 ± 0.0379 OD, t_d 31.9 min, R² 0.994; hypoxia 1.2747 ± 0.0337, K 1.4578, 32.6 min.
  Logistic beats Baranyi by 8.26 AICc and Gompertz by 10.46 — seven hourly points cannot pay
  for a lag parameter. The 5.5% hypoxia drop has Welch df = 2.72 and should never be quoted
  without it. All 17 handoff numbers reproduced, zero disagreements.
* **The 18-day photometer run**, 2,671 valid readings, 434.2 h. Two growth phases, not one:
  µ 0.0329 h⁻¹ over 7–40 h and 0.0165 h⁻¹ over 160–205 h, measured plateau 1.4691 ± 0.0158.
  The single-point 1.490 blank factor was rejected in favour of the 28-point affine map
  `OD_BioDrop = 0.0041 + 1.0383 · OD_photometer` (R² 0.9957): one point cannot establish
  linearity, and the choice moves K by 4.1% instead of 49%. The pump-failure window was
  **located from the data** at 234–294 h, peak local scatter 13.6× the run median, reference
  light channel down to 1.39 lux against 26.67 — i.e. the in-house photometer detected the
  failure of the pump in the reactor it was monitoring.
* **Hydraulics** (`reports/hydraulics.md`). Includes its own retraction: a first revision read
  the pressure fields as MPa when they are bar, and §0 withdraws six specific findings by name.
  Corrected: Hagen-Poiseuille slope 3.53496 × 10⁻⁴ bar per mL/min against the stored
  3.537 × 10⁻⁴; module sits at 0.90–1.26 of eleven-parallel-tube theory, so no fibre is
  blocked (effective fibre count 8.7–12.2 against 11 stated); background fittings are 45–55%
  of the measured drop; recommended 230–300 mL/min on the shear window, not on any pressure
  ceiling; and the handoff's 138 passes/h becomes **34.5 passes/h** once the loop is 400 mL
  rather than 100 mL, which weakens the cumulative-shear argument four-fold. n = 1 sweep.
* **Transport** (`reports/transport.md`). Under a TMP indistinguishable from zero, ACCD still
  crosses by diffusion: k_m·A = 0.170 mL/min at 22 °C (0.045–0.817 over the porosity /
  tortuosity / wall sweep, a factor of 18), about 1/15 of the assumed 2.5 mL/min convective
  flow — fast enough to equilibrate a ~20 mL shell within a working day. Decision: blot the
  **lumen** lane, because it needs only V_L = 400 mL and it is the only lane that carries the
  41.9 kDa precursor, which is what separates a translocation failure from an expression failure.
* **Instrument audit** (`reports/instrument.md`). The dashboard computes TMP as `F − P`, not
  `(F+R)/2 − P`. Displayed TMP −0.0232 bar with a 95% interval of ±0.0548 bar even on the
  favourable error model: 18% of the 0.30 bar design point, so **nothing about filtration
  performance can be concluded from this dashboard**. The measured axial drop has the wrong
  sign, and the flow meter's implied 2,581 pulses/L matches no catalogue part found.
* **Secretion** (`reports/secretion.md`). 74 of 75 printed handoff values reproduce; the one
  exception is the handoff printing a table from its own rounded q_P. Verdict
  AGREE_AFTER_ROUNDING, with nothing silently adopted.
* **Sentinel** (`reports/sentinel.md`). Train on t < 120 h, alarm at the 99.5th percentile,
  threshold fixed before any result was looked at. It separates the two events correctly:
  120–160 h is a **process** event (72.9% process axis, reference channel clean, OD genuinely
  falling) and 240–300 h is a **sensor** fault (100% sensor axis, reference channel collapsed).
  Lead time 26.7 h. Two events means there is no validated error rate and the report says so.

One live defect: `params/parameters.yaml` still tags `tmp_at_rec: 0.30` as **MPa**. Every
other document in that repository, and the sensor's own error budget, says 0.30 **bar**. That
is the exact unit error `hydraulics.md` §0 retracted, still sitting in the parameter table.

### 3.3 Strand C — the AIoT stress and control model (`AIoT Sensors/`)

Finished 25 September, 12-script pipeline, EN + ZH technical report, and the only part of the
project that publishes a negative result at the top of its own findings file.

* **The reactive threshold loses to doing nothing.** Relative regret: never 0.95, reactive
  threshold 1.71, fixed nightly block 2.59, receding horizon without a sensor 0.78, receding
  horizon with the sensor **0.02**, oracle 0.00. Ten hours pass between lamp-on and protection
  on the plant, so a rule that waits for a threshold crossing has already spent its budget.
* **The leaf wetness sensor is worth 70% of the available control gap**, value of information
  5.50 [4.06, 7.08] cost units per season; it pins the canopy dew-point offset (1.15 → 0.46 →
  0.13 °C posterior SD at 3 / 14 / 30 days) but never the guttation supply, which needs a
  second measurement.
* **Standard wetness estimators disagree more than their own error bars** (LWD 8.3–14.4 h/d,
  blast-favourable days 41–82%), and per-station RH calibration fixes the bias without
  improving the correlation at all.
* **The honest negative result**: on the 19-year county-season yield panel, ablating wetness
  changes mechanistic AUC 0.549 → 0.460 but ridge AUC 0.719 → 0.745. The county-season label
  cannot adjudicate it, and the report says the label is the problem.
* **Three hardware conclusions.** Sunlight saturates CcaS ~50× at midday, so the lamp is a
  night-only actuator unless the reactor is shaded; rice is a short-day plant and the lowest
  reported night-break threshold is ~0.01 µmol m⁻² s⁻¹, so the lamp must be optically isolated;
  and the epiphyte-versus-reactor ranking flips at a metabolic burden of 0.01 per hour of full
  expression (epiphyte 514 h per season against the reactor's 82 h) — one number the wet lab
  only has to bracket, not measure precisely.

---

## 4. What the wiki says that the archive cannot support

1. **Block 1 in full** — 32%, 32,767, 19.8 kg/ha, 399 county-seasons, 365/419, 7.9%/8.8%,
   the 18-to-15 candidate narrowing, the index lookup tables and NT$7,539/ha. No archived
   source of any kind. Either the code and its outputs get dropped into the project folder
   before the 21 October freeze, or these stay pending on the Fact-Check page with the reason
   visible.
2. **"a run of seven adenines"** — it is eight.
3. **"a homotetramer of about 144 kDa", "36.5 kDa per subunit"** — the project's own dossier
   says trimer and 41 kDa, our construct is 37.6 kDa.
4. **"8,000 random synonymous candidates"** on the Methodology page — the archived round 2 ran
   33,395 to 40,899 legal candidates per group, and the sharp optimiser folded 4,437 structures
   for v2 and 110,040 for v3. The 8,000 figure matches nothing in the archive.
5. **"roughly 50,000 synonymous draws"** on the Peptide Design page — same issue, same fix:
   quote the counts from `round2_tables.txt`.
6. **The P_cpcG2 figure's 1,500 / 30,000 MEFL anchors** — the fitted values in the parameter
   table are 1,997.6 and 106,740.5 MEFL. The figure is already labelled as unmeasured, so this
   is cosmetic, but a judge who knows the paper will notice.
7. **`model_figures.py:63` credits Ohlendorf for Castillo-Hair's constants.** One-line fix,
   and it resolves a Fact-Check conflict.
8. **The His tag.** Settled against the order files, and two sentences are wrong. Molecular
   Dynamics: "the decision to move the purification tag to the C-terminus" — the shipped
   cassettes are N-terminal. GRAFT Methodology Phase 2: "appending a C-terminal 6xHis tag" —
   true of the June–July codon work only, so it needs the qualifier.
9. **"in the full-length peptide the Lys7 side chain salt-bridges receptor Asp129 in 98.7% of
   frames"** on Molecular Dynamics. That is the 7-23 run's number. Full length is 44.2% on the
   same receptor residue, and the sentence is the hinge of the argument it supports.
10. **"111 free grid points at the N-terminus, 2 at the C-terminus"** on Peptide Design. Those
    are the flood fill's seed counts; the free points are 694 and 1,055. The distances and
    residue counts are right.
11. **"HADDOCK 2.4" on GRAFT Methodology.** What ran is 2.5. The 2.4 is the protocol paper.

---

## 5. Fact-Check: what changed

Scope of the first pass: the codon-optimisation facts and the Math Model Blocks 1–3 facts, plus
the ACCD kinetics and the His-tag conflict they touch. A second pass over the docking, MD and
peptide-design audit facts followed and is in section 7. Plants, bioreactor runs, hardware,
geospatial, education and regulatory facts were not re-examined.

Rules used, and they are stricter than "the arithmetic works":

* **confirmed** — the value itself is in a source file in the project archive, or it is pure
  arithmetic or a physical constant that I reproduced exactly from inputs that are themselves
  confirmed. The source path is recorded on the fact.
* **conflict** — a source file and the wiki disagree about the value.
* **pending** — the arithmetic may be verified, but the value depends on a measurement whose
  raw file is not in the archive. The note now says which, so nobody re-does this search.

| Fact | Was | Now | Why |
|---|---|---|---|
| WM-129 codons 2–31 | pending | **confirmed** | `codon_opt_sharp_results.json` v3 has exactly 30 editable SP codons, 2–31; note flags the 8,000-candidate claim |
| WM-130 four cargos | pending | **confirmed** | `REPORT.md`, `round2_tables.txt`, the four figures |
| WM-175 bottleneck 0.067 → 0.528 | pending | **confirmed** | exact match in `codon_opt_sharp_results.json` and `sharp_opt.log`, including CAI 0.78, ho1 0.681, the 0.911/0.050 failure and the codon-only 0.054 |
| WM-177 seven adenines | pending | **conflict** | the run is eight; the second clause (greedy made a payload worse) is confirmed on LEA14 |
| WM-027 CcaSR K½ and n | conflict | **confirmed** | `parameters.yaml` and the 4 July spec freeze; the attribution error is in the build script, named in the note |
| WM-032 105 / 75 min | pending | **confirmed** | t½ on 105.1 ± 1.5, off 74.97 ± 0.39 min |
| WM-033 chassis and chromophore | pending | **confirmed** | `parameters.yaml` caveat, `pTwist Amp High - Ho1_pcyA.dna` |
| WM-028 usable band | pending | **confirmed** | Hill inversion reproduces 0.015 → 0.50 µmol and 0.94 → 20.1 µmol |
| WM-029 124 lux | pending | **confirmed** | reproduced from the photon energy at 526 nm and the photopic efficacy |
| WM-030 setpoint table | pending | **confirmed** | all six rows reproduce to the printed digits |
| WM-002 32,767 | pending | **confirmed** | 2¹⁵ − 1; the 18-to-15 gap stays in the note |
| WM-025 ACCD kinetics | pending | **conflict** | K_M and k_cat confirmed; subunit mass 36.5 vs 41 vs 37.6 kDa, and tetramer vs trimer |
| WM-159 His tag | conflict | conflict, with evidence | the archive settles June and July as C-terminal; the ask is narrowed to the post-16-August order |
| WM-020, WM-021, WM-024, WM-026, WM-034 | pending | pending, annotated | arithmetic reproduced; the FlexA raw file is not in the archive, and the dossier's 3.3 mU/mL LOQ cross-check is now recorded |
| WM-038, WM-040, WM-041, WM-043–WM-046, WM-048, WM-050 | pending | pending, annotated | every arithmetic step reproduced, including the 2.444 canopy factor and the 4,082/4,008 rounding; inputs still assumed |
| WM-001, WM-003–WM-008, WM-010, WM-019 | pending | pending, annotated | searched both project folders on 14 October; no archived source for Block 1 |
| WM-176, WW-201 | pending | pending, annotated | the signal-peptide screen output lives in a compute workspace that is not in this archive; S15A and G17A are not in the codon archive either |
| WM-036 promoter curve | confirmed | confirmed, annotated | the fitted MEFL anchors differ from the figure's |

Mechanics: `data/facts.json` edited, `data/changelog.json` appended, `meta.version` bumped to
`2026-10-14.1`, `python3 build/build.py` run. Nothing pushed.

---

## 6. What I would ask for next

1. **The Block 1 code and outputs**, dropped anywhere in the project folder. It is the biggest
   unsourced block on the wiki and the freeze is on 21 October.
2. **The 7 October FlexA raw file**, which closes WM-020, WM-021, WM-024, WM-026 and WM-034 in
   one move, and with it which batch the permeate came from.
3. **One sentence from the wet lab on the His tag** after 16 August.
4. **A decision on the subunit mass** — 36.5, 37.6 or 41 kDa — because it moves the mg/L figure.
5. Whether to run the same pass over the MD, Protein Design and Peptide Design facts, where the
   archive (`00_Deliverable_Reports/21_MD_Simulation/`, `30_MD_Public_Clone/analysis/`) does hold
   the data and a lot of it should be confirmable.

---

## 7. Second pass: docking, MD and the peptide-design audit

The archive turned out to hold far more of this than of the math model, so the same method ran
over it. 36 more facts touched, 20 moved to confirmed, 3 to conflict. Version `2026-10-14.2`.

### What the data settled

| Claim | Source | Verdict |
|---|---|---|
| The His tag on the shipped cassettes | `0823_Order_Report_Gabriel/BoPep4_0823_parts.csv` | **N-terminal**, with the note "never fuse His to Asn23"; all six cassette lengths reproduce (691 / 715 / 715 / 673 / 697 / 715 bp) |
| HADDOCK version | methodology audit, software stack | **2.5**, `haddock2.5-2026-07`, 121 production runs, local, Python 3.12. The 2.4 is the protocol paper |
| 121 production runs, 44 AF3 jobs, seven campaigns | audit reproducibility tables | reproduces item by item, down to the AF3 gates (ipTM ≥ 0.60, PAE ≤ 5 Å, zero clashes) |
| The founding campaign against the later five | audit | 8 runs with crystal restraints and a 0.77 Å positive control, against 113 runs started from the pose being tested with no control. 8 + 113 = 121 |
| The canonical pose was chosen, not predicted | audit cluster landscape | cluster 1, 39 models, 5.80 Å non-native; the one carried forward is cluster 3 of 4 at 1.48 Å. Median l-RMSD over all 60 water-refined models 9.08 Å |
| Truncation ladder | `MASTER_MATRIX_34complexes.csv` | 17 fragments × 2 receptors = 34; score −197.8 → −85.1; ipTM flat 0.82–0.94 to 13-23 then 0.87 → 0.54; PAE 2.49 → 8.85 |
| The cliff is a method artefact | recomputed | score on length + net charge R² = **0.929** (PEPR1), −7.44 per residue — the page's "about −7.4". Per buried area the series is flat at −72 to −86 per 1,000 Å², and the shortest fragment is the *most* favourable per residue |
| Tandem repeats | `repeat_metrics.csv` | buried area per residue 127.3 → 31.7 Å² monotonically, copies touching the receptor saturate at 3 |
| 9-23's mass and protease load | recomputed | 1,612.73 Da against 2,409.74, −33.1%; trypsin-type sites 3 → 1 (R9-P10 and K18-P19 are proline-blocked) |
| K8Q+K18R | AF3 and two-method matrices | ipTM 0.49, PAE 9.45 Å, 42 receptor residues, HADDOCK −194.7, verdict string literally `DISCORDANT-HADDOCK-rescues` |
| The tagged construct's best seed | `scores_repC.csv` | −181.927 at seed 4242, against the crystal positive control's −180.749. Best in the study, and it makes none of the clamp contacts |
| His14 is not the pH switch | `bopep4-lowph-vs-wt.json` | 6.09 Å at pH 7 and 6.08 Å at pH 5.5, 0.0% occupancy in both. His227–Glu12 is the pair |

### Three new conflicts

1. **WM-138, Lys7–Asp129.** The 98.7% at 2.81 Å is the **7-23** trajectory. In full length the
   same receptor residue is occupied 44.2% of the time — the 7-23 page's own delta table says
   so (44.2 → 98.7, d = 54.5). The Molecular Dynamics sentence has it backwards, and it is the
   sentence the "missing salt bridge explains 9-23" argument rests on.
2. **WM-162, the exit channel.** 111 and 2 are `n_seeds` in `exit_channel.json`, not free grid
   points, which are 694 and 1,055. Everything else in that sentence is right.
3. **WM-161, −155.7 against −125.9.** Not in the archived score tables. At the panel seed the
   tagged construct is −173.1 and untagged wild type −144.8. The −181.9 is right. Someone has
   to supply the 30-pose panel summary those two came from.

### Still pending, and now it says why

* **The 18-position alanine scan.** `18_PointMutation_Panel/` has `build_panel.py`,
  `panel_manifest.tsv` and a folder per complex, but no summary table, so +150.4, +32.6, −1.3,
  −2.9, +9.5 and the backbone shifts could not be checked. One file would close five facts.
* **The restraint derivation** — WHISCY, US-align, the Kabsch refit, DisVis, the PEPR2
  transfer, the threading f-nat. None of it is in either project folder; it stayed in
  `~/software/haddock-runs/bopep4-pepr1/`, which is not on this machine. Nine facts.
