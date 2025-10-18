import random 
# lebegőpontos - float - tört
a = 1.25
b = float(input("Adjonmeg egy tizedes törtöt"))
print(a)
print(b * 4)

# generáljon ki [1,10[ közötti tört számot 2 tizedesjegyre
# pl. 1.36, 2.30

# c = random.randint(100,999)/100
c = random.random() # [0,1[
print(c)
print(round(c,2))

# szövegkezelés
szoveg = input("Adjonmeg egy szövegevt: ")
print(szoveg)
print("szöveg hossza: ",len(szoveg))
print("első karkter",szoveg[0])
#szöveg karakterekből épül fel
# szöveg = karakter lánc
karakter = szoveg[0]
kod = ord(szoveg[0])
print(kod)
ujkod = kod + 1
ujkarakter = chr(ujkod)
print(ujkarakter)

d = int(random.randint(97,122))
e = int(random.randint(97,122))
f = int(random.randint(97,122))
print(chr(d), chr(e), chr(f))

# Kérj a felhasználó keresztnevét! Generáljon neki egy jelszót, az első 3 karakterének ascii kódjának szorzatát! Ha nincs a név 3 jegyü, akkor kettő esetén a hossz érték legyen a szorzat 3. taja 1 esetén pedig a szám köb legyen.
# Alma - 65 *108 * 109
# Co - 67 * 111 * 2
# G - 71 * 71 * 71
nev = input("Adja meg a nevét: ")
