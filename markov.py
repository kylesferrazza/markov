import random
import string
def adjust(l):
	a = 0
	for (i,n) in enumerate(l):
		a += n
		l[i] = a

def weighted_pick(l):
	n = random.random()
	i = 0
	while i < 25:
		if n < l[i]:
			return i
		i += 1
	return i

l = [[0]*26 for _ in range(26)]
 
f = open("corpus.txt").read()
words = f.split()

for word in words:
	for i in range(len(word)-1):
		l[ord(word[i])-ord('a')][ord(word[i+1])-ord('a')] += 1

total = sum(map(sum, l))


start = []
for x in l:
	start.append(sum(x) / total)

for y in range(len(l)):
	subtotal = sum(l[y])
	for x in range(len(l[y])):
		l[y][x] /= subtotal

adjust(start)
for y in l:
	adjust(y)

for _ in range(20):
	s = ""
	old = weighted_pick(start)
	s += string.ascii_lowercase[old]

	for _ in range(random.randint(2, 6)):
		new = weighted_pick(l[old])
		s += string.ascii_lowercase[new]
		old = new
	print(s)
