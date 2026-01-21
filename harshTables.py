from collections import defaultdict

s = "LISTENlisten"
t = "SILENTsilent"

def is_anagram(s,t):
   if len(s) != len(t):
      return False
   
   s= s.lower()
   t = t.lower()
   
   count = [0] * 26
   
#    count = [0] * 52

#    for ch in s:
#       if 'A' <= ch <= 'Z':
#          index = ord (ch) - ord ('A')
#       else:
#          index = ord (ch) - ord('a') + 26
#       count[index] += 1

#    for ch in t:
#       if 'A' <= ch <= 'Z':
#          index = ord (ch) - ord ('A')
#       else:
#          index = ord(ch) - ord('a') + 26
#       count[index] -= 1
#       if count[index] < 0:
#          return False
      
#    return True

   
   
   for ch in s:
      count[ord(ch) - ord('a')] += 1

   for ch in t:
      count[ord(ch) - ord('a')] -= 1
      if count[ord(ch) - ord('a')] < 0:
         return False
      
   return True
      
print(is_anagram(s,t))