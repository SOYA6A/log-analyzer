# Importer la bibliothèque 're' pour utiliser les expressions régulières
# (ça sert à chercher des patterns dans du texte, comme trouver une IP)
import re

def analyser_logs(fichier_log):
    """
    Fonction qui analyse un fichier de logs et extrait les IPs.
    
    Arguments:
        fichier_log -- Le chemin du fichier de logs à analyser
    """
    compteur_ips = {}
     # Ouvrir le fichier de logs en mode lecture
    with open(fichier_log, 'r') as fichier:
        # Lire toutes les lignes du fichier
        lignes = fichier.readlines()
        
        print(f"\n=== ANALYSE DES LOGS ===\n")
        print(f"Total de lignes analysées : {len(lignes)}\n")
        
        # Pour chaque ligne du fichier
        for ligne in lignes:
            # Chercher une adresse IP dans la ligne
            # Pattern regex pour une IP : \d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}
            # Explication : \d = chiffre, {1,3} = de 1 à 3 chiffres, \. = point
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ligne)
            
            # Si on a trouvé une IP
            if ip:
                ip_adresse = ip.group()  # Récupérer l'IP trouvée
                
                # Si l'IP est déjà dans le dictionnaire, on ajoute 1
                if ip_adresse in compteur_ips:
                    compteur_ips[ip_adresse] += 1
                # Sinon, on l'ajoute avec la valeur 1
                else:
                    compteur_ips[ip_adresse] = 1
    
    # Trier les IPs par nombre d'occurrences (du plus grand au plus petit)
    ips_triees = sorted(compteur_ips.items(), key=lambda x: x[1], reverse=True)
    
    # Afficher le top 10
    print("Top 10 des IPs les plus actives :\n")
    for i, (ip, count) in enumerate(ips_triees[:10], 1):
        # Si plus de 5 requêtes, marquer comme suspect
      suspect = "⚠️ SUSPECT" if count >= 5 else "" 
     print(f"{i}. {ip} - {count} requêtes {suspect}")
  
    # Détecter les IPs suspectes (plus de 5 requêtes)
    print("\n=== IPs SUSPECTES DÉTECTÉES ===\n")
    ips_suspectes = [ip for ip, count in compteur_ips.items() if count >=  5]
    
    if ips_suspectes:
        for ip in ips_suspectes:
            print(f"🚨 {ip} : {compteur_ips[ip]} tentatives (possibles attaque)")
    else:
        print("✅ Aucune IP suspecte détectée")

# Point d'entrée du programme
if __name__ == "__main__":
    # Demander à l'utilisateur le chemin du fichier
    fichier = input("Entrez le nom du fichier de logs : ")
    
    # Appeler la fonction d'analyse
    try:
        analyser_logs(fichier)
    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{fichier}' n'existe pas")
           
