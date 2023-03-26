# derfer-un-drakonen

Yiddish resources for D&amp;D 5e

- Character sheets pdf on the [internet archive](https://archive.org/details/derfer-un-drakonen)
- Persistent URL for the
  [website](https://purl.prod.archive.org/derfer-un-drakonen),
  [pdfs](https://purl.prod.archive.org/derfer-un-drakonen/pdfs) via the internet
  archive PURL service.

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

## Develop

Clone the repo to make changes locally. You can view a local version by running
a webserver with python: navigate to this directory on the command line and run
`python -m http.server 8008` (or some other open port) and then navigating to
`localhost:8008` in your browser. Refresh the browser to view any local changes.

After pushing to github, it will take roughly ~1 minute before the changes are
reflected on the webiste. You can check out the [actions
page](https://github.com/billbrod/derfer-un-drakonen/actions) to see the status
of the build
