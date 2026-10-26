# Architecture

Un produit, un package Python installé, une application Django déployable et une base PostgreSQL. Le frontend est rendu par Django. Le découpage métier sera décidé avec le planning produit ; les statuts SASU/EI/EURL ne définissent pas automatiquement trois modules.

## Carte du code

| Emplacement | Responsabilité |
| --- | --- |
| `src/revenue_app/config/` | Lecture typée de la configuration, settings, routes racines et point d’entrée WSGI |
| `src/revenue_app/web/` | App Django technique : page du socle, contrôle de disponibilité et présentation associée |
| `tests/` | Comportements unitaires, intégration PostgreSQL, smoke et contrôles d’architecture |
| `pyproject.toml`, `uv.lock`, `justfile` | Dépendances, outils verrouillés et commandes communes au local et à la CI |

`web` n’est pas un module métier. Aucun module vide n’est créé pour anticiper une future fonctionnalité. Les prochains modules seront placés sous `revenue_app` dans un regroupement utile à la navigation ; leur nom, label Django et responsabilité seront décidés avant leurs premières migrations.

## Frontières

- Chaque comportement et donnée métier possède un module propriétaire.
- Les consommateurs d’un module passent par son interface Python publique, par exemple `api.py`, lorsqu’un contrat intermodule existe. Cette API ne désigne pas des routes HTTP.
- Les modèles, managers et querysets restent internes entre modules. Les views d’un module peuvent utiliser leur propre ORM.
- Les résultats publics utilisent des identifiants et données explicites ; ils n’exposent pas de requêtes ORM paresseuses ou de mutations implicites.
- Les dépendances métier ne forment pas de cycle. La configuration assemble les composants ; les composants n’importent pas les détails du bootstrap Django pour accéder à leurs règles.
- Une FK inter-apps protège éventuellement l’intégrité, sans accorder un droit général d’accès aux tables du voisin. Les lectures transversales et cascades ont une responsabilité explicite.

Les contrats Import Linter vérifient les dépendances Python configurées. Ils ne couvrent pas tous les accès par chaînes Django, SQL, signaux ou imports dynamiques : compléter par revue et tests concernés. Tant qu’aucun module métier n’existe, les preuves techniques du garde-fou ne constituent pas une validation de frontières métier.

## Django et validation

Conserver la découverte Django : les modèles sont définis ou importés dans `models.py` ou `models/__init__.py`, leurs migrations restent dans leur app. Ne pas ajouter `_internal/`, repository, conteneur d’injection ou couche service partout par principe.

| Besoin | Propriétaire |
| --- | --- |
| Cycle HTML et erreurs de saisie | Forms/ModelForms Django |
| Contrat structuré à une frontière utile | Pydantic, si un type Python plus simple ne suffit pas |
| Configuration d’environnement | pydantic-settings dans `config/environment.py`, puis adaptation aux settings Django |
| Persistance et intégrité relationnelle | ORM Django et contraintes PostgreSQL |
| Calculs et invariants métier | Implémentation canonique dans le module concerné |

Ne pas générer systématiquement un schéma Pydantic par modèle ORM ni dupliquer une même règle dans chaque couche. Les montants futurs utilisent `Decimal` ; la définition des revenus, les arrondis, périodes et paramètres réglementaires restent à préciser.

## Transactions et exécution

Le cas d’usage qui promet l’atomicité porte un `transaction.atomic()` explicite et court. Pas de commit caché dans un helper. Les effets externes attendent le commit lorsque nécessaire ; `on_commit` ne garantit pas leur livraison après un crash. Une outbox attend un besoin de livraison durable établi.

Les tests utilisent une base PostgreSQL isolée ; une réussite SQLite ne prouve pas le comportement cible. La configuration et les imports ne doivent pas ouvrir de connexion métier ou exécuter de migration. Les données persistantes ne vivent pas dans le filesystem du déploiement.

## Évolution

### Source des règles de simulation

Le choix utilisateur est de s’appuyer sur [Mon-entreprise de l’Urssaf](https://mon-entreprise.urssaf.fr/), son [code et ses règles ouverts](https://github.com/betagouv/mon-entreprise), notamment `modele-social`, et le moteur [Publicodes](https://github.com/publicodes/publicodes). Ne pas recopier les règles fiscales en Python par défaut.

L’intégration n’est pas encore décidée : appel de l’API REST depuis Django ou exécution du moteur JavaScript avec règles épinglées. Cela demande un choix explicite sur reproductibilité, réseau, déploiement et traçabilité ; aucune dépendance métier n’est installée à ce stade. Garder distincts la version du moteur, la version du modèle, la date d’effet, les hypothèses, unités, avertissements et variables manquantes. Une valeur numérique seule ne prouve pas qu’une simulation est complète ou applicable au cas demandé.

La prochaine conception devra vérifier les cas SASU/EI/EURL et les variantes fiscales sur des scénarios de référence du site officiel, ainsi que leurs sources réglementaires. Aucun skill spécialisé officiel ou largement adopté n’a été identifié et vérifié ; les skills génériques installés ne constituent pas une validation fiscale.

### Règles d’évolution

YAGNI et KISS : ajouter une abstraction, dépendance ou couche pour un problème présent et identifiable. L’intérieur d’un module reste proportionné à sa complexité.

Ce fichier décrit l’architecture actuelle et ses invariants. Une décision durable ou exception coûteuse peut justifier un ADR court, référencé ici ; ne pas créer un second document d’architecture concurrent. Le [workflow de développement](docs/development.md) définit la mise à jour et l’arbitrage des conflits.
