# Développement

Le backlog Markdown dans [tasks](../tasks/README.md) est la source de vérité du travail. Le [README](../README.md) porte les commandes ; [ARCHITECTURE.md](../ARCHITECTURE.md) porte les frontières. Ce document porte le processus, sans second plan concurrent.

## Une tâche jusqu’à sa clôture

1. Borner le besoin, les exclusions, prérequis et critères d’acceptation dans la tâche. Rechercher les usages et comportements proches avant de proposer une nouvelle abstraction.
2. Identifier le propriétaire du changement. Un responsable garde l’intégration. Déléguer une exploration avec une question, un périmètre et une preuve attendue ; séparer les écritures concurrentes.
3. Implémenter par changement cohérent. Tester les comportements et frontières utiles ; les vérifications locales ciblées accélèrent l’itération, la CI exécute les contrôles obligatoires.
4. Mettre à jour la documentation affectée et supprimer les éléments rendus obsolètes. Exécuter les commandes pertinentes et conserver leur code de sortie.
5. Faire revoir le diff exact en contexte frais selon la procédure ci-dessous. Corriger, revérifier et tracer la résolution des constats.
6. Soumettre le résultat à validation humaine pour les décisions et actions concernées. Un push autorisé publie une branche, sans fusion ou déploiement implicite.
7. Clore la tâche avec résultat, preuves, limites et prochaine action. Un run CI non exécuté reste non vérifié, même si tous les contrôles locaux passent.

## Revue en contexte frais

Le reviewer est distinct de l’auteur et démarre **sans historique de conversation de l’implémenteur**. Avec les outils actuels, utiliser un nouveau sous-agent avec `fork_turns="none"` ; changer de rôle dans la même session ne suffit pas. Si ce mécanisme est indisponible, signaler que la revue reste incomplète.

Le paquet de revue contient : besoin et critères, instructions du dépôt, base et tête exactes du diff, changements non commités concernés et preuves vérifiables. Pour un document nouveau, fournir le contenu complet et son périmètre. Ne pas transmettre le raisonnement justificatif de l’auteur.

Le reviewer travaille en lecture seule et examine deux axes : conformité au besoin et qualité/architecture. Il cherche notamment duplications de règles, abstractions sans usage, anciens chemins actifs, fuites ORM, tests insuffisants et contrôles affaiblis. Chaque constat indique fichier/ligne, scénario, impact et gravité ; une préférence de conception n’est pas un défaut démontré. Aucun quota de constats.

L’intégrateur traite les constats, motive un désaccord et relance les contrôles affectés. Après correction substantielle, **un nouveau reviewer en contexte frais** vérifie le diff final. La revue d’agent ne fournit aucune permission externe ni approbation humaine.

## Refactoring terminé

1. Nommer le chemin ou l’implémentation canonique et le comportement à préserver.
2. Inventorier les consommateurs : HTTP, commandes, tâches, tests, registres, settings et scripts.
3. Migrer les parcours réels, puis supprimer l’ancien code, configuration, tests et dépendances devenus inutiles.
4. Chercher les références résiduelles ; compléter la recherche textuelle par inspection des chargements dynamiques Django et tests concernés.
5. Vérifier les comportements et transactions affectés ; rendre compte des ajouts, remplacements et suppressions.

Toute compatibilité conservée nomme un consommateur réel, le contrat garanti, la condition de suppression et un responsable. Un rapport de code mort ou de clones est un indice de revue, pas une preuve suffisante pour supprimer ou fusionner des comportements.

## Documentation et entretien

YAGNI/KISS s’appliquent aussi aux documents. Modifier la référence existante avant d’ajouter un fichier. Les tâches portent les actions et états ; la documentation décrit le fonctionnement actuel ; les ADR futurs décriront seulement les décisions durables ou exceptions importantes. Ne pas maintenir des copies des mêmes règles dans les skills.

Chaque changement nettoie ce qu’il rend obsolète. À la fin d’une étape, faire un point borné sur chemins inutilisés, dépendances, imports, liens et instructions périmées. Un entretien plus large devient une tâche avec problème identifié, périmètre et critère de fin ; aucune boucle de nettoyage illimitée.

Toute modification de contrats, exclusions, baselines, assertions ou contrôles obligatoires est explicitée dans le diff et justifiée en revue. Les protections de branche effectives dépendent des règles GitHub configurées ; `AGENTS.md` et `CODEOWNERS` seuls ne les garantissent pas.

## Arbitrage

Lorsqu’une demande, une instruction, une décision d’architecture ou deux modifications se contredisent : relever les références et le conflit, présenter les options et conséquences, puis demander à l’utilisateur de trancher. Marquer la tâche `blocked` pour la partie dépendante et continuer ce qui reste indépendant. Après réponse, mettre à jour la référence canonique et la tâche, sans multiplier les comptes rendus.

Une panne d’outil, erreur de test ou incompatibilité technique routinière ne crée pas automatiquement un conflit de décision : diagnostiquer et corriger dans le périmètre autorisé. Si la correction exige un choix qui change ce périmètre, revenir à l’arbitrage.

## Skills et documentation technique

Les skills tiers sont installés sous `.agents/skills/`, à des révisions épinglées avec licences et empreintes dans [lock.json](../.agents/skills/lock.json). Leurs fichiers sont conservés sans réécriture ; une mise à jour doit être explicite et reviewable. Les scripts Python vendus avec `skill-creator` sont seuls exclus du formatage/lint du projet pour préserver leurs sources ; cette exclusion ne concerne pas notre code.

| Usage | Skills installés |
| --- | --- |
| Clarification | `grill-me`, avec sa dépendance `grilling` |
| Modèle métier | `domain-modeling` |
| Revue | `code-review`, en complément de notre point d’entrée local `review` |
| Diagnostic et preuves | `systematic-debugging`, sa dépendance `test-driven-development`, `verification-before-completion` |
| Interface | `frontend-design`, `web-design-guidelines` |
| Procédures réutilisables | `skill-creator` ; notre skill local `refactor` est conservé |
| Documentation de bibliothèques | `context7-mcp` |

Le tracker du projet est `tasks/`, pas un service à créer pour satisfaire une convention tierce. Les références `superpowers:<nom>` renvoient ici au skill installé du même nom, sans plugin Superpowers global. Une référence à un outil absent (`Skill`, `WebFetch`, etc.) demande d’utiliser l’équivalent disponible ou de signaler l’indisponibilité, sans prétendre l’avoir exécuté. Les revues, y compris UI, restent en contexte frais. Avant tout glossaire, ADR ou fichier supplémentaire demandé par un skill, vérifier son besoin et l’emplacement canonique existant ; en cas de conflit, appliquer la procédure d’arbitrage.

Context7 est configuré comme MCP hébergé dans [`.codex/config.toml`](../.codex/config.toml), avec le skill officiel correspondant. Il n’ajoute pas de dépendance Node au runtime Django. Les clients qui prennent en charge la configuration projet doivent faire confiance au dépôt ; une nouvelle session peut être nécessaire. Le client hôte actuel a signalé que la configuration projet n’était pas activée et que ses fichiers d’état globaux étaient en lecture seule. Un fichier de configuration ne prouve ni le chargement des outils dans ce chat ni une connexion réussie ; la confiance doit être accordée via le mécanisme du client, sans contourner ses restrictions.

Après un premier CONNECT 403, l’ajout de `mcp.context7.com` a été sauvegardé dans le brouillon réseau en préservant les domaines existants. Le test suivant a obtenu HTTP 200 et une initialisation MCP réussie : les outils `resolve-library-id` et `query-docs` ont été listés puis utilisés pour récupérer de la documentation Django. Ce test direct ne prouve pas leur chargement dans le chat courant. Aucune clé Context7 n’était nécessaire à cet essai ; OAuth ou une clé restent possibles pour les quotas authentifiés, dans les paramètres sécurisés seulement. Aucun flux de connexion interactif n’a été lancé. La publication du brouillon cloud reste distincte et doit passer par les paramètres du produit lorsque requise.

Context7 sert à la documentation technique des bibliothèques. Ne lui envoyer ni secret, code privé non nécessaire, ni situation financière personnelle ; il ne remplace pas les règles et sources métier de l’Urssaf.
