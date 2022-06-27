import enum
from pydantic import BaseModel


class MachineType(int, enum.Enum):
    ECG = 0,
    MRI = 1,
    CT = 3


class DoctorType(int, enum.Enum):
    HEART_SURGEON = 0,
    BRAIN_SURGEON = 1


class SurgeryRequest(BaseModel):
    doctor_type: DoctorType
    doctor_id: int