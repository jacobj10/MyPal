import configparser

from bot import Client

class Pal(object):
    def __init__(self, jid, password):
        ui = 'TODO'
        self.xmpp = Client(jid, password, self)
        self.xmpp.register_plugin('xep_0030') # Service Discovery
        self.xmpp.register_plugin('xep_0199') # XMPP Ping
        self.xmpp.connect()
        self.xmpp.process(block=False)

    def stop(self):
        print('disconnecting')
        self.xmpp.disconnect(wait=True)
        print('disconnected')

    def send(self, msg, recipient):
        print('sending')
        self.xmpp.send_message(mto=recipient,
                         mbody=msg,
                         mtype='chat')
        print('sent')



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('pal.conf')
    jid = config['info']['username']
    password = config['info']['password']
    pal = Pal(jid, password)
    while True:
        x = input('shell: ')
        if x == 'exit':
            pal.stop()
            break
        elif x == 'send':
            to = input('to: ')
            msg = input('msg: ')
            pal.send(msg, to)
