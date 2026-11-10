# Les sept rois traditionnels de Rome

La fondation dynamique de `c:ROME` créait déjà Romulus. Cette suite le complète sans charger des personnages romains au début de la partie (1209 av. J.-C.). Les dates ci-dessous reprennent la chronologie demandée. Ce sont les dates de la tradition romaine, pas une chronologie archéologiquement établie ; les sources modernes donnent parfois des années de transition légèrement différentes.

| Roi | Règne traditionnel demandé | Années internes | Traits en jeu |
| --- | --- | --- | --- |
| Romulus | 753–715 av. J.-C. | 457–495 | `be_romulus_she_wolf` : moral, légitimité et contrôle modérés |
| Numa Pompilius | 715–673 av. J.-C. | 495–537 | `lawgiver`, `righteous` : lois et rites civiques attribués par la tradition |
| Tullus Hostilius | 673–641 av. J.-C. | 537–569 | `conqueror`, `bold_fighter` : réputation guerrière |
| Ancus Marcius | 641–616 av. J.-C. | 569–594 | `architectural_visionary`, `careful` : travaux et prudence politique |
| Tarquin l'Ancien | 616–575 av. J.-C. | 594–635 | `architectural_visionary`, `charismatic_negotiator` : chantiers et alliances |
| Servius Tullius | 575–535 av. J.-C. | 635–675 | `lawgiver`, `benevolent` : réformes civiques traditionnelles |
| Tarquin le Superbe | 535–509 av. J.-C. | 675–701 | `cruel`, `conqueror` : autorité violente et politique militaire |

La conversion du mod est `année interne = 1210 - année av. J.-C.`. La fondation de Rome conserve sa date interne `457.4.21` (21 avril 753 av. J.-C.). Les successions sont vérifiées dans la pulsation mensuelle du seul pays `ROME`, et chaque roi est créé une fois dans sa fenêtre. Si Rome apparaît tardivement, la fonction choisit directement le roi de la période courante. Si elle apparaît après 509 av. J.-C., elle commence comme république.

En 509 av. J.-C., une Rome contrôlée par l'IA adopte la république. Le joueur reçoit un événement avec le choix de fonder la république ou de conserver la royauté. Le choix est définitif pour cette séquence ; la décision de conserver la royauté laisse Tarquin ou son successeur au pouvoir selon le déroulement de la partie.

## Enlèvement des Sabines

Un événement unique se produit sous Romulus après le 18 août de l'année interne 457, tant que Rome possède la ville et reste une monarchie. L'IA applique directement l'effet ; le joueur voit l'événement dans `in_game/events/Roman/bronze_roman_kings_events.txt`. Le texte décrit l'enlèvement comme une violence racontée par les auteurs romains, sans reprendre leur justification comme un fait établi.

L'événement ajoute `0.500` millier de POP paysannes latiales (environ 500 personnes à l'échelle du mod) à Rome. La culture latiale suit les données existantes de `location:sabina` : le mod ne définit pas de culture sabine distincte. La ville reçoit `+0.0015` de croissance locale pendant douze ans. Les pays voisins perdent 35 points d'opinion envers Rome ; ce malus s'atténue de deux points par an. Le choix de ne pas soustraire une quantité précise à chaque communauté voisine évite d'attribuer à des lieux déterminés les chiffres contradictoires des sources antiques. La POP ajoutée représente une abstraction de l'arrivée des captives et de leur intégration dans la ville, et non un décompte historique certain.

L'illustration fournie a été étendue au format panoramique de l'interface, en conservant la scène centrale. Le jeu utilise `main_menu/gfx/interface/illustrations/situation/bronze_rome_sabine_women.dds` ; la source PNG adaptée est conservée dans `docs/assets/bronze_rome_sabine_women_source.png`. L'architecture visible relève de la peinture historique, non d'une reconstitution archéologique de Rome au VIIIe siècle av. J.-C. [Plutarque, *Vie de Romulus*, 14–15](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Plutarch/Lives/Romulus%2A.html) rapporte plusieurs chiffres incompatibles et situe la fête des Consualia au 18 août. [Tite-Live, *Histoire de Rome*, I, 9–13](https://pressbooks.claremont.edu/clas112pomonavalentine/chapter/livy/) présente également l'épisode comme un récit des origines de la cité.

Le trait propre à Romulus, « Fils de la louve », traduit un récit fondateur rapporté par les Romains. Il n'affirme pas que l'épisode légendaire a eu lieu. Les six autres rois utilisent des traits natifs vérifiés dans les fichiers installés d'EU5. Les Tarquins portent la culture étrusque du mod et la religion italique de Rome ; la culture de Servius, dont les traditions d'origine divergent, reste latiale pour éviter d'imposer une version unique.

Sources de contexte : [Tite-Live, *Histoire de Rome*, livre I](https://classicslaunch.org/works/livy-history-of-rome-books-i-v/) et [sourcebook de l'université de Warwick](https://warwick.ac.uk/fac/arts/classics/warwickclassicsnetwork/stoa/anchist/gcse/foundations/resources/early_rome_sourcebook_and_key_learning.pdf). La [synthèse d'Oxford sur la royauté romaine](https://academic.oup.com/reference/62365/reference-article-abstract/554619978?login=false) rappelle le caractère tardif et disputé de la chronologie des sept rois.

Vérification actuelle : syntaxe, identifiants, traits, noms et références croisées des scripts ; intégrité du fichier DDS contrôlée pixel par pixel sur plusieurs points. L'ordre réel des successions, l'affichage du nom de famille, l'événement sabin et le passage à la république demandent encore un test en jeu. Une mort naturelle précoce peut faire accéder un dirigeant intermédiaire au trône avant la date traditionnelle suivante ; la suite installe alors le roi prévu à la date indiquée. Un changement de type de gouvernement avant 509 av. J.-C. suspend la suite des rois.
