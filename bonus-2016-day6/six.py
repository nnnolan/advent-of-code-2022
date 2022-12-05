from collections import Counter

with open(r'c:\Users\Nolan\Documents\GitHub\advent-of-code-2022\bonus-2016-day6\six.txt') as f:
  x = f.readlines()
  lines = [item.strip() for item in x]

first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eighth = []

count = 1

for i in lines:
  print(i)
  first.append(i[0])
  second.append(i[1])
  third.append(i[2])
  fourth.append(i[3])
  fifth.append(i[4])
  sixth.append(i[5])
  seventh.append(i[6])
  eighth.append(i[7])

print(first)

one = Counter(first)
two = Counter(second)
three = Counter(third)
four = Counter(fourth)
five = Counter(fifth)
six = Counter(sixth)
seven = Counter(seventh)
eight = Counter(eighth)

print(one, two, three, four, five, six, seven, eight)
#x, h, n, q, p, q, q, l,
#xhnqppql