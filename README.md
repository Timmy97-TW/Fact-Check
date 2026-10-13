# ReLeaf Fact-Check

One shared list of the team's results, material specs, event dates and milestone numbers,
each marked confirmed, pending, conflict or retired. Plain HTML, no server.

Wiki freeze: 21 October 2026, 23:00 Taiwan time.

## For team members

1. Open the page and type your name at the top right.
2. Press **Edit** or **Confirm** on any item. Say what you based it on.
3. Press **Export changes**. Send the downloaded `factcheck-changes_<date>_<time>_<name>.md`
   (and any image or data file you mentioned) to Timmy.

Your edits stay in your own browser until Timmy imports them.

## For Timmy

Hand the exported file to Claude. The file is a complete prompt: it lists each change by fact id
with old and new values, the stated basis, and the wiki pages that quote the value. Claude updates
`data/facts.json`, corrects the wiki pages, appends to `data/changelog.json` and rebuilds.

## Layout

```
index.html            the page
assets/app.css .js    styling and behaviour
assets/img/           evidence images (plant/ from raw data, wiki/ copied from the wiki)
data/facts.json       the single source of truth
data/changelog.json   one entry per imported change request
data/facts.js         generated from the two files above; what the page loads
build/build.py        validates facts.json and writes facts.js
build/seed.py         one-time merge of the first extraction (data/_seed/)
```

After any change to `data/facts.json`:

```bash
python3 build/build.py
```

## A fact

`id`, `tab` (results, plant, materials, timeline, terms), `group`, `title`, `statement`,
`value`, `unit`, `date`, `status`, `status_note`, `ask`, `source[]`, `wiki[]` (page, anchor,
exact quote), `images[]`, `critical`, `confirmed_by`, `confirmed_on`. Text fields carry `zh` and `en`.

"Confirmed" means the value was seen in a raw data file or stated by the person responsible.
A value that only appears on the wiki is "pending".
