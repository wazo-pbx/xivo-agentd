# -*- coding: utf-8 -*-

# Copyright (C) 2013 Avencall
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

import unittest
from mock import Mock
from xivo_agent.ctl import error
from xivo_agent.service.steps import CheckExtensionIsNotInUseStep


class TestCheckExtensionIsNotInUseStep(unittest.TestCase):

    def test_execute_when_not_in_use(self):
        command = Mock()
        response = Mock()
        response.error = None
        blackboard = Mock()
        blackboard.extension = '1001'
        blackboard.context = 'default'

        agent_status_dao = Mock()
        agent_status_dao.is_extension_in_use.return_value = False

        step = CheckExtensionIsNotInUseStep(agent_status_dao)
        step.execute(command, response, blackboard)

        agent_status_dao.is_extension_in_use.assert_called_once_with(blackboard.extension, blackboard.context)
        self.assertEqual(response.error, None)

    def test_execute_when_in_use(self):
        command = Mock()
        response = Mock()
        response.error = None
        blackboard = Mock()
        blackboard.extension = '1001'
        blackboard.context = 'default'

        agent_status_dao = Mock()
        agent_status_dao.is_extension_in_use.return_value = True

        step = CheckExtensionIsNotInUseStep(agent_status_dao)
        step.execute(command, response, blackboard)

        agent_status_dao.is_extension_in_use.assert_called_once_with(blackboard.extension, blackboard.context)
        self.assertEqual(response.error, error.ALREADY_IN_USE)
