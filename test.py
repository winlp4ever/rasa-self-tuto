def power(x, n):
	p = 1
	while n > 0:
		if n % 2:
			p *= x
		n = n >> 1
		x = x * x
	return p

print(power(3, 0))
print(power(3, 1))
print(power(3, 2))
print(power(3, 3))
print(power(2, 15))