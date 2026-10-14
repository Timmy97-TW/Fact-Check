# B4_WH_b: Fact-Check vs Discord

68 facts in the batch. 24 verdicts written: 9 confirmed (all high confidence), 15 annotate (all medium), 0 new conflicts. 44 facts have no Discord evidence and were left alone.

## Read in full
Main server: Teams/📐-drylab and both threads (DryLab Notebook, hardware notebook), Phase2/dry-bioreactor, dry-fluorometer, dry-lpa. Teams/🧬wetlab, wetlab-progression, wetlab-notice and general-announcement were read in full for 16 to 30 September and for 15 June to 9 July (wetlab), and grepped for everything else.
Research server: every 🧪-bioreactor, ⚫-lpa and od600-spectrophotometer thread, 📈-math-model/Bioreactor Calculations and AmilCP Prediction, regulations/Bioreactor laws.
Attachments opened: the 19 September plate-reader screenshot, 20260919_OptoLPA_ACCD_Run1_ODresults.xlsx, and Chars's two vendor-table screenshots of 20 and 24 June.

## Main findings
1. WH-120: the LPA culture run happened on 19 September 2026 (Joshua, Timmy, Chloe, and the OD workbook). The LPA page's "no run on record" is out of date.
2. WH-125: the workbook gives 24 h readings of 0.969 to 1.083 and background 0.059. Confirmed from the attached file.
3. WH-127: sampling was at 2, 4, 6, 8 and 24 h. There is no 10 h point; the "8 to 10 hours total" protocol wording does not describe the run.
4. WH-129: the highest-green arm has the highest plateau (1.056, 1.083, 1.081 against weak green 1.000, 1.020, 1.031). Biomanufacturing is right; Digital Twin and Measurement have the weak and high labels swapped. The arm mapping was cross-checked against the 2 h screenshot and Timmy's well list.
5. WH-187: flow cuvette path is 2 mm (Noah and Joshua on 12 October, Timmy's purchase note of 27 June). The 0.2 mm on three pages looks like 0.2 cm with the wrong unit.
6. WH-153, WH-154, WH-152: two modules were ordered. Minilab 60 cm (150 cm², 8 fibres, part HF-E-MI-M020-10-60-P) came first; M+ 60 cm (200 cm², 11 fibres, two purchased) was ordered on 24 June because the first could not arrive before 20 July. The wiki pairs the Minilab part number with the M+ geometry. Which module each run used is not in Discord.
7. WH-174: pressure transducers are voltage output (Chars), 0 to 1 MPa, 0 to 5 V, 24 V, 1.0% FS. Measurement's "current signal, 0 to 1 A" is the wrong side.
8. WH-184: the rig ran on an Uno Q by 7 September; the Uno R4 is the 4 July specification.
9. WH-132: gels of the 19 September LPA samples do exist (lanes G100, G12, G2, R100 at 2 to 8 h, posted 21 September), and Chloe reported a band near 63 kDa. This corrects the earlier note that no such lanes exist.
10. WH-173: 4 mm in, 6 mm out, off-the-shelf design for 16 mm tube. Confirmed from Noah and Chars on 4 August.

## Closest without settling
- WH-123 and WH-124: run-day arms are Green 100/12/2% and Red 100/12/2%. Red was run at three levels, but no lux figure for any level is in Discord.
- WH-159: Joshua says the HFM goes to 0.7 bar, while the transcribed M+ sheet says 0.25 MPa maximum operating pressure.
- WH-160: wetting came after 12 August and the hydraulic data file is dated 16 August; 15 August itself is not stated.
- WH-169: 94 mL/min is the vendor table flow for the Minilab at 2000 s⁻¹, so it may be a catalogue number.
- WH-167: pump died and was replaced on 1 August; the replacement model is not named.
- WH-165: run 4 used an ACCD-secreting construct; host strain not stated.
- WH-126: the run is called test1 and Run1 and nothing later is reported, which is only an absence of record.
- WH-175, WH-182, WH-172: partial matches on transducer count, pH probe status and the servo change date (4 August in Discord).

## Notes for whoever applies this
- Four evidence entries point at image-only or file-only messages whose text is empty, so their quote is an empty string; the attachment path is in "image". The xlsx is given in the "image" field with evidence_kind "image".
- The 4 July "Hardware Specifications" post and the 27 June M+ sheet are formatted transcripts posted by Timmy. I used them as confirmation only where a second person or an image backs the same point (WH-174, WH-158) and otherwise as annotation.
- One small transcription slip in the workbook: G3 Rep3 at 2 h is 0.103 in the xlsx, but the plate-reader screenshot shows Un 03 as 0.109. It does not affect any fact here.
