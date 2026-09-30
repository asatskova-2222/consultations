from .models import Interval, Participant, Booking


class Storage:
    # Простое in-memory хранилище.

    def __init__(self):
        self.intervals = {}
        self.participants = {}
        self.bookings = {}
        self._ids = {"i": 1, "p": 1, "b": 1}

    def _next(self, key):
        value = self._ids[key]
        self._ids[key] += 1
        return value

    def add_interval(self, start, end):
        obj = Interval(start, end, self._next("i"))
        self.intervals[obj.id] = obj
        return obj

    def add_participant(self, name, contact):
        obj = Participant(name, contact, self._next("p"))
        self.participants[obj.id] = obj
        return obj

    def add_booking(self, interval_id, participant_id):
        obj = Booking(interval_id, participant_id, self._next("b"))
        self.bookings[obj.id] = obj
        return obj

    def is_busy(self, interval_id):
        return any(b.interval_id == interval_id for b in self.bookings.values())