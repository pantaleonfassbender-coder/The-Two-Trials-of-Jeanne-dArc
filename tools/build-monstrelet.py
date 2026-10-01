"""Build data/monstrelet.json: Enguerrand de Monstrelet on the Maid, 1429-1430 (Quicherat IV, 1847).

Conventions in tools/monstrelet_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from monstrelet_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "monstrelet.json"


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
        "titel": "The Burgundian chronicler: Monstrelet on the Maid",
        "autor": "Enguerrand de Monstrelet (d. 1453), in the service of Jean de Luxembourg; present at the camp before Compiègne in 1430",
        "jahr": "1429–1430 (written c. 1440–1453)",
        "orig_sprache": "fr",
        "pg_label": "Quicherat IV p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. IV (Paris: Renouard, 1847), pp. 360–404, after Bibliothèque royale ms. fr. 8346; here pp. 361–363, 399–402. Internet Archive, procsdecondam04joanuoft. Public domain.",
        "hinweis": "Four excerpts read against the page images, in the Picard spelling of the manuscript Quicherat followed. Cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
