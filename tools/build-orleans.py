"""Build data/orleans.json: the Journal du siège d'Orléans, March-May 1429 (Quicherat IV, 1847).

Conventions in tools/orleans_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from orleans_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "orleans.json"


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
        "titel": "The Journal of the siege of Orléans",
        "autor": "Anonymous, for the town of Orléans; put in its present form about 1467 from a register kept during the siege",
        "jahr": "March–May 1429 (compiled c. 1467)",
        "orig_sprache": "fr",
        "pg_label": "Quicherat IV p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. IV (Paris: Renouard, 1847), pp. 94–212 (Journal du siège d'Orléans et du voyage de Reims), here pp. 140–164. Internet Archive, procsdecondam04joanuoft. Public domain.",
        "hinweis": "Six excerpts read against the page images, with Quicherat's footnotes where they correct the text. Cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
