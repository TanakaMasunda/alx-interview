#!/usr/bin/python3
""" prime game with 2 players drawing out a prime number and its multiples ,last to draw wins
"""


def isWinner(x, nums):
  """ You can assume n and x will not be larger than 10000
      Args:
          x: is the number of rounds
          nums: is an array of n
      Return: name of the player that won the most rounds and none if no winner is determined
   """
          
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
for x in range(1, 10):
     print(x, prime_game(x))