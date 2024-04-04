from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Dict
@dataclass
class Note:
    code: int
    title: str
    text: str
    importance: str
    creation_time: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def __str__(self):
        tag_str = ', '.join(self.tags)
        return f'Code: {self.code}\nCreation date: {self.creation_time}\n{self.title}: {self.text}\nTags: {tag_str}\n---\n'

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

@dataclass
class Notebook:
    notes: List[Note] = field(default_factory=list)

    def add_note(self, title: str, text: str, importance: str) -> int:
        new_note = Note(len(self.notes), title, text, importance)
        self.notes.append(new_note)
        return new_note.code

    def important_notes(self) -> List[Note]:
        return [note for note in self.notes if note.importance in ['HIGH', 'MEDIUM']]

    def tags_note_count(self) -> Dict[str, int]:
        tag_count = {}
        for note in self.notes:
            for tag in note.tags:
                if tag not in tag_count:
                    tag_count[tag] = 0
                tag_count[tag] += 1
        return tag_count