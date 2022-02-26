class Ventilador:
   # atributos
   """
   voltagem =   0
   velocidade = 0
   ligado = False
   """
   # init permite passagem de parametros 
   # na hora de instanciar uma classe
   # permite que o obj receba argumentos
   # armazenando os valores nos atributos
   # conhecido como constructor
   def __init__(self, volt=0, vel=0, lig=0): # defualt prameters
       self.voltagem = volt
       self.velocidade = vel
       self.ligado = lig
       
       # self placeholder para o nome
       # do objeto instanciado
       # v1 = Ventilador(120, 2, True)
       # v1.voltagem = volt = 120
       
   # metodo    
   def ligar(self):
       self.ligado = True
      #v1.ligado = True
   def desligar(self):
       self.ligado = False
      #v1.ligado = False
   def rotacao(self, v):
       self.velocidade = v
      #v1.velocidade = v
   
   # status
   def status(self):
       print(f"{self.velocidade}")
               #v1.velocidade
       print(f"{self.voltagem}")
               #v1.voltagem
       print(f"{self.ligado}")
               #v1.ligado

# sem constructor __init__(self)
"""
v1 = Ventilador() # instanciando sem argumentos
v1.voltagem = 120 # contruindo
v1.velocidade = 2 # construindo
v1.ligado = True  # construindo
v1.status() # method
"""

# com constructor __init__(self)
v2 = Ventilador(120, 3, True) # instanciando com argumentos
v2.status()
v2.desligar()
v2.rotacao(0)
v2.status()

