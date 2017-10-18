# packing
def new_user(name, age):
    print('Nome: %s Idade: %s' % (name, age))

aluno_1 = {'name': 'Pedro Silva', 'age': 25}
aluno_2 = ['Pedro Silva', 25]

new_user(**aluno_1)
new_user(*aluno_2)


# unpacking
def new_user_loop(*args):
    for i in range(len(args)):
        for j in range(len(args[i])):
            print(args[i][j])

aluno_3 = [['Pedro', 25], ['Maria', 45], ['Tiago', 55]]
aluno_4 = ['Pedro', 'Tiago', 'Maria']

new_user_loop(aluno_3)

print(__name__)