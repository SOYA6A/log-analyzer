import re

def analyser_logs(fichier_log):
    """
    Fonction qui analyse un fichier de logs et extrait les IPs.
    
    Arguments:
        fichier_log -- Le chemin du fichier de logs à analyser
    """
    
    compteur_ips = {}
    
    with open(fichier_log, 'r') as fichier:
        lignes = fichier.readlines()
        
        print(f"\n=== ANALYSE DES LOGS ===\n")
        print(f"Total de lignes analysées : {len(lignes)}\n")
        
        for ligne in lignes:
            ip = re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', ligne)
            
            if ip:
                ip_adresse = ip.group()
                
                if ip_adresse in compteur_ips:
                    compteur_ips[ip_adresse] += 1
                else:
                    compteur_ips[ip_adresse] = 1
    
    ips_triees = sorted(compteur_ips.items(), key=lambda x: x[1], reverse=True)
    
    print("Top 10 des IPs les plus actives :\n")
    for i, (ip, count) in enumerate(ips_triees[:10], 1):
        suspect = "⚠️ SUSPECT" if count >= 5 else ""
        print(f"{i}. {ip} - {count} requêtes {suspect}")
    
    print("\n=== IPs SUSPECTES DÉTECTÉES ===\n")
    ips_suspectes = [ip for ip, count in compteur_ips.items() if count >= 5]
    
    if ips_suspectes:
        for ip in ips_suspectes:
            print(f"🚨 {ip} : {compteur_ips[ip]} tentatives (possibles attaque)")
    else:
        print("✅ Aucune IP suspecte détectée")

if __name__ == "__main__":
    fichier = input("Entrez le nom du fichier de logs : ")
    
    try:
        analyser_logs(fichier)
    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier '{fichier}' n'existe pas")
