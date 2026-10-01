"""Build data/witnesses.json: witnesses of the nullity trial, 1456 (Quicherat II-III, 1844-1845).

Conventions in tools/witnesses_text.py.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witnesses_text import SECTIONS  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "data" / "witnesses.json"


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
        "titel": "The witnesses of the nullity trial",
        "autor": "Depositions taken by the commissioners of the nullity trial, recorded in Latin by its notaries",
        "jahr": "January–May 1456",
        "orig_sprache": "la",
        "pg_label": "Quicherat",
        "quelle": "J. Quicherat (ed.), Procès de condamnation et de réhabilitation de Jeanne d'Arc, dite la Pucelle, vol. II (Paris: Renouard, 1844), pp. 418–419, 436–437, and vol. III (1845), pp. 5–6, 86–87, 135–137, 156–157. Internet Archive, procsdecondam02joanuoft and procsdecondam03joanuoft. Public domain.",
        "hinweis": "Six depositions, excerpted and read against the page images. The record is in Latin; Jeanne's words, when a witness reports them, sometimes stand in French. Cuts are marked [...]. The English is this site's working translation (CC0); Murray's English (1902) was compared.",
        "sections": sections,
    }
    OUT.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{OUT.name}: {sum(len(s['units']) for s in sections)} units in {len(sections)} sections")


if __name__ == "__main__":
    build()
