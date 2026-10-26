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
