#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 11 00:48:06 2019

@author: ultra_jason
"""

def conditional_roulette_probs(history):
    '''Return a dictionary where the keys are numbers on the roulette wheel,
    and the values are dictionaries mapping numbers on the wheel to
    probabilities, such that `d[n1][n2]` is an estimate of the probability that
    the next spin will land on n2, given that the previous spin landed on n1.

    Example: 
    conditional_roulette_probs([1, 3, 1, 5, 1])
    > {1: {3: 0.5, 5: 0.5}, 
       3: {1: 1.0},
       5: {1: 1.0}
      }
    '''
    return following_spins_probabilities(following_spins(history))

def following_spins_probabilities(following_spins_history):
    '''Return dictionary where keys are unique spin values and values are
    dictionaries where keys are unique values of following spins and values are
    the probabilities of the key follow-up spin occurring.
    
    Example
    print(following_spins_probabilities({1: [3, 5], 3: [1], 5: [1]}))
    > {1: {3: 0.5, 5: 0.5}, 3: {1: 1.0}, 5: {1: 1.0}}
    '''
    return {spin: spin_probabilities(spin_counts(following_spins_history[spin])) for spin in list(following_spins_history)}

def spin_probabilities(spin_counts):
    '''Given list of spin values and counts, return dictionary where keys are
    spin values and values are probabilities for the spin value to occur.
    
    Example
    print(spin_probabilities({3: 1, 5: 1}))
    > {3: 0.5, 5: 0.5}
    '''
    total_occurrences = sum(spin_counts.values())
    return {spin: spin_counts[spin]/total_occurrences for spin in spin_counts.keys()}
    
def spin_counts(following_spins):
    '''Given list of following spins, return dictionary where keys are unique
    spin values and values are counts of occurrences of those spin values.
    
    Example
    print(spin_counts([3, 5]))
    > {3: 1, 5: 1}
    '''
    
    return {spin: sum([value == spin for value in following_spins]) for spin in set(following_spins)}

def following_spins(history):
    '''Return dictionary where keys are unique spin values and values are lists
    of spins which immediately follow instances of key being spun.
    
    Example
    print(following_spins([1, 3, 1, 5, 1]))
    > {1: [3, 5], 3: [1], 5: [1]}
    '''
    following_spins = {}
    for index, spin in enumerate(history[:-1]):
        # initialize list of next spins if not exist
        if spin not in list(following_spins):
            following_spins[spin] = []
        # append the following spin to list of following spins for current spin
        # value
        following_spins[spin].append(history[index + 1])
    return following_spins
