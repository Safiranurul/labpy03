import random

a = 0
jumlah = int(input("Masuka jumlah N : "))
for x in range(0,jumlah):
		i = random.uniform(0.0, 0.5)
		a += 1
		print("data ke-",a,"=>",i)
