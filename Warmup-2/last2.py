def last2(str):
  last2 = str[-2:]
  return sum(1 for i in range(len(str) - 2) if str[i:i + 2] == last2)
