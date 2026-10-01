"""Build data/nullity.json: the sentence of nullity, 7 July 1456 (Quicherat III, 1845).

Conventions in tools/nullity_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from nullity_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "nullity.json"


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
        "titel": "The sentence of nullity",
        "autor": "Jean Jouvenel des Ursins, archbishop of Reims, Guillaume Chartier, bishop of Paris, Richard Olivier, bishop of Coutances, and the inquisitor Jean Bréhal, papal judges delegate",
        "jahr": "7 July 1456",
        "orig_sprache": "la",
        "pg_label": "Quicherat III p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. III (Paris: Renouard, 1845), pp. 355–362. Internet Archive, procsdecondam03joanuoft. Public domain.",
        "hinweis": "Five excerpts read against the page images, together most of the operative part of the sentence. Cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
