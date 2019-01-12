#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 17:44:46 2019

@author: jason
"""
def conditional_roulette_probs(history):
    """Given a history of roulette spins (as list of integer values)
    return a dictionary where the keys are numbers on the roulette wheel, and
    the values are dictionaries mapping numbers on the wheel to probabilities,
    such that `d[n1][n2]` is an estimate of the probability that the next spin
    will land on n2, given that the previous spin landed on n1.

    Example: 
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5}, 
       3: {1: 1.0},
       5: {1: 1.0}
      }
    """
    pass

def next_spins(history):
    '''Given a history of roulette spins, return a dictionary where the keys
    are spins and the values are lists of spins immediately following.
    
    Example:
    print(next_spins([1, 3, 1, 5, 1]))
    > {1: [3, 5], 3: [1], 5: [1]}
    '''
    next_spins = {}
    for index, spin in enumerate(history[:-1]):
        # initialize list of next spins if not exist
        if spin not in list(next_spins):
            next_spins[spin] = []
        next_spins[spin].append(history[index + 1])

    return next_spins

def next_spin_probabilities(next_spins):
    '''Given a dictionary where keys are spins and values are lists of spins
    immediately following, return a dictionary where keys are spins and values
    are dictionaries of next spins and their probabilities.
    
    Example:
    print(next_spin_probabilites({1: [3, 5], 3: [1], 5: [1]}))
    > {1: {3: 0.5, 5: 0.5}, 3: {1: 1.0}, 5: {1: 1.0}}
    '''
    next_spin_probabilities = {}
    
    for spin in list(next_spins):
        total_events = len(next_spins[spin])
        spin_probabilites = {}
        for next_spin in next_spins[spin]:
            if next_spin not in list(spin_probabilities):
                spin_probabilities