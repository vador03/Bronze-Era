# Cultes peu développés : audit et ajouts

## Périmètre

L'inventaire de `00_bronze_age_religions.txt` compte 76 religions. Avant ces ajouts, 13 disposaient d'au moins une divinité et un lieu sacré propres au mod, et 38 avaient au moins un lieu sacré. Les 25 autres n'avaient ni divinité, ni lieu sacré propre : 23 n'avaient aucun événement religieux repéré et `punic` et `armenian_pagan` servaient surtout à la fondation de pays. Ces 25 religions constituent le périmètre de cette modification. Les religions disposant déjà d'un sanctuaire sont préservées.

| Religion | Deux situations ajoutées | Organisation représentée |
| --- | --- | --- |
| `bilozerka_rites` | Pâturages appauvris ; serments près d'un tertre | Foyers et clans pastoraux |
| `baltic_pagan` | Bois sacré disputé ; offrandes au passage du fleuve | Anciens et gardiens locaux |
| `finnic_pagan` | Réserves du lac ; présages avant un conflit | Familles et devins locaux |
| `baiyue_rites` | Récolte fluviale ; visiteurs de l'estuaire | Communautés des fleuves et des côtes |
| `mumun_rites` | Réserves de grain ; entretien d'un lieu funéraire | Conseils villageois |
| `austroasiatic_rites` | Nouveau défrichement ; repas après une mauvaise récolte | Foyers et anciens locaux |
| `khmer_rites` | Eau et sanctuaire local ; serment de nouveaux établissements | Gardiens locaux et pouvoir émergent |
| `karasuk_rites` | Parcours des troupeaux ; divination avant la guerre | Familles pastorales |
| `puntite_rites` | Voyage côtier ; pénurie à l'intérieur | Foyers, marins et marchands |
| `cushitic_rites` | Point d'eau contesté ; protection des troupeaux en guerre | Clans pastoraux |
| `nilo_saharan_rites` | Niveau bas du fleuve ; entretien d'un passage | Villages et gardiens locaux |
| `mande_rites` | Routes d'échange ; forgerons pendant la guerre | Lignages et communautés |
| `bantu_rites` | Semences partagées ; champs de nouveaux villages | Parenté et anciens locaux |
| `khoisan_rites` | Point d'eau ; traces d'un ennemi | Groupes locaux sans clergé commun |
| `mayan_rites` | Pluie tardive ; mémoire d'un lignage dirigeant | Foyers et cour émergente |
| `zapotec_rites` | Calendrier public après 600 av. J.-C. ; mauvaise récolte | Villages et gardiens du calendrier |
| `puebloan_rites` | Réserves d'eau ; lieu de rassemblement | Communautés distinctes |
| `woodland_rites` | Tertre ancestral avant la guerre ; échange fluvial | Communautés régionales |
| `arawak_rites` | Retour des canoës ; jardins endommagés | Foyers côtiers et insulaires |
| `tupi_rites` | Pêche et voisinage ; conseil de guerre fluvial | Villages et parentés |
| `saqqaq_rites` | Glace et chasse ; visiteurs de la côte | Foyers arctiques |
| `papuan_rites` | Échanges de coquillages ; chemins entre jardins | Clans locaux |
| `dreaming_ways` | Soin d'un point d'eau ; routes troublées par la guerre | Gardiens locaux et liens au territoire ancestral |
| `punic` | Offrandes avant un voyage maritime ; serment d'une cité en guerre | Temple civique et familles du port |
| `armenian_pagan` | Offrande royale dans un district instable ; serment défensif | Cour et temples locaux, sans autorité religieuse unique |

## Règles de jeu

Les 50 événements utilisent la pulsation annuelle du pays. Chaque sous-pulsation vérifie d'abord sa propre religion. Elle ne cherche une province en pénurie ou mal contrôlée que pour un pays concerné. Les autres contextes sont guerre, port ou plusieurs établissements encore peu contrôlés. Une situation admissible a 8 % de chances par an de lancer son événement, puis un délai commun de six ans bloque les nouveaux récits religieux de ce pays. Chaque événement propose un rite financé, s'il reste assez d'or, et une réponse pratique gratuite. Les effets varient selon la situation et durent deux à quatre ans.

Neuf petits modificateurs réutilisables portent sur les pâturages, réserves, lignages, défense, chasse, accords locaux, nourriture, échanges et routes côtières. Aucun bonus permanent de pouvoir clérical n'a été ajouté ; deux cérémonies civiques donnent une faible satisfaction au clergé punique ou arménien. Les choix liés aux cours maya et zapotèque peuvent édifier le bâtiment existant `neolithic_sanctuary` dans la capitale s'il n'y est pas déjà. Le récit maya de cour n'est disponible qu'à partir de l'année interne 410 (environ 800 av. J.-C.) ; le calendrier zapotèque à partir de 610 (environ 600 av. J.-C.). Les récits Bilozerka, Karasuk et Saqqaq cessent après l'année interne 410, afin de ne pas projeter ces étiquettes archéologiques trop tard. Les récits puniques nommés commencent à l'année interne 710 (environ 500 av. J.-C.) et les récits arméniens à 910 (environ 300 av. J.-C.).

Aucun lieu sacré fixe ni panthéon commun n'a été créé pour ces ensembles très larges. Deux cultes nommés distincts ont été ajoutés là où la tradition est mieux attestée : Baal Hammon pour `punic` et Aramazd pour `armenian_pagan`. Tanit et Anahit figurent dans leurs récits, sans dupliquer la divinité `tanit_sea_star` déjà associée à `sea_peoples_cult` dans le mod. Les scènes de présage, d'ancêtres ou d'esprits expriment la manière dont les personnages comprennent leurs traditions. Elles ne déclarent pas une intervention surnaturelle réelle. Les 20 descriptions auparavant identiques ont été remplacées en anglais et en français ; leurs noms français ont aussi été traduits.

## Sources et incertitudes

La chronologie modifiée du jeu est positive : l'année interne 1 représente 1209 av. J.-C. Pour Oaxaca, le [Metropolitan Museum of Art](https://www.metmuseum.org/toah/hd/alban/hd_alban.htm) situe des structures de rituel public vers 600 av. J.-C. et la fondation de Monte Albán vers 500 av. J.-C. Les noms de divinités mayas abondamment documentés dans les collections du [Met](https://www.metmuseum.org/es/exhibitions/gods-divinity-maya-art/guia-del-visitante) appartiennent surtout à des œuvres postérieures à la fin du mod ; aucun nom tardif n'a donc été imposé à tous les Mayas préclassiques. L'[AIATSIS](https://aiatsis.gov.au/sites/default/files/research_pub/teaching_aboriginal_and_torres_strait_islander_art_in_the_gallery_and_the_classroom.pdf) souligne la diversité des traditions des peuples autochtones d'Australie ; `dreaming_ways` reste une catégorie de jeu large, sans divinité ni institution uniformes.

Les cultes de Karasuk, Bilozerka, Saqqaq, du Pount et plusieurs catégories linguistiques très étendues n'ont pas de mythologie nommée sûre pour toute la période. Leurs récits sont des interprétations de jeu fondées sur les thèmes locaux déjà présents dans le mod (pâturages, chasse, eau, parenté et échanges), pas des reconstitutions certaines. Aucune localisation de sanctuaire historique supplémentaire n'a été inventée sans identifiant de carte et justification fiables.

Le [British Museum](https://www.britishmuseum.org/sites/default/files/2020-08/R2-Collecting-the-World_LPG.pdf) documente le couple punique Baal Hammon–Tanit, surtout à travers des témoignages plus tardifs. L'[Encyclopaedia Iranica](https://www.iranicaonline.org/articles/armenia-iii/) décrit Aramazd et Anahit dans la religion arménienne marquée par les échanges iraniens. Leurs événements sont donc limités aux périodes tardives. Les deux dieux ont aussi un `potential` daté sur le modèle des définitions natives ; la disponibilité en jeu de ce filtre reste à vérifier.

Vérification actuelle : références et structure des scripts seulement. Les événements ne sont pas encore vérifiés en jeu. Plusieurs religions ciblées n'ont aucun pays de cette foi dans le scénario initial ; leurs événements deviennent disponibles si un pays de cette religion apparaît ensuite.
