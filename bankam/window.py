from gi.repository import Gtk, Gio, Gdk
import utils
import os
import sys

from timer import Timer

class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, title="Bankam",
                                      application=app,
                                      hide_titlebar_when_maximized=True)
        self.set_default_size(640, 480)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file(utils.getAppIcon())
        self.timer = Timer()
        self._setupView()
        self.timer.start()

        css = Gtk.CssProvider()
        css.load_from_path(utils.getStyleSheet())

        context = Gtk.StyleContext()
        context.add_provider_for_screen(Gdk.Screen.get_default(),
                                        css,
                                        Gtk.STYLE_PROVIDER_PRIORITY_USER)

    def _setupView(self):
        builder = Gtk.Builder()
        builder.add_from_file(utils.getUserInterface())
        layout = builder.get_object("layout")
        container = builder.get_object("container")
        revealer = Gtk.Revealer()
        revealer.add(self.timer.logger)
        revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_LEFT)
        revealer.set_transition_duration(1000)
        container.pack_end(revealer, False, False, 0)
        self.add(layout)
        self.show_all()
        revealer.set_reveal_child(True)
