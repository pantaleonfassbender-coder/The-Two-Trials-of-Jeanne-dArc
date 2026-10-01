# The Two Trials of Jeanne d'Arc

A documentary apparatus for the two trials of Jeanne d'Arc: the trial of condemnation at Rouen (1431) and the trial of nullity (1455–1456), with the years from Chinon (1429) between them. Public-domain sources with the original (Latin, Middle French) beside an English translation, a timeline linked into the texts, and a list of what is still to come.

Its thesis, to be tested against the texts: the court won its case, and England lost France. The judges of Rouen condemned Jeanne as a relapsed heretic and the English burned her; within twenty years the king she had crowned held Paris and Rouen, and in 1456 a second court declared the first trial null.

Stage 1 (in progress) carries seven modules:

- **The interrogations at Rouen** — Quicherat I (1841), pp. 45–187: eight excerpts from the public sessions (Latin) and the sessions in her prison (the French minute), read against the page images, with T. Douglas Murray's English (1902) where checked and a working translation elsewhere.
- **The Twelve Articles and the University of Paris** — Quicherat I (1841), pp. 203–204, 328–340, 414–418: the promoter's charges, three of the Twelve Articles, and the verdicts of the doctors at Rouen and of the faculties of Paris, with a working translation.
- **Saint-Ouen: abjuration, relapse and sentence** — Quicherat I (1841), pp. 442–475: the scene of 24 May, the abjuration in French, the mitigated sentence, the relapse of 28 May in the French minute, and the sentence of 30 May, with a working translation. The execution is not carried here.
- **Jeanne's letters** — Quicherat V (1849), pp. 95–159: to the English before Orléans, to the duke of Burgundy, to Reims and to Riom in French, and the letter to the Hussites in the German version Quicherat printed, with a working translation.
- **The Journal of the siege of Orléans** — Quicherat IV (1847), pp. 140–164: the English answer to her letter, her entry into the city, the insults from the Tourelles, the wound, the fall of the Tourelles with Quicherat's correction from the town accounts, and the Sunday of 8 May, with a working translation.
- **Christine de Pizan, Ditié de Jehanne d'Arc** — Quicherat V (1849), pp. 3–21: twenty of the sixty-one stanzas of 31 July 1429, with a line-for-line working translation.
- **The Burgundian chronicler: Monstrelet on the Maid** — Quicherat IV (1847), pp. 361–363, 399–402: her coming to Chinon, the beheading of Franquet d'Arras, the capture before Compiègne, and the duke of Burgundy's visit, with a working translation.

A **Compare** page sets her words beside the articles drawn from them, and her letter to the English beside what she told her judges.

Planned, in the order of work (see `data/modules.json`):

- **The witnesses of the nullity trial** (1455–1456).
- **The end, as two friars remembered it.**
- **The sentence of nullity** (7 July 1456).

Main editions: Jules Quicherat, *Procès de condamnation et de réhabilitation de Jeanne d'Arc* (5 vols., Paris 1841–1849); Pierre Champion, *Procès de condamnation* (Paris 1920–1921); T. Douglas Murray, *Jeanne d'Arc, Maid of Orleans* (London 1902). All in the public domain.

The companion game *En nom Dieu* takes its title from Jeanne's own formula.

## Building the data

```
python tools/build-interrogations.py
python tools/build-articles.py
python tools/build-saintouen.py
python tools/build-letters.py
python tools/build-orleans.py
python tools/build-christine.py
python tools/build-monstrelet.py
```

The texts are kept in `tools/interrogations_text.py`, `tools/articles_text.py`, `tools/saintouen_text.py`, `tools/letters_text.py`, `tools/orleans_text.py`, `tools/christine_text.py` and `tools/monstrelet_text.py`.

## Running locally

Any static server, e.g. `python -m http.server 8144`.

Licences: see `LICENSES.md`.
