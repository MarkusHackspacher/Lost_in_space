#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""lost_in_space.py,v 0.1 2010/12/20 Markus Hackspacher cc by-sa
2013 Markus Hackspacher: pep8
2014 Markus Hackspacher: Unittest
2015 Markus Hackspacher: pep8
"""

import random
import sqlite3
import datetime


class NumberGuessing(object):
    """
    Class numberguessing
    """

    def __init__(self, numberof, area):
        """
        Initialisation of numberguessing
        numberof = How many number you want for guessing
        area = select the highest number to guessing
        """
        self.game = []
        self.evaltest = ['=', '>', '<']
        for z in range(numberof):
            self.game.append(int(random.random() * area) + 1)

    def bet(self, numberbets):
        """
        numberbets = number of your bet
        return = evaluation
        """
        evaluation = []
        for numbergame, numberbet in zip(self.game, numberbets):
            if numberbet == numbergame:
                evaluation.append(self.evaltest[0])
            elif numberbet > numbergame:
                evaluation.append(self.evaltest[1])
            elif numberbet < numbergame:
                evaluation.append(self.evaltest[2])
        return evaluation

    def __repr__(self):
        return "<Game numbers {}>".format(self.game)


class LostInSpace(object):
    """game class
    """

    def __init__(self):
        """initial game

        :return:
        """
        self.coordinate = ['X', 'Y', 'Z']
        self.numberguess = NumberGuessing(3, 100)
        self.numberguess.evaltest = ['!!!Treffer!!!',
                                     'Wert zu groß',
                                     'Wert zu klein']
        self.start()

    def start(self):
        """start"""
        runde = 0
        geraten = [0, 0, 0]
        self.startzeit = datetime.datetime.now()
        print('\nStart Spiel\n')

        while (geraten != self.numberguess.game) and (runde < 20):
            runde += 1
            print('\nRunde: {0}'.format(runde))
            for z in range(3):
                try:
                    zahl = int(input('\n Bitte {0}-Korrdinate eingeben: '
                                     .format(self.coordinate[z])))
                except ValueError:
                    print('keine Zahl eingegeben, letzter Wert {0} wird '
                          'übernommen!'.format(geraten[z]))
                    zahl = geraten[z]
                geraten[z] = zahl
            for coord, vergleiche in zip(self.coordinate,
                                         self.numberguess.bet(geraten)):
                print('{0}-Korrdinate: {1}'.format(coord, vergleiche))

        if (geraten == self.numberguess.game):
            self.astronautfound(runde)
        else:
            print('Der Astronaut hat kein Sauerstoff mehr!')
            print('Spiel ist verloren')
            print('Bitte eine beliebige Taste drücken.'
                  ' Dann werden die Lösungen verraten')
            self.press_any_key()
            print('Die richtigen Zahlen wären gewesen: ')
            for coord, number in zip(self.coordinate, self.numberguess.game):
                print('{0}-Korrdinate: {1}'.format(coord, number))
            self.press_any_key()

    def astronautfound(self, runde):
        """astronaut is found"""
        self.endzeit = datetime.datetime.now()
        endseqenz()
        print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print('Herzlichen Glückwunsch')
        benoetige_zeit = self.endzeit - self.startzeit
        print('Du hast den Astronaut nach {1}s in der {0} Runde gefunden!'
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

    @staticmethod
    def press_any_key():
        """Wait for press enter

        :return:
        """
        input('Bitte eine beliebige Taste drücken!\n')


def endseqenz():
    """Game sequence"""
    print('Herzlichen Glückwunsch!  Du hast den Astronaut gefunden. \n' * 20)
    print()


def spielregeln():
    """Rules"""
    print('Finden sie den Astronaut im Korrdinatensystem,')
    print('bei dem das Raumschiff während eines Asteroidensturm beschädigt')
    print('wurde, und alle Systeme ausgefallen sind!')
    print('Beeilen sie sich, sie haben nur 20 Runden Zeit!')
    print('Die Korrdinaten sind im Bereich von 0 bis 100')


def anzeigeliste():
    """Best list"""
    conn = sqlite3.connect('datenbank.sqlite')
    c = conn.cursor()
    try:
        c.execute('select * from bestenliste order by runden limit 10')
    except:
        print('keine Liste vorhanden')
        c.close()
        return
    print('Bestenliste sortiert nach Runden:')
    nach_runden = c.fetchone()
    while nach_runden is not None:
        print("Datum: {0} Name: {1} Runden: {2} Zeit: {3}s ".format(
            nach_runden[0], nach_runden[1], nach_runden[2], nach_runden[3]))
        nach_runden = c.fetchone()
    c.execute('select * from bestenliste order by zeit limit 10')
    print('Bestenliste sortiert nach Zeit:')
    nach_runden = c.fetchone()
    while nach_runden is not None:
        print("Datum: {0} Name: {1} Zeit: {3}s Runden: {2}  ". format(
            nach_runden[0], nach_runden[1], nach_runden[2], nach_runden[3]))
        nach_runden = c.fetchone()
    c.close()

if __name__ == '__main__':
    print('The game start with "python start.py"')
