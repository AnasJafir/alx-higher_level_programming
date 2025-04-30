Voici les réponses aux questions d'interview sur Python :

### Avantages de Python vs Java/C++
Python offre une syntaxe plus lisible et concise, un développement plus rapide grâce à son typage dynamique, une grande bibliothèque standard, et ne nécessite pas de compilation. Il est multiplateforme avec une courbe d'apprentissage plus douce que Java/C++, qui sont plus verbeux et stricts.

### Gestion de la mémoire en Python
Python utilise un gestionnaire de mémoire automatique avec un garbage collector qui libère la mémoire des objets qui ne sont plus référencés. Il emploie le comptage de références comme mécanisme principal et un algorithme de détection de cycles pour gérer les références circulaires.

### Le GIL (Global Interpreter Lock)
Le GIL est un verrou qui permet à un seul thread d'exécuter du code Python à la fois dans un même processus. Implications : performances limitées pour le multithreading CPU-intensif, mais protège les structures de données internes de Python contre les conditions de concurrence. Pour contourner, on utilise souvent le multiprocessing.

### Domaines où Python excelle
Data science, IA/ML, web backend (Django/Flask), automation/scripting, DevOps, traitement d'images, éducation en programmation, prototypage rapide.

### Vérifier si un set est sous-ensemble d'un autre
```python
set_a.issubset(set_b)  # ou: set_a <= set_b
```

### Complexité temporelle pour vérifier si un élément est dans un set
O(1) en moyenne - temps constant grâce au hachage.

### Pourquoi pas de listes/dictionnaires dans un set
Ces types sont mutables et non-hashables. Un set requiert des éléments hashables pour maintenir son intégrité et son efficacité.

### Différence entre remove() et discard()
`remove()` lève une KeyError si l'élément n'existe pas, tandis que `discard()` ne génère pas d'erreur.

### Fusionner efficacement plusieurs sets
```python
set_final = set().union(*[set1, set2, set3])  # ou
set_final = set1 | set2 | set3
```

### Différence entre update() et union()
`update()` modifie le set original (in-place), tandis que `union()` retourne un nouveau set sans modifier l'original.

### Quand choisir un set plutôt qu'une liste
Quand l'unicité des éléments est importante, pour des opérations d'appartenance fréquentes, et quand l'ordre n'est pas significatif.

### Liste avec éléments uniques préservant l'ordre
```python
def liste_unique_ordonnee(iterable):
    seen = set()
    return [x for x in iterable if not (x in seen or seen.add(x))]
```
En Python 3.7+ : `list(dict.fromkeys(liste))`

### Différence de performance recherche set vs liste
Set: O(1) - temps constant
Liste: O(n) - temps linéaire (doit parcourir potentiellement toute la liste)

### Itérer sur deux sets simultanément
```python
for item_a, item_b in zip(set_a, set_b):
    # traitement
```
Notez que l'ordre n'est pas garanti.

### Garantir un ordre d'itération dans un set
Impossible. Pour un ordre spécifique, convertir en liste et trier.

### Créer un set en appliquant une transformation
Utiliser la compréhension d'ensemble :
```python
nouveau_set = {transformation(x) for x in set_original}
```

### Gérer l'accès à une clé potentiellement absente
```python
# Méthode 1: get() avec valeur par défaut
valeur = dico.get('clé', 'valeur_défaut')

# Méthode 2: try/except
try:
    valeur = dico['clé']
except KeyError:
    valeur = 'valeur_défaut'
```

### Restrictions sur les types de clés
Les clés doivent être hashables (immuables) : strings, nombres, tuples (contenant uniquement des éléments hashables), frozensets.

### Fusionner deux dictionnaires en Python 3.9+
```python
dict_combiné = dict1 | dict2  # L'opérateur pipe, clés de dict2 ont priorité
```

### Quand privilégier dictionnaire vs liste d'objets
Quand l'accès se fait par clé plutôt que par position, quand la recherche est fréquente, et pour représenter des relations clé-valeur.

### Choisir entre dict.keys() et set
`dict.keys()` quand on veut maintenir le lien avec le dictionnaire original; `set` pour des opérations ensemblistes pures.

### Structure pour compter les occurrences
`collections.Counter` ou un dictionnaire simple :
```python
from collections import Counter
comptage = Counter(['a', 'b', 'a', 'c'])  # {'a': 2, 'b': 1, 'c': 1}
```

### Pourquoi les listes ne peuvent pas être clés de dictionnaire
Elles sont mutables, donc leur hash peut changer, ce qui briserait le mécanisme interne du dictionnaire.

### Utiliser un tuple comme clé
```python
dict_coords = {(1, 2): 'point A', (3, 4): 'point B'}
valeur = dict_coords[(1, 2)]  # 'point A'
```

### Rendre une classe compatible comme clé
Implémenter `__hash__` et `__eq__` :
```python
def __hash__(self):
    return hash((self.attr1, self.attr2))
    
def __eq__(self, autre):
    return (self.attr1, self.attr2) == (autre.attr1, autre.attr2)
```

### Itérer simultanément sur clés et valeurs
```python
for cle, valeur in dico.items():
    # traitement
```

### Méthode efficace pour vérifier si une clé existe
```python
if cle in dico:  # Plus performant que try/except pour simple vérification
    # traitement
```

### Filtrer un dictionnaire pendant l'itération
```python
# Avec compréhension de dictionnaire
dico_filtré = {k: v for k, v in dico.items() if condition(k, v)}
```

### Différence lambda vs fonction régulière
Lambda est anonyme, limitée à une seule expression, et ne peut contenir que des expressions (pas d'instructions). Les fonctions régulières permettent documentation, multiples instructions et réutilisation.

### Cas appropriés/inappropriés pour lambda
**Approprié** : arguments de fonctions (comme key pour sorted), opérations simples, callbacks.
**Inapproprié** : logique complexe, fonctions réutilisées, code nécessitant de la documentation.

### Lambda avec plusieurs conditions
```python
lambda x: expression1 if condition1
          else expression2 if condition2
          else expression3
```

### Différence map vs compréhension de liste
Map est plus fonctionnel et peut être plus efficace avec de très grands ensembles de données (lazy evaluation), tandis que les compréhensions sont plus lisibles et pythoniques.

### Pourquoi reduce dans functools
Pour simplifier le langage de base; Guido van Rossum (créateur de Python) considère que les compréhensions sont plus lisibles pour la plupart des cas d'usage.

### Quand utiliser filter() vs compréhension
Quand l'approche fonctionnelle est préférée ou quand la fonction de filtrage est déjà définie ailleurs.

### Chaîner map, filter et reduce
```python
from functools import reduce
resultat = reduce(lambda x, y: x + y, 
                 map(lambda x: x**2, 
                    filter(lambda x: x % 2 == 0, nombres)))
```

### Type hashable vs non-hashable
**Hashable** : Un objet dont la valeur de hachage ne change jamais pendant sa durée de vie (immuable), implémentant `__hash__()` et `__eq__()`.
**Non-hashable** : Un objet mutable dont la valeur de hachage peut changer, ne pouvant pas être utilisé comme clé de dictionnaire ou élément de set.