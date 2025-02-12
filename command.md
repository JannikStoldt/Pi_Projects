# USEFULL COMMANDS


## -----Linux-----

### 1. Systeminfos

top
htop
//zeigen beide jeweils infos über das aktuelle System an

df -h
//zeigt Speicher an



### 2. apt (Paketmanager)

sudo apt update
//aktualisiert die Paketliste --> damit System bzw. apt weiß, welche Pakete es gibt

sudo apt upgrade
//aktuallisiert die installierten Pakete anhand der Paketliste

sudo apt install <name>
//installiert das entsprechende Paket

sudo apt remove <name>
//entfernt das entsprechende Paket

sudo apt autoremove
//entfernt zusätzlich Pakete die als Abhängigkeiten installiert jetzt aber nicht mehr benötigt werden

sudo apt search <name>
//sucht die Paketliste nach Paket durch

sudo apt show <name>
//zeigt Infos über entsprechendes Paket

sudo apt depends <name>
//zeigt Abhängigkeiten