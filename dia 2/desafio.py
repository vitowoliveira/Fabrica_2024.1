#crie uma classe (Animal, Som) e faça uma relação entre elas 
#Definindo uma classe "Animal e uma função para emitir os sons do Animal"

#Definindo outra subclasse "Cachorro" que herda de "Animal"

#Definindo outra subclasse "Gato" que herda de "Animal"

#Criando instancias das classes

#Chamando métodos

class Animal:
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade= idade

class Gato(Animal):
    def miau(self):
        print(f"o seu gato {self.nome} que tem {self.idade} faz miau")

class Cachorro(Animal):
    def auau (self):
        print(f"O seu cachorro {self.nome} que tem {self.idade}faz auau")

meu_cachorro = Cachorro("theo", "1 ano")   
meu_cachorro.auau()

meu_gato = Gato("Xano","4 anos")
meu_gato.miau()


        

