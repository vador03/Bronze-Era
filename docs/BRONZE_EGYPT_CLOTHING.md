# Vêtements égyptiens : premier prototype

## Portée

Ce prototype modifie uniquement les vêtements des portraits des cultures `egyptian`, `upper_egyptian` et `lower_egyptian`, repérées par `egyptian_gfx`. Il ne change ni les coiffes, ni les bijoux, ni les règles de jeu.

- Personnages ordinaires : lin écru.
- Élites : lin clair avec accents ocre.
- Dirigeant du pays `EGY` : lin clair avec accents or et bleu.

Les formes réutilisent des modèles 3D d'EU5 : un vêtement masculin noué à la taille et une tunique féminine simple. Les entités, les variations de matière et les palettes sont propres à Bronze Era. Cela donne un premier résultat visible sans écraser les ressources d'origine. Les coupes restent approximatives : les modèles réemployés n'ont pas été sculptés pour l'Égypte ancienne. Une version à silhouette historiquement précise demanderait de nouveaux maillages et leur export dans le format du moteur.

## Points d'entrée

1. `in_game/common/genes/08_be_bronze_egypt_clothes.txt` : trois gènes de vêtement, indices 230 à 232.
2. `main_menu/gfx/portraits/portrait_modifiers/08_be_bronze_egypt_clothes.txt` : choix selon culture, statut et dirigeant d'EGY.
3. `main_menu/gfx/portraits/accessories/08_be_bronze_egypt_clothes.txt` : six accessoires liés aux entités.
4. `in_game/gfx/models/portraits/attachments/**/be_egypt_linen.asset` : entités et maillages réutilisés.
5. `main_menu/gfx/portraits/accessory_variations/08_be_bronze_egypt_clothes.txt` et ses trois palettes DDS : matière et couleurs.

## Contrôle en jeu

Lancer une nouvelle partie avec Bronze Era, puis inspecter les portraits d'un dirigeant d'EGY, d'un autre personnage égyptien de haut rang et d'un personnage issu des paysans ou des tribus égyptiennes. Vérifier que les trois tenues se distinguent, que les corps ne traversent pas le vêtement et que les cultures nubienne et medjay conservent leur tenue antérieure. Examiner `error.log` pour les identifiants `be_egypt_` et `be_bronze_egypt_clothes`.

Cette vérification visuelle en jeu n'a pas été exécutée ici.

## Référence historique

Le choix du lin clair et de vêtements drapés s'inspire de la documentation du [Metropolitan Museum of Art sur la vie quotidienne dans l'Égypte ancienne](https://resources.metmuseum.org/resources/metpublications/pdf/The_Daily_Life_of_the_Ancient_Egyptians_The_Metropolitan_Museum_of_Art_Bulletin_v_31_no_3_Spring_1973.pdf). Les couleurs de rang sont un choix de lisibilité pour le jeu ; elles ne constituent pas une reconstitution uniforme de toutes les périodes de Bronze Era.
