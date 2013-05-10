#  File: Books.py

#  Description: Compares the vocabulary of two different authors

#  Student Name: Collin Murphy

#  Student UT EID: cbm772

#  Course Name: CS 303E

#  Unique Number: 52680

#  Date Created: 14 Nov 2012

#  Date Last Modified: 26 Nov 2012

wordDict = set()

def createWordDict():
  
  '''function to create a word dictionary from a comprehensive word list'''

  global wordDict
  wordList = open('words.txt','r')
  wordDict = set()
  i = 0
  for line in wordList:
    wordDict.add(line.rstrip('\n'))
  wordList.close()
  return wordDict

def removePunc(st):
  if len(st) == 0: return st
  if st[0].isalpha():
    if st[-1].isalpha():
      return st
    return removePunc(st[:-1])
  return removePunc(st[1:])

def parseString(st):

  '''function to parse a string; remove all unwanted punctuation
      and spaces, and return a list of unique words'''

  parsed = []
  for word in st.replace('-',' ').split():
    if not word.isalpha():
      word = removePunc(word).replace("'s",'')
    if word:
      parsed.append(word)
  
  return parsed

def getWordFreq(file):

  '''function to get frequency of words in a text document'''

  #open file and read in words
  f = open(file, 'r', encoding = 'utf-8')
  words = {}
  for line in f:
    parsed = parseString(line.rstrip('\n'))
    for word in parsed:
      try:
        words[word] += 1
      except:
        words[word] = 1
    a = line
      
  #check for existence of lower case version of upper case words
  upperWords = {}
  removedWords = set()
  for word in words:
    if word[0].isupper():
      upperWords[word] = words[word]
  for word in upperWords:
    if word.lower() in words:
      words[word.lower()] += upperWords[word]
    elif word.lower() in wordDict:
      words[word.lower()] = upperWords[word]
    else:
      removedWords.add(word) 
    del words[word]

  #close file and return word dictionary
  f.close()
  return words

def wordComparison(author1, freq1, author2, freq2):

  '''function to calculate statistics of authors'''

  #initialize counting variables and create set differences
  totalCount1 = 0
  wordCount1 = 0
  for word in freq1:
    totalCount1 += freq1[word]
    wordCount1 += 1
  totalCount2 = 0
  wordCount2 = 0
  for word in freq2:
    totalCount2 += freq2[word]
    wordCount2 += 1
  set1 = set(freq1)
  set2 = set(freq2)
  diff1 = set1 - set2
  diff2 = set2 - set1
  count1 = 0
  for x in diff1:
    count1 += freq1[x]
  count2 = 0
  for x in diff2:
    count2 += freq2[x]
  
  #Print results
  print()
  print(author1)
  print('Total distinct words =', wordCount1)
  print('Total words (including duplicates) =', totalCount1)
  print('Ratio (% of total distinct words to total words) =', \
        wordCount1/totalCount1*100, end = '\n\n')
  print(author2)
  print('Total distinct words =', wordCount2)
  print('Total words (including duplicates) =', totalCount2)
  print('Ratio (% of total distinct words to total words =', \
        wordCount2/totalCount2*100, end = '\n\n')
  print('%s used %d words that %s did not use.' %(author1, len(diff1), author2))
  print('Relative frequency of words used by %s not in common with %s =' \
        %(author1, author2), count1/totalCount1*100, end = '\n\n')
  print('%s used %d words that %s did not use.' %(author2, len(diff2), author1))
  print('Relative frequency of words used by %s not in common with %s =' \
        %(author2, author1), count2/totalCount2*100, end = '\n\n')
  

def main():

  '''main function to compare two authors' vocabularies'''

  createWordDict()

  # Enter names of the two books in electronic form
  book1 = input("Enter name of first book: ")
  book2 = input("Enter name of second book: ")

  # Enter names of the two authors
  author1 = input("Enter last name of first author: ")
  author2 = input("Enter last name of second author: ")
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq(book1)
  wordFreq2 = getWordFreq(book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)

main()
