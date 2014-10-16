#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""start.py,v 0.1 2010/12/20 Markus Hackspacher cc by-sa
2013 Markus Hackspacher: pep8
"""

import sys
import gettext

import lost_in_space

gettext.install('message')


def ende():
    print ('Auf Wiedersehen und bis zum nächsten Mal')
    sys.exit(0)


def handle_menu(menu):
    """ Das Menü wurde gemäß diesem Tutorial erstellt:
    github.com/Lysander/snippets/blob/master/Python/
        python-misc/simplemenus/TUTORIAL.md
    """
    while True:
        print ('=== Lost in Space ===')
        for index, item in enumerate(menu, 1):
            print("{}  {}".format(index, item[0]))
        try:
            choice = int(input("Ihre Wahl? ")) - 1
        except:
            choice = -1
        if 0 <= choice < len(menu):
            menu[choice][1]()
        else:
            print("Bitte nur Zahlen im Bereich 1 - {} eingeben".format(
                len(menu)))

menu = [
    ["Spielstart", lost_in_space.lost],
    ["Spielregeln", lost_in_space.spielregeln],
    ["Endsequenz", lost_in_space.endseqenz],
    ["Bestenliste", lost_in_space.anzeigeliste],
    ["Beenden", ende]
]

handle_menu(menu)
