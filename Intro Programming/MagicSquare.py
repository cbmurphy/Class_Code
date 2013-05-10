#  File: MagicSquare.py

#  Description: Check if a square of numbers is "magic"

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E

#  Unique Number: 52680

#  Date Created: 8 Nov 2012

#  Date Last Modified: 12 Nov 2012

def isMagic(b):
  '''function to check validity of a magic square'''

  #initialize variables
  diag1 = 0
  diag2 = 0
  n = len(b)
  column = [0] * n
  magicNum = sum(b[0])

  #loop over square
  for i in range(len(b)):
    row = sum(b[i])
    if row != magicNum: #check row
      return False
    diag1 += b[i][i]
    diag2 += b[i][len(b)-i-1]
    for j in range(len(b[i])):
      column[i] += b[i][j]
  print(column)
      
  if diag1 != diag2 != magicNum: #check diagonals
    return False
  
  for col in column: #check columns
    if col != magicNum:
      return False

  return True

def main():
  '''main function for input from file and output of results'''

  inFile = 'squares.txt' #input("Enter name of input file: ")
  outFile = 'out.txt' #input("Enter name of output file: ")
  if inFile == outFile:
    print("The file names are the same!")
    return 0
  f = open(inFile,'r')
  out = open(outFile,'w')

  numSquares = int(f.readline().rstrip('\n'))
  out.write('%d\n' %numSquares)

  for square in range(numSquares):
    f.readline() #delete space between squares
    out.write('\n')
    lenSquare = int(f.readline().rstrip('\n')) #size of each square
    square = []
    line = []
    for i in range(lenSquare):
      line.append(f.readline())
      square.append([int(x) for x in line[i].rstrip('\n').split('  ')])
    if isMagic(square):
      validity = 'valid'
    else:
      validity = 'invalid'
    out.write('%d %s\n' %(lenSquare, validity))
    for row in line:
      out.write(row)
  print("The output has been written to %s" %outFile)

  f.close()
  out.close() 
  
main()
