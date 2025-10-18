import math
import random

a = 2
gyoka = math.sqrt( a )
print("gyoka("+str(a)+") = ",gyoka )

felkerekit = math.ceil(gyoka)
print("felsőegészrész:", felkerekit)
lefelkerekit = math.floor(gyoka)
print("alsóegészrész:", lefelkerekit)
kerekites = round(gyoka,2)
print("kerekítés 2 tizedes jegyre:", kerekites)
hatvanyozas1 = math.pow(gyoka, 2)
print("gyoka négyzete:", hatvanyozas1)

alap = 2
kitevo = 5
#hatvanyozas2 = math.pow(alap,kitevo) 
hatvanyozas2 = alap ** kitevo
print(alap,"^", kitevo,"=",hatvanyozas2)

vszam1 = random.randint(2,10)
print(vszam1)











