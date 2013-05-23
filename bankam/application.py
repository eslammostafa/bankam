from gi.repository import Gtk, Gio, Gdk
from window import Window
import sys

class Bankam(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = Window(self)
        win.present()
