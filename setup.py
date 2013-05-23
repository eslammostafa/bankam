#!/usr/bin/python

from DistUtilsExtra.auto import setup

APP_NAME = "bankam"
VERSION = '2.0'
AUTHOR = "Eslam Mostafa"
AUTHOR_EMAIL = 'me@eslammostafa.com'
LICENSE = "GPL"
DESC = 'Bankam is a timer that applies that pomodoro technique, designed for gnu/linux, written in python/gtk.'

setup(name=APP_NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      license=LICENSE,
      description=DESC,
      packages=['bankam'],
      scripts=['bin/bankam',],
      data_files=[('/usr/share/icons/hicolor/scalable/apps', ['data/bankam.png']),
            ('/usr/share/applications',['data/bankam.desktop']),
            ('/usr/share/bankam', ['data/layout.ui']),
            ('/usr/share/bankam', ['data/gtk-style.css']),
        ],
      )
