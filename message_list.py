from gi.repository import Gtk, GObject, Gdk

gtk_builder_file = 'pal.ui'

class MessageList(object):
    def __init__(self, tv):
        self.treeview_message = tv
        self.tv_model = Gtk.ListStore(str, str, str)

        for text in ['Message', 'Time', 'Test']:
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(text, renderer, text=0)
            self.treeview_message.append_column(column)
        self.treeview_message.set_model(self.tv_model)
        self.treeview_message.show_all()

    def add(self, _from, content):
        print(1)
        self.tv_model.append((_from, content, 'hello'))
        print(2)
