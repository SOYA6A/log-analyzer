## 📊👩🏽‍💻Analyseur de Logs
Un petit programme Python qui analyse des fichiers de logs pour détecter les adresses IP suspectes et identifier les potentielles attaques.


## Pourquoi ce projet ?
En apprenant la cybersécurité, j'ai découvert que l'analyse de logs est une tâche quotidienne pour les analystes SOC. J'ai voulu créer un outil simple pour comprendre comment détecter des activités suspectes dans des fichiers de logs.


## Le programme analyse un fichier de logs et :

Extrait toutes les adresses IP présentes.
Compte combien de fois chaque IP apparaît.
Affiche les 10 IPs les plus actives.
Détecte les IPs suspectes (plus de 5 requêtes = potentiel brute force ou scan).


## 🛠️ Installation
```bash
# 1. bashgit clone https://github.com/SOYA6A/log-analyzer.git
# 2. cd log-analyzer
# 3. python log_analyzer.py
# 4. Pas de bibliothèques externes nécessaires, j'utilise juste les modules Python de base (re pour les expressions régulières).
