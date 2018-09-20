import unittest

import mock

from beeswax_wrapper.core.access import get_beeswax_dal, BeeswaxDAL, BeeswaxRESTException


class TestBeeswaxDalPrivateCall(unittest.TestCase):

    def setUp(self):
        self.dal = BeeswaxDAL(None)

    def test_bad_endpoint(self):
        self.dal.endpoint_url = None
        with self.assertRaises(RuntimeError):
            self.dal._call('get', [])

    def test_bad_response(self):
        self.dal.endpoint_url = ''
        with mock.patch('beeswax_wrapper.core.access.BeeswaxDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.json.return_value = {'errors': ['error_1', 'error_2'], 'success': False, 'message': ''}
            with self.assertRaises(BeeswaxRESTException):
                self.dal._call('get', [])

    def test_good_response(self):
        self.dal.endpoint_url = ''
        with mock.patch('beeswax_wrapper.core.access.BeeswaxDAL.session', new_callable=mock.PropertyMock) as p:
            p.return_value = p.get = p
            p.json.return_value = {'payload': 'output', 'success': True}
            self.assertEqual(self.dal._call('get', []), 'output')


class TestBeeswaxDalAuthenticate(unittest.TestCase):

    def setUp(self):
        self.dal = BeeswaxDAL(None)
        self.dal._call = mock.Mock()

    def test_get_credentials(self):
        with mock.patch('beeswax_wrapper.core.access.get_beeswax_credentials') as f:
            self.dal.authenticate()
            self.assertEqual(f.called, True)
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal._call.called, True)

    def test_not_get_credentials(self):
        with mock.patch('beeswax_wrapper.core.access.get_beeswax_credentials') as f:
            self.dal.authenticate('username', 'password')
            self.assertEqual(f.called, False)
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal._call.called, True)


class TestBeeswaxDalCall(unittest.TestCase):

    def setUp(self):
        self.dal = BeeswaxDAL(None)
        self.dal.authenticate = mock.Mock()

    def test_success(self):
        self.dal._call = mock.Mock()  # definitely callable
        self.dal.call('method', [])
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal.authenticate.called, False)

    def test_recurse(self):
        self.dal._call = mock.Mock(side_effect=[BeeswaxRESTException, None])
        self.dal.call('method', [])
        # noinspection PyUnresolvedReferences
        self.assertEqual(self.dal.authenticate.called, True)


class TestGetBeeswaxDal(unittest.TestCase):

    def test_singleton(self):
        dal1 = get_beeswax_dal()
        dal2 = get_beeswax_dal()
        self.assertIs(dal1, dal2)
