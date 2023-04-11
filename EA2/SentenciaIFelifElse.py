# if elif else

# candidato1 candidato2 nulo/blanco
print("Ingrese su voto:")
print("[1] candidato 1 [2] candidato 2 [3] nulo o blanco")
voto = input("Ingrese su voto:") # input devuelve str (String)
voto = int(voto) # convertir string (str) a entero o int
c1 = 0
c2 = 0
nb = 0

if voto == 1:
    c1 = c1 + 1 # contador
elif voto == 2:
    c2 = c2 + 1
elif voto == 3:
    nb = nb + 1

if voto == 1:
    c1 = c1 + 1 # contador
elif voto == 2:
    c2 = c2 + 1
else:
    nb = nb + 1

print(f"Candidato 1: {c1} \nCandidato 2: {c2} \nNulo/Blanco: {nb} \n")