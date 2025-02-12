import cv2
import time

# Aktuelle Zeit im Format 'HH:MM:SS'
current_time = time.strftime("%H_%M_%S")

save_dir = "./images/"
pictureName = save_dir + current_time + "_bild.jpg"

# Öffne die Webcam (0 ist die Standard-Webcam)
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_V4L2)

# Überprüfe, ob die Webcam erfolgreich geöffnet wurde
if not cap.isOpened():
    print("Fehler beim Öffnen der Webcam")
    exit()

# Lese ein Bild von der Webcam
ret, frame = cap.read()

# Überprüfe, ob das Bild erfolgreich gelesen wurde
if ret:

    # Speichere das Bild auf der Festplatte
    cv2.imwrite(pictureName, frame)
    print("Bild wurde gespeichert.")

# Release die Webcam
cap.release()
