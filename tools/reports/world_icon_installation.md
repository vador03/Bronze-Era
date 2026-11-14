# Icônes des situations et institutions

Les neuf situations et les dix-huit institutions déclarées dans `in_game/common/situations` et `in_game/common/institution` disposent maintenant toutes d'un fichier d'icône. Vingt fichiers ont été ajoutés : six pour les situations, quatorze pour les institutions.

## Situations ajoutées

Dans `main_menu/gfx/interface/icons/situations/` :

- `bronze_achaemenid_rise.dds`
- `egyptian_rule_in_canaan.dds`
- `trojan_war_phase_1.dds` — illustration reprise de `00_bronze_trojan_war_phase_1.dds`, dont le nom ne correspondait pas à l'identifiant de la situation
- `trojan_war_phase_2.dds`
- `bronze_zoroastrian_revelation.dds`
- `bronze_assyrian_campaigns.dds`

## Institutions ajoutées

Dans `main_menu/gfx/interface/icons/institutions/` :

- `bronze_routes.dds`
- `commercial_counters.dds`
- `iron_metallurgy.dds` — illustration reprise de `main_menu/gfx/interface/advance/iron_metallurgy_advance.dds`
- `tribal_migrations.dds`
- `hoplite_phalanx.dds`
- `phoenician_alphabet.dds`
- `classical_philosophy.dds`
- `imperial_administration.dds`
- `standardized_currency.dds`
- `bronze_large_libraries.dds`
- `bronze_professional_armies.dds`
- `hellenistic_cosmopolitanism.dds`
- `road_network.dds`
- `roman_law.dds`

## Références et contrôle

Le jeu recherche ces icônes par identifiant dans les dossiers ci-dessus ; aucune ligne `icon =` n'est présente dans les définitions concernées et aucune référence explicite n'a dû être ajoutée. Les deux illustrations reprises ont été installées sous leur nom attendu, en conservant les sources.

Les vingt nouveaux fichiers sont des DDS DXT5 de 128 × 128 pixels avec huit niveaux de mipmaps et un canal alpha contenant des pixels entièrement transparents. Les quatre coins sont transparents. Les vingt fichiers ont été décodés et examinés sur la [planche de contrôle](world_icon_contact_sheet.png). Aucune situation ou institution déclarée ne reste sans icône. Le jeu n'a pas été lancé.
