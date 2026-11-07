# Bronze Era music integration

## Verified EU5 audio structure

The installed EU5 build uses Wwise. The game ships compiled banks under `game/loading_screen/sound/banks/windows/`, including `sb_music_logic.bnk`, `sb_music_media.bnk`, and numbered `.wem` media. Its companion `sb_music_logic.txt` lists events such as `mus_culture_track_start`, `mus_sys_dynamic_cultural`, and `MusicPlayer_01_Overture_I_Genesis`.

The script file `game/in_game/common/music_player_tracks/00_music_player_tracks.txt` documents that new songs must be registered by their Wwise event name, with optional composer/performer/soloist metadata and localization. These entries describe songs in the music player; they do not expose a script trigger for choosing a song by country culture or situation. No event-to-situation or event-to-country-culture hook was found in the installed script or bank text. Do not treat a `music_player_tracks` entry as a playback condition.

In this mod, `loading_screen/sound/map/ambience/sound_alias_bank.txt` maps map/terrain ambience aliases to `silence`; these are not music tracks. No `.bank`, `.wem`, source audio, Wwise project, or Wwise bank-generation tool is present in the mod. The repository's existing report builders are unrelated to audio.

The vanilla Windows bank layout is evidence about EU5's installed assets, not proof that a mod can replace those banks by copying files to the same path. No mod bank output path, bank override precedence, or dynamic music script API has been confirmed in-game. Do not copy vanilla banks or publish a guessed bank.

## Proposed catalogue

Conditions below are design intent, not executable EU5 syntax. They must not be turned into script until an EU5 music condition or runtime mechanism is verified.

| Reference | Intended use | Intended condition | Status |
| --- | --- | --- | --- |
| [Main theme](https://www.youtube.com/watch?v=62pa9YAf6f8) | Main theme; also Mesopotamia and Iranian Plateau | Main menu/start theme; regional play only for cultures in `mesopotamian_group` or `iranian_plateau_group` | Reference only; source audio, redistribution permission, Wwise event/bank, and runtime test missing |
| [General ambience 1](https://www.youtube.com/watch?v=nzK62clVNdc) | General pool, placement pending listening | No regional assignment until the reference is auditioned | Reference only; audio review, source/license, Wwise integration, and test missing |
| [General ambience 2](https://www.youtube.com/watch?v=r32Qg7JyHws) | General pool, placement pending listening | No regional assignment until the reference is auditioned | Reference only; audio review, source/license, Wwise integration, and test missing |
| [General ambience 3](https://youtu.be/3P7tIBn3PBo) | General pool, placement pending listening | No regional assignment until the reference is auditioned | Reference only; audio review, source/license, Wwise integration, and test missing |
| [General ambience 4](https://www.youtube.com/watch?v=rK17O821zio) | General pool, placement pending listening | No regional assignment until the reference is auditioned | Reference only; audio review, source/license, Wwise integration, and test missing |
| [General ambience 5](https://youtu.be/QpxN2VXPMLc) | General pool, placement pending listening | No regional assignment until the reference is auditioned | Reference only; audio review, source/license, Wwise integration, and test missing |
| [Northern/Celtic 1](https://www.youtube.com/watch?v=Ld6Dt-Lce6M) | Nordic/Celtic regional pool | Candidate culture groups: `germanic_nordic_group` and `gaulish_bronze_group`; confirm track-to-region after listening | Reference only; source/license, Wwise integration, and test missing |
| [Northern/Celtic 2](https://youtu.be/sOVUOQtn0Io) | Nordic/Celtic regional pool | Candidate culture groups: `germanic_nordic_group` and `gaulish_bronze_group`; confirm track-to-region after listening | Reference only; source/license, Wwise integration, and test missing |
| [Northern/Celtic 3](https://youtu.be/ouiW8fPDG1A) | Nordic/Celtic regional pool | Candidate culture groups: `germanic_nordic_group` and `gaulish_bronze_group`; confirm track-to-region after listening | Reference only; source/license, Wwise integration, and test missing |
| [Egypt](https://youtu.be/nBmWXmn11YE) | Egyptian regional pool | Candidate group `egypt_nile_group` (Egyptian, Upper Egyptian, Lower Egyptian, Nubian, Medjay, Libyan); validate player-country culture scope | Reference only; source/license, Wwise integration, and test missing |
| [Trojan War](https://www.youtube.com/watch?v=FSDooEjiclM) | Trojan War situation | While `trojan_war_phase_1` or `trojan_war_phase_2` is active; those situations begin at internal dates 5.1.1 and 14.1.1 respectively | Situations verified; conditional audio playback is not exposed/verified; source/license and Wwise integration missing |
| [Hittite collapse](https://www.youtube.com/watch?v=xmQ3leDTZRU) | Hittite collapse situation | While `bronze_hatti_collapse` is active; its start is gated from internal date 15.1.1 plus the existing Sea Peoples/raid conditions | Situation verified; conditional audio playback is not exposed/verified; source/license and Wwise integration missing |
| [Roman Music by Farya Faraji playlist](https://www.youtube.com/playlist?list=PLMlRYqqqM5rrjeaJuVaC6MWN7e7fSXGJt) | Roman/Latin pool; include playlist tracks except its final approximately 20-minute video | The player's country culture must be exactly `latin`. Do not gate on Roman ownership, Italian territory, or the broader `italic_bronze_group` | Playlist title confirmed from public feed; full ordered list/durations and excluded video's title/ID unavailable; source/license, Wwise integration, and test missing |

## Culture and situation anchors

- The mod defines `latin`, `etruscan`, `umbrian`, `samnite`, and `ligurian` in `italic_bronze_group`. Roman playlist eligibility is intentionally narrower: exact country culture `latin` only.
- Mesopotamian cultures use `mesopotamian_group`; Iranian Plateau cultures use `iranian_plateau_group`.
- Nordic identities include `nordic`, `jutlandic`, and `germanic` in `germanic_nordic_group`. Gaulish/Celtic definitions use `gaulish_bronze_group` (some also carry a `celtic` group).
- The Trojan War situations and the Hatti collapse situation already exist. Their lifecycle can provide the desired thematic timing in game logic, but no supported music-call syntax is present to connect it to Wwise.

## Integration prerequisites

1. Obtain source audio files and written permission that explicitly covers modification, game-mod redistribution, and the intended platforms. YouTube URLs alone do not grant those rights; no YouTube audio has been copied here.
2. Obtain or create an authorized Wwise authoring project/build profile for the EU5-compatible event and media format. Produce actual Windows `.bnk`/`.wem` output and verify how EU5 discovers mod banks before adding files under the mod's `loading_screen/sound/banks/windows/` tree.
3. Only after a real Wwise event and bank exist, add the event's actual name and authorized credits/localization to the game's `music_player_tracks` data shape. Separately verify how playback selection is controlled; metadata alone cannot implement the regional or situation conditions above.
4. Test each condition in EU5: Latin player country versus non-Latin player in Italy/Rome, regional culture changes, Trojan War phase transitions, Hatti-collapse start/end, and vanilla music fallback.

## Current replacements

None. No vanilla music track is disabled, replaced, or re-registered by this mod. The current `sound_alias_bank.txt` ambience aliases are not music replacements. Replacing vanilla tracks is blocked on authorized audio and a verified EU5 Wwise/mod playback path.
