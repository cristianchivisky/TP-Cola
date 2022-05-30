from cola import Cola
from random import randint

def random_character():
    return chr(randint(65, 70))

cola_turnos = Cola()
cola_1 = Cola()
cola_2 = Cola()

for i in range(10):
    dato = [random_character(), str(randint(0, 9)), str(randint(0, 9)), str(randint(0, 9))]
    dato2=''.join(dato)
    print(dato2)
    cola_turnos.arribo(dato2)
    
cont1=0
cont2=0
cont_a=0
cont_b=0
cont_c=0
cont_d=0
cont_e=0
cont_f=0
while not cola_turnos.cola_vacia():
    dato = cola_turnos.atencion()
    if dato[0] in ["A", "C", "F"]:
        cola_1.arribo(dato)
        print("cola_1: ", dato)
        cont1 += 1
        if dato[0]=="A":
            cont_a += 1
        elif dato[0] == "C":
            cont_c += 1
        else: cont_f += 1
    else:
        cola_2.arribo(dato)
        print("cola_2: ", dato)
        cont2 += 1
        if dato[0]=="B":
            cont_b += 1
        elif dato[0] == "D":
            cont_d += 1
        else: cont_e += 1
    
if cont1 == cont2:
    print("Las colas tienen la misma cant de turnos")
elif cont1 > cont2:
    print("cola_1 tiene mayor cant de turnos")
    if cont_a > cont_c and cont_a > cont_f:
        print("la mayoria de los turnos empieza con A")
    elif cont_a == cont_c and cont_c > cont_f:
        print("la mayoria de los turnos empiezan con A y C ")
    elif cont_a > cont_c and cont_a == cont_f:
        print("la mayoria de los turnos empiezan con A y F")
    elif cont_c > cont_a and cont_c > cont_f:
        print("la mayoria de los turnos empieza con C")
    elif cont_c > cont_a and cont_c == cont_f: 
        print("la mayoria de los turnos empiezan con C y F")
    elif cont_f > cont_a and cont_f > cont_c:
        print("la mayoria de los turnos empieza con F")
    else:
        print("hay la misma cant de furnos A, C y F")
    while not cola_2.cola_vacia():
        dato=cola_2.atencion()
        if int(dato[1:4])>506:
            print(dato)
else:
    print("cola_2 tiene mayor cant de turnos") 
    if cont_b > cont_d and cont_b > cont_e:
        print("la mayoria de los turnos empieza con B")
    elif cont_b == cont_d and cont_b > cont_e:
        print("la mayoria de los turnos empiezan con B y D ")
    elif cont_b > cont_d and cont_b == cont_e:
        print("la mayoria de los turnos empiezan con B y E")   
    elif cont_d > cont_b and cont_d > cont_e:
        print("la mayoria de los turnos empieza con D")
    elif cont_d > cont_b and cont_d == cont_e: 
        print("la mayoria de los turnos empiezan con D y E")
    elif cont_e > cont_b and cont_e > cont_d: 
        print("la mayoria de los turnos empieza con E")
    else: 
        print("hay la misma cant de furnos A, C y F")
    while not cola_1.cola_vacia():
        dato=cola_1.atencion()
        if int(dato[1:4])>506:
            print(dato)
