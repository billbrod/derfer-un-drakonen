# derfer-un-drakonen

Yiddish resources for D&amp;D 5e

## Preparation

Vocabulary list originally assembled by Marnie Manning on [Google
Docs](https://docs.google.com/document/d/1iKFyX_j3SmRckf8Zcp7QnZCDsoEOyjzj-MDHIJ34aoY/edit#heading=h.i083l3g702nq).

`input/from_google_doc.json` contains a json with the data directly from that
Google Doc (by copying and pasting). Running `python
input/construct_initial_list.py` (requires `pandas`) creates `vocab.json`, which
is actually used by the website. You will not need to rerun this script unless
you add additional words to `from_google_doc.json` or modify its contents. 

The `construct_initial_list.py` also contains some modifications /
restructuring, which you may also wish to change.

# TODO
- [ ] add placeholders for licensing, thanking me
- [ ] upload pdfs to internet archive and link
- [ ] get persistent url working
- [ ] get js to pdf table export working
- [ ] get working on gh pages
