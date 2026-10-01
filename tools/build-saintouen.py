"""Build data/saintouen.json: Saint-Ouen, the abjuration, the relapse and the sentence, 24-30 May 1431 (Quicherat I, 1841).

Conventions in tools/saintouen_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from saintouen_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "saintouen.json"


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
        "titel": "Saint-Ouen: abjuration, relapse and sentence",
        "autor": "The court of Pierre Cauchon and Jean Le Maistre; the record kept by the notaries Manchon, Boisguillaume and Taquel",
        "jahr": "24–30 May 1431",
        "orig_sprache": "fr",
        "pg_label": "Quicherat I p.",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. I (Paris: Renouard, 1841), pp. 442–475. Internet Archive, procsdecondam01joanuoft. Public domain.",
        "hinweis": "Six excerpts read against the page images: the French minute where it survives, the abjuration in its French form, and the Latin of the sentences. The execution is not carried here. Cuts are marked [...]. The English is this site's working translation (CC0).",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
