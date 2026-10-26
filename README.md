# Revenue app

Socle d’un monolithe Django pour une future application de comparaison de revenus selon le statut d’entreprise. Les simulations SASU, EI et EURL seront planifiées ensuite ; aucun calcul fiscal n’est implémenté.

## Développer

Prérequis : Python 3.13, [uv](https://docs.astral.sh/uv/), [just](https://just.systems/) et PostgreSQL 17 local pour les tests d’intégration. Les versions Python et des dépendances sont déclarées dans `.python-version`, `pyproject.toml` et `uv.lock`.

Pour installer la version de just utilisée par la CI : `uv tool install rust-just==1.59.0`. Le répertoire des exécutables uv doit être dans le `PATH`.

Depuis la racine du dépôt :

```sh
just setup
# Première installation uniquement : créer .env sans afficher les secrets.
uv run --locked python - <<'PYTHON'
from pathlib import Path
from secrets import token_urlsafe

path = Path(".env")
if path.exists():
    raise SystemExit(".env existe déjà : conserver et adapter ses valeurs.")
content = Path(".env.example").read_text()
content = content.replace("SECRET_KEY=", f"SECRET_KEY={token_urlsafe(64)}", 1)
content = content.replace("DB_PASSWORD=", f"DB_PASSWORD={token_urlsafe(32)}", 1)
path.write_text(content)
path.chmod(0o600)
PYTHON
just db-up
just check
just run
```

Conserver un `.env` déjà présent ; adapter ses valeurs à la base locale avant les tests. Ne jamais versionner ce fichier ni y reprendre des credentials de production. `compose.yaml` fournit PostgreSQL 17 pour le développement et la base de test ; Docker et son moteur sont requis pour `just db-up`. Un PostgreSQL local déjà disponible convient aussi, avec un rôle autorisé à créer la base de test ou une base isolée préparée explicitement.

| Variable | Usage |
| --- | --- |
| `DEBUG` | Développement local uniquement ; désactivé hors développement |
| `SECRET_KEY` | Clé Django obligatoire dans tous les environnements, au moins 50 caractères |
| `ALLOWED_HOSTS` | Liste JSON des hôtes autorisés |
| `DB_HOST`, `DB_PORT` | Serveur PostgreSQL local |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD` | Base et compte dédiés au développement |

Les noms et exemples non secrets sont dans `.env.example`. La configuration de tests vit dans `tests/settings.py` ; aucun service distant n’est nécessaire.

## Commandes

| Commande | Effet |
| --- | --- |
| `just setup` | Installe l’environnement depuis le lockfile |
| `just db-up` | Démarre PostgreSQL local via Compose |
| `just db-down` | Arrête PostgreSQL local sans supprimer son volume |
| `just check` | Exécute les contrôles du socle |
| `just test` | Exécute les tests, dont PostgreSQL isolé |
| `just smoke` | Vérifie les parcours techniques de démarrage |
| `just run` | Démarre le serveur de développement Django |

La page `/` affiche le socle ; `/health/` est une sonde de vie du processus, sans contrôle de PostgreSQL. Ces routes ne représentent aucune fonctionnalité de simulation.

## Références

- [Architecture](ARCHITECTURE.md) : responsabilités, données et frontières.
- [Développement](docs/development.md) : tâches, revues, refactoring et entretien.
- [Instructions des agents](AGENTS.md) : règles et commandes opérationnelles.
- [Tâches](tasks/README.md) : source de vérité du travail à mener.

La CI est déclarée dans `.github/workflows/ci.yml`. Un fichier de workflow ne prouve pas un run réussi : consulter les résultats GitHub Actions. Vercel et Supabase restent des cibles futures, sans déploiement ni connexion distante validés par ce socle. [La recherche consolidée](docs/research.md) conserve les justifications et limites des choix initiaux.
