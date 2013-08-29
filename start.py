#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""start.py,v 0.1 2010/12/20 Markus Hackspacher cc by-sa 
2013 Markus Hackspacher: pep8
"""

import lost_in_space
import gettext
gettext.install('message')

#Hauptteil
aktion = ''
while aktion != 'q':
    print ('=== Lost in Space ===')
    print ('s = Start')
    print ('r = Spielregeln')
    print ('e = Endsequenz')
    print ('b = Bestenliste')
    print ('q = Beenden')
    print ('Bitte Aktion eingeben: ')
    aktion = input()
    if aktion == 's':
        lost_in_space.lost()
    elif aktion == 'r':
        lost_in_space.spielregeln()
    elif aktion == 'e':
        lost_in_space.endseqenz()
    elif aktion == 'b':
        lost_in_space.anzeigeliste()
    elif aktion != 'q':
        print ('  !!!! Falsche Eingabe !!!!')
print ('Ende - Bis zum nächsten Mal')
