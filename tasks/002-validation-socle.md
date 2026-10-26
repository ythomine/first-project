# 002 — Clôturer la validation du socle

État : ready

## Besoin et périmètre

Compléter les preuves manquantes avant de présenter le socle local/CI comme validé. Les fichiers et vérifications locales sont livrés dans [001](001-socle.md) ; ne pas refaire le setup ou multiplier les plans sans nouvelle raison.

Exclusions : calculs fiscaux, création de modules métier, provisionnement Vercel/Supabase, migrations distantes et fusion automatique de la branche.

## Prérequis et décisions

- Dernière observation : lecture de GitHub Actions refusée par l’API ; ne pas supposer que le blocage persiste ni qu’un token supplémentaire est nécessaire.
- Instructions cloud et ajout de `api.github.com` sauvegardés en brouillon. Leur enregistrement ne prouve ni application réseau ni publication. La revue/enregistrement et publication passent par les paramètres de l’environnement.
- Reprendre les accès existants, sans afficher leurs valeurs. Vérifier chaque accès avec un délai court ; en cas de blocage, préciser politique réseau, authentification ou refus distant avant de demander une action.

## Critères d’acceptation et vérifications

- [ ] Relire le dernier run GitHub Actions de la branche et relever son URL, SHA et conclusion ; confirmer qu’il correspond au code actuel.
- [ ] Si échec : diagnostiquer les logs, corriger dans le périmètre ou soumettre tout conflit de décision à l’utilisateur ; refaire les contrôles affectés et la revue fraîche si nécessaire.
- [ ] Après revue/enregistrement des réglages cloud, vérifier les opérations affectées. Ne déclarer la publication réalisée qu’après confirmation du produit.
- [ ] Vérifier la reprise dans une nouvelle tâche : instructions trouvées, outils disponibles, PostgreSQL redémarré si nécessaire, `just check` exécuté. La réussite de la session initiale ne prouve pas la restauration.
- [ ] Faire un point de nettoyage borné des références et instructions ; consigner uniquement les nouvelles preuves dans cette tâche.
- [ ] Soumettre à l’utilisateur le bilan local/CI/reprise et les limites, puis recueillir sa validation du socle avant de commencer l’implémentation métier.

La CI est bloquante pour une revendication de chaîne locale/CI validée. La reprise cloud est une preuve distincte : si elle reste en attente, le bilan doit le dire et l’utilisateur peut décider de poursuivre le cadrage produit. Aucun succès ne doit être déduit du seul push.

## Revue et clôture

Résultats : non exécutés dans cette mise à jour du plan. Aucun run CI ni nouvelle restauration déclaré réussi.

Prochaine action : vérifier l’accès aux runs et l’état du dernier run de la branche. Le cadrage produit peut avancer indépendamment si cet accès reste bloqué ; le planning métier sera soumis à validation séparément.
