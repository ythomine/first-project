# Tâches

## Plan de reprise

Ce fichier est l’entrée unique du plan de travail. Les états et preuves détaillés restent dans les tâches liées ; pas de `Plan.md` concurrent à la racine. Les recherches initiales sont conservées dans [la synthèse](../docs/research.md).

| Ordre | Étape | Résultat attendu |
| --- | --- | --- |
| 1 | [Création du socle](001-socle.md) | Fichiers de référence, squelette Django, contrôles locaux et branche poussée ; preuves dans la tâche |
| 2 — prochaine action | [Clôturer la validation du socle](002-validation-socle.md) | Résultat CI réel, reprise de l’environnement vérifiée, limites restantes explicites et validation humaine du socle |
| 3 | Cadrer le produit avec l’utilisateur | Définir utilisateurs, revenu comparé, entrées/sorties, périmètre France et exercices, variantes SASU/EI/EURL, hypothèses et sources réglementaires |
| 4 | Décider une première tranche métier | Découpage initial, scénarios de référence, règles de précision/arrondi et critères d’acceptation d’un premier parcours minimal |
| 5 | Soumettre le planning métier à validation | Tâches petites et ordonnées avec dépendances et stratégie de tests ; aucune implémentation métier avant cet accord |

Les étapes 3–5 décrivent les décisions à préparer, pas un backlog métier déjà approuvé. Le cadrage peut avancer pendant un blocage technique indépendant ; ne pas annoncer la chaîne locale/CI complètement validée avant les preuves attendues à l’étape 2.

Vercel/Supabase réels restent différés : aucune ressource, migration distante ou publication de production implicite. Leur validation sera programmée séparément après choix des cibles et autorisations. La publication de l’environnement cloud de développement est distincte d’un déploiement de l’application.

## Organisation

Un fichier Markdown par changement cohérent, créé depuis [le modèle](templates/task.md). Nommer les fichiers avec un identifiant stable et un intitulé court. Le backlog produit n’est pas encore défini : ne pas générer de tâches métier par anticipation.

États : `ready`, `in_progress`, `blocked`, `review`, `done`. Une tâche bloquée décrit le motif et l’action nécessaire. Une tâche terminée conserve son résultat et ses preuves ; ne pas dupliquer son état dans un plan ou GitHub Issues.

Les PR et runs CI sont liés depuis la tâche quand ils existent. Le [workflow](../docs/development.md) définit revue, arbitrage et clôture. Aucun état de test ou d’accès distant ne doit être déduit de la seule présence d’un fichier.
