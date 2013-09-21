#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""lost_in_space.py,v 0.1 2010/12/20 Markus Hackspacher cc by-sa
2013 Markus Hackspacher: pep8
"""

import random
import datetime
import sqlite3


class lost:
    def vergleiche(self, korrd, geraten, zufall):
        if geraten == zufall:
            print ("{0}: !!!Treffer!!!".format(korrd))
        if geraten < zufall:
            print ('{0}: Wert zu klein'.format(korrd))
        if geraten > zufall:
            print ('{0}: Wert zu groß'.format(korrd))

    def start(self):
        zufallX = int(random.random() * 100) + 1
        zufallY = int(random.random() * 100) + 1
        zufallZ = int(random.random() * 100) + 1
        runde = 0
        zahl = 0
        geratenX = 0
        geratenY = 0
        geratenZ = 0
        self.startzeit = datetime.datetime.now()
        print('\nStart Spiel\n')
        #print zufallX,zufallY,zufallZ

        while ((geratenX != zufallX) or (geratenY != zufallY) or
              (geratenZ != zufallZ)) and (runde < 20):
            runde += 1
            print ('\nRunde: {0}'.format(runde))
            try:
                zahl = int(input('\n Bitte {0} eingeben: '
                                 .format('X-Korrdinate')))
            except:
                print ('keine Zahl eingegeben, letzter Wert {0} wird '
                       'übernommen!'.format(geratenX))
                zahl = geratenX
            geratenX = zahl
            try:
                zahl = int(input('\n Bitte {0} eingeben: '
                                 .format('Y-Korrdinate')))
            except:
                print ('keine Zahl eingegeben, letzter Wert {0} wird '
                       'übernommen!'.format(geratenY))
                zahl = geratenY
            geratenY = zahl
            try:
                zahl = int(input('\n Bitte {0} eingeben: '
                                 .format('Z-Korrdinate')))
            except:
                print ('keine Zahl eingegeben, letzter Wert {0} wird '
                       'übernommen!'.format(geratenZ))
                zahl = geratenZ
            geratenZ = zahl
            self.vergleiche('X-Korrdinate', geratenX, zufallX)
            self.vergleiche('Y-Korrdinate', geratenY, zufallY)
            self.vergleiche('Z-Korrdinate', geratenZ, zufallZ)

        if (geratenX == zufallX) and (geratenY == zufallY) and \
           (geratenZ == zufallZ):
            self.gefunden(runde)
        else:
            print ('Der Astronaut hat kein Sauerstoff mehr!')
            print ('Spiel ist verloren')
            print ('Bitte eine beliebige Taste drücken. Dann werden die Lösungen verraten')
            self.pressAnyKey()
            print ('Die richtigen Zahlen wären gewesen: ')
            print ('X : ')
            print (zufallX)
            print ('\n')
            print ('Y : ')
            print (zufallY)
            print ('\n')
            print ('Z : ')
            print (zufallZ)
            print ('\n\n')
            self.pressAnyKey()
            

    def gefunden(self, runde):
        self.endzeit = datetime.datetime.now()
        endseqenz()
        print ('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print ('Herzlichen Glückwunsch')
        benoetige_zeit = self.endzeit - self.startzeit
        print ('Du hast den Astronaut nach {1}s in der {0} Runde gefunden!'
               .format(runde, benoetige_zeit.seconds))
        conn = sqlite3.connect('datenbank.sqlite')
        c = conn.cursor()
        try:
            c.execute('select * from bestenliste')
        except:
            c.execute("create table bestenliste (d date, name text,"
                      "runden INTEGER, zeit INTEGER, stufe INTEGER)")
        c.execute('select d from bestenliste where runden < ? ', (runde,))
        nach_runden = len(c.fetchall())
        c.execute('select d from bestenliste where zeit < ?',
                 (benoetige_zeit.seconds,))
        nach_zeit = len(c.fetchall())
        if nach_runden < 10 or nach_zeit < 10:
            name = input('Du darfst dich jetzt in die Bestenliste eintragen,'
                         'bitte deinen Namen eingeben:')
            today = datetime.date.today()
            c.execute("insert into bestenliste(d, name, runden, zeit, stufe)"
                      "values (?, ?, ?, ?, ?)", (today, name, runde,
                                                 benoetige_zeit.seconds, 100,))
            conn.commit()
        c.close()
        anzeigeliste()

    def __init__(self):
        self.start()

    def pressAnyKey(pressedKey):
        pressedKey = input('Bitte eine beliebige Taste drücken!\n')


def endseqenz():
    for i in range(40):
        print ('Herzlichen Glückwunsch!  Du hast den Astronaut gefunden.',)
    print


def spielregeln():
    print ('Finden sie den Astronaut im Korrdinatensystem,')
    print ('bei dem das Raumschiff während eines Asteroidensturm beschädigt')
    print ('wurde, und alle Systeme ausgefallen sind!')
    print ('Beeilen sie sich, sie haben nur 20 Runden Zeit!')
    print ('Die Korrdinaten sind im Bereich von 0 bis 100')


def anzeigeliste():
    conn = sqlite3.connect('datenbank.sqlite')
    c = conn.cursor()
    try:
        c.execute('select * from bestenliste order by runden limit 10')
    except:
        print ('keine Liste vorhanden')
        c.close()
        return
    print ('Bestenliste sortiert nach Runden:')
    nach_runden = c.fetchone()
    while nach_runden is not None:
        print ("Datum: {0} Name: {1} Runden: {2} Zeit: {3}s ".format(
            nach_runden[0], nach_runden[1], nach_runden[2], nach_runden[3]))
        nach_runden = c.fetchone()
    c.execute('select * from bestenliste order by zeit limit 10')
    print ('Bestenliste sortiert nach Zeit:')
    nach_runden = c.fetchone()
    while nach_runden is not None:
        print ("Datum: {0} Name: {1} Zeit: {3}s Runden: {2}  ". format(
            nach_runden[0], nach_runden[1], nach_runden[2], nach_runden[3]))
        nach_runden = c.fetchone()
    c.close()
