import os

def getAppIcon():
    path = '/usr/share/icons/hicolor/scalable/apps/bankam.png'
    if not os.path.exists(path):
        path = os.getcwd()+'bankam.png'
    return path

def getDataFolder():
    path = '/usr/share/bankam/'
    if not os.path.exists(path):
        path = '../data/'
    return path

def getUserInterface():
    return getDataFolder()+"layout.ui"

def getStyleSheet():
    return getDataFolder()+"gtk-style.css"
