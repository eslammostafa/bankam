#!/usr/bin/env python
from distutils.core import *

setup(name='bankam',
      version='1.0',
      author='Eslam Mostafa',
      author_email='me@eslammostafa.com',
      license='GPL',
      description='Bankam is a timer that applies that pomodoro technique, designed for gnu/linux, written in python/gtk.',
      packages=['bankam'],
      scripts=['data/bankam',],
      data_files=[('/usr/share/icons/hicolor/scalable/apps', ['data/bankam.png']),
            ('/usr/share/applications',['data/bankam.desktop']),
            ('/usr/share/bankam', ['data/toolbar.ui']),
            ('/usr/share/bankam', ['data/gtk-style.css']),
        ],
      )
