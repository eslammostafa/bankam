from gi.repository import Gtk, Gio, Gst, GObject, Notify
import time, subprocess

LABEL_MARKUP = "<span font_desc=\"64.0\">%02i:%02i</span>"
SOUND_FILE = "/usr/share/sounds/gnome/alerts/drip.ogg"

class Alert():
    def __init__(self):
        Notify.init('bankam')
        self._n = Notify.Notification.new('Bankam', 'Ding ! time is ticking.', '')

    def playSound(self):
        subprocess.call(["/usr/bin/canberra-gtk-play", "--file", "/usr/share/sounds/gnome/default/alerts/drip.ogg"])

    def run(self):
        self._n.show()
        self.playSound()
        time.sleep(15)
        self._n.close()

class Timer(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.set_orientation(Gtk.Orientation.VERTICAL)
        self.timeLabel = Gtk.Label('')
        self.time = 0
        self.alert = Alert()
        upperSpace = Gtk.Label('')
        bottomSpace = Gtk.Label('')
        rightSpace = Gtk.Label('')
        leftSpace = Gtk.Label('')
        center = Gtk.Box()
        center.pack_start(leftSpace, True, True, 0)
        center.pack_start(self.timeLabel, True, True, 0)
        center.pack_start(rightSpace, True, True, 0)
        self.pack_start(upperSpace, False, True, 24)
        self.pack_start(center, True, True, 0)
        self.pack_start(bottomSpace, True, True, 0)
        self.timeLabel.set_markup(LABEL_MARKUP % (0, 0))
        self.timeout_id = None

    def setTimer(self, count):
        self.clear()
        self.timeLabel.set_markup(LABEL_MARKUP % (count, 0))
        self.time = count * 60
        self.timeout_id = GObject.timeout_add(1000, self.countDown)

    def countDown(self):
        if self.time == 0:
            self.alert.run()
            return False
        else:
            self.time -= 1
            m, s = divmod(self.time, 60)
            h, m = divmod(m, 60)
            self.timeLabel.set_markup(LABEL_MARKUP % (m, s))
        return True

    def clear(self):
        if self.timeout_id:
            GObject.source_remove(self.timeout_id)
        self.timeLabel.set_markup(LABEL_MARKUP % (0, 0))
