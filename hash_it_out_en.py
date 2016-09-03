max_m = 129 * 255

def guess_0(digest):
	n = digest[0]
	a = []
	while n <= max_m:
		if n % 129 == 0:
			a.append(int(n/129))
		n += 256
	return a

def inv(digest):
	a = []
	while digest <= max_m:
		a.append(digest)
		digest += 256
	return a

def guess_next(prev, d):
	a = inv(d)
	guesses = []
	for e in a:
		for p in prev:
			x = p ^ e
			if x % 129 == 0:
				guesses.append(int(x/129))
	return guesses

digest = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]

g = guess_0(digest)
for i in range(1, 16):
	print(g)
	g = guess_next(g, digest[i])

print (g)
