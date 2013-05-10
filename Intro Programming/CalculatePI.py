#  File: CalculatePI.py

#  Description: calculate the value of PI statistically

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E

#  Unique Number: 52680

#  Date Created: 15 Oct 2012

#  Date Last Modified: 15 Oct 2012

from math import pi as actualPI
import random

def computePI(numThrows):
  '''computes the statistical value of pi'''

  insideCircle = 0
  for throw in range(numThrows):
    xPos = random.uniform(-1, 1)
    yPos = random.uniform(-1, 1)
    if (xPos ** 2 + yPos ** 2) ** 0.5 <= 1: insideCircle += 1
  return 4 * insideCircle / numThrows

def main():
  '''main function to run computerPI function multiple times'''

  #print header for table
  print("Computation of PI using Random Numbers", end = '\n\n')

  #perform computations
  for x in range(6):
    throws = 100 * 10 ** x
    calcPI = computePI(throws)
    print("num = %d \t Calculated PI = %f    Difference = %+f" %(throws, calcPI, calcPI - actualPI))

  print('\n', "Difference = Calculated PI - math.pi", sep = '')
    
main()
