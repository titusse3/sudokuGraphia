# uninstall_dependencies.py

import subprocess

def uninstall_dependencies():
    try:
        # Désinstalle les modules listés dans le fichier requirements.txt
        subprocess.run(["pip", "uninstall", "-r", "requirements.txt", "-y"])
        print("Modules désinstallés avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de la désinstallation des modules : {e}")

if __name__ == "__main__":
    uninstall_dependencies()
