#definindo a classe (entidade)
class Carro:
        #Construtor (exec. quando é criado o objt)
    def __init__(self, marca, placa, ano, modelo):
        print("novo carro criado")
        self.marca = marca
        self.placa = placa
        self.ano = ano 
        self.modelo = modelo
        self.velocidadeAtual = 0
    
    def descrever(self):
        print(f"{self.marca}")
        print(f"{self.placa}")
        print(f"{self.ano}")
        print(f"{self.modelo}")

    def acelerar(self, novaVelocidade):
        for i in range(novaVelocidade):
            self.velocidadeAtual +=1
            print(f"Acelerando... {self.modelo} - {self.velocidadeAtual}")

class CarroEsportivo(Carro):
    def acelerar(self, novaVelocidade):
        for i in range(0, novaVelocidade, 5):
            self.velocidadeAtual +=5
            print(f"Acelerando... {self.modelo} - {self.velocidadeAtual} Km/h")            

# criando um objt carro   
fusca = Carro("Volks", "1234", "1970", "1.3") 
gol = Carro("Volks", "5678", "2004", "goleta bola")
Civic = Carro("honda", "8765", "2019", "touring 1.5")
corolinha = Carro("toyota", "4321", "2024", "carro bixo")
Uno = Carro("fiat", "1594", "1990", "com escada")

bugatti = CarroEsportivo("bugatti", "serámeu", "2026", "chiron")

bugatti.acelerar(100)
Uno.acelerar(100)

