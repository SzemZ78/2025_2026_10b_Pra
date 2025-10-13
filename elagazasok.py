import math
# kérjen be egy egész számot és döntse el, hogy páros vagy páratlan?

szam = int(input("Adjon meg egy egész számot:"))
if(szam % 2 == 0):
    print("páros")
else:
    print("páratlan")

# kérjen be a felhasználótól egy számot és mondja meg, hogy 10-zel osztható-e? H nem osztható tízel akkor írja ki az utolsó számjegyét
# pl. be: 10 ki: tízzel osztható
#pl. be: 12 ki: tízzel nem ossztható, utolsó számjegy 2

a = int(input("Adjon meg egy egész számot:"))
if(a % 10 == 0):
    print("tízzel osztható")
else:
    print("tízzel nem osztható")
    print("az utolsó számjegy: " + str(a % 10))

# Kérjen be egy másik számot és írassa ki a két szám reciprokának összegét

b = int(input("Adjon meg egy egész számot:"))

if(a != 0):
    if(b != 0):
        rec1 = 1 / a
        rec2 = 1 / b
        print(rec1 + rec2)
    else:
        print("A második számnak nincs reciproka")
else:
    print("Az első számnak nincs reciproka")


# Adja meg a két szám összegének a gyökét
if(a + b >= 0):
    print(math.sqrt(a + b))
else:
    print("A két szám összege negatív")

# Logikai operátorok
#and, or, xor, not

if(a != 0 and b != 0):
    rec1 = 1 / a
    rec2 = 1 / b
    print(rec1 + rec2)
else:
    print("A kát szám valamelyike nulla!")

# HF bool algebra

# Kérjen be a felhasználótól 3 db számot (lehet tört is). Ez a három szám egy háromszög három oldala.
# 1. Derékszögű-e a háromszög?
# 2. Szabályos-e a háromszög?

# Generáljon ki három véletlen háromjegyű számot, amleyek 13-al oszthatók!
# Álítsa sorrendbe
# Adja meg az átlagukat
# Van e közötök 4-el végződő?