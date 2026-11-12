# The Revelation of Zarathustra

The scenario's old Iranian faith is keyed `iranic` (displayed as "Iranian
Rites" / "Rites iraniens"). The new `zoroastrian` religion reuses vanilla
EU5's named colour, religious group, Persian language, own-faith tolerance,
selling-efficiency bonus (0.1), icon and English/French religion localization. Its
small extra heathen tolerance and kindred relationship with `iranic` make
the transition less disruptive to Iranian communities.

The micro situation becomes eligible in internal year 580, corresponding to
630 BC in the mod. This is a gameplay date for the emergence of teachings;
the traditional birth date around 660 BC is not treated as the date of the
new religion's foundation. The chronology of Zarathustra is debated.

Every country following `iranic`, or with at least 35% of its population
following `iranic`, receives the founding event once. A small community of
followers appears in an eligible location. Embracing changes the court and
ruling family to `zoroastrian`; resisting keeps the state religion and stops
the scripted spread. The AI weights the embrace option 99 to 1. An embracing
country converts 12% of each remaining `iranic` pop per year through
`split_pop`, even after the situation ends, so conquest or release cannot
silently stop the transition. Other faiths and countries that resist are not
converted by this script. A 25-year tolerance and unrest modifier cushions
the change, and reaching 60% Zoroastrian population triggers a settlement
event with a 15-year reward.

The Achaemenid claimant trigger and `PERSIA_f` formation accept both the old
Iranian rites and Zoroastrianism, so the new faith cannot block Persia's
formation. The situation ends in internal year 700 (510 BC), while annual
conversion for courts that embraced it continues.

Sources for the dating and religious background:
[Zoroastre](https://fr.wikipedia.org/wiki/Zoroastre),
[Zoroastrisme](https://fr.wikipedia.org/wiki/Zoroastrisme).

Static checks completed: balanced braces and clean whitespace in the 12
affected scripts, matching English/French situation keys, localization for
both events, available vanilla icon and religion text, available event art,
and `git diff --check`. An in-game run is still needed to confirm the event
flow and population conversion pace.
