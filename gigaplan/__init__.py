#! /usr/bin/env python
# -*- coding: utf-8 -*-


from .request import Request
from .tasks import Tasks
from .projects import Projects
from .comments import Comments
from .tags import Tags
from .clients import Clients
from .users import Users


class Megaplan(object):
    def __init__(self, hostname, login, password):
        self.request = Request(hostname, login, password)
        self.tasks = Tasks(self.request)
        self.projects = Projects(self.request)
        self.comments = Comments(self.request)
        self.tags = Tags(self.request)
        self.clients = Clients(self.request)
        self.users = Users(self.request)
