class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, personagem):
        dano = self.ataque - personagem.defesa
        if dano < 0:
            dano = 0
        personagem.vida -= dano
        print(
            f"{self.nome} atacou {personagem.nome} "
            f"e causou {dano} pontos de dano."
        )

    def esta_vivo(self):
        return self.vida > 0


class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 100, 10, 5)


class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, 80, 5, 3)

    def lancar_magia(self, personagem):
        dano = self.ataque * 2 - personagem.defesa
        if dano < 0:
            dano = 0
        personagem.vida -= dano
        print(f"{self.nome} lançou uma magia em {personagem.nome} e causou {dano} pontos de dano.")
        
guerreiro = Guerreiro("Leônidas")
mago = Mago("Merlin")

while guerreiro.esta_vivo() and mago.esta_vivo():
    guerreiro.atacar(mago)
    mago.lancar_magia(guerreiro)

if guerreiro.esta_vivo():
    print(f"{guerreiro.nome} venceu.")
else:
    print(f"{mago.nome} venceu.")
    