"""Build data/articles.json: the charges, the Twelve Articles and the University of Paris (Quicherat I, 1841).

Conventions in tools/articles_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from articles_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "articles.json"


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
        "titel": "The charges, the Twelve Articles and the University of Paris",
        "autor": "The promoter Jean d'Estivet; the judges' Twelve Articles; the doctors at Rouen; the faculties of theology and decrees of the University of Paris",
        "jahr": "March–May 1431",
        "orig_sprache": "la",
        "pg_label": "Quicherat I p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. I (Paris: Renouard, 1841), pp. 203–204, 328–340, 414–418. Internet Archive, procsdecondam01joanuoft. Public domain.",
        "hinweis": "Seven excerpts read against the page images: the preamble of the seventy articles, three of the Twelve Articles, and the verdicts of the doctors at Rouen and of the two faculties of Paris. Cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
