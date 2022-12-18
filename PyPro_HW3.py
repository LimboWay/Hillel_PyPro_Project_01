lst1 = [
	[34587, 'Learning Python, Mark Lutz', 4, 40.95],          # (34587, 163.8)
	[98762, 'Programming Python, Mark Lutz', 5, 56.80],       # (98762, 284.0)
	[77226, 'Head First Python, Paul Barry', 3, 32.95],       # (77226, 98.85) 98.85 < 100 ==> (98.85 + 10 = 108.85)
	[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]   # (88112, 74.97) 74.97 < 100 ==> (74.97 + 10 = 84.97)
]

print(list(map(lambda x: (x[0], round((x[-1] * x[-2]), 2)) if (x[-2] * x[-1]) > 100 else (x[0], round(((x[-1] * x[-2]) + 10), 2)), lst1)))
