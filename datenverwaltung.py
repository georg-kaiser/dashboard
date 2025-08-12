from klassen import Pruefungsleistung, Modul, Semester, Studiengang
import json
import pandas as pd



class Datenspeicherung:
    '''
        Die Klasse übernimmt die automatische Speicherung von Datenobjekten, die sie übergeben bekommt.
    '''
    def __init__(self, datenobjekt):
        '''
            Bei der Initalisierung wird ein Datenobjekt übergeben. Es wird überprüft, zu welcher Klasse dieses Objekt gehört und danach entsprechend abgespeichert.
        '''
        self.datenobjekt = datenobjekt

        if isinstance(datenobjekt, Pruefungsleistung):
            self.pruefungsleistung_speichern(datenobjekt)

        elif isinstance(datenobjekt, Modul):
            self.modul_speichern(datenobjekt)

        elif isinstance(datenobjekt, Semester):
            self.semester_speichern(datenobjekt)

        elif isinstance(datenobjekt, Studiengang):
            self.studiengang_speichern(datenobjekt)

        else:
            print("Fehler bei der Eingabe! Falscher Datentyp!")


    def pruefungsleistung_speichern(self, pruefungsleistung):
        '''
            Diese Methode speichert die Pruefungsleistungen in eine 'pruefungsleistungen.json'-Datei ab.
            Falls diese Datei noch nicht exisiert, wird eine Neue erstellt.
            Ansonsten wird die bestehende Datei geöffnet und die neue Pruefungsleistung angehängt und erneut abgespeichert.
        '''
        try:
            with open('pruefungsleistungen.json', 'r', encoding='utf-8') as file:
                liste = json.load(file)
            liste.append(pruefungsleistung.__dict__)
            with open('pruefungsleistungen.json', 'w', encoding='utf-8') as file:
                json.dump(liste, file, ensure_ascii=False, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            with open('pruefungsleistungen.json', 'w', encoding='utf-8') as file:
                json.dump([pruefungsleistung.__dict__], file, ensure_ascii=False, indent=4)
            

    def modul_speichern(self, modul):
        '''
            Diese Methode speichert die Module in eine 'module.json'-Datei ab.
            Falls diese Datei noch nicht exisiert, wird eine Neue erstellt.
            Ansonsten wird die bestehende Datei geöffnet, das neue Modul angehängt und erneut abgespeichert.
        '''
        try:
            with open('module.json', 'r', encoding='utf-8') as file:
                liste = json.load(file)
            liste.append(modul.__dict__)
            with open('module.json', 'w', encoding='utf-8') as file:
                json.dump(liste, file, ensure_ascii=False, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            with open('module.json', 'w', encoding='utf-8') as file:
                json.dump([modul.__dict__], file, ensure_ascii=False, indent=4)
            

    def semester_speichern(self, semester):
        '''
            Diese Methode speichert die Semester in eine 'semester.json'-Datei ab.
            Falls diese Datei noch nicht exisiert, wird eine Neue erstellt und mit sechs Semester gefüllt. Danach wird die Methode rekursiv aufgerufen.
            Existiert die Datei bereits, wird das entsprechende Semester aufgerufen, das neue Modul hinzugefügt, sowie die ECTS des Semesters aktualisiert.
        '''
        try:
            with open('semester.json', 'r', encoding='utf-8') as file:
                liste = json.load(file)
            for sem in liste:
                if sem["nummer"] == semester.nummer:
                    sem["module"].append(semester.module)
                    sem["ects_semester"] += semester.ects_semester
            with open('semester.json', 'w', encoding='utf-8') as file:
                json.dump(liste, file, ensure_ascii=False, indent=4)
        except (FileNotFoundError, json.JSONDecodeError):
            s1 = Semester(1)
            s2 = Semester(2)
            s3 = Semester(3)
            s4 = Semester(4)
            s5 = Semester(5)
            s6 = Semester(6)
            semster_liste = [s1.__dict__, s2.__dict__, s3.__dict__, s4.__dict__, s5.__dict__, s6.__dict__]
            with open('semester.json', 'w', encoding='utf-8') as file:
                json.dump(semster_liste, file, ensure_ascii=False, indent=4)
            self.semester_speichern(semester)
    
    def studiengang_speichern(self, studiengang):
        '''
            Diese Methode speichert den Studiengang in eine 'studiengang.json'-Datei ab.
            Falls diese Datei noch nicht exisiert, wird eine Neue erstellt.
            Ansonsten wird die bestehende Datei überschrieben.
        '''
        with open('studiengang.json', 'w', encoding='utf-8') as file:
                json.dump(studiengang.__dict__, file, ensure_ascii=False, indent=4)



class Nutzereingabe:
    '''
        Diese Klasse erhält der Daten aus der Nutzereingabe im Dashboard. Danach speichert sie die Daten ab 
        und erstellt alle nötigen objektrationalen Verbindungen zwischen den Datenkalssen.
        Erhaltene Daten: Modulname, Modulnummer, Semesternummer, Pruefungsart, ECTS und Note
    '''
    def __init__(self, modulname_wert, modulnummer_wert, semester_wert, pruefungsart_wert, ects_wert, note_wert):
        '''
            Bei der Initialiserung werden mit Hilfe der übergebenen Daten neue Datenobjekte erstellt und abgespeichert.
            Anschließend werden die neune Objekte abgespeichert.
            Zusätzlich wird überprüft ob es sich bei dem neuen Modul um die beste oder schlechteste Note handelt und rechnet den Notendurshcschnitt aus.
            Diese Informationene werden dann ebenfalls gespeichert.
        '''
        self.modulname_wert = modulname_wert, 
        self.modulnummer_wert = modulnummer_wert,
        self.semester_wert = semester_wert,
        self.prüfungsart_wert = pruefungsart_wert,
        self.ects_wert = ects_wert,
        self.note_wert = note_wert

        neue_pruefungsleistung = Pruefungsleistung(pruefungsart=pruefungsart_wert, note=note_wert)
        Datenspeicherung(neue_pruefungsleistung)
        neues_modul = Modul(nummer=modulnummer_wert, name=modulname_wert, pruefungsleistung=neue_pruefungsleistung.id, ects=ects_wert)
        Datenspeicherung(neues_modul)
        neues_semester = Semester(nummer=semester_wert, module=modulnummer_wert, ects_semester=ects_wert)
        Datenspeicherung(neues_semester)
        aktueller_studiengang = Datenzugriff().studiengang_ausgeben()
        aktueller_studiengang.ects_gesamt += ects_wert
        beste_note = self.beste_note_finden()
        #Falls es sich um die beste Note handelt, werden die Informationen im Studiengang aktualisiert.
        if beste_note:
                aktueller_studiengang.beste_note = note_wert
                aktueller_studiengang.bestes_modul = modulname_wert
                aktueller_studiengang.beste_pruefungsart = pruefungsart_wert
        schlechteste_note = self.schlechteste_note_finden()
        #Falls es sich um die schlechteste Note handelt, werden die Informationen im Studiengang aktualisiert.
        if schlechteste_note:
                aktueller_studiengang.schlechteste_note = note_wert
                aktueller_studiengang.schlechtestes_modul = modulname_wert
                aktueller_studiengang.schlechteste_pruefungsart = pruefungsart_wert
        #Notendurschnitt aktualiseren
        aktueller_studiengang.notenduchschnitt_gesamt = self.notendurschschnitt_berechnen()
        Datenspeicherung(aktueller_studiengang)


    def beste_note_finden(self):
        '''
            Diese Methode öffnet 'pruefungsleistungen.json', geht alle Pruefungen durch und findet die Prüfung mit der besten Note.
            Falls es gleiche Noten gibt, wird die zuletzt hinzugefügte Pruefung berücksichtigt.
            Da zu diesem Zeitpunkt bereits die neue Pruefungsleistung zur Datei hinzugefügt wurde, wird vergleichen ob die Note übereinstimmt.
            Falls ja, ist die neue Pruefung die Beste und es wird True zurück gegeben.
            Falls nicht oder falls die Datei nicht exisiert/ nicht gelesen werden kann wird False zurück gegeben.
        '''
        try:
            with open('pruefungsleistungen.json', 'r', encoding='utf-8') as pruefungen:
                pruefungsliste = json.load(pruefungen)
                beste_pruefung = pruefungsliste[0]
            for pruefung in pruefungsliste:
                if pruefung["note"] <= beste_pruefung["note"]:
                    beste_pruefung = pruefung
            if beste_pruefung["note"] == self.note_wert:
                return True
            else:
                return False
        except (FileNotFoundError, json.JSONDecodeError):
            return True
 

    def schlechteste_note_finden(self):
        '''
            Diese Methode öffnet 'pruefungsleistungen.json', geht alle Pruefungen durch und findet die Prüfung mit der schlechtesten Note.
            Falls es gleiche Noten gibt, wird die zuletzt hinzugefügte Pruefung berücksichtigt.
            Da zu diesem Zeitpunkt bereits die neue Pruefungsleistung zur Datei hinzugefügt wurde, wird vergleichen ob die Note übereinstimmt.
            Falls ja, ist die neue Pruefung die Schlechteste und es wird True zurück gegeben.
            Falls nicht oder falls die Datei nicht exisiert/ nicht gelesen werden kann wird False zurück gegeben.
        '''
        try:
            with open('pruefungsleistungen.json', 'r', encoding='utf-8') as pruefungen:
                pruefungsliste = json.load(pruefungen)
                schlechteste_pruefung = pruefungsliste[0]
            for pruefung in pruefungsliste:
                if pruefung["note"] >= schlechteste_pruefung["note"]:
                    schlechteste_pruefung = pruefung
            if schlechteste_pruefung["note"] == self.note_wert:
                return True
            else:
                return False
        except (FileNotFoundError, json.JSONDecodeError):
            return True
        

    def notendurschschnitt_berechnen(self):
        '''
             Diese Methode öffnet 'pruefungsleistungen.json', geht alle Pruefungen durch und berechnet den Notendurchschnitt.
             Es werden alle Noten addiert und durch die Anzahl der Pruefungen geteilt.
             Anschließend wird der Notendurschschnitt zurückgeben
             Falls die Datei nicht geöffent werden kann oder nicht exisitert wird 0.0 zurückgegeben
        '''
        try:
            with open('pruefungsleistungen.json', 'r', encoding='utf-8') as pruefungen:
                pruefungsliste = json.load(pruefungen)
                noten_gesamt = 0.0
            for pruefung in pruefungsliste:
                noten_gesamt += pruefung["note"]
            notendurchschnitt = noten_gesamt / len(pruefungsliste)
            return notendurchschnitt
        except (FileNotFoundError, json.JSONDecodeError):
            return 0.0



class Datenzugriff:
    '''
        Diese Klasse lässt das Dashboard auf die bereits in den JSON-Datein gespeicherten Daten zugreifen.
        Dabei wird von außen auf die jeweiligen Methoden zugegriffen.
    '''
    def __init__(self):
        pass

    def studiengang_ausgeben(self):
        '''
            Diese Methode gibt ein Studiengang-Objekt zurück. Das Objekt enthält fast alle wichtigen Attribute für das Dashbaord.
            Dies macht die Datenabfrage simpel und felxibel.
            Falls die Datei nicht exisiert oder nicht gelesen werden kann, wird ein neuer Studiengang mit Standardwerten erstellt.
        '''
        try:
            with open('studiengang.json', 'r', encoding='utf-8') as studiengang:
                studiengang_daten = json.load(studiengang)
            return Studiengang(**studiengang_daten)
        except (FileNotFoundError, json.JSONDecodeError):
            return Studiengang()
        
    def ects_semeseter_ausgeben(self):
        '''
            Diese Methode gibt ein Pandas DataFrame aus, dass zwei Spalten für Nummer und ECTS enthält.
            Falls die 'semester.json'-Datei nicht aufgerufen werden kann, gibt die Methode einen DataFrame mit Standardwerten zurück.
        '''
        try:
            with open('semester.json', 'r', encoding='utf-8') as semester:
                semester_liste = json.load(semester)
                nummer_liste = []
                ects_liste = []
                for sem in semester_liste:
                    nummer_liste.append(sem["nummer"])
                    ects_liste.append(sem["ects_semester"])
            return pd.DataFrame({'Semester': nummer_liste, 'ECTS': ects_liste})
        except (FileNotFoundError, json.JSONDecodeError):
            return pd.DataFrame({'Semester': [1,2,3,4,5,6], 'ECTS': [0,0,0,0,0,0]}) #Standardwerte sind 0 ECTS für jedes Semester