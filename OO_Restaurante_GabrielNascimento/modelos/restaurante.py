
class Restaurante:
    nome=''
    categoria='churrascaria'
    ativo=False


restaurante_praca=Restaurante()
restaurante_praca.nome='Praça'
restaurante_praca.categoria='Gourmet'

restaurante_pizza=Restaurante()


restaurantes=[restaurante_praca,restaurante_pizza]


restaurante_praca.categoria='Italiana'
print(restaurante_praca.categoria)
print('')


nome_restaurante=restaurante_praca.nome
print(nome_restaurante)
print('')


if restaurante_praca.ativo:
    print('O resturante está ativo')
else:
    print('O restaurante está inativo')
print('')


categoria=Restaurante.categoria
print(categoria)
print('')


restaurante_praca.nome='Bistrô'
print(restaurante_praca.nome)
print('')


restaurante_pizza.nome='Pizza Place'
restaurante_pizza.categoria='Fast Food'
print(vars(restaurante_pizza))
print('')


if restaurante_pizza.categoria=='Fast Food':
    print('A categoria é fast food')
else:
    print('A categoria não é fast food')

print('')


restaurante_pizza.ativo=True
print(restaurante_pizza.ativo)
print('')


print(f'Nome: {restaurante_praca.nome} e a categoria: {restaurante_praca.categoria}')


