# Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
jesus="VIN JWENN JEZI LA SOVE OU"
va=jesus.lower()
# print(va)

# ==============================Exercice2======================================
# Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp:
# >>> "Ayibobo Ayiti"
# >>> ["Ayibobo", "Ayiti"]
bon="Ayibobo Ayiti"
ex = bon.split()
# print(ex)

# ===============================exercice3=====================================
# Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
jesus="jezi ap retounen nan yn date nou poko knnen"
je= jesus.title()
# print(je)


# ===============================Exercice4======================================
# Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
messi = "messi pran yn paket balon do nan karye li "
mes= messi.split() 
pakouri = [index[0] for index in mes]
nouvomo = "".join(pakouri)
# print(nouvomo)

# ===============================Exercice 5=====================================
# Ranplase tout karaktè "a" ki nan yon chenn pa "@"
messi="messi pran yon paket balon do anne sa"
mes=messi.replace("a","@")
# print(mes)

# ==============================Exercice 6======================================
# Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. Ekzanp:
# >>> "Ayiti"
# >>> "ITIYA"

ballon="Messi"
bal=ballon.upper()
# print(bal)
# print(bal[::-1])   
                                
# =================================Exercice7===================================
# Afiche endeks premye karaktè "a" ki nan yon chenn. Ekzanp:
# >>>  "Ayiti kapab avanse"
# >>> 7
messi= "messi prAn 8em balon do li lundi a"
karakte= 'u'
mes= messi.find(karakte)
# if mes != -1:
    # print(f'{karakte}\n {mes}') 

# ==================================Exercice 8=================================
# Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:
# >>> "Ayiti kapab avanse"
# >>> 42
frans= "messi prAn 8em balon do li lundi A"
konvesyn=frans.lower()
leo=0
for el in konvesyn:
    if el[0]=="a":
        leo = leo + 1
# print(leo)

# ================================Exercice9====================================
# Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil
messi2 = "messi se meye jwe mond football lan t ka konnen"
inisyalize= []
for el in range(len(messi2)):
    if messi2[el] == 'a':
        inisyalize.append(el)
# print(inisyalize)

# =================================Exercice 10=================================
# Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo)
messi3 = "messi pran 8em balon do li a 36 zan"
kole = messi3.replace(" ", "") 
kantitekarakte = len(kole) 
# print(kole)
# print(kantitekarakte)

# ============================================================================
# =============================================================================

# MASTER LIST (Union & Intersection & Lis comprehension)
# ===============================Exercice 1====================================
# Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n = 15 
divizib= []
for el in range(n + 1):
    if el % 2 == 0: 
        divizib.append(el)
# print("Lis eleman ki divizib pa 2 nan entèval [0-n] yo se :", divizib)

# ================================Exercice 2===================================
# Ou gen yon lis antye, konvèti l an yon lis chenn.
lis_antye = [100, 70, 80, 48, 55]
chenn = []
for el in lis_antye:
    chenn.append(str(el))
# print("Lis chenn lan se :", chenn)

# ===============================Exercice 3===================================
# Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis = ["manje", "benyen", "domi", "travay" , "jwe"]
majiskil = []
for el in lis:
    majiskil.append(el.upper())
# print(majiskil)

# ================================Exercice 4====================================
# Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lisin= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nouvolis = []
for el in range(0, len(lisin), 3):
    nouvolis.append(lisin[el])
# print(nouvolis)

# ================================Exercice 5====================================
# Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.
lis= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
lisgwoup = []
for i in range(0, len(lis), 3):
    tipl = tuple(lis[i:i+3])
    lisgwoup.append(tipl)
# print("Lis done:", lis)
# print("Nouvo lis ak tipl ki gen 3 eleman:", lisgwoup)

# ================================Exercice 6===================================
# Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
doublon = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
sandoublon = list(set(doublon))
# print(sandoublon)

# ================================Exercice 7===================================
# Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
listotal = []
for i in lis1:
    for j in lis2:
        if i == j:
            listotal.append(i)
# print(listotal)

# ================================Exercice 8===================================
# Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
set1 = set(lis1)
set2 = set(lis2)
distenge = list(set1.symmetric_difference(set2))
# print(distenge)

# ================================Exercice 9===================================
# Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
diksyone0 = {'messi': 'balon', 'do': 'ane', 'a': 'fanatik', 'CRbwet': 'yo', 'pleyen': 'antouka'}
kle = list(diksyone0.keys())  
vale = list(diksyone0.values())
# print(kle)
# print(vale)

# ================================Exercice 10===================================
# Reyini 3 lis ansanm, san okenn doublon.
lis1 = [1, 2, 3, 4, 5]
lis2 = [3, 4, 5, 6, 7]
lis3 = [5, 6, 7, 8, 9]
adisyonelis= lis1 + lis2 + lis3
messi= set(adisyonelis)
adisyonelis = list(messi)
# print(adisyonelis)

# =====================================================================================================
# ===============================MASTER DICTIONNAIRE (isinstance, eval)================================
# ================================Exercice 1==========================================================
# Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.

diksyone01 = {'messi': 'balondo', 'messi2': 'balondo2'}
messi= list(diksyone01.values())
# print(messi)

# ================================Exercice 2==========================================================
# Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
# chan = input("rantre yn non ::")
# if chan.startswith("{") and chan.endswith("}"):
#     print("li gn akolad ni devan ni deye")
# print("pa gn akolad")

# =================================Exercice 3=========================================================
# Pakouri yon diksyonè, epi afiche tout kle yo.
diksyone1 = {'leo': 'messi', 'luis': 'suarez'}
kle = list(diksyone1.keys())
# print(kle)

# ================================Exercice 4===========================================================
# Pakouri yon diksyonè, epi afiche tout valè yo.
diksyone2 = {'leo': 'messi', 'chritiano': 'Ronaldo', 'neymar': 'junior'}
toutvale = list(diksyone2.values())
# print(toutvale)

# =================================Exercice 5==========================================================
# Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
diksyone3 = {'leo': 'messi', 'chritiano': 'Ronaldo', 'neymar': 'junior'}
diksyonekopi = diksyone3.copy()
# print(diksyonekopi)

# ==================================Exercice 6=========================================================
# Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo.
diksyone4 = {'leo': 'messi', 'chritiano': 'Ronaldo', 'neymar': 'junior'}
for kle, vale in diksyone4.items():
    if isinstance(vale, str):
        diksyone4[kle] = f'_{vale}_'
# print(diksyone)

# =====================================Exercice 7=====================================================
# Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. 
diksyone5 = {'leo': 'messi', 'luis': 'suarez'}
nouvodiksyone = {}
for kle, vale in diksyone5.items():
    if vale.isdigit():
        nouvodiksyone[kle] = vale
# print(nouvodiksyone)

# ====================================Exercice 8======================================================
# Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la. Ekzanp:
# >>> {"a":1, "b": 2}
# >>> [("a",1), ("b",2)]

diksyone= {"a": 1, "b": 2}
tipl = list(diksyone.items())
# print(tipl)

# ======================================Exercice 9======================================================
# Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. Ekzanp:
# >>> [("a",1), ("b",2)]
# >>> {"a":1, "b": 2}
fomdiksyone= [("a", 1), ("b", 2)]
diksyone= dict(fomdiksyone)
# print(diksyone)

# =====================================Exercice 10======================================================
# Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo:
# Antye: ADISYON
# Chenn, lis, set: KONKATENASYON
# Rès eleman ki pa gen valè ki gen tip sa yo, pap nan nouvo diksyonè a.

diksyone1 = {"a": 1, "b": [2, 3], "c": "bonjou"}
diksyone2 = {"b": [4, 5], "d": "ayiti", "y": {6, 7}}

nouvodiksyone = {}
adisyon = (int,)
konkatenasyon = (str, list, set)
for kle, vale in diksyone1.items():
    if isinstance(vale, adisyon):
        if kle in diksyone2 and isinstance(diksyone2[kle], adisyon):
            nouvodiksyone[kle] = vale + diksyone2[kle]
        else:
            nouvodiksyone[kle] = vale

for kle, vale in diksyone2.items():
    if isinstance(vale, adisyon) and kle not in diksyone1:
        nouvodiksyone[kle] = vale
        
for kle, vale in diksyone1.items():
    if isinstance(vale, konkatenasyon):
        if kle in diksyone2 and isinstance(diksyone2[kle], konkatenasyon):
            nouvodiksyone[kle] = vale + diksyone2[kle]
        else:
            nouvodiksyone[kle] = vale

for kle, vale in diksyone2.items():
    if isinstance(vale, konkatenasyon) and kle not in diksyone1:
        nouvodiksyone[kle] = vale
print(nouvodiksyone)

# ======================================================================================================
# =====================================================================================================

# ==========================================Exercice 1=================================================
# kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def moinvese(mo):
    moinvese = mo[::-1]
    return moinvese
inves = "Hello"
recep = moinvese(inves)
# print(recep)

# =========================================Exercice 2===================================================
# kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
import random
import string

def kodaleyatwa(el):
    kons = ''.join(random.choice(string.ascii_lowercase) for _ in range(el))
    return kons
el = 10
kòdAleyatwa = kodaleyatwa(el)
# print(kòdAleyatwa)

# =====================================Exercice 3======================================================
# kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
import random
import string
def aleyatwa(n):
    if n > 26:
        return "sa ou antre an depase kantite let alfabe an ki c: (26)."
    
    kòd = ''.join(random.sample(string.ascii_lowercase, n))
    return kòd
n = 10 
kòd_aleyatwa = aleyatwa(n)
# print(kòd_aleyatwa)


# ===================================Exercice 4========================================================
# kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
import random
import string
def aleyatwa(el):
    if el > 62:
        return "saw antre an depase karaktè alafanimerik ki disponib yo ki c: (62)."
    karakte = string.ascii_letters + string.digits
    var = ''.join(random.sample(karakte, el))
    return var
n = 12 
x = aleyatwa(n)
# print(x)

# ===================================Exercice 5=========================================================
# Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
def jenere():
    alfanimerik="abcdefghijklmnopqrstuvwxyz1234567890-ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lischenn35="Freedom, nou se Valeyen"
    lischenn35=lischenn35.replace(" ","-")
    for element in lischenn35:
        if element not in alfanimerik:
            lischenn35=lischenn35.replace(f"{element}","-")
#     print(lischenn35)
# jenere()

# =====================================Exercice 6======================================================
# Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe(mo):
    nouvomo=""
    for el in mo:
        nouvomo+=f"{el},"
    return nouvomo
# mo=input("Antre mo a: ")
# print(separe(mo))

# ======================================Exercice 7=====================================================
# Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
# >>> "ALO"
# >>> "0-11-14"
def kripte():
    konve=string.ascii_uppercase
    print(konve)
    mo_poukripte=input("Antre mo wap kripte a: ")
    mo_poukripte=mo_poukripte.upper()
    mokripte=""
    for el in mo_poukripte: 
        mokripte+=f'{konve.index(el)}-'
    mokripte[-1]=""
    print(mokripte)
kripte()

# =========================================Exercice 8==================================================
# Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
# >>> "0-11-14"
# >>> "ALO"
def dekripte():
    alfabe=string.ascii_uppercase
    mo_poudekripte=input("Antre mo wap kripte a: ")
    mo_poudekripte=mo_poudekripte.split("-")
    modekripte=""
    for el in mo_poudekripte:
        el=int(el)
        modekripte+=alfabe[el]
    # print(modekripte)
# dekripte()


# =====================================Exercice 9=====================================================
# Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.
def pemitasyon(val1,val2):
    temp=val1
    val1=val2
    val2=temp
    fomtuple=(val1,val2)
    # print(fomtuple)
# pemitasyon(28,22)


# ========================================Exercice 10==================================================
# Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.
# ```
#  >>> "Jean-Baptiste Jean"
#  >>> "JBJ"
# ```

def para():
    non="Jean-Baptiste Jean"
    non = non.replace("-", " ")
    non=non.split(" ")
    inisyal=""
    for el in non:
        inisyal+=el[0]
#     print(inisyal.upper())
# para()
