from gi.repository import Gtk
import time

class Logger(Gtk.ScrolledWindow):
    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self._tree = Gtk.TreeView()
        self._model = Gtk.TreeStore(str, str)
        self._tree.set_model(self._model)
        renderer = Gtk.CellRendererText()
        actionColumn = Gtk.TreeViewColumn("Action", renderer, text=0)
        timeColumn = Gtk.TreeViewColumn("Time", renderer, text=1)
        self._tree.append_column(actionColumn)
        self._tree.append_column(timeColumn)
        self._iter = self._model.append(None, ['Application started', time.strftime("%H:%M")])
        self.add(self._tree)
        self.show_all()

    def push(self, string):
        self._iter = self._model.append(None, [string, time.strftime("%H:%M")])
        self.show_all()
