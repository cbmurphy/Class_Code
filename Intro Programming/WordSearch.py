#  File: WordSearch.py

#  Description: Find words in a word search

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E 

#  Unique Number: 52680

#  Date Created: 10 Nov 2012

#  Date Last Modified: 16 Nov 2012

def revStr(str):
  if len(str) <= 1: return str
  return str[-1] + revStr(str[:-1])

def findWords(orgSquare, foundWords, dims):
  '''function to find position of key words in square of words'''
  height = int(dims[0])
  width = int(dims[1])

  #find words in horizontal rows
  square = orgSquare[:]
  for word in foundWords:
    for i in range(height):
      pos = square[i].find(word)
      if pos >= 0:
        foundWords[word] = (i + 1, pos + 1)
        continue
      posRev = square[i].find(revStr(word))
      if posRev >= 0:
        foundWords[word] = (i + 1, posRev + len(word))

  #transpose matrix
  square = []
  for i in range(width):
    a = []
    for j in range(height):
      a.append(orgSquare[j][i])
    square.append(''.join(a))
    
  #find words in transposed matrix (vertical words)
  for word in [x for x in foundWords if foundWords[x] == (0, 0)]:
    for i in range(width):
      pos = square[i].find(word)
      if pos >= 0:
        foundWords[word] = (pos + 1, i + 1)
      else:
        posRev = square[i].find(revStr(word))
        if posRev >= 0:
          foundWords[word] = (posRev + len(word), i +1)

  #find words in diagonals
  square = orgSquare[:]
  for word in [x for x in foundWords if foundWords[x] == (0, 0)]:
    lenWord = len(word)
    for i in range(height - lenWord):
      for j in range(width - lenWord):
        for x in range(lenWord):
          if x == lenWord - 1:
            if word[x] == square[i+x][j+x]:
              foundWords[word] = (i+1, j+1)
          elif word[x] == square[i+x][j+x]:
            continue
          else:
            break
    for i in range(lenWord-1, height):
      for j in range(width - lenWord):
        for x in range(lenWord):
          if x == lenWord - 1:
            if word[x] == square[i-x][j+x]:
              foundWords[word] = (i+1, j+1)
              print(word)
          elif word[x] == square[i-x][j+x]:
            continue
          else:
            break
          
  #find reversed words in diagonals
  for word in [x for x in foundWords if foundWords[x] == (0, 0)]:
    revWord = revStr(word)
    lenWord = len(word)
    for i in range(height - lenWord):
      for j in range(width - lenWord):
        for x in range(lenWord):
          if x == lenWord - 1:
            if revWord[x] == square[i+x][j+x]:
              foundWords[word] = (i+lenWord, j+lenWord)
          elif revWord[x] == square[i+x][j+x]:
            continue
          else:
            break
    for i in range(lenWord-1, height): ##### CHECK HERE!!!!#####
      for j in range(width - lenWord + 1):
        for x in range(lenWord):
          if x == lenWord - 1:
            if revWord[x] == square[i-x][j+x]:
              foundWords[word] = (i-lenWord+2, j+lenWord)
              print(word)
          elif revWord[x] == square[i-x][j+x]:
            continue
          else:
            break

  return foundWords


def main():
  '''main function to check for hidden words'''

  #open two files, one for input and one for output
  f = open('hidden.txt', 'r')
  out = open('found.txt', 'w')

  #store all information from input file and create 2D list
  dimension = f.readline().split()
  numLines = int(dimension[0])
  f.readline() #skip empty line

  square = []
  for line in range(numLines):
    square.append(f.readline().rstrip('\n').upper().replace(' ',''))

  f.readline() #skip empty line
  numWords = int(f.readline())

  #create dictionary to store words to find, with (0,0) as initial positions
  words = []
  for line in range(numWords):
    words.append(f.readline().rstrip('\n').upper())
  foundWords = dict((x,(0,0)) for x in words)

  #call function to check for words in square and print results
  found = findWords(square, foundWords, dimension)
  
  for word in words:
    out.write('%-12s%3s%5s\n' %(word, found[word][0], found[word][1]))

main()
