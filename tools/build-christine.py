"""Build data/christine.json: Christine de Pizan, Ditié de Jehanne d'Arc, 31 July 1429 (Quicherat V, 1849).

Conventions in tools/christine_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from christine_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "christine.json"


def build():
    sections = []
    for s in SECTIONS:
        units = []
        for i, u in enumerate(s["units"], 1):
            unit = {"n": i, "pg": u["pg"], "titel": u["titel"], "orig": u["orig"], "en": u["en"]}
            if u.get("lang"):
                unit["lang"] = u["lang"]
            if u.get("note"):
                unit["note"] = u["note"]
            units.append(unit)
        sections.append({"id": s["id"], "zk": s["zk"], "titel": s["titel"], "blurb": s["blurb"], "units": units})
    data = {
        "titel": "Christine de Pizan, Ditié de Jehanne d'Arc",
        "autor": "Christine de Pizan (c. 1364 – c. 1430), in a convent since 1418",
        "jahr": "31 July 1429",
        "orig_sprache": "fr",
        "pg_label": "Quicherat V p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. V (Paris: Renouard, 1849), pp. 3–21, after A. Jubinal's edition (1838) of the Berne manuscript. Internet Archive, ProcesDeCondamnationV5. Public domain.",
        "hinweis": "Twenty of the sixty-one stanzas, read against the page images, numbered as in Quicherat; his supplements in brackets are kept. The English is this site's working translation (CC0), line for line where the syntax allows.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
