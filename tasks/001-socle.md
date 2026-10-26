# 001 — Socle Django et références de développement

État : done

## Besoin et périmètre

Créer les fichiers du monolithe Django, les références et le workflow agentique validés, puis pousser une branche Git. Aucun calcul métier, module fiscal, déploiement Vercel ou accès Supabase distant.

## Décisions et critères

- YAGNI/KISS, documentation limitée et maintenue, nettoyage borné, conflits soumis à l’arbitrage utilisateur.
- Package installé sous `src/`, configuration Pydantic, frontend Django technique et PostgreSQL isolé.
- Commandes locales/CI communes, modèles de tâche et PR, skills locaux de revue/refactoring.
- Revue indépendante en contexte frais avant push ; pas de fusion implicite.

## Vérifications réalisées

- `just check` : Ruff lint/format, mypy strict sur le code applicatif, contrat Import Linter et checks Django passent ; **13 tests passent**.
- PostgreSQL 17 local : commit et rollback réels vérifiés sur la base de test.
- Fixtures du vrai Import Linter : façade acceptée, import privé et cycle refusés.
- `uv build` : sdist et wheel construits. Installation non éditable, template et CSS embarqués vérifiés.
- `collectstatic`, `makemigrations --check --dry-run` : passent.
- Démarrage HTTP réel : page, sonde de vie et CSS répondent 200 ; processus arrêté après validation.
- `.env`, environnement et sorties générées ignorés ; aucune valeur secrète versionnée.

## Nettoyage et limites

L’ancien squelette Poetry, son test de version et son README vide sont remplacés. Les recherches et le plan initiaux sont consolidés dans `docs/research.md` ; originaux préservés dans l’archive locale de la session, hors checkout. Aucune référence active ne doit dépendre de cette archive.

L’API GitHub reçoit un refus depuis cet environnement : le workflow sera poussé, mais un run CI ne sera déclaré vérifié que si son résultat est effectivement accessible. Aucun déploiement ou connexion SQL distante validé.

## Revue et prochaine action

Diff de référence : commit initial `3566975be7ddfabadbf8ce2ffa0db4238fc3ee25` vers les fichiers de cette tâche. Deux revues indépendantes en contexte frais ont examiné le diff final : aucun défaut actionnable. Le reviewer code a aussi exécuté `just check` hors ligne : 13 tests et tous les contrôles passent. Le wheel final a été reconstruit et comparé aux sources après la dernière correction. Push autorisé sur `setup/django-foundation`, sans fusion ; le résultat du push sera fourni dans le compte rendu de livraison. CI distante non vérifiée à cette clôture locale. Après le socle, reprendre le planning produit avec l’utilisateur ; aucun backlog métier anticipé.
