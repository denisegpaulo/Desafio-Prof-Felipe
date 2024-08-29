class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo


    def atacar(self):
        if self.tipo == "mago":
            ataque = "magia"
        elif self.tipo == "guerreiro":
            ataque = "espada"
        elif self.tipo == "monge":
            ataque = "artes marciais"
        elif self.tipo == "ninja":
            ataque = "shuriken"
        else:
            ataque = "ataque desconhecido"        

        print(f"O {self.tipo} atacou usando {ataque}.")

heroi1 = Heroi("Aragorn", 87, "guerreiro")
heroi2 = Heroi("Gandalf", 2019, "mago")
heroi3 = Heroi("Buda", 2000, "monge")
heroi4 = Heroi("Naruto", 4000, "ninja")
heroi5 = Heroi("Saruman", 3000, "mago")
heroi6 = Heroi("Denise", 3000, "Estudante")


heroi1.atacar()  
heroi2.atacar()
heroi3.atacar()
heroi4.atacar()
heroi5.atacar()
heroi6.atacar()