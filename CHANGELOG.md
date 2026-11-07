# Changelog

## Unreleased — Tribal Migration development build

- Removed the Bronze Age right-click frontier colony action. Added dated regional pirate spawns in the Mediterranean, China Sea and Persian Gulf; the player-controlled Lukka receive an opening choice to adopt piracy (90% AI preference). New pirate havens can claim an unowned coast or a non-capital coast below 30% control, then create a wharf, recruitment buildings and age-appropriate fleets with matching culture and religion.
- Added two Country Content decisions for an army-based migrant: colonize the unowned land under its escort while remaining migratory, or settle permanently and become territorial. Colonization costs 25 gold, has a five-year cooldown and a four-colony cap beyond the original camp. Native POPs move immediately to the new colony or permanent settlement.
- Fixed the game-reported province-definition scope error that prevented the total migration decision and action from executing; camp locations now use native province-definition location iterators.
- Corrected decision localization keys to `.title`/`.desc`, event AI choice weights, and the optional offshoot player-switch scope; encoded new script files as UTF-8 with BOM as required by the game lexer.
- Removed the decision's engine-level `only_once` flag so a failed attempt in an existing save can be retried; the successful departure still sets the shared once-per-country guard.
- Converted the tribal migration action into a total migration that makes the original country army-based and commandable.
- Added the total migration to Country Content decisions and restored its manual camp-selection action in the current Form New Country interface.
- Updated the overridden Form New Country GUI to the installed game's layout, retaining the two village-community transition buttons.
- Added exact departure shares by POP type: all nobles/soldiers, 60% of burghers/laborers/clergy, and 20% of peasants/tribesmen.
- Added a controllable migration escort, manual POP-follow order, and settlement action.
- Added a partial migration that creates an army-based vassal without ending the parent country's independence, with an optional player switch to the new group.
- Added costs, one-total-migration-per-country and one-active-offshoot limits, offshoot cooldown, crisis-only AI total departures, and quarterly camp food shortage and foreign-passage events.
- Added English and French localization.
- Documented native script evidence, technical limits and historical-zone data plan. Vanilla colonization and POP-country migration files were not modified.
