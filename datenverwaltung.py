from klassen import Pruefungsleistung, Modul, Semester, Studiengang
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


            
class Datenspeicherung:
    '''
        Erkennt automatisch welche Art von Datenobjekt übergeben wird und speichert es entsprechend ab.
    '''
    def __init__(self, datenobjekt):
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
        try:
            with open('pruefungsleistungen.json', 'r', encoding='utf-8') as file:
                liste = json.load(file)
            print(pruefungsleistung.__dict__)
            liste.append(pruefungsleistung.__dict__)
            with open('pruefungsleistungen.json', 'w', encoding='utf-8') as file:
                json.dump(liste, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            with open('pruefungsleistungen.json', 'w', encoding='utf-8') as file:
                json.dump([pruefungsleistung.__dict__], file, ensure_ascii=False, indent=4)
            print("Neue Datei erstellt!")
        except json.JSONDecodeError:
            with open('pruefungsleistungen.json', 'w', encoding='utf-8') as file:
                json.dump([pruefungsleistung.__dict__], file, ensure_ascii=False, indent=4)
            print("Leere oder fehlerhafte Datei überschrieben!")

    def modul_speichern(self, modul):
        try:
            with open('module.json', 'r', encoding='utf-8') as file:
                liste = json.load(file)
            print("Datei erfolgreich geladen!")
            liste.append(modul.__dict__)
            with open('module.json', 'w', encoding='utf-8') as file:
                json.dump(liste, file, ensure_ascii=False, indent=4)
        except FileNotFoundError:
            with open('module.json', 'w', encoding='utf-8') as file:
                json.dump([modul.__dict__], file, ensure_ascii=False, indent=4)
            print("Neue Datei erstellt!")
        except json.JSONDecodeError:
            with open('module.json', 'w', encoding='utf-8') as file:
                json.dump([modul.__dict__], file, ensure_ascii=False, indent=4)
            print("Leere oder fehlerhafte Datei überschrieben!")

    def semester_speichern(self, semester):
        print(semester.nummer)
        try:
            with open('semester.json', 'r', encoding='utf-8') as file:
                liste = json.load(file)
                print(liste)
            for sem in liste:
                if sem["nummer"] == semester.nummer:
                    sem["module"].append(int(semester.module))
                print(sem)
            with open('semester.json', 'w', encoding='utf-8') as file:
                json.dump(liste, file, ensure_ascii=False, indent=4)
                print("Erfolg")
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
            print("Neue Datei erstellt!")
    
    def studiengang_speichern(self, studiengang):
        with open('studiengang.json', 'w', encoding='utf-8') as file:
                json.dump(studiengang.__dict__, file, ensure_ascii=False, indent=4)
        print("Studiengang aktualisiert!")
        return
        
    


def studiengang_laden():
    with open('studiengang.json', 'r', encoding='utf-8') as datei:
        studiengang_daten = json.load(datei)
    return Studiengang(**studiengang_daten)



class Nutzereingabe:
    def __init__(self, modulname_wert, modulnummer_wert, semester_wert, pruefungsart_wert, ects_wert, note_wert):
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
        neues_semester = Semester(semester_wert, modulnummer_wert)
        Datenspeicherung(neues_semester)

        print("Gespeichtert!")
        

class Datenzugriff:
    def __init__(self):
        pass

    def schlechteste_note_finden(self):
        pass

    def gesamt_ects_berechnen(self):
        pass

    def notendurchschnitt_berechnen(self):
        pass

    def semester_ects_berechnen(self):
        pass

    def beste_note_finden(self):
        try:
            with open('pruefungsleistungen.json', 'r', encoding='utf-8') as pruefungen:
                pruefungsliste = json.load(pruefungen)
                print(pruefungsliste)
                beste_pruefung = pruefungsliste[0]
            for pruefung in pruefungsliste:
                if pruefung["note"] <= beste_pruefung["note"]:
                    beste_pruefung = pruefung
                print(pruefung)
            print(beste_pruefung)
            modulname = self.passendes_modul_finden(beste_pruefung)
            return [modulname, beste_pruefung["note"], beste_pruefung["pruefungsart"]]

        except (FileNotFoundError, json.JSONDecodeError):
            return ["-", "-", "-"]
 
    def passendes_modul_finden(self,beste_pruefung):
        try:
            with open('module.json', 'r', encoding='utf-8') as module:
                modulliste = json.load(module)
                print(modulliste)
            for modul in modulliste:
                if modul["pruefungsleistung"] == beste_pruefung["id"]:
                    print(modul["name"])
                    return modul["name"]
                
        except(FileNotFoundError, json.JSONDecodeError):
            return "-"