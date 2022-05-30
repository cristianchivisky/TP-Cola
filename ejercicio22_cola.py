from cola import Cola

class Mcu():
    personaje, superheroe, genero = None, None, None

personajes = ['Tony Stark', 'Steve Rogers', 'Natasha Romanoff', 'Carol Danvers', 'Scott Lang']
superheroes = ['Iron man', 'Capitan America','Black Widow', 'Capitana Marvel', 'Ant-Man']
generos = ['M', 'M', 'F', 'F', 'M']

cola1=Cola()
for i in range(len(personajes)):
    dato = Mcu()
    dato.personaje = personajes[i]
    dato.superheroe = superheroes[i]
    dato.genero = generos[i] 
    print(dato.personaje, dato.superheroe, dato.genero)
    cola1.arribo(dato)
aux=False
aux1=''
while not cola1.cola_vacia():
    dato = cola1.atencion()
    if (dato.superheroe == 'Capitana Marvel'):
        print('Nombre del peronaje de Capitana Marvel: ', dato.personaje)
    if dato.genero == 'F':
        print(dato.superheroe)
    else:
        print(dato.personaje)
    if dato.personaje == 'Scott Lang':
        print('Superheroe correspondiente a Scott Lang: ', dato.superheroe)
    if dato.personaje[0]=='S' or dato.superheroe[0]=='S':
        print(dato.personaje, dato.superheroe, dato.genero)
    if dato.personaje=='Carol Danvers':
        aux=True
        aux1=dato.superheroe
if aux:
    print('Carol Danvers si se encuentra en la cola y su nombre de superheroe es: ', aux1)
else:
    print('Carol Danvers no esta en la cola.')