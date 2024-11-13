
#mosre-me as seguintes listas,derivadas de:
    #[0,1,2,3,4,5,6,7,8,9,0,10,11,12,13,14,15]
    #intervalo de 1 a 9 
numeros = list(range(1, 10))
print(numeros)

    #intervalo de 8 a 13
for i in range(8, 14):
    print(i)

    #números pares
numeros_pares = list(range(0, 16, 2))
print(numeros_pares)

    #números ímpares
for i in range(1, 16, 2):
    print(i)


    #razão entre a soma e o intervalo de 10 a 15 pelo intervalo de 3 a 9 em float!

soma_intervalo_10_15 = sum(range(10, 16)) 
soma_intervalo_3_9 = sum(range(3, 10))
razao = soma_intervalo_10_15 / soma_intervalo_3_9
print(float(razao))