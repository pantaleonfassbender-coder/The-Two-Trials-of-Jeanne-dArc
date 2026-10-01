"""Build data/interrogations.json: the interrogations of Jeanne d'Arc at Rouen, February-March 1431 (Quicherat I, 1841).

Conventions in tools/interrogations_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from interrogations_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "interrogations.json"


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
        "titel": "The interrogations at Rouen",
        "autor": "The court of Pierre Cauchon, bishop of Beauvais; the notaries Guillaume Manchon, Guillaume Colles (Boisguillaume) and Nicolas Taquel; Latin by Thomas de Courcelles",
        "jahr": "February–March 1431",
        "orig_sprache": "la",
        "pg_label": "Quicherat I p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. I (Paris: Renouard, 1841), pp. 45–187. Internet Archive, procsdecondam01joanuoft. English in part from T. Douglas Murray, Jeanne d'Arc, Maid of Orleans (London 1902). Public domain.",
        "hinweis": "Eight excerpts from the record of the public and private sessions, read against the page images: the Latin of the official record, and for the sessions in her prison the surviving French minute. Cuts are marked [...]. The English is Murray's where it was checked and found close, otherwise this site's working translation (CC0); each note says which.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
