## 📊👩🏽‍💻Analyseur de Logs
Un petit programme Python qui analyse des fichiers de logs pour détecter les adresses IP suspectes et identifier les potentielles attaques.


## Pourquoi ce projet ?
En apprenant la cybersécurité, j'ai découvert que l'analyse de logs est une tâche quotidienne pour les analystes SOC. J'ai voulu créer un outil simple pour comprendre comment détecter des activités suspectes dans des fichiers de logs.


## Comment ça marche ?

Le programme utilise des expressions régulières (regex) pour trouver les adresses IP dans chaque ligne du fichier. Ensuite, il compte les occurrences avec un dictionnaire Python et trie les résultats pour afficher les IPs les plus actives.

Une IP est considérée comme suspecte si elle apparaît 5 fois ou plus, ce qui peut indiquer :
- Une tentative de brute force (connexions répétées)
- Un scan de ports
- Une activité anormale


## 🛠️ Installation
```bash
# 1. bashgit clone https://github.com/SOYA6A/log-analyzer.git
# 2. cd log-analyzer
# 3. python log_analyzer.py
# 4. Pas de bibliothèques externes nécessaires, j'utilise juste les modules Python de base (re pour les expressions régulières).
```
Pas de bibliothèques externes nécessaires, j'utilise juste les modules Python de base.
## Utilisation
```bash
python3 log-analyzer.py
```
Le programme demande le nom du fichier de logs à analyser.

### Exemple avec le fichier de test
```
Entrez le nom du fichier de logs : access.log

=== ANALYSE DES LOGS ===






<img width="1612" height="724" alt="image" src="https://github.com/user-attachments/assets/b8cd966f-e47f-4162-8051-0c05fe6d5b3a" />
