# 003 — Installer les skills retenus et Context7

État : blocked

## Périmètre et décisions

Installer les huit skills de la sélection validée, leurs deux dépendances (`grilling`, `test-driven-development`) et le skill officiel Context7. Préserver les procédures locales. Configurer le MCP Context7, sans secret ni installation globale aveugle. Pour le métier, utiliser les sources officielles Mon-entreprise/Publicodes ; pas d’implémentation fiscale ni de skill communautaire non vérifié.

## Résultats et blocages

- Onze répertoires tiers copiés sous `.agents/skills/`, avec ressources, licences, révisions et empreintes dans `lock.json` ; `review` et `refactor` locaux préservés.
- MCP Context7 configuré dans `.codex/config.toml`. Premier test refusé par le proxy (CONNECT 403, HTTP 000), puis HTTP 200 au test suivant après sauvegarde du domaine nécessaire.
- Domaine `mcp.context7.com` ajouté au brouillon réseau en préservant les domaines existants. Connectivité effective ensuite prouvée par les opérations ci-dessous ; aucun état de publication n’en est déduit. La revue/enregistrement et publication via les paramètres restent distinctes.
- `CONTEXT7_API_KEY` absente du processus et des liaisons cloud inspectés. Aucune clé Context7 nécessaire au test MCP réussi ; aucune nouvelle clé déclarée.
- Le client `codex mcp list` ne liste que la configuration globale dans cette version. Le serveur applicatif local échoue sur des fichiers globaux en lecture seule ; il signale aussi que la configuration projet est désactivée tant que le dépôt n’est pas déclaré de confiance dans le client hôte. Aucun fichier global ni réglage de confiance n’a été modifié. Le chargement effectif du MCP et des outils dans ce chat n’est pas prouvé par la copie de fichiers.
- Aucun skill officiel ou fortement étoilé pour Mon-entreprise/Publicodes identifié et vérifié. Les sources et limites sont dans `docs/research.md` ; un éventuel skill local serait nouveau et demanderait un périmètre explicite, sans prétendre à une adoption préexistante.

## Vérifications et prochaine action

Empreintes des onze sources copiées conformes ; frontmatters des treize skills (dont les deux locaux) et configuration TOML vérifiés. `just check` passe : Ruff, mypy, Import Linter, checks Django et **13 tests**, dont PostgreSQL réel. Aucun nouveau calcul métier exécuté.

Test MCP direct par JSON-RPC, requêtes bornées à cinq secondes : initialisation `Context7` réussie, `tools/list` retourne `resolve-library-id` et `query-docs`, résolution de Django puis récupération d’un extrait de documentation (6 801 caractères). Aucun code privé, situation financière ni secret envoyé. Ce test démontre le service distant sans prétendre à sa présence dans le catalogue d’outils du chat.

Une revue indépendante en contexte frais a confirmé les sources, licences et empreintes, les règles locales, le TOML et les contrôles du projet. Une seconde revue documentaire fraîche a vérifié les observations actualisées du test MCP ; sa remarque sur le statut historique de l’authentification est corrigée.

Action externe restante : activer la configuration projet dans un client/session Codex compatible et de confiance, puis vérifier la présence des outils Context7 dans son catalogue. Les fichiers globaux du client hôte sont en lecture seule ici ; leur politique n’a pas été contournée. En cas de demande d’authentification réelle, configurer OAuth ou une valeur personnelle dans les paramètres sécurisés, jamais dans le chat ou Git. Le service a été testé avec succès, son activation dans le chat reste non vérifiée.
