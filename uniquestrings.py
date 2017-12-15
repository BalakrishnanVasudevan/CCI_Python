#Implement an algorithm to determine if a string has all unique characters What if you can not use additional data structures?
import sys
"""Set based method
def unique(s):
 print s
 if len(set(s)) == len(s):
  print 'True'
 else:
  print 'False'


unique(str(sys.argv[1]))

this is a less pythonic way. In this all we do is add the string to a set so that only unique elements are stored, we then compare it with the original text to see if they match.
"""
def unique(s):
 chars = set()
 for c in s:
  if c in chars:
   print 'False'
  chars.add(c)
 print 'True'

unique(str(sys.argv[1]))
