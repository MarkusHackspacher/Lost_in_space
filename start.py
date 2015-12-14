#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""start.py,v 0.1 2010/12/20 Markus Hackspacher cc by-sa
2013 Markus Hackspacher: pep8
2015 Markus Hackspacher: pep8
"""

import sys
import gettext
import webbrowser

import lost_in_space

gettext.install('message')


def visithomepage():
    """Open website

    :return: none
    """
    webbrowser.open_new_tab("http://ratgeber---forum.de/wbb3/"
                            "index.php?page=Thread&threadID=4826")


def ende():
    """End sequence and game exit
    """
    print('Auf Wiedersehen und bis zum nächsten Mal')
    sys.exit(0)


def handle_menu(menu):
    """ Das Menü wurde gemäß diesem Tutorial erstellt:
    github.com/Lysander/snippets/blob/master/Python/
        python-misc/simplemenus/TUTORIAL.md
    """
    while True:
        print('=== Lost in Space ===')
        for index, item in enumerate(menu, 1):
            print("{0}  {1}".format(index, item[0]))
        try:
            choice = int(input("Ihre Wahl? ")) - 1
        except ValueError:
            choice = -1
        if 0 <= choice < len(menu):
            menu[choice][1]()
        else:
            print("Bitte nur Zahlen im Bereich 1 - {} eingeben".format(
                len(menu)))

menu = [
    ["Spielstart", lost_in_space.LostInSpace],
    ["Spielregeln", lost_in_space.spielregeln],
    ["Endsequenz", lost_in_space.endseqenz],
    ["Bestenliste", lost_in_space.anzeigeliste],
    ["open Homepage", visithomepage],
    ["Beenden", ende]
]

if __name__ == '__main__':
    handle_menu(menu)
