#  File: ISBN.py

#  Description: Program to check validity of ISBN numbers

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E

#  Unique Number: 52680

#  Date Created: 5 Nov 2012

#  Date Last Modified: 5 Nov 2012

def main():
  '''main function to open file containing ISBNs and output their validity to a file'''

  #open the input and output files
  f = open('isbn.txt','r')
  out = open('isbnOut.txt','w')

  #loop over the lines of the input file to check ISBNs
  for line in f:
    isbn = line.strip('\n')
    if isValid(isbn):
      valid = 'valid'
    else:
      valid = 'invalid'
    out.write('%s %s\n' %(isbn, valid))

  #close input and output files
  f.close()
  out.close()

def isValid(isbn):
  '''function to check validity of a given ISBN number'''

  #format ISBN and do initial format validation (parse)
  isbn = isbn.replace('-','')
  if not ((len(isbn) == 10) and isbn[:-1].isdigit() and \
          (isbn[-1].lower() == 'x' or isbn[-1].isdigit())):
    return False
  isbn = [x for x in isbn[:-1]] + [x for x in isbn[-1] if \
        isbn[-1].isdigit()] + [10 for x in isbn[-1].lower() if x[-1] == 'x']

  #do sums and check if divisible by 11
  s1 = [isbn[0]]
  for x in range(1,10):
    s1.append(int(s1[x-1]) + int(isbn[x]))
  s2 = [s1[0]]
  for x in range(1,10):
    s2.append(int(s2[x-1]) + int(s1[x]))

  if s2[-1] % 11 == 0: return True
  return False

main()
