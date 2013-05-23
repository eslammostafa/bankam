from gi.repository import Gtk

class Logger(Gtk.ScrolledWindow):
    def __init__(self):
        Gtk.ScrolledWindow.__init__(self)
        self.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
        self._tree = Gtk.TreeView()
        self._model = Gtk.TreeStore(str)
        self._tree.set_model(self._model)
        renderer = Gtk.CellRendererText()
        column = Gtk.TreeViewColumn("Log", renderer, text=0)
        self._tree.append_column(column)
        self._iter = self._model.append(None, ['Application started.'])
        self.add(self._tree)
        self.show_all()

    def push(self, string):
        self._iter = self._model.append(None, [string])
        self.show_all()
