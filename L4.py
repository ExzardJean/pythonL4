# Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
# jesus="VIN JWENN JEZI LA SOVE OU"
# va=jesus.lower()
# print(va)

# ==============================Exercice2======================================
# Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp:
# >>> "Ayibobo Ayiti"
# >>> ["Ayibobo", "Ayiti"]
# bon="Ayibobo Ayiti"
# ex = bon.split()
# print(ex)

# ===============================exercice3=====================================
# Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
# jesus="jezi ap retounen nan yn date nou poko knnen"
# je= jesus.title()
# print(je)


# ===============================Exercice4======================================
# Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo.
# messi = "messi pran yn paket balon do nan karye li "
# mes= messi.split() 
# pakouri = [index[0] for index in mes]
# nouvomo = "".join(pakouri)
# print(nouvomo)
# ===============================Exercice 5=====================================
# Ranplase tout karaktè "a" ki nan yon chenn pa "@"
# messi="messi pran yon paket balon do anne sa"
# mes=messi.replace("a","@")
# print(mes)

# ==============================Exercice 6======================================
# Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. Ekzanp:
# >>> "Ayiti"
# >>> "ITIYA"

# ballon="Messi"
# bal=ballon.upper()
# print(bal)
# print(bal[::-1])   
                                
# =================================Exercice7===================================
# Afiche endeks premye karaktè "a" ki nan yon chenn. Ekzanp:
# >>>  "Ayiti kapab avanse"
# >>> 7
# messi= "messi prAn 8em balon do li lundi a"
# karakte= 'u'
# mes= messi.find(karakte)
# if mes != -1:
#     print(f'{karakte}\n {mes}') 

# ==================================Exercice 8=================================
# Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:
# >>> "Ayiti kapab avanse"
# >>> 42
# messi= "messi prAn 8em balon do li lundi A"
# konvesyn=messi.lower()
# leo=0
# for el in konvesyn:
#     if el[0]=="a":
#         leo = leo + 1
# print(leo)

# ================================Exercice9====================================
# Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil
# messi = "messi se meye jwe mond football lan t ka konnen"
# inisyalize= []
# for el in range(len(messi)):
#     if messi[el] == 'a':
#         inisyalize.append(el)
# print(inisyalize)

# =================================Exercice 10=================================
# Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo)
# messi = "messi pran 8em balon do li a 36 zan"
# kole = messi.replace(" ", "") 
# kantitekarakte = len(kole) 
# print(kole)
# print(kantitekarakte)

# ============================================================================
# =============================================================================

# MASTER LIST (Union & Intersection & Lis comprehension)
# ===============================Exercice 1====================================
# Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
# n = 15 
# divizib= []
# for el in range(n + 1):
#     if el % 2 == 0: 
#         divizib.append(el)
# print("Lis eleman ki divizib pa 2 nan entèval [0-n] yo se :", divizib)

# ================================Exercice 2===================================
# Ou gen yon lis antye, konvèti l an yon lis chenn.
# lis_antye = [100, 70, 80, 48, 55]
# chenn = []
# for el in lis_antye:
#     chenn.append(str(el))
# print("Lis chenn lan se :", chenn)

# ===============================Exercice 3===================================
# Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
# lis = ["manje", "benyen", "domi", "travay" , "jwe"]
# majiskil = []
# for el in lis:
#     majiskil.append(el.upper())
# print(majiskil)

# ================================Exercice 4====================================
# Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman


# ================================Exercice 5====================================
# Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl.
# lis_done = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# lis_gwoup = []
# for i in range(0, len(lis_done), 3):
#     tipl = tuple(lis_done[i:i+3])
#     lis_gwoup.append(tipl)
# print("Lis done:", lis_done)
# print("Nouvo lis ak tipl ki gen 3 eleman:", lis_gwoup)

# ================================Exercice 6===================================
# Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
# doublon = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
# sandoublon = list(set(doublon))
# print(sandoublon)

# ================================Exercice 7===================================
# Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# listotal = []
# for i in lis1:
#     for j in lis2:
#         if i == j:
#             listotal.append(i)
# print(listotal)

# ================================Exercice 8===================================
# Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# set1 = set(lis1)
# set2 = set(lis2)
# distenge = list(set1.symmetric_difference(set2))
# print(distenge)

# ================================Exercice 9===================================
# Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
# diksyone = {'messi': 'balon', 'do': 'ane', 'a': 'fanatik', 'CRbwet': 'yo', 'pleyen': 'antouka'}
# kle = list(diksyone.keys())  
# vale = list(diksyone.values())
# print(kle)
# print(vale)

# ================================Exercice 10===================================
# Reyini 3 lis ansanm, san okenn doublon.
# lis1 = [1, 2, 3, 4, 5]
# lis2 = [3, 4, 5, 6, 7]
# lis3 = [5, 6, 7, 8, 9]
# adisyonelis= lis1 + lis2 + lis3
# messi= set(adisyonelis)
# adisyonelis = list(messi)
# print(adisyonelis)

# =====================================================================================================
# ===============================MASTER DICTIONNAIRE (isinstance, eval)================================
# ================================Exercice 1==========================================================
# Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.

# diksyone = {'messi': 'balondo', 'messi2': 'balondo2'}
# messi= list(diksyone.values())
# print(messi)

# ================================Exercice 2==========================================================
# Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
# chan = input("rantre yn non ::")
# if chan.startswith("{") and chan.endswith("}"):
#     print("li gn akolad ni devan ni deye")
# else:
#     print("pa gn akolad")

# =================================Exercice 3=========================================================
# Pakouri yon diksyonè, epi afiche tout kle yo.
# diksyone = {'leo': 'messi', 'luis': 'suarez'}
# kle = list(diksyone.keys())
# print(kle)

# ================================Exercice 4===========================================================
# Pakouri yon diksyonè, epi afiche tout valè yo.
# diksyone = {'leo': 'messi', 'chritiano': 'Ronaldo', 'neymar': 'junior'}
# toutvale = list(diksyone.values())
# print(toutvale)

# =================================Exercice 5==========================================================
# Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
# diksyone = {'leo': 'messi', 'chritiano': 'Ronaldo', 'neymar': 'junior'}
# diksyonekopi = diksyone.copy()
# print(diksyonekopi)

# ==================================Exercice 6=========================================================
# Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo.
# diksyone = {'leo': 'messi', 'chritiano': 'Ronaldo', 'neymar': 'junior'}
# for kle, vale in diksyone.items():
#     if isinstance(vale, str):
#         diksyone[kle] = f'_{vale}_'
# print(diksyone)

# =====================================Exercice 7=====================================================
# Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. 
# diksyonè_orijinal = {'kle1': '123', 'kle2': '45', 'kle3': '678', 'kle4': '9'}
# nouvo_diksyonè = {}
# for kle, valè in diksyonè_orijinal.items():
#     if valè.isdigit():
#         nouvo_diksyonè[kle] = valè
# print(nouvo_diksyonè)



