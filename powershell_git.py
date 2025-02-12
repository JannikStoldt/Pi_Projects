import subprocess

# Liste von Git-Befehlen, die ausgeführt werden sollen
commands = [
    "git add ./",               
    "git commit -m'updates",
    "git push",
]

# Befehle der Reihe nach ausführen
for command in commands:
    print(f"Führe aus: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # Ausgabe des Befehls anzeigen
    print("Ergebnis:")
    print(result.stdout)  # Ausgabe des Befehls
    print(result.stderr)  # Fehlerausgabe, falls vorhanden
