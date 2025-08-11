from dataclasses import dataclass, field
import uuid

def uuid_generieren() -> str:
    return str(uuid.uuid4())

@dataclass
class Pruefungsleistung:
    id: str = field(init=False, default_factory=uuid_generieren)
    pruefungsart: str
    note: float
    
@dataclass
class Modul:
    nummer: int
    name: str
    pruefungsleistung: str
    ects: int = 5

@dataclass
class Semester:
    nummer: int
    module: list[int] = field(default_factory=list)
    ects_semester: int = 0

@dataclass
class Studiengang:
    bezeichnung: str
    student: str
    semester_liste: list[int] = field(default_factory=list)
    ects_gesamt: int = 0
    notenduchschnitt_gesamt: float = 1.0
    beste_note: float = 1.0
    schlechteste_note: float = 1.0
