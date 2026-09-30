from datetime import datetime
from .storage import Storage


class Service:
    """Прикладные правила: интервалы, участники, записи."""

    def __init__(self, storage: Storage):
        self.storage = storage

    def add_interval(self, start: datetime, end: datetime):
        if end <= start:
            raise ValueError("Конец должен быть позже начала")
        return self.storage.add_interval(start, end)

    def add_participant(self, name, contact):
        if not name.strip() or not contact.strip():
            raise ValueError("Имя и контакт обязательны")
        return self.storage.add_participant(name.strip(), contact.strip())

    def free_intervals(self):
        return sorted(
            [i for i in self.storage.intervals.values()
             if not self.storage.is_busy(i.id)],
            key=lambda i: i.start,
        )

    def book(self, interval_id, participant_id):
        if interval_id not in self.storage.intervals:
            raise ValueError("Интервал не найден")
        if participant_id not in self.storage.participants:
            raise ValueError("Участник не найден")
        if self.storage.is_busy(interval_id):
            raise ValueError("Интервал уже занят")
        return self.storage.add_booking(interval_id, participant_id)