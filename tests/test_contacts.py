import os
from unittest import TestCase
from hubspot.client import Client

class ContactsTest(TestCase):
    def setUp(self):
        self.client = Client(os.environ.get('token'))

    def test_create_contact(self):
        result_create = self.client.contacts.create_contact(data={'email':'grplugtest2@gmail.com'}).json()
        _id = None
        _contacts = self.client.contacts.get_contacts().json()['contacts']
        for _contact in _contacts:
            if _contact['vid'] == result_create['vid']:
                _id = _contact['vid']
        self.assertIsNotNone(_id)
        self.client.contacts.delete_contact(result_create['vid'])

    def test_delete_contact(self):
        result_create = self.client.contacts.create_contact(data={'email':'grplugtest2@gmail.com'}).json()
        self.client.contacts.delete_contact(result_create['vid'])
        _id = None
        _contacts = self.client.contacts.get_contacts().json()['contacts']
        for _contact in _contacts:
            if _contact['vid'] == result_create['vid']:
                _id = _contact['vid']
        self.assertIsNone(_id)