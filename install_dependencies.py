# install_dependencies.py

import subprocess

def install_dependencies():
    try:
        # Installe les modules à partir du fichier requirements.txt
        subprocess.run(["pip", "install", "-r", "requirements.txt"])
        print("Modules installés avec succès.")
    except Exception as e:
        print(f"Une erreur s'est produite lors de l'installation des modules : {e}")

if __name__ == "__main__":
    install_dependencies()
