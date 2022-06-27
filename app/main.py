import logging
from hospital import Hospital
from operating_room import OperatingRoom
from hospital_types import *

from fastapi import FastAPI

app = FastAPI()


hospital = Hospital([
    OperatingRoom([MachineType.MRI, MachineType.MRI, MachineType.ECG], 3),
    OperatingRoom([MachineType.MRI, MachineType.CT, MachineType.ECG], 1),
    OperatingRoom([MachineType.MRI, MachineType.CT], 2),
]
)


@app.post('/book', summary="assign a surgery slot as per the doctor specifications")
def book_operating_room(request: SurgeryRequest):
    slot = -1
    room = -1
    if request.doctor_type == DoctorType.HEART_SURGEON:
        slot, room = hospital.book_heart_room()
    elif request.doctor_type == DoctorType.BRAIN_SURGEON:
        slot, room = hospital.book_brain_room()

    if slot is False:
        hospital.save_a_slot_for_tomorrow(request)
        msg = f'Have been added to tomorrows queue'
    else:
        msg = f'booked for the hour {slot}, in the room id {room}'
    logging.info(msg)
    return msg


@app.get('/alive')
def alive():
    return {'status': 'ok'}
