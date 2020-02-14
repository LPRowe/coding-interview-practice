# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 01:42:14 2020

@author: Logan Rowe

You are playing an RPG game. Currently your experience points (XP) total is equal to experience. To reach the next level your XP should be at least at threshold. If you kill the monster in front of you, you will gain more experience points in the amount of the reward.

Given values experience, threshold and reward, check if you reach the next level after killing the monster.

Example

For experience = 10, threshold = 15, and reward = 5, the output should be
reachNextLevel(experience, threshold, reward) = true;
For experience = 10, threshold = 15, and reward = 4, the output should be
reachNextLevel(experience, threshold, reward) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] integer experience

Guaranteed constraints:
3 ≤ experience ≤ 250.

[input] integer threshold

Guaranteed constraints:
5 ≤ threshold ≤ 300.

[input] integer reward

Guaranteed constraints:
2 ≤ reward ≤ 65.

[output] boolean

true if you reach the next level, false otherwise.
"""

def reachNextLevel(experience, threshold, reward):
    return reward>=threshold-experience
