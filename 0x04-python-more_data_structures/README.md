# Notes de cours Python - Préparation aux interviews techniques

## 1. Pourquoi Python est un langage de programmation excellent

### Explications
- **Lisibilité** : Syntaxe claire et intuitive qui privilégie l'indentation
- **Polyvalence** : Applications en développement web, data science, IA, automatisation, etc.
- **Écosystème riche** : Vaste bibliothèque standard et nombreux packages tiers (pip)
- **Interprété** : Pas besoin de compilation, développement rapide
- **Multi-paradigmes** : Programmation orientée objet, fonctionnelle et procédurale

### Exemples concrets
```python
# Exemple de lisibilité
def est_pair(nombre):
    if nombre % 2 == 0:
        return True
    return False

# Exemple d'utilisation de bibliothèques
import requests
response = requests.get('https://api.github.com')
data = response.json()
```

### Questions d'interview courantes
- Quels sont les avantages de Python par rapport à Java/C++?
- Comment Python gère-t-il la mémoire?
- Qu'est-ce que le GIL en Python et quelles sont ses implications?
- Citez quelques domaines d'application où Python excelle.

## 2. Les ensembles (sets) et leur utilisation

### Explications
- Collection non ordonnée d'éléments **uniques**
- Mutable, mais contient uniquement des objets hashables (immuables)
- Implémentation basée sur les tables de hachage (opérations O(1) en moyenne)
- Optimisé pour tester l'appartenance, éliminer les doublons, opérations mathématiques

### Exemples concrets
```python
# Création de sets
nombres = {1, 2, 3, 4, 5}
fruits = set(['pomme', 'orange', 'banane'])

# Élimination des doublons
liste_avec_doublons = [1, 2, 2, 3, 4, 4, 5]
liste_sans_doublons = list(set(liste_avec_doublons))  # [1, 2, 3, 4, 5]

# Opérations ensemblistes
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
union = set_a | set_b                # {1, 2, 3, 4, 5, 6}
intersection = set_a & set_b         # {3, 4}
difference = set_a - set_b           # {1, 2}
diff_symetrique = set_a ^ set_b      # {1, 2, 5, 6}
```

### Questions d'interview courantes
- Comment vérifier si un set est un sous-ensemble d'un autre?
- Quelle est la complexité temporelle pour vérifier si un élément est dans un set?
- Pourquoi ne peut-on pas stocker des listes ou des dictionnaires dans un set?

## 3. Méthodes courantes des sets

### Explications
- **add()** : Ajoute un élément
- **remove()** : Supprime un élément (erreur si absent)
- **discard()** : Supprime un élément (sans erreur si absent)
- **pop()** : Retire et renvoie un élément aléatoire
- **clear()** : Vide l'ensemble
- **update()** : Ajoute plusieurs éléments

### Exemples concrets
```python
s = {1, 2, 3}

# Manipulation d'éléments
s.add(4)                   # s devient {1, 2, 3, 4}
s.remove(2)                # s devient {1, 3, 4}
s.discard(10)              # Aucune erreur même si 10 n'existe pas
element = s.pop()          # Retire un élément aléatoire
s.clear()                  # s devient set()

# Opérations ensemblistes avec méthodes
a = {1, 2, 3}
b = {3, 4, 5}
a.update(b)                # a devient {1, 2, 3, 4, 5}
a.intersection_update(b)   # a devient {3, 4, 5}
```

### Questions d'interview courantes
- Quelle est la différence entre remove() et discard()?
- Comment fusionner efficacement plusieurs sets?
- Expliquez la différence entre update() et union().

## 4. Sets vs Lists : quand utiliser chacun

### Explications
| Sets | Lists |
|------|-------|
| Éléments uniques | Doublons autorisés |
| Non ordonnés | Ordonnés |
| Recherche rapide O(1) | Recherche linéaire O(n) |
| Pas d'indexation | Accès par index |
| Éléments hashables uniquement | Tout type d'élément |

### Exemples concrets
```python
# Quand utiliser des sets
emails_uniques = set(emails_collectes)  # Dédupliquer
if user_id in users_authorized:         # Test d'appartenance rapide
tags = {'python', 'dev', 'web'}         # Quand l'ordre n'importe pas

# Quand utiliser des listes
resultats_tries = [95, 87, 78, 65]      # Ordre important
historique_actions = []                 # Ajouts séquentiels
historique_actions.append('action1')    # Maintien de l'ordre
```

### Questions d'interview courantes
- Dans quel scénario choisiriez-vous un set plutôt qu'une liste?
- Comment implémenteriez-vous une liste avec des éléments uniques tout en préservant l'ordre?
- Quelle est la différence de performance pour chercher un élément dans un set vs une liste?

## 5. Itération dans un set

### Explications
- L'ordre d'itération n'est pas garanti
- Syntaxe similaire aux autres itérables
- Possibilité d'utiliser la compréhension d'ensemble

### Exemples concrets
```python
couleurs = {'rouge', 'vert', 'bleu'}

# Itération simple
for couleur in couleurs:
    print(couleur)

# Compréhension d'ensemble
couleurs_majuscules = {couleur.upper() for couleur in couleurs}  # {'ROUGE', 'VERT', 'BLEU'}

# Avec enumerate si besoin d'un index
for i, couleur in enumerate(couleurs):
    print(f"Couleur {i}: {couleur}")
```

### Questions d'interview courantes
- Comment itérer sur deux sets simultanément?
- Peut-on garantir un ordre d'itération spécifique dans un set?
- Comment créer un set à partir d'un autre set en appliquant une transformation?

## 6. Dictionnaires et leur utilisation

### Explications
- Collection de paires clé-valeur
- Clés uniques et hashables (immuables)
- Accès, insertion et suppression rapides (O(1) en moyenne)
- Maintiennent l'ordre d'insertion (depuis Python 3.7)

### Exemples concrets
```python
# Création de dictionnaires
utilisateur = {
    'id': 42,
    'nom': 'Dupont',
    'email': 'dupont@example.com'
}

# Accès aux valeurs
print(utilisateur['nom'])              # Dupont
print(utilisateur.get('age', 'N/A'))   # N/A (valeur par défaut)

# Modification
utilisateur['age'] = 30
utilisateur.update({'role': 'admin', 'age': 31})

# Suppression
del utilisateur['email']
age = utilisateur.pop('age')           # Retire et renvoie la valeur
```

### Questions d'interview courantes
- Comment gérer l'accès à une clé qui pourrait ne pas exister?
- Quelles sont les restrictions sur les types de clés?
- Comment fusionner deux dictionnaires en Python 3.9+?

## 7. Dictionnaires vs Lists vs Sets

### Explications
| Structure | Cas d'utilisation |
|-----------|-------------------|
| Dictionary | Mappage clé-valeur, recherche par clé, attributs d'objets |
| List | Séquence ordonnée, accès par index, maintien de l'ordre d'insertion |
| Set | Éléments uniques, tests d'appartenance, opérations ensemblistes |

### Exemples concrets
```python
# Dictionary - Association clé-valeur
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
print(scores['Alice'])  # 95

# List - Collection ordonnée
top_players = ['Alice', 'Charlie', 'Bob']
print(top_players[0])  # Alice

# Set - Éléments uniques sans ordre
qualified_players = {'Alice', 'Bob', 'Charlie', 'Bob'}  # {'Alice', 'Bob', 'Charlie'}
```

### Questions d'interview courantes
- Quand privilégier un dictionnaire plutôt qu'une liste d'objets?
- Comment choisir entre un dict.keys() et un set?
- Quelle structure utiliser pour compter les occurrences d'éléments?

## 8. Clés dans un dictionnaire

### Explications
- Doivent être **hashables** (immuables) : strings, numbers, tuples (d'objets hashables)
- Doivent être uniques (les doublons écrasent les valeurs)
- Utilisent la fonction hash() et la méthode __eq__() pour comparaison
- Les objets personnalisés peuvent être des clés s'ils implémentent __hash__() et __eq__()

### Exemples concrets
```python
# Types valides pour les clés
dict_valide = {
    'string': 1,
    42: 'nombre',
    (1, 2): 'tuple',
    True: 'booléen'
}

# Types invalides pour les clés
# dict_invalide = {[1, 2]: 'liste'}  # TypeError: list is not hashable
# dict_invalide = {{1: 'a'}: 'dict'}  # TypeError: dict is not hashable

# Classe personnalisée hashable
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, autre):
        return self.x == autre.x and self.y == autre.y

points = {Point(0, 0): 'origine'}
```

### Questions d'interview courantes
- Pourquoi les listes ne peuvent-elles pas être des clés de dictionnaire?
- Comment utiliser un tuple comme clé de dictionnaire?
- Comment rendre une classe compatible pour être utilisée comme clé?

## 9. Itération sur un dictionnaire

### Explications
- Par défaut, itération sur les clés
- Méthodes `.items()`, `.keys()` et `.values()` pour itération spécifique
- Maintient l'ordre d'insertion (depuis Python 3.7)

### Exemples concrets
```python
produit = {
    'nom': 'Laptop',
    'prix': 999,
    'stock': 10
}

# Itération sur les clés (comportement par défaut)
for cle in produit:
    print(cle)  # nom, prix, stock

# Itération sur les paires clé-valeur
for cle, valeur in produit.items():
    print(f"{cle}: {valeur}")

# Itération sur les valeurs uniquement
for valeur in produit.values():
    print(valeur)

# Compréhension de dictionnaire
prix_euros = {nom: prix * 0.92 for nom, prix in produit.items() if isinstance(prix, (int, float))}
```

### Questions d'interview courantes
- Comment itérer simultanément sur les clés et les valeurs?
- Quelle est la méthode la plus efficace pour vérifier si une clé existe?
- Comment filtrer un dictionnaire pendant l'itération?

## 10. Fonctions lambda

### Explications
- Fonctions anonymes créées avec le mot-clé `lambda`
- Syntaxe : `lambda arguments: expression`
- Limitées à une seule expression
- Utilisées pour des fonctions simples et éphémères

### Exemples concrets
```python
# Fonction lambda simple
carre = lambda x: x**2
print(carre(5))  # 25

# Utilisation avec des fonctions de tri
etudiants = [('Alice', 92), ('Bob', 85), ('Charlie', 90)]
etudiants_tries = sorted(etudiants, key=lambda etudiant: etudiant[1], reverse=True)
# [('Alice', 92), ('Charlie', 90), ('Bob', 85)]

# Dans une expression conditionnelle
est_pair = lambda x: True if x % 2 == 0 else False
```

### Questions d'interview courantes
- Quelle est la différence entre une fonction lambda et une fonction régulière?
- Dans quels cas l'utilisation de lambda est-elle appropriée/inappropriée?
- Comment écrire une fonction lambda avec plusieurs conditions?

## 11. Les fonctions map(), reduce() et filter()

### Explications
- **map(fonction, iterable)** : Applique une fonction à chaque élément
- **filter(fonction, iterable)** : Filtre les éléments selon une condition
- **reduce(fonction, iterable)** : Réduit l'itérable à une seule valeur (nécessite `functools`)

### Exemples concrets
```python
# map
nombres = [1, 2, 3, 4, 5]
carres = list(map(lambda x: x**2, nombres))  # [1, 4, 9, 16, 25]

# filter
pairs = list(filter(lambda x: x % 2 == 0, nombres))  # [2, 4]

# reduce
from functools import reduce
somme = reduce(lambda x, y: x + y, nombres)  # 15
produit = reduce(lambda x, y: x * y, nombres)  # 120

# Alternative avec compréhension de liste
carres_alt = [x**2 for x in nombres]  # Équivalent à map
pairs_alt = [x for x in nombres if x % 2 == 0]  # Équivalent à filter
```

### Questions d'interview courantes
- Quelle est la différence entre map et une compréhension de liste?
- Pourquoi reduce a-t-il été déplacé vers le module functools?
- Dans quel cas utiliseriez-vous filter() plutôt qu'une compréhension de liste?
- Comment chaîner map, filter et reduce ensemble?