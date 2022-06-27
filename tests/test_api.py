import sys
import unittest
sys.path.append('./app')
from hospital_types import *

from app import main
from fastapi.testclient import TestClient


class TestReaders(unittest.TestCase):

    def setUp(self):
        self.client = TestClient(main.app)

    def test_book_ct(self):

        assign_request = SurgeryRequest(doctor_id=1, doctor_type=DoctorType.BRAIN_SURGEON)
        expected_output = 'booked for the hour 0, in the room id 1'
        response = self.client.post('/book', json=assign_request.dict()).json()
        self.assertEqual(response, expected_output)

    def test_book_heart(self):
        assign_request = SurgeryRequest(doctor_id=1, doctor_type=DoctorType.HEART_SURGEON)
        expected_output = 'booked for the hour 0, in the room id 3'
        response = self.client.post('/book', json=assign_request.dict()).json()
        self.assertEqual(response, expected_output)
