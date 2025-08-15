## Dashbaord-Protyp mit grafischer Benutzeroberfläche

### Voraussetzungen
- Python 3.13.6 oder neuer

### Anleitung
1. Repository klonen:
   ```bash
   git clone https://github.com/georg-kaiser/dashboard.git
   cd dashboard
   ```

2. Virtuelle Umgebung erstellen und aktivieren:
   ```bash
   # Linux/Mac
   python -m venv venv
   source venv/bin/activate
   ```
   ```bash
   # Windows
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. Progamm ausführen:
   ```bash
   streamlit run main.py
   ```

### Verwendung
Beim ersten Ausführen des Dashboards wird der Nutzer aufgefordert, einen Namen und einen Stu-diengang anzugeben. Danach wird er auf das eigentliche Dashboard weitergeleitet.
Bei der ersten Ausführung ist dieses größtenteils leer. Sobald der Nutzer neue Module hinzufügt, werden alle Met-riken aktualisiert. 
Wenn zukünftig der Nutzer das Programm ausführt, landet er direkt auf dem Dashboard. Dabei bleiben alle eigegebenen Daten erhalten.
