import cv2

# Öffne die Webcam (0 ist die Standard-Webcam)
cap = cv2.VideoCapture(0)

# Überprüfe, ob die Webcam erfolgreich geöffnet wurde
if not cap.isOpened():
    print("Fehler beim Öffnen der Webcam")
    exit()

# Lese ein Bild von der Webcam
ret, frame = cap.read()

# Überprüfe, ob das Bild erfolgreich gelesen wurde
if ret:

    # Speichere das Bild auf der Festplatte
    cv2.imwrite('webcam_bild.jpg', frame)
    print("Bild wurde gespeichert.")

# Warte, bis eine Taste gedrückt wird, und schließe dann das Fenster

# Release die Webcam
cap.release()
