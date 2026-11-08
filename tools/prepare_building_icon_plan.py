"""Map missing building icons to matching advance art or generation prompts."""

from __future__ import annotations

import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
ADVANCE_ICONS = ROOT / "main_menu/gfx/interface/advance"
REPORT = ROOT / "tools/reports/missing_tech_building_icons.md"
OUTPUT = ROOT / "tools/reports/building_icon_plan.json"

# Reuse only when the subject of the advance icon depicts the building clearly.
REUSE = {
    "bronze_age_bronze_foundry": "bronze_foundry_advance",
    "bronze_age_bronze_forge": "bronze_forge_advance",
    "tablets_guild": "royal_tablets_workshop_advance",
    "naval_supplies_palace": "royal_navy_supply_advance",
    "bronze_age_burial_pits": "ceremonial_burial_advance",
    "bronze_age_aristocratic_mounds": "aristocratic_burial_advance",
    "bronze_age_urnfield_burial_site": "urnfield_advance",
    "frontier_post": "frontier_post_advance",
    "town_walls": "town_walls_advance",
    "bronze_city_walls": "bronze_city_walls_advance",
    "hill_fort": "hill_forts_advance",
    "iron_city_walls": "iron_city_walls_advance",
    "iron_citadel": "iron_citadel_advance",
    "bronze_age_victory_stelae": "triumphal_monuments_advance",
    "royal_scribe_guild": "royal_scribe_guild_advance",
    "bronze_age_triumphal_monument": "triumphal_monuments_advance",
    "megalithic_religious_monument": "megalithic_monument_advance",
    "bronze_monumental_gates": "monumental_gates_advance",
    "tools_maker": "tools_maker_advance",
    "weaponry_maker": "weaponry_maker_advance",
    "navy_supplies_maker": "royal_navy_supply_advance",
    "palace_registry": "royal_registry_advance",
    "palace_trade_registry": "palace_trade_registry_advance",
    "bronze_dock": "wharf_unlock_advance",
    "neolithic_river_outpost": "river_trading_outpost_advance",
    "river_trading_outpost": "river_trading_outpost_advance",
    "neolithic_feast_court": "ritual_service_advance",
    "neolithic_sanctuary": "ritual_sites_advance",
    "temple_complex": "temple_complex_advance",
    "temple_granary": "temple_granary_advance",
    "temple_scribes_guild": "temple_scribes_advance",
    "temple_healing_sanctuary": "temple_healing_sanctuary_advance",
    "temple_court": "temple_court_advance",
    "house_of_remedies": "house_of_remedies_advance",
    "sponsored_tool_maker": "tools_maker_advance",
    "sponsored_weaponry_maker": "weaponry_craft_patronage_advance",
    "sponsored_navy_supplies_maker": "royal_navy_supply_advance",
    "bronze_age_trade_office": "bronze_age_trade_posts_advance",
    "weapon_iron_age_workshop": "iron_weaponry_maker_maintenance_advance",
    "tools_iron_age_workshop": "iron_tools_maker_maintenance_advance",
    "naval_supplies_iron_age": "royal_navy_supply_advance",
    "cyclopean_walls": "cyclopean_walls_advance",
    "megaron": "megarons_advance",
    "bronze_age_oppidum": "bronze_age_oppidum_advance",
    "warrior_halls": "warrior_lodges_advance",
}

SUBJECTS = {
    "fine_cloth_palace": "a royal Bronze Age weaving room with one loom and richly woven cloth",
    "beer_palace": "a royal Bronze Age brewery with fermentation jars and a small grain basket",
    "pottery_palace": "a palace potter's wheel, painted ceramic vessels and a kiln opening",
    "winery_palace": "a royal wine press with grape baskets and decorated wine amphorae",
    "jewelry_palace": "a Bronze Age goldsmith bench with a necklace, beads and small tools",
    "bronze_age_collective_tombs": "a compact communal stone tomb with a wide burial chamber entrance",
    "gate_court": "an ancient city gate with a small judicial seat and stone steps inside the gate",
    "pottery_maker": "a simple Neolithic potter's wheel with fresh clay vessels",
    "neolithic_leather_maker": "a Bronze Age tannery workbench with stretched hide and tanning tools",
    "neolithic_beer_maker": "a village brewery with clay fermenting jars and barley",
    "neolithic_dyes_maker": "a village dyer's vat with colored woven cloth and natural dye plants",
    "neolithic_slave_market": "a fenced Bronze Age captive yard with simple wooden enclosure and trade ledger, no people",
    "neolithic_dock": "a simple timber river boatyard with one wooden landing and small boat",
    "neolithic_granary": "a cluster of small raised household grain storage huts with woven baskets",
    "sponsored_fine_cloth_maker": "a patron-funded weaving workshop with one loom and fine dyed textile",
    "sponsored_beer_maker": "a sponsored brewery with large clay fermentation jars and barley sacks",
    "sponsored_pottery_maker": "a sponsored pottery workshop with kiln and decorated vessels",
    "sponsored_wine_maker": "a sponsored wine press and several amphorae",
    "sponsored_jewelry_maker": "a sponsored goldsmith workshop with polished bronze and gold jewelry",
    "sponsored_leather_maker": "a sponsored leatherworking bench with cut hides and bronze awls",
    "fine_cloth_iron_age": "an Iron Age textile workshop with vertical loom and fine cloth",
    "beer_iron_age": "an Iron Age brewing workshop with barley sacks and brewing jars",
    "pottery_iron_age": "an Iron Age pottery kiln, wheel and finished vessels",
    "winery_iron_age": "an Iron Age wine workshop with grape press and amphorae",
    "jewelry_iron_age": "an Iron Age jewelry workshop with metalworking bench and ornaments",
    "trade_district": "a compact ancient city market district with several stalls and covered shops",
    "bronze_monument_giza_pyramid_complex": "the three main ancient Egyptian pyramids of Giza as one compact monument",
    "bronze_monument_karnak_complex": "the ancient Egyptian Karnak temple pylon and dense hypostyle columns",
    "bronze_monument_luxor_temple": "Luxor Temple's ancient Egyptian pylon gateway with obelisk",
    "bronze_monument_abu_simbel": "the rock-cut facade of Abu Simbel with four colossal seated statues",
    "bronze_monument_theban_necropolis": "ancient Egyptian Theban cliff tomb entrances carved into rock",
    "bronze_monument_hattusa_complex": "the Hittite Lion Gate and massive walls of Hattusa",
    "bronze_monument_mycenae_citadel": "the Lion Gate and Cyclopean wall of Mycenae",
    "bronze_monument_tiryns_cyclopean": "the massive rough-stone Cyclopean fortifications of Tiryns",
    "bronze_monument_pylos_palace": "the Mycenaean palace of Pylos with a central megaron",
    "bronze_monument_troy_citadel": "the Bronze Age citadel wall and gateway of Troy",
    "bronze_monument_knossos_complex": "the Minoan palace of Knossos with red tapered columns and painted facade",
    "bronze_monument_ugarit_complex": "the Bronze Age royal palace of Ugarit with Syrian courtyard architecture",
    "bronze_monument_ur_ziggurat": "the stepped mudbrick Great Ziggurat of Ur",
    "bronze_monument_assur_complex": "an ancient Assyrian sacred temple precinct and stepped ziggurat at Assur",
    "bronze_monument_chogha_zanbil": "the stepped Elamite brick ziggurat of Chogha Zanbil",
    "bronze_monument_yin_xu": "a Shang dynasty rammed-earth palace platform at Yin Xu with bronze ritual vessel",
    "bronze_monument_su_nuraxi": "the multi-tower stone nuraghe complex of Su Nuraxi in Sardinia",
    "bronze_monument_nuraghe_arrubiu": "the many-towered red-stone Nuraghe Arrubiu of Sardinia",
    "bronze_monument_santu_antine": "the three-lobed stone Nuraghe Santu Antine of Sardinia",
    "bronze_monument_romanzesu": "the Sardinian Romanzesu sacred well and stone ceremonial enclosure",
    "bronze_monument_serra_orrios": "the Sardinian Serra Orrios sanctuary with circular stone huts",
    "bronze_monument_madau_giants_tombs": "a Sardinian giants' tomb of Madau with curved stone exedra and upright stele",
    "bronze_monument_stonehenge": "the ring of massive trilithons at prehistoric Stonehenge",
    "bronze_monument_avebury": "a broad circle of prehistoric standing stones at Avebury",
    "bronze_monument_bru_na_boinne": "the Newgrange passage tomb at Brú na Bóinne with decorated entrance stone",
    "bronze_monument_shedet_sluice": "an ancient Egyptian canal sluice with timber gates and stone channel",
    "bronze_monument_great_pyramid_new": "the Great Pyramid of Giza newly completed with smooth pale limestone casing",
    "bronze_monument_great_pyramid_unfinished": "an unfinished ancient Egyptian pyramid with visible stepped blocks and construction ramp",
    "nuragic_simple_nuraghe": "one small conical Sardinian stone nuraghe tower",
    "carpenter_yard": "an ancient carpenter's yard with timber beams, wooden workbench and bronze saw",
    "cloth_palace": "a royal Bronze Age cloth workshop with vertical loom and folded fabric",
}


def main() -> None:
    text = REPORT.read_text(encoding="utf-8").split("## Bâtiments", 1)[1]
    ids = re.findall(r"^- `([A-Za-z0-9_]+)`", text, flags=re.MULTILINE)
    localization: dict[str, str] = {}
    for path in (ROOT / "main_menu/localization/english").rglob("*.yml"):
        content = path.read_text(encoding="utf-8-sig")
        localization.update(re.findall(r'^\s*([A-Za-z0-9_]+):\s*"([^"]*)"', content, flags=re.MULTILINE))

    plan = []
    for name in ids:
        advance = REUSE.get(name)
        if advance and not (ADVANCE_ICONS / f"{advance}.dds").exists():
            raise FileNotFoundError(f"Reuse source missing: {advance}")
        plan.append({
            "id": name,
            "method": "reuse_advance" if advance else "generate",
            "advance_icon": advance,
            "label": localization.get(name, name.replace("_", " ")),
            "description": localization.get(f"{name}_desc", ""),
            "subject": SUBJECTS.get(name, ""),
        })
    if len(plan) != 102:
        raise ValueError(f"Expected 102 missing building icons, got {len(plan)}")
    OUTPUT.write_text(json.dumps(plan, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{len(plan)} buildings: {len(REUSE)} reuse, {len(plan) - len(REUSE)} generate")


if __name__ == "__main__":
    main()
