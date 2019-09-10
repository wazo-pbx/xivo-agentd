# Copyright 2012-2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

import unittest
from mock import Mock, patch
from wazo_agentd.ami.facade import FacadeAMIClient


class TestFacade(unittest.TestCase):

    @patch('wazo_agentd.ami.client.ReconnectingAMIClient')
    def test_new(self, ReconnectingAMIClient):
        facade = FacadeAMIClient('example.org', '1', '2')
        facade._ami_client = Mock()

        facade.db_del('foo', 'bar')

        ReconnectingAMIClient.assert_called_once_with('example.org', 5038, facade._login)
        self.assertTrue(facade._ami_client.execute.called)

    @patch('wazo_agentd.ami.client.ReconnectingAMIClient', Mock())
    def test_close_call_ami_client_disconnect(self):
        facade = FacadeAMIClient('example.org', '1', '2')
        facade._ami_client = Mock()

        facade.close()

        facade._ami_client.disconnect.assert_called_once_with()