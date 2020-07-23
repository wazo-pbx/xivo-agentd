# Copyright 2019 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import assert_that, calling, has_properties, is_

from wazo_agentd_client.error import AgentdClientError, UNAUTHORIZED
from xivo_test_helpers.hamcrest.raises import raises

from .helpers.base import BaseIntegrationTest, UNKNOWN_UUID
from .helpers import fixtures


class TestAgents(BaseIntegrationTest):

    asset = 'base'

    def test_authentication(self):
        agentd_client = self.make_agentd(token=UNKNOWN_UUID)
        assert_that(
            calling(agentd_client.agents.get_agent_statuses),
            raises(AgentdClientError, has_properties(error=UNAUTHORIZED)),
        )

    @fixtures.user_line_extension(exten='1001', context='default')
    @fixtures.agent()
    def test_login_logoff(self, user_line_extension, agent):

        self.agentd.agents.login_agent(
            agent['id'], user_line_extension['exten'], user_line_extension['context'],
        )

        status = self.agentd.agents.get_agent_status(agent['id'])
        assert_that(status.logged, is_(True))

        self.agentd.agents.logoff_agent(agent['id'])

        status = self.agentd.agents.get_agent_status(agent['id'])
        assert_that(status.logged, is_(False))

    @fixtures.user_line_extension(exten='1001', context='default', name_line='abcdef')
    @fixtures.agent(number='1234')
    def test_agent_status(self, user_line_extension, agent):

        self.agentd.agents.login_agent(
            agent['id'], user_line_extension['exten'], user_line_extension['context'],
        )

        status = self.agentd.agents.get_agent_status(agent['id'])
        assert_that(
            status,
            has_properties(
                {
                    'id': agent['id'],
                    'logged': True,
                    'context': 'default',
                    'extension': '1001',
                    'number': '1234',
                    'paused': False,
                    'paused_reason': None,
                    'state_interface': 'PJSIP/abcdef',
                }
            ),
        )
