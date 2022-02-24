lista = [6,4,3,1,2,5]

# ordem crecente
maior = lista[0]
menor = lista[0]

while lista[0] > lista[1]:
    for i in range(0, len(lista)):
        if i+1 > 5:
            break  
        elif lista[i] > lista[i+1]:
            maior = lista[i]
            menor = lista[i+1]
        
            lista[i] = menor
            lista[i+1] = maior         
       
    print(lista)  
