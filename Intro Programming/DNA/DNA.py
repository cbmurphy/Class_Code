#  File: DNA.py

#  Description: finds the longest similar sequence in pairs of DNA strands

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E

#  Unique Number: 52680

#  Date Created: 21 Oct 2012

#  Date Last Modified: 21 Oct 2012

def shortLong(firstStrand, secondStrand):
  '''return a short strand, a long strand and the length of the shorter strand'''
  
  if len(firstStrand) < len(secondStrand): return (firstStrand, secondStrand, len(firstStrand))
  return (secondStrand, firstStrand, len(secondStrand))

def main():
  '''main function to find common sequences in a given sequence of DNA nucleotides'''

  #get number of pairs and print header
  f = open('dna.txt', 'r')
  pairs = f.readline().rstrip('\n')
  print("Longest Common Sequences")

  for pair in range(eval(pairs)): #loop over number of pairs of strands

    #get a pair of strands
    print()
    firstStrand = f.readline().upper().rstrip('\n')
    secondStrand = f.readline().upper().rstrip('\n')

    #initialize parameters
    shortStrand, longStrand, length = shortLong(firstStrand, secondStrand)
    longestSequence = []
    sequenceLength = length

    #loop over pair to find sequences
    while ((not longestSequence) and sequenceLength >= 2): #loop to control length of sequence
      for x in range(length - sequenceLength + 1): #loop to control position of sequence
        newSequence = shortStrand[x:x+sequenceLength]
        if (newSequence in longStrand): #check if sequence from first is in second
          longestSequence.append(newSequence)
      sequenceLength -= 1

    #print results
    print("Pair %d:" %(pair + 1), end='')
    if longestSequence:
      for x in longestSequence:
        print('\t%s' %x)
    else:
      print("\tNo Common Sequence Found")

  f.close()

main()
