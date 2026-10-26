# Recherche initiale — 26 octobre 2026

Cette note conserve les raisons des choix du socle. Le fonctionnement actuel est décrit dans le README et la carte d’architecture ; les vérifications et travaux restants sont suivis dans `tasks/README.md`. Elle ne constitue pas un deuxième plan.

## Choix retenus

| Sujet | Décision et raison |
| --- | --- |
| Disposition | Package installé sous `src/`, tests séparés : éviter les imports accidentels depuis le checkout et vérifier le packaging |
| Django | Apps idiomatiques ; modèles découvrables, migrations par app et frontend Django. Pas de couches uniformes imposées |
| Versions | Série Python 3.13, Django 5.2 LTS, psycopg 3 et PostgreSQL 17 ; versions correctives et outils verrouillés dans les fichiers exécutables |
| Modularité | API Python publique aux frontières utiles ; propriété des données explicite. Aucun découpage SASU/EI/EURL automatique |
| Validation | Forms pour HTML, Pydantic aux frontières utiles, pydantic-settings pour la configuration, ORM et contraintes SQL pour la persistance |
| Frontières | Import Linter plutôt que deux outils : contrats explicites de dépendances, protection et cycles |
| Typage | mypy + django-stubs : plugin Django documenté ; Pyright reste une alternative si un besoin concret le justifie |
| SDLC | Tâches Markdown, ADR ponctuels, PR courtes, intégrateur responsable, toute revue en contexte frais |
| Diagnostics | deptry après calibration ; clones/code mort facultatifs. Pas de dépendances supplémentaires sans usage présent |

## Alternatives et limites

Le projet Django plat reste une alternative simple. Une disposition hexagonale uniforme apporterait ici des couches avant que les besoins métier soient établis. Une façade n’impose ni `_internal/` partout, ni repository générique, ni framework d’injection.

Import Linter et Tach ont été comparés. Tach propose des interfaces symboliques et un graphe déclaré ; Import Linter a été retenu pour exprimer simplement nos contraintes Python. Les options de protection, dépendances indirectes, exhaustivité et imports de typage doivent être vérifiées sur la version utilisée. Les contrôles ne voient pas tout : références de modèles par chaînes, traversées ORM, SQL et chargements dynamiques exigent aussi revue et tests de comportement.

La propriété des transactions reste dans les cas d’usage qui promettent l’atomicité. `atomic` imbriqué utilise normalement des savepoints ; un commit intérieur n’empêche pas un rollback extérieur. `on_commit` retarde un effet mais ne garantit pas sa livraison après un crash. Pas d’outbox ni de Unit of Work supplémentaire sans besoin établi.

Vercel possède un exemple et un builder Django/Python officiels : points d’entrée Django, traitement uv et collecte de statiques sont présents dans la révision examinée. Ce code ne prouve pas son déploiement sur un compte ni les quotas d’une offre. La compatibilité réelle avec notre package reste à tester dans une future phase distante.

La source officielle Supabase distingue connexions directes, session et transaction. Le mode transaction convient à étudier pour le serverless, avec limites sur prepared statements, curseurs et état de session. Les migrations peuvent demander un autre endpoint. SSL chiffré seul n’est pas une vérification d’identité : prévoir une validation TLS complète avec le serveur choisi. Aucun projet distant n’a été sélectionné ou modifié.

## Méthode et provenance

La recherche a utilisé HTTPS via le proxy, vérification TLS conservée et sondes d’environ cinq secondes. Aucun outil Web dédié ou connecteur applicatif n’a été utilisé. Les documents de recherche détaillés et l’ancien plan ont été consolidés ici ; leurs originaux sont conservés dans l’archive locale de cette session, hors du dépôt. Les références primaires ci-dessous restent la provenance portable.

Les SHA rendent les lectures reproductibles ; ils n’établissent pas un consensus universel en octobre 2026, ni la compatibilité de versions jamais exécutées ensemble. La synthèse de praticiens fournie par l’utilisateur a été confrontée aux sources accessibles, pas adoptée comme configuration prête à appliquer. Les publications attribuées à Buczyński, Ronacher, Willison et matklad n’ont pas toutes pu être lues ; aucune conclusion ne repose sur leur vérification supposée.

Le réseau évolue : lors des dernières investigations, la racine `developers.openai.com` répondait 200, mais les anciennes pages Codex redirigeaient vers `learn.chatgpt.com`, refusé par le proxy. Les documentations web Vercel/Supabase étaient également refusées ; leurs dépôts officiels ont servi de sources. Cela ne démontre ni authentification utilisateur ni accès SQL.

## Références consultées

- [PyPA — src vs flat](https://github.com/pypa/packaging.python.org/blob/d1ad4ad3d6d6f3a3582e4c6b8a1b6f8284f4cb3b/source/discussions/src-layout-vs-flat-layout.rst) et [pytest — imports/tests](https://github.com/pytest-dev/pytest/blob/41d12cdbb4a35a7877768d93d8dc50a9117a8d8c/doc/en/explanation/goodpractices.rst).
- [Django — découverte des apps](https://github.com/django/django/blob/cae7247962de54a94023d28d84f05fc9842e9646/docs/ref/applications.txt) et [transactions](https://github.com/django/django/blob/cae7247962de54a94023d28d84f05fc9842e9646/docs/topics/db/transactions.txt).
- [Pydantic — modèles](https://github.com/pydantic/pydantic/blob/8459f597aac7f86bf44338b7a140010f9471368f/docs/concepts/models.md) et [pydantic-settings](https://github.com/pydantic/pydantic-settings/blob/7e2dacb6db07b41abb0c80d0608e46e197265554/docs/index.md).
- [Import Linter — protected](https://github.com/seddonym/import-linter/blob/857ae28bc9cb383ce9c831e7e8345eb9b40667ae/docs/contract_types/protected.md), [layers](https://github.com/seddonym/import-linter/blob/857ae28bc9cb383ce9c831e7e8345eb9b40667ae/docs/contract_types/layers.md) et [acyclic siblings](https://github.com/seddonym/import-linter/blob/857ae28bc9cb383ce9c831e7e8345eb9b40667ae/docs/contract_types/acyclic_siblings.md).
- [Tach — configuration](https://github.com/gauge-sh/tach/blob/bc92d71520a1acdb9aacd1f2362ca49b58259dda/docs/usage/configuration.md) et [django-stubs — plugin et compatibilité](https://github.com/typeddjango/django-stubs/blob/8e4fcf77c8a23301064dcfdd7ec137526dbcfd58/README.md).
- [uv — lock et synchronisation](https://github.com/astral-sh/uv/blob/656d02b614609dd6c982707b6d6c325b6120285b/docs/concepts/projects/sync.md).
- [Vercel — builder Python](https://github.com/vercel/vercel/blob/c628be7835e03a965b93e9cf9e2bd5ac2acbf5eb/packages/python/src/index.ts) et [hook Django](https://github.com/vercel/vercel/blob/c628be7835e03a965b93e9cf9e2bd5ac2acbf5eb/packages/python/src/django.ts).
- [Supabase — modes de connexion PostgreSQL](https://github.com/supabase/supabase/blob/ffe3f35a42611665e27b31ca75695fe6bcb46dea/apps/docs/content/guides/database/connecting-to-postgres.mdx).
- [Codex — instructions](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/core/src/agents_md.rs) et [découverte des skills](https://github.com/openai/codex/blob/970111f6cb62cc02fe36a82ea7d71b37a2889c97/codex-rs/ext/skills/src/host_roots.rs).
- [Matt Pocock — revue](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/code-review/SKILL.md) et [Steinberger — suppression des anciens chemins](https://github.com/steipete/agent-scripts/blob/1159adf26ad007df38b87debb107d3946008d38b/AGENTS.MD).
