import random
# első feladat

a = random.randint(0, 9)
if(a == 1 or a == 6):   # if a % 5 == 1
    print("labda")
elif(a == 2 or a == 7): # if a % 5 == 2
    print("ceruza")
elif(a == 3 or a == 8): # if a % 5 == 3
    print("színes papír")
elif(a == 4 or a == 9): # if a % 5 == 4
    print("bicikli")
else:
    print("Nem nyert")

# Második feladt

a = int(input("Adja meg a számot: "))
het = a // 24 // 7
nap = (a - het * 168) // 24
ora = (a - het * 168) - nap * 24
print(het, nap ,ora)

# Harmadik feladat

a = random.randint(100, 999)
print("Generált háromjegyü szám: " + str(a))
b = a // 100
c = (a - b *100) // 10
d = a % 10
if(b ** 3 + c ** 3 + d ** 3 == a):
    print("Az a szám")
else:
    print("Nem az a szám")

#4. fel

a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
print(a, b, c)
if(a != 0 and b != 0 and c != 0):
    harmonikus = 3 / (1/a + 1/b + 1/c)
elif(a != 0 and b != 0):
    harmonikus = 2 / (1/a + 1/b)
elif(a != 0 and c != 0):
    harmonikus = 2 / (1/a + 1/c)
elif(b != 0 and c != 0):
    harmonikus = 2 / (1/b + 1/c)
elif(a == 0 and b == 0 and c != 0):
    harmonikus = 1 / (1/c)
elif(a == 0 and b != 0 and c == 0):
    harmonikus = 1 / (1/b)
elif(a != 0 and b == 0 and c == 0):
    harmonikus = 1 / (1/a)
else:
    harmonikus = "nincs megoldás"
print(round(harmonikus, 3))
