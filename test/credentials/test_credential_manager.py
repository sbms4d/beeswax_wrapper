import unittest
import mock


from beeswax_wrapper.credentials.credential_manager import get_beeswax_credentials, store_beeswax_credentials


class TestStoreBeeswaxCredentials(unittest.TestCase):

    def test_keyring(self):
        with mock.patch('beeswax_wrapper.credentials.credential_manager.keyring') as f:
            store_beeswax_credentials('a', 'b')
            self.assertEqual(f.set_password.call_count, 2)


class TestGetBeeswaxCredentials(unittest.TestCase):

    def test_keyring(self):
        with mock.patch('beeswax_wrapper.credentials.credential_manager.keyring') as f:
            get_beeswax_credentials()
            self.assertEqual(f.get_password.call_count, 2)
