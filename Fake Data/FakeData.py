from faker import Faker

# Inicializa a lib
fake = Faker()

# Cria variaveis com dados falsos
nome = fake.name()
primeiro_nome_fem =fake.first_name_female()
usuario = fake.user_name()
senha = fake.password()
mes = fake.month()


print( f'Nome: {nome}')
print(f'Nome Feminino: {primeiro_nome_fem}')
print(f'Usuario: {usuario}')
print(f'Senha: {senha}')
print(f'Mes: {mes}')

