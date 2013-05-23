from gi.repository import Gtk, Gio, Gdk
from timer import Timer
from logger import Logger
import os
import sys

POMODORO_COUNT = 25
SHORT_BREAK_COUNT = 5
LONG_BREAK_COUNT = 15

class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.ApplicationWindow.__init__(self, title="Baknam",
                                      application=app,
                                      hide_titlebar_when_maximized=True)
        self.set_default_size(640, 480)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_icon_from_file(self.getIconPath())
        
        css = Gtk.CssProvider()
        css.load_from_path(self.getDataFolder()+'gtk-style.css')

        context = Gtk.StyleContext()
        context.add_provider_for_screen(Gdk.Screen.get_default(),
                                        css,
                                        Gtk.STYLE_PROVIDER_PRIORITY_USER)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        container = Gtk.HBox()
        self.logger = Logger()
        revealer = Gtk.Revealer()
        revealer.add(self.logger)
        revealer.set_transition_type(Gtk.RevealerTransitionType.SLIDE_LEFT)
        revealer.set_transition_duration(1000)
        builder = Gtk.Builder()
        builder.add_from_file(self.getDataFolder()+'toolbar.ui')
        self.toolbar = builder.get_object('toolbar')
        self.pomodoroBtn = builder.get_object('pomodoroBtn')
        self.shortBreakBtn = builder.get_object('shortBreakBtn')
        self.longBreakBtn = builder.get_object('longBreakBtn')
        self.clearBtn = builder.get_object('clearBtn')
        eventbox = Gtk.EventBox()
        self.timer = timer = Timer()
        eventbox.add(timer)

        container.pack_start(eventbox, True, True, 0)
        container.pack_start(Gtk.VSeparator(), False, False, 0)
        container.pack_start(revealer, False, False, 0)
        box.pack_start(self.toolbar, False, False, 0)
        box.pack_start(container, True, True, 0)
        self.add(box)

        self.show_all()
        revealer.set_reveal_child(True)
        eventbox.grab_focus()

        self.pomodoroBtn.connect('clicked', self._onPomodoro)
        self.shortBreakBtn.connect('clicked', self._onShortBreak)
        self.longBreakBtn.connect('clicked', self._onLongBreak)
        self.clearBtn.connect('clicked', self._onClear)

    def _onPomodoro(self, btn):
        btn.set_sensitive(False)
        self.shortBreakBtn.set_sensitive(True)
        self.longBreakBtn.set_sensitive(True)
        self.timer.setTimer(POMODORO_COUNT)
        self.logger.push("Pomodoro...")

    def _onShortBreak(self, btn):
        btn.set_sensitive(False)
        self.pomodoroBtn.set_sensitive(True)
        self.longBreakBtn.set_sensitive(True)
        self.timer.setTimer(SHORT_BREAK_COUNT)
        self.logger.push("Short break...")

    def _onLongBreak(self, btn):
        btn.set_sensitive(False)
        self.pomodoroBtn.set_sensitive(True)
        self.shortBreakBtn.set_sensitive(True)
        self.timer.setTimer(LONG_BREAK_COUNT)
        self.logger.push("Long break...")

    def _onClear(self, btn):
        self.timer.clear()
        self.logger.push("Clear")

    def getIconPath(self):
        path = '/usr/share/icons/hicolor/scalable/apps/domore.png'
        if not os.path.exists(path):
            path = os.getcwd()+'domore.png'
        return path

    def getDataFolder(self):
        path = '/usr/share/domore/'
        if not os.path.exists(path):
            path = '../data/'
        return path

class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self)

    def do_activate(self):
        win = Window(self)
        win.present()

if __name__ == '__main__':
    app = App()
    sys.exit(app.run(sys.argv))
