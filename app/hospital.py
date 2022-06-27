import threading
import queue
from operating_room import OperatingRoom
from hospital_types import *


class Hospital:
    def __init__(self, operating_rooms : [list[OperatingRoom]]):
        self.operating_rooms = operating_rooms
        self.tomorrow_slots = queue.Queue()
        self.room_lock = threading.Lock()

    def book_heart_room(self):
        return self._book_room_by_type(duration_in_hours=3, machine_type=MachineType.ECG)

    def book_brain_room(self):
        slot, id = self._book_room_by_type(duration_in_hours=2, machine_type=MachineType.CT)

        if slot == -1:
            return self._book_room_by_type(duration_in_hours=3, machine_type=MachineType.MRI)
        else:
            return slot, id

    def _book_room_by_type(self, duration_in_hours, machine_type):
        with self.room_lock:
            for room in self.operating_rooms:
                if room.has_machine(machine_type=machine_type):
                    slot = room.try_book_a_slot(duration_in_hours=duration_in_hours)
                    if slot != -1:
                        return slot, room.id
            return -1, -1

    def save_a_slot_for_tomorrow(self, surgery_request):
        self.tomorrow_slots.put(surgery_request)
