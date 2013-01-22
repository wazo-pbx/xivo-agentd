# -*- coding: utf-8 -*-

# Copyright (C) 2012-2013 Avencall
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

from __future__ import unicode_literals


class AbstractAgentCommand(object):

    def __init__(self):
        self.agent_id = None
        self.agent_number = None

    def by_id(self, agent_id):
        self.agent_id = int(agent_id)
        return self

    def by_number(self, agent_number):
        self.agent_number = unicode(agent_number)
        return self

    def _set_agent_id_and_number(self, agent_id, agent_number):
        if agent_id is not None:
            self.agent_id = int(agent_id)
        if agent_number is not None:
            self.agent_number = unicode(agent_number)


class AbstractNoDataCommand(object):

    def marshal(self):
        return None

    @classmethod
    def unmarshal(cls, msg):
        return cls()


class AbstractAgentIDCommand(object):

    def __init__(self, agent_id):
        self.agent_id = int(agent_id)

    def marshal(self):
        return {'agent_id': self.agent_id}

    @classmethod
    def unmarshal(cls, msg):
        return cls(msg['agent_id'])


class AbstractQueueIDCommand(object):

    def __init__(self, queue_id):
        self.queue_id = int(queue_id)

    def marshal(self):
        return {'queue_id': self.queue_id}

    @classmethod
    def unmarshal(cls, msg):
        return cls(msg['queue_id'])
