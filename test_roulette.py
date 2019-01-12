#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 00:43:30 2019

@author: ultra_jason
"""

import unittest

import roulette

class TestRouletteModule(unittest.TestCase):

    def test_following_spins(self):
        # a test history of roulette spins
        input = [1, 3, 1, 5, 1]
        expected_output = {1: [3, 5], 3: [1], 5: [1]}
        self.assertEqual(roulette.following_spins(input), expected_output)

    def test_spin_counts(self):
        input = [3, 5]
        expected_output = {3: 1, 5: 1}
        self.assertEqual(roulette.spin_counts(input), expected_output)

    def test_spin_probablities(self):
        input = {3: 1, 5: 1}
        expected_output = {3: 0.5, 5: 0.5}
        self.assertEqual(roulette.spin_probabilities(input), expected_output)

    def test_following_spins_probabilities(self):
        input = {1: [3, 5], 3: [1], 5: [1]}
        expected_output = {1: {3: 0.5, 5: 0.5}, 3: {1: 1.0}, 5: {1: 1.0}}
        self.assertEqual(roulette.following_spins_probabilities(input), expected_output)

    def test_conditional_roulette_probs(self):
        input = [1, 3, 1, 5, 1]
        expected_output = {1: {3: 0.5, 5: 0.5}, 3: {1: 1.0}, 5: {1: 1.0}}
        self.assertEqual(roulette.conditional_roulette_probs(input), expected_output)
        
if __name__ == '__main__':
    unittest.main()