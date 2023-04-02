import os
import tkinter as tk
from tkinter import filedialog
import subprocess
import moviepy.editor as mp

# Liste des modules nécessaires
required_modules = ["moviepy"]

# Vérification et installation automatique des modules manquants
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{module} n'est pas installé. Installation en cours...")
        subprocess.check_call(["pip", "install", module])

# Initialisation de la fenêtre principale
root = tk.Tk()
root.title("AudioWizardos")
root.config(bg="#121212")
root.geometry("600x400")

# Ajout d'une étiquette
label = tk.Label(root, text="Cliquez sur le bouton pour sélectionner un fichier MP4", fg="#ffffff", bg="#121212", font=("Arial", 14))
label.pack(pady=20)

# Fonction pour sélectionner le fichier MP4
def select_file():
    file_path = filedialog.askopenfilename(title="Sélectionnez un fichier MP4", filetypes=(("Fichiers MP4", "*.mp4"),))
    if file_path:
        convert_to_mp3(file_path)

# Fonction pour convertir le fichier MP4 en MP3
def convert_to_mp3(file_path):
    mp4_file = mp.VideoFileClip(file_path)
    mp3_file = os.path.splitext(file_path)[0] + ".mp3"
    mp4_file.audio.write_audiofile(mp3_file)
    label.config(text=f"Le fichier MP3 a été créé à l'emplacement suivant: {mp3_file}")

# Bouton pour sélectionner le fichier MP4
select_button = tk.Button(root, text="Sélectionner un fichier MP4", fg="#ffffff", bg="#262626", font=("Arial", 12), command=select_file)
select_button.pack(pady=10)

# Exécution de la boucle principale
root.mainloop()
