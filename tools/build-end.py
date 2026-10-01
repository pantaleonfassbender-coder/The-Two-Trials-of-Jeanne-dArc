"""Build data/end.json: the end, as two friars remembered it (Bouillé inquiry, March 1450; Quicherat II, 1844).

Conventions in tools/end_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from end_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "end.json"


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
        "titel": "The end, as two friars remembered it",
        "autor": "Isambart de la Pierre and Martin Ladvenu, Dominicans of Rouen, before Guillaume Bouillé's inquiry",
        "jahr": "5 March 1450",
        "orig_sprache": "fr",
        "pg_label": "Quicherat II p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. II (Paris: Renouard, 1844), pp. 4–9 (Préliminaires de la réhabilitation: Informatio prævia). Internet Archive, procsdecondam02joanuoft. Public domain.",
        "hinweis": "Eight excerpts read against the page images, in the French in which Quicherat prints the inquiry of 1450. The burning itself is not described here: where the friars describe it, the passage is cut and the cut marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
