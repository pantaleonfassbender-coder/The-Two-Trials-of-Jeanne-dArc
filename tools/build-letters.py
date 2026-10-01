"""Build data/letters.json: Jeanne's letters, 1429-1430 (Quicherat V, 1849).

Conventions in tools/letters_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from letters_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "letters.json"


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
        "titel": "Jeanne's letters, 1429–1430",
        "autor": "Jeanne d'Arc, by dictation; the letter to the Hussites composed in her name by a clerk",
        "jahr": "22 March 1429 – March 1430",
        "orig_sprache": "fr",
        "pg_label": "Quicherat V p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. V (Paris: Renouard, 1849), pp. 95–159. Internet Archive, ProcesDeCondamnationV5. Public domain.",
        "hinweis": "Five letters read against the page images, in Quicherat's French text; the letter to the Hussites in the German version he printed, the only one known to him. Cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
