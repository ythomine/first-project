# Tâches

Un fichier Markdown par changement cohérent, créé depuis [le modèle](templates/task.md). Nommer les fichiers avec un identifiant stable et un intitulé court. Le backlog produit n’est pas encore défini : ne pas générer de tâches métier par anticipation.

États : `ready`, `in_progress`, `blocked`, `review`, `done`. Une tâche bloquée décrit le motif et l’action nécessaire. Une tâche terminée conserve son résultat et ses preuves ; ne pas dupliquer son état dans un plan ou GitHub Issues.

Les PR et runs CI sont liés depuis la tâche quand ils existent. Le [workflow](../docs/development.md) définit revue, arbitrage et clôture. Aucun état de test ou d’accès distant ne doit être déduit de la seule présence d’un fichier.
