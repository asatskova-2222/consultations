from dataclasses import dataclass
from datetime import datetime


@dataclass
class Interval:
    """Интервал времени, на который можно записаться."""
    start: datetime
    end: datetime
    id: int | None = None

    def __str__(self):
        return f"#{self.id} {self.start:%d.%m %H:%M}-{self.end:%H:%M}"


@dataclass
class Participant:
    """Участник консультации."""
    name: str
    contact: str
    id: int | None = None


@dataclass
class Booking:
    """Запись участника на интервал."""
    interval_id: int
    participant_id: int
    id: int | None = None