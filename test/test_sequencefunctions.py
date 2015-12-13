# -*- coding: utf-8 -*-

# Copyright (C) <2015> Markus Hackspacher

# This file is part of lost_in_space.

# lost_in_space is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# lost_in_space is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with lost_in_space.  If not, see <http://www.gnu.org/licenses/>.

import unittest
import lost_in_space


class TestSequenceFunctions(unittest.TestCase):

    @staticmethod
    def test_spielregel():
        """Test rules"""
        lost_in_space.spielregeln()

    @staticmethod
    def test_endseqenz():
        """Test endsequenze"""
        lost_in_space.endseqenz()

    @staticmethod
    def test_anzeigeliste():
        """Test list"""
        lost_in_space.anzeigeliste()

    def test_numberguessing3(self):
        """Test 1 numberguessing"""
        a = lost_in_space.numberguessing(3, 100)
        self.assertEqual(a.bet([a.game[0], a.game[1] - 1, a.game[2] + 1]),
                         ['=', '<', '>'])
        a.evaltest = ['eval', 'too high', 'too low']
        self.assertEqual(a.bet(a.game), ['eval', 'eval', 'eval'])
        self.assertEqual(a.bet(z - 1 for z in a.game),
                         ['too low', 'too low', 'too low'])
        self.assertEqual(a.bet(z + 1 for z in a.game),
                         ['too high', 'too high', 'too high'])
        a.evaltest = ['=', '>', '<']

    def test_numberguessing2(self):
        """Test 2 numberguessing"""
        a = lost_in_space.numberguessing(2, 100)
        self.assertEqual(a.bet([a.game[0], a.game[1] - 1]), ['=', '<'])
        self.assertEqual(a.bet([a.game[0], a.game[1] + 1]), ['=', '>'])
        a.evaltest = ['eval', 'too high', 'too low']
        self.assertEqual(a.bet(a.game), ['eval', 'eval'])
        self.assertEqual(a.bet(z - 1 for z in a.game), ['too low', 'too low'])
        self.assertEqual(a.bet(z + 1 for z in a.game),
                         ['too high', 'too high'])
