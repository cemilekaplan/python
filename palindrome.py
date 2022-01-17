'''
Write a program to check if a given string is a Palindrome.
A palindrome reads same from front and back e.g.- aba, ccaacc, mom, etc.

INPUT:  aba

OUTPUT: True
'''

sentence = input("please enter the sentence : ")
new_st = ""

for i in sentence :
  if i.isalnum():
    new_st += i

if new_st[::-1].lower() == new_st[::].lower() :
  print("{} is a palindrome.".format(sentence))
else:
  print("{} is not a palindrome.".format(sentence))