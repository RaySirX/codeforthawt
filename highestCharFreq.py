# Given a non-empty string find the character that occurs most frequently
#
# highestFreqChar1 - use collections.defaultdict to initialized undefined keys -> value = 0
# highestFreqChar2 - take advantage of collections.Counter char frequency counter
# for testing, assert both functions should return same result

from collections import defaultdict

def highestFreqChar1(s):
  # check for invalid input, return immediately with ""
  if s == None:
     return ""

  # initialize values of undefined keys to 0
  charFreq = defaultdict(lambda: 0)

  # char frequency counter
  for aChar in s:
    charFreq[aChar] += 1

  # sort dict by value in reverse order
  # doing so will convert dict into a list of (k,v) elements
  sortedCharFreqList = sorted(charFreq.items(), key=lambda kv : kv[1], reverse=True)

  # each element is (k, v), first element is the max freq
  # 1st (k,v) element in list is what we want
  # array is 0-based
  # added guard for edge case where input is "" 
  return sortedCharFreqList[0][0] if sortedCharFreqList else ""

from collections import Counter
def highestFreqChar2(s):
  # check for invalid input, return immediately with ""
  if s == None:
     return ""

  # collections.Counter - character frequency counter as dict
  # sort Counter -> dict by value in reverse order
  # doing so will convert dict into a list of (k,v) elements
  sortedCharFreqList = sorted(Counter(s).items(), key=lambda kv: kv[1], reverse=True)

  # each element is (k, v), first element is the max freq
  # 1st (k,v) element in list is what we want
  # array is 0-based
  # added guard for edge case where input is "" 
  return sortedCharFreqList[0][0] if sortedCharFreqList else ""


def highestFreqChar3(s):
  # Full marks!!

  return max(set(s), key=lambda c:str.count(c))


if __name__ == "__main__":
  #
  # white-box testing sort function used so include test case of unsorted strings
  # not tested but could try non-ascii, unicode chars; need to determine collation sequence first
  # edge case where multiple characters have same frequency
  # evil case - try empty string contrary to assumption in problem statement
  # error case - null input via None
  #
  print(highestFreqChar1("baabbbaaaaaab"))
  print(highestFreqChar1("bbbaaaa"))
  print(highestFreqChar1("bbbaa"))
  print(highestFreqChar1("bbbaaa"))
  print(highestFreqChar1("aaabbb"))
  print(highestFreqChar1("aaabbbb"))
  print(highestFreqChar1("aaabb"))
  print(highestFreqChar1(""))
  print(highestFreqChar1(None))

  assert highestFreqChar1("baabbbaaaaaab") == highestFreqChar2("baabbbaaaaaab"), highestFreqChar2("baabbbaaaaaab") 
  assert highestFreqChar1("bbbaaaa") == highestFreqChar2("bbbaaaa"), highestFreqChar2("bbbaaaa")
  assert highestFreqChar1("bbbaa") ==  highestFreqChar2("bbbaa"), highestFreqChar2("bbbaa")
  assert highestFreqChar1("bbbaaa") == highestFreqChar2("bbbaaa"), highestFreqChar2("bbbaaa")
  assert highestFreqChar1("aaabbb") == highestFreqChar2("aaabbb"), highestFreqChar2("aaabbb")
  assert highestFreqChar1("aaabbbb") == highestFreqChar2("aaabbbb"), highestFreqChar2("aaabbbb")
  assert highestFreqChar1("aaabb") == highestFreqChar2("aaabb"), highestFreqChar2("aaabb")
  assert highestFreqChar1("") == highestFreqChar2(""), highestFreqChar2("")
  assert highestFreqChar1(None) == highestFreqChar2(None), highestFreqChar2(None)

  assert highestFreqChar1("baabbbaaaaaab") == highestFreqChar2("baabbbaaaaaab"), highestFreqChar3("baabbbaaaaaab")
  assert highestFreqChar1("bbbaaaa") == highestFreqChar2("bbbaaaa"), highestFreqChar3("bbbaaaa")
  assert highestFreqChar1("bbbaa") ==  highestFreqChar2("bbbaa"), highestFreqChar3("bbbaa")
  assert highestFreqChar1("bbbaaa") == highestFreqChar2("bbbaaa"), highestFreqChar3("bbbaaa")
  assert highestFreqChar1("aaabbb") == highestFreqChar2("aaabbb"), highestFreqChar3("aaabbb")
  assert highestFreqChar1("aaabbbb") == highestFreqChar2("aaabbbb"), highestFreqChar3("aaabbbb")
  assert highestFreqChar1("aaabb") == highestFreqChar2("aaabb"), highestFreqChar3("aaabb")
  assert highestFreqChar1("") == highestFreqChar2(""), highestFreqChar3("")
  assert highestFreqChar1(None) == highestFreqChar2(None), highestFreqChar3(None)

