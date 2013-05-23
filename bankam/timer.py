from gi.repository import Gtk, Gio, Gst, GObject, Notify
import time, subprocess

from logger import Logger
import utils

LABEL_MARKUP = "<span font_desc=\"64.0\">%02i:%02i</span>"
SOUND_FILE = "/usr/share/sounds/gnome/alerts/drip.ogg"
POMODORO_COUNT = 25 #Pomodoro session in minutes
SHORT_BREAK_COUNT = 5 #Short break session in minutes
LONG_BREAK_COUNT = 15 #Long break session in minutes

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

class Timer():
    def __init__(self):
        self.counter = 0 #goes from 0 up to 7
        self.time = 0
        self.timeout_id = 0
        self.logger = Logger()
        builder = Gtk.Builder()
        builder.add_from_file(utils.getUserInterface())
        self.timeLabel = builder.get_object('timeLabel')

    def start(self):
        if(self.counter % 2 == 0): #pomodoro
            session = POMODORO_COUNT
            self.counter += 1
        elif(self.counter == 7): #long break
            session = LONG_BREAK_COUNT
            self.counter = 0
        else: #short break
            session = SHORT_BREAK_COUNT
            self.counter += 1
        print(self.counter, session)
        self.setTimer(session, 0)
        self.time = session * 60
        self.timeout_id = GObject.timeout_add(1000, self.countDown)

    def setTimer(self, m, s):
        self.timeLabel.set_text(str(m)+":"+str(s))
        self.timeLabel.show()

    def countDown(self):
        if self.time == 0:
            self.alert.run()
            return False
        else:
            self.time -= 1
            m, s = divmod(self.time, 60)
            h, m = divmod(m, 60)
            self.setTimer(m,s)
        return True

    def clear(self):
        if self.timeout_id:
            GObject.source_remove(self.timeout_id)
            self.setTimer('00','00')
