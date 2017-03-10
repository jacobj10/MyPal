import configparser
import os

from gi.repository import Gtk, GObject, Gdk

from bot import Client
from message_list import MessageList

gtk_builder_file = os.path.splitext(__file__)[0] + '.ui'

class Pal(  object):
    def __init__(self, jid, password):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(gtk_builder_file)

        self.window = self.builder.get_object('main_window')
        self.window.connect('destroy', self.signal_window_destroy)

        self.message_list = MessageList(self.builder.get_object('conversation_list'))

        self.xmpp = Client(jid, password, self.message_list)
        self.xmpp.register_plugin('xep_0030') # Service Discovery
        self.xmpp.register_plugin('xep_0199') # XMPP Ping


        self.window.show()
        self.xmpp.connect()
        self.xmpp.process(block=False)


    def signal_window_destroy(self, _):
        self.xmpp.disconnect(wait=True)
        self.window.destroy()
        Gtk.main_quit()

    def stop(self):
        print('disconnecting')
        self.xmpp.disconnect(wait=True)
        print('disconnected')

    def send(self, msg, recipient):
        print('sending')
        self.xmpp.send_message(mto=recipient,
                         mbody=msg,
                         mtype='chat')
        self.message_list.add(recipient, msg)
        print('sent')



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('pal.conf')
    jid = config['info']['username']
    password = config['info']['password']
    pal = Pal(jid, password)
    Gtk.main()
