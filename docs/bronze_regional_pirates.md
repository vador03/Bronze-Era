# Regional pirates

The Bronze Age right-click frontier colony action has been removed. Existing tribal migration and its separate settlement decisions are unchanged.

On the first day, LUKKA receives a visible event: retain its government or become a pirate brotherhood. The AI weights the pirate choice 90 to 10. Accepting keeps the Lukka country and its population, converts its government to the native pirate republic reform, makes its best coastal location the capital, constructs a wharf, pirate stronghold and tavern, and gives it three early galleys and one round ship. A natural port also gets the Bronze dock. A slave market is added only if the country's slavery rule permits it.

Other pirate groups use hidden yearly events. Each group can appear once per campaign where an eligible coast exists in its area. An unowned coast can be granted to the new naval country. Pirates can also seize an owned coastal location when local control is strictly below 30%, provided it is neither the owner's capital nor its last location. Existing POPs and the former country's core are retained; additional matching culture and religion POPs join the pirate settlement. It receives a wharf, the vanilla pirate stronghold restored in the mod's overridden building file, a pirate tavern and an age-appropriate fleet. A rural location is upgraded to town, while an existing town or city keeps its rank. The wharf is built **after** the spawn and `is_port` is not a spawn condition. A Bronze dock is added where the map already marks a natural port.

| Group | Internal years | Display period, approximately | Area | Culture | Religion |
| --- | --- | --- | --- | --- | --- |
| Sherden | 1–60 | 1209–1150 BC | Aegean archipelago | `sherden` | `sea_peoples_cult` |
| Tjekker or Peleset, one per campaign | 1–60 | 1209–1150 BC | Levant | `tjekker` or `peleset` | `sea_peoples_cult` |
| Illyrian | 910–1100 | 300–110 BC | Croatia | `illyrian` | `illyrian_pagan` |
| Etruscan | 410–910 | 800–300 BC | Sicily | `etruscan` | `etruscan` |
| Baiyue | Bronze Age | Bronze Age | Fujian | `baiyue` | `baiyue_rites` |
| Dilmunite | Bronze Age | Bronze Age | Bahrein | `dilmunite` | `dilmunite` |

## Middle and late Iron Age expansion

The northern groups are eligible from internal year 260 to 710 (approximately 950–500 BC). The Phoenician groups are eligible from year 250 to 910 (approximately 960–300 BC). Each yearly roll has a 4% chance per eligible country. Alternative areas within the same sea share a global spawn flag, so at most one new pirate country is founded for each of the six sea groups below. All use the same free-coast or below-30%-control rule, and the wharf is still added after the country appears.

| Sea group | Alternative coastal areas | Culture | Religion | Warship |
| --- | --- | --- | --- | --- |
| North Sea | Denmark or Friesland | `jutlandic` or `germanic` | `nordic_pagan` | `n_long_boat` |
| Baltic Sea | Prussia or Götaland | `Baltic` or `nordic` | `baltic_pagan` or `nordic_pagan` | `n_long_boat` |
| Phoenician Iberia | Andalusia or Catalonia | `phoenician` | `phoenician` | `n_traditional_galley` |
| Phoenician Mediterranean | Balearic Islands | `phoenician` | `phoenician` | `n_traditional_galley` |
| Phoenician North Africa | Morocco or Tunis | `phoenician` | `phoenician` | `n_traditional_galley` |
| Phoenician Black Sea | Crimea or Pontus | `phoenician` | `phoenician` | `n_traditional_galley` |

These are regional pirate labels for gameplay. They do not assert that permanent pirate states with these exact names existed at every listed coast. The Black Sea Phoenician group is an alternate-history possibility requested for this mod. Northern groups are named for their regions rather than as Vikings, which would be anachronistic in this period.

The Sherden, Tjekker, Peleset, Illyrian and Etruscan labels follow the supplied historical periods. Baiyue and Dilmunite sea raiders are regional fictional groups using the mod's existing cultures and faiths; the labels do not assert attested pirate states. Cretans, Aetolians, Cilicians and Jewish raiders were not made permanent pirate countries here because the supplied chronology, cultures or episodic nature of their activity need different event designs.

Technical basis: EU5's installed `wokou_events.txt` uses `create_country_from_location` on free land, then changes government and applies the pirate reform. `golden_age_of_piracy.txt` uses the naval country type and pirate stronghold. The mod already defines `n_early_galley`, `n_long_boat`, `n_traditional_galley` and `n_round_ship`, and its `wharf` allows ship construction on any coast. The mod's `capital_buildings.txt` had commented out `pirate_stronghold`, so that definition was restored from the installed game's version.

Verification so far is static only. The game has not been launched with these new files. A group cannot appear if its area has neither an unowned coast nor a non-capital coast below 30% control during its eligible years. Ship spawning from a coastal location that is not a natural map port must be confirmed in game.
