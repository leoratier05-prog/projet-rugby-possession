# Possession et victoire en Top 14 : quel lien réel ?

## Contexte et question de recherche

Ce projet a pour but d'explorer une idée reçue du rugby : est-ce que le fait d'avoir plus de possession de balle qu'un adversaire est réellement lié à la victoire ? Contrairement au football, où la possession est souvent perçue comme un facteur clé de domination, le rugby laisse une place importante au jeu au pied et à la défense, ce qui pourrait rendre ce lien plus faible.

## Données

Les données couvrent 36 lignes correspondant aux 9 premières journées du Top 14, pour 4 équipes suivies (Stade Toulousain, Stade Rochelais, Union Bordeaux-Bègles, US Montauban). Chaque ligne représente un match, avec le pourcentage de possession de l'équipe, son pourcentage d'occupation du terrain, et le résultat (victoire ou défaite).

Les statistiques ont été récupérées manuellement sur les feuilles de match officielles du Top 14 (top14.lnr.fr).

## Méthodologie

Le projet est réalisé en Python, avec les librairies `pandas` pour la manipulation des données et `matplotlib` pour la visualisation. La démarche consiste à charger les données, calculer des statistiques descriptives, mesurer la corrélation entre possession/occupation et victoire, et visualiser ces relations avec des boxplots.

## Résultats

Sur l'ensemble des 36 matchs, la corrélation entre possession et victoire est de **0.19**, ce qui est faible. En revanche, la corrélation entre occupation du terrain et victoire est de **0.46**, une relation modérée, nettement plus marquée.

En regardant l'équipe de Toulouse isolément (9 matchs), la possession moyenne est de **58%**, et la corrélation entre possession et victoire monte à **0.47** pour cette équipe spécifiquement, un lien plus fort que la moyenne générale.

## Interprétation

Ces résultats suggèrent que la possession seule n'est pas un bon indicateur de la victoire en Top 14 : ce qui semble compter davantage, c'est l'occupation du terrain, c'est-à-dire la capacité à jouer dans le camp adverse plutôt qu'à simplement garder le ballon. Cela colle avec la réalité stratégique du rugby, où le jeu au pied pour gagner du terrain est une arme fréquente. Le résultat spécifique à Toulouse suggère aussi que l'importance de la possession peut varier selon le style de jeu propre à chaque équipe.

## Limites

L'échantillon reste petit (36 matchs au total, 9 par équipe), ce qui rend les résultats indicatifs plutôt que généralisables. Une corrélation ne démontre pas non plus de lien de causalité. Les analyses par équipe, en particulier, reposent sur un nombre de matchs trop faible pour être robustes statistiquement.

## Pistes d'amélioration

Élargir le jeu de données à une saison complète et à plus d'équipes, ajouter d'autres variables (plaquages, pénalités, essais marqués) et construire un modèle de régression logistique pour évaluer l'effet de chaque facteur en tenant compte des autres.

## Outils utilisés

Python, pandas, matplotlib
