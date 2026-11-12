# Rise of the Achaemenids

The situation starts in internal year 460 (750 BC on the Bronze Era calendar).
Independent Median and Persian states with an Iranian religion and a capital in
`persia_region` compete for the imperial claim. Once per year, the situation
ranks them by levies, standing army, income and country rank. Media receives a
selection bonus and an automatic military modifier until internal year 510
(700 BC). If Media falls, another eligible realm can take the claim.

The timeline has three stages: the Median confederation, the road to Nineveh
from internal year 598 (612 BC), and the Median-Persian settlement from internal
year 658 (552 BC). `mosul` represents Nineveh; `hillah` represents Babylon;
`shush` represents Susa. These are the map's actual location IDs. The
historical ruler names are flavor cues, not forced ruler replacements.

The existing `PERSIA_f` is the only formation route. From 552 BC, the current
claimant needs kingdom rank, Abhar, Hamadan/Ecbatana, Istakhr and 55% of the
listed Iranian heartland. This replaces the earlier Persian-only culture and
Bronze institution gates. Formation grants empire rank, Persian court culture,
Median acceptance and a permanent foundation modifier. Post-formation events
reward control of Babylon and, from 522 BC, Susa with the Royal Road.

The situation panel, map colors and event illustration use
`bronze_achaemenid_rise.dds`. The editable generated source PNG is beside it;
`tools/Convert-PngToDds.ps1` regenerates the DXT5/BC3 DDS.

After formation, Persia adopts the expansionist AI personality. The situation
continues through two sequential 240-month campaigns. The first requires
Babylon (`hillah`) and a net gain of eight locations in `iraq_arabi_area`.
The second requires Balkh and a net gain of eight locations in
`eastern_khorasan_area` or `sistan_area`. Direct Persian holdings and the
holdings of Persian satrapies both count. Success grants a 20-year country
modifier; missing the deadline gives five years of court discontent. The
campaign panel shows net gains and remaining months, and the map highlights
the active area. AI area preferences and temporary levy/movement bonuses help
Persia pursue each target.

`bronze_satrapy` is a Persia-only subject type that can be used when releasing
a country or creating a province subject. The "Establish a Satrapy" country
interaction converts an existing Persian vassal with less than 70 liberty
desire. Satrapies pay 25% scaled gold and 5% scaled manpower, join imperial
wars, preserve their local ruler and religion, and consume 65% of a normal
vassal's diplomatic capacity. Persia can build roads, buildings and resource
operations and recruit regiments there. Annexation becomes possible after 20
years. Named satrapies and exact geographic limits are reserved for the list
the user plans to provide; the generic mechanic works without it.

The illustration was generated with the built-in imagegen tool using this
prompt: "A cinematic wide 16:9 historical painting of the rise of the Median
and Achaemenid Persian empire around 750–550 BCE: a Median mounted leader and
Persian noble envoys on the Iranian plateau at dawn, cavalry and banners behind
them, Ecbatana's mudbrick walls and dry mountains in the distance. Richly
painted grand strategy key art, natural anatomy, atmospheric depth, ochre,
bronze, lapis blue and muted crimson. No text, logos, watermarks, modern
objects, Greek or Roman armor, or fantasy elements."

Static checks after the satrapy update: balanced braces in modified scripts,
matching English and French keys, localization for all situation events, valid
map area and location IDs, and `git diff --check`. An in-game campaign test is
still needed to confirm UI rendering, subject creation and event pacing.
