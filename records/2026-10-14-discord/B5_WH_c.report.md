# B5_WH_c: hardware facts vs Discord

67 facts in the batch. 39 verdicts written, 28 left alone.

| Verdict | Count | Facts |
|---|---|---|
| confirmed (high) | 5 | WH-205, WH-261, WH-269, WH-271, WH-277 |
| conflict (medium) | 1 | WH-243 |
| annotate | 33 | WH-204, 208, 213, 223, 228, 231, 233, 234, 235, 238, 241, 245, 248, 250, 252, 253, 255, 256, 258, 263, 264, 266, 268, 278, 281, 284, 285, 287, 289, 291, 297, 298, 301 |
| nothing | 28 | WH-206, 207, 209, 211, 214 to 219, 225, 226, 229, 230, 232, 244, 259, 260, 262, 267, 275, 283, 286, 290, 295, 296, 300, 302 |

## Read in full
Main server: Teams/drylab (all 869 messages), its DryLab Notebook and hardware notebook threads, Phase2/dry-bioreactor, dry-lpa, dry-fluorometer, dry-hydroponics, the 9/4 Chang visit, 9/5 forum and 9/12 Sattely and Endy threads, the 8/28 Cheng visit thread.
Research server: every bioreactor, lpa and od600-spectrophotometer thread, regulations/Bioreactor laws, drylab-notebook threads.
Everything else by grep. Attachments opened: run 3 CSV, both run 4 CSVs, the pressure workbook, the two bioreactor OD workbooks, the LPA OD workbook, the LPA shopping list and assembly guide, six photos.

## Main findings
1. WH-243 (pump failure): the run 3 log posted on Discord shows the OD drop at about 242 to 246.6 h, recovering at 18:24 Taipei on 31 July, and Chars explains it on 1 August. At 217 h there is only a one-step change in the reference reading. The wiki's 30 July looks one day early.
2. WH-235 (first growth test): Chars' workbook puts the first test on a sheet named 260606 with points at 0 to 7 h and 24 to 27 h, and the 7 June wet lab log lists the bioreactor growth test. The "10 June" comes from a file name and from an evening summary that reuses the same numbers. It was a 6 to 7 June test.
3. WH-256 (forum vs run 4): two units existed. The "commercialized" computer-case unit was the booth showpiece (not wired on 30 August); run 4 was on the lab rig.
4. WH-205 confirmed by Anton's posted firmware (16 July, not 11 July). The 19 September run used tiers described as 100%, 12%, 2%, so those duty levels were not what ran that day.
5. WH-277: the OD workbook was posted on 3 October, but its metadata says created 20 September. Both notebook statements hold.
6. WH-258: the asker was Ethan (regulations); asked 7 September, answered 8 September with Chars' reply relayed by Joshua.
7. WH-250: the pressure workbook is named 260816 and runs to dial 24; the page tables stopping at 22 are missing a row.
8. WH-238: the stepper pinch valve was not assembled by 27 June; screws were still in transit on 9 July.
9. WH-281: the humidity box was still being sized on 13 May, which contradicts the Dry Lab Notebook's 18 April entry.
10. WH-298: the team's own announcement writes Professor Chang Jo-Shu.

## Closest without settling
- WH-266: thread titled "22 past photometers" opened 27 July; the count and week match, but the quote is only a link, so left as annotate.
- WH-253: photos bracket the mounting between 29 August 17:32 (case empty) and 30 August 15:05 (cartridge and reservoir in); sensors not wired.
- WH-268: TiO2 vs BioDrop calibration listed as done on 24 August; 23 August itself not stated.
- WH-255: visit on 4 September confirmed; the three requests are only in a linked meeting note.
- WH-285: countdown messages agree with 21 October but no message states the date.
- WH-213: the 5 July "Calibration" image is a figure from the published LPA paper, not team data.

## Notes for the merger
- Five evidence items point at a message that has an attachment and no text, so their quote is an empty string: WH-277 (3 Oct xlsx), WH-289, WH-204 (shopping list PDF), WH-245 (do_ph_test.zip), WH-243 and WH-297 (run 3 CSV). Each has a second text quote except WH-289. If the checker rejects empty quotes, drop those items; WH-277 then rests on the attachment alone and should fall back to annotate.
