## 📊👩🏽‍💻Analyseur de Logs
Un petit programme Python qui analyse des fichiers de logs pour détecter les adresses IP suspectes et identifier les potentielles attaques.


## Pourquoi ce projet ?
En apprenant la cybersécurité, j'ai découvert que l'analyse de logs est une tâche quotidienne pour les analystes SOC. J'ai voulu créer un outil simple pour comprendre comment détecter des activités suspectes dans des fichiers de logs.


Le programme analyse un fichier de logs et extrait toutes les adresses IP présentes 
Compte combien de fois chaque IP apparaît.
Affiche les 10 IPs les plus actives.
Détecte les IPs suspectes (plus de 5 requêtes = potentiel brute force ou scan).


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

Total de lignes analysées : 13

Top 10 des IPs les plus actives :

1. 203.0.113.5 - 5 requêtes ⚠️ SUSPECT
2. 192.168.1.10 - 3 requêtes
3. 198.51.100.42 - 3 requêtes
4. 45.123.67.89 - 2 requêtes

=== IPS SUSPECTES DÉTECTÉES ===

🚨 203.0.113.5 : 5 tentatives (possibles attaque)
```
<img width="1612" height="724" alt="image" src="https://github.com/user-attachments/assets/b8cd966f-e47f-4162-8051-0c05fe6d5b3a" />
