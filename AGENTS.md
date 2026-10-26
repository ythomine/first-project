# Instructions de travail

Lire [README.md](README.md), [ARCHITECTURE.md](ARCHITECTURE.md) et la tâche concernée. Le [workflow](docs/development.md) détaille les procédures ; ne pas les recopier dans un nouveau plan.

## Principes obligatoires

- **YAGNI** : ne créer que ce qu’un besoin présent justifie. Pas de module métier, couche, dépendance ou compatibilité spéculative.
- **KISS** : préférer la solution cohérente la plus simple ; une fonction peut rester une fonction.
- Rechercher les implémentations existantes avant d’ajouter un comportement. Chaque règle et donnée possède un propriétaire.
- Respecter les interfaces publiques, l’ownership des données et les conventions Django décrits dans l’architecture.
- Un refactoring inclut migration des consommateurs et suppression de l’ancien chemin. Toute compatibilité restante nomme son consommateur et sa condition de suppression.
- Ne pas affaiblir un test, contrat, exclusion ou contrôle pour masquer un échec. Toute évolution de règle doit être visible et justifiée.

## Documentation, nettoyage et conflits

- Une seule source de vérité par sujet : commandes dans le README, architecture dans sa carte, processus dans le workflow, travail dans les tâches.
- Mettre à jour la documentation dans le même changement que le comportement concerné. Éviter les nouveaux documents ou plans sans usage identifié ; compléter le document existant.
- Nettoyer les imports, anciens chemins, dépendances et références rendus obsolètes par chaque changement. À la fin d’une étape, effectuer un point de nettoyage borné ; pas de refonte opportuniste.
- **Conflit de décisions, d’instructions, de responsabilités, de documentation ou de modifications concurrentes : exposer les faits, options et conséquences à l’utilisateur et le laisser trancher.** Suspendre la partie dépendante ; continuer les travaux indépendants autorisés. Ne pas modifier silencieusement la référence pour résoudre le conflit. Une erreur technique ordinaire reste à diagnostiquer et corriger dans le périmètre convenu.

## Vérification et agents

- Commandes de référence : `just setup`, `just check`, `just test`, `just smoke`, `just run` ; détails dans le README et recettes dans `justfile`.
- Exécuter les vérifications pertinentes ; distinguer succès, échec et non-exécution. Un test non collecté ou une déclaration de workflow ne prouve rien.
- Les explorations peuvent être déléguées ; un responsable garde l’intégration. Ne paralléliser les écritures que sur des périmètres et interfaces indépendants.
- **Toute revue utilise un reviewer distinct en contexte frais**, sans historique ni raisonnement de l’auteur. Ici, lancer un nouveau sous-agent avec `fork_turns="none"`. Fournir besoin, critères, règles et diff exact ; revue en lecture seule. Après correction substantielle, faire revoir le diff final dans un nouveau contexte.
- Préserver le travail utilisateur. En tâche cloud déjà isolée, utiliser le checkout existant ; ne pas créer de worktree sans demande explicite.
- Skills tiers : provenance et empreintes dans `.agents/skills/lock.json`, usage dans `docs/development.md`. Leurs permissions ne dépassent jamais celles de la tâche. Respecter nos revues fraîches et le backlog Markdown ; remonter tout conflit non résolu avant application d’une convention tierce. Ne pas installer tout un framework ni créer de documents supplémentaires automatiquement.

## Autorisations et compte rendu

- Aucune valeur de secret dans le code, les documents, prompts ou logs. Conserver TLS et les routes réseau supportées.
- Ne pas provisionner, migrer une base existante, déployer en production ou fusionner sans autorisation correspondante. Une revue d’agent ne remplace pas une validation humaine.
- Un push explicitement demandé est autorisé dans son périmètre ; il ne vaut ni fusion ni déploiement. Ne pas forcer un push ou réécrire l’historique partagé.
- Terminer par le résultat, les vérifications, les limites et les ajouts/remplacements/suppressions utiles à la revue.
