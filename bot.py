#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import configparser

import sleekxmpp



class Client(sleekxmpp.ClientXMPP):
    def __init__(self, jid, password, parent):
        sleekxmpp.ClientXMPP.__init__(self, jid, password)
        self.parent = parent
        self.add_event_handler("session_start", self.start, threaded=True)
        self.add_event_handler('message', self.recv, threaded=True)

    def start(self, event):
        self.send_presence()
        self.get_roster()


    def recv(self, event):
        self.parent.add('a','b')
        print('Received ' + event['body'])

