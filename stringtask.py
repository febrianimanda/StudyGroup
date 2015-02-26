kata = "Febrian".lower()
vowels = ['a','i','u','e','o','y']
x = []
for y in kata :
	if y not in vowels :
		x.append(y)
titik = ['.' for i in range(0,len(x))]
for a,b in zip(titik,x):
	print a,b,