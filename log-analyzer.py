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