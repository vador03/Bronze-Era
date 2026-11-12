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

The illustration was generated with the built-in imagegen tool using this
prompt: "A cinematic wide 16:9 historical painting of the rise of the Median
and Achaemenid Persian empire around 750–550 BCE: a Median mounted leader and
Persian noble envoys on the Iranian plateau at dawn, cavalry and banners behind
them, Ecbatana's mudbrick walls and dry mountains in the distance. Richly
painted grand strategy key art, natural anatomy, atmospheric depth, ochre,
bronze, lapis blue and muted crimson. No text, logos, watermarks, modern
objects, Greek or Roman armor, or fantasy elements."

Static checks completed: balanced braces, matching English and French keys,
all referenced location IDs, all event text and art references, DDS dimensions
and payload size, and `git diff --check`. An in-game campaign test is still
needed to confirm UI rendering and event pacing.
