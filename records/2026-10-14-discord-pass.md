# Discord record pass, 14 October 2026

Source: the GEMS-Taiwan iGEM 2026 Discord server, 51 channels and threads, 6,001 messages with 1,055
attachments, pulled 14 October with DiscordChatExporter (general-announcement, communication-encouraged,
wetlab, wetlab-progression, wetlab-notice, drylab, human-practice, software, education, outreach and its
15 meeting threads, all 12 Phase2 channels). Gallery was left out. The Research server pull of 7 October
(987 messages) was searched as well.

## Result

753 unresolved facts compared, 315 updated.

| change | facts |
|---|---|
| conflict to confirmed | 21 |
| pending to confirmed | 20 |
| pending to conflict | 6 |
| annotated, status unchanged | 268 |

After this pass: 583 confirmed, 494 pending, 218 conflict, 2 retired.

## Rule for confirmed

The member who did the work, a lead or an instructor wrote the same value, unit, date and object on Discord,
quoted verbatim. A value in a raw data file that member posted (run log CSV, OD workbook, model report)
counts once the file has been reopened and read again by whoever applies the patch. Plans and
announcements do not confirm an outcome. Values that would have to be estimated from a photo do not count.
Every quote was machine-checked as a substring of the Discord message text; attachment-only messages are
recorded as `[attachment] <file name>`.

## Confirmed

PS-017 WW-002 WW-024 WW-106 WW-120 WW-126 WW-128 WW-129 WW-161 WW-162 WW-201 WW-205 WW-254 WH-045 WH-076
WH-085 WH-116 WH-120 WH-125 WH-127 WH-129 WH-158 WH-173 WH-174 WH-184 WH-187 WH-205 WH-261 WH-269 WH-271
WH-277 WP-005 WP-008 WP-011 WP-013 WP-049 WP-121 WP-153 WP-159 WM-003 WM-004

## New conflicts

WW-074 WW-130 WH-243 WP-052 WP-066 WP-043

## Kept open although a checker proposed confirmed

- WW-065, WW-069, WW-075, WW-115: Discord supports part of the fact only.
- WW-160, WP-166: two hollow-fibre modules were bought, a Minilab at 150 cm² with 8 fibres and an M+ at
  200 cm² with 11 fibres. No message says which run used which. Chars would know.
- WM-020, WM-021, WM-022, WM-023, WM-026, WM-035: the DNPH numbers appear in an analysis report PDF posted
  on 7 October. The plate-reader file it was built from is not on Discord.
- WM-107: the page says AlphaFold3 for PEPR2; Felix wrote AlphaFold2/ColabFold.
- WH-039: direction settled, the 434 h figure is not stated in a message.

## Wiki wording these results put in question

- Results and Engineering describe run 4 as two runs; the logs show one (WW-126).
- "Bubble rejection stayed at 0 %" (WW-130).
- LPA page "no culture run on record"; Digital Twin and Measurement weak and high green labels (WH-120, WH-129).
- Measurement protocol "8 to 10 hours total" (WH-127).
- Flow cuvette 0.2 mm on Photometer, Hardware landing and Bioreactor 3.2; it is 2 mm (WH-187).
- Measurement "current signal, 0 to 1 A" for the pressure transducers (WH-174).
- Entrepreneurship 0.22 µm (WP-121).
- Parts lists S15A and G17A as Designed (WW-201); Experiments says electroporation ran on 168 only (WW-205).
- Education page dates the junior high lesson 2 September; Discord has 2 July (WP-052). WP-061 to WP-065
  carry the same date.
- Education page Q4 synthetic biology 93 %; the chart shows 82 % (WP-066).
- Milestone "10 to 15 Apr" for Prof. Chen Wen-Liang (WP-005); body text "Chang Jia-Xiu" (WP-013).
- Biomanufacturing "longest run 102.4 h" (WH-039).

## What Discord does not hold

ELISA (M-001), every booth and forum survey number, market and cost figures, Registry accessions,
shell-side platings, Block 3 dose and payback, geospatial numbers, per-seedling plant measurements.
The GIS and data physicalization group moved to a separate server on 1 July that is in neither pull.

## Files

`records/2026-10-14-discord/`: ten per-area patch files and reports (B1 to B10), `Z_overrides.jsonl`
(the review decisions above) and `_applied.json` (every change with old and new status).
