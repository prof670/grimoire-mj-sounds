import os

owner = "prof670"
repo = "grimoire-mj-sounds"
branch = "main"

audio_extensions = (".mp3", ".ogg", ".wav", ".flac", ".m4a")
links = []

print("Recherche locale des fichiers audio dans les dossiers...\n")

# Parcourt tous les dossiers et sous-dossiers locaux
for root, dirs, files in os.walk("."):
    for file in files:
        if file.lower().endswith(audio_extensions):
            # Construit le chemin relatif propre (ex: ambiances/combat/musique.mp3)
            rel_path = os.path.relpath(os.path.join(root, file), ".")
            rel_path = rel_path.replace(os.sep, "/")
            if rel_path.startswith("./"):
                rel_path = rel_path[2:]

            raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{rel_path}"
            links.append(raw_url)
            print(raw_url)

with open("liens_sons.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(links))

print(f"\n✅ {len(links)} liens audio trouvés et enregistrés dans 'liens_sons.txt' !")
