from dataclasses import dataclass, field
import uuid

def uuid_generieren() -> str:
    '''
        Generiert eine eindeutige ID für jede Prüfungsleistung.
    '''
    return str(uuid.uuid4())

@dataclass
class Pruefungsleistung:
    '''
        Die Datenklasse Pruefungsleistung enthält eine eindeutige ID, die Pruefungsart und die Note.
    '''
    id: str = field(init=False, default_factory=uuid_generieren)
    pruefungsart: str
    note: float
    
@dataclass
class Modul:
    '''
        Die Datenklasse Modul enthält eine Nummer (Kürzel an der IU können auch Buchstaben enthalten, deshalb ist es ein String), 
        einen Namen, die eindeutige ID einer Prüfungsleistung (Kompostion) und die ECTS.
    '''
    nummer: str
    name: str
    pruefungsleistung: str
    ects: int = 5

@dataclass
class Semester:
    '''
        Die Datenklasse Semester enthält eine Nummer, eine Liste an Modulnummern (Aggregation) und die erreichten ECTS pro Semester.
    '''
    nummer: int
    module: list[str] = field(default_factory=list) #die field()-Methode muss verwendet werden, ansonten verweist jedes Objekt dieser Datenklasse auf die selbe Liste
    ects_semester: int = 0

@dataclass
class Studiengang:
    '''
        Die Datenklasse Studiengang enthält die Bezeichnung des Studiengangs, den Namen des Studenten, 
        eine Liste an Semesternummern (Aggregation), die insgesamt erreichten ECTS, den Notendurchschnitt, 
        Informationen über Note, Namen und Pruefungsart des besten Moduls  
        und Note, Namen und Pruefungsart des schlechtesten Moduls.
    '''
    bezeichnung: str = "Angewandte Künstliche Intelligenz" #Standardwert, falls der Nutzer ncihts angibt.
    student: str = "Georg Kaiser" #Standardwert, falls der Nutzer ncihts angibt.
    semester_liste: list[int] = field(default_factory=list)
    ects_gesamt: int = 0
    notenduchschnitt_gesamt: float = 0.0
    beste_note: float = 5.0 #wird am Anfang auf 5.0 gesetzt, damit der Wert bei Hinzufügen des ersten Moduls überschrieben wird
    bestes_modul: str = ""
    beste_pruefungsart:str = ""
    schlechteste_note: float = 0.0 #wird am Anfang auf 0.0 gesetzt, damit der Wert bei Hinzufügen des ersten Moduls überschrieben wird
    schlechtestes_modul: str = ""
    schlechteste_pruefungsart:str = ""

