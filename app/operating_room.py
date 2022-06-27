from hospital_types import *

class OperatingRoom:
    def __init__(self, machine_types : [list[MachineType]], id : int):
        self.machine_types = machine_types
        self.busy_slots = [False for i in range(12)]
        self.id = id

    def has_machine(self, machine_type :MachineType):
        return machine_type in self.machine_types

    def try_book_a_slot(self, duration_in_hours: int):
        consecutive_free_slots = 0
        for slot_id in range(len(self.busy_slots)):
            if not self.busy_slots[slot_id]:
                if consecutive_free_slots == duration_in_hours:
                    slot_start = slot_id - duration_in_hours
                    for book_slot_id in range(slot_start, slot_id):
                        self.busy_slots[book_slot_id] = True
                    return slot_start
                else:
                    consecutive_free_slots += 1
            else:
                consecutive_free_slots = 0
        return -1
