from abc import ABC, abstractmethod

 ### MESMA ASSINATURA DE MÉTODO E COMPORTAMENTOS DIFERENTES!

class A(ABC):
    @abstractmethod
    def fala(selfs, msg):
        pass

class B(A):
    def fala(self, msg):
        print(f'B está falando {msg}')

class C(A):
    def fala(self, msg):
        print(f'C está falando {msg}')

b = B()
c = C()
b.fala('UM ASSUNTO')
c.fala('OUTRO ASSUNTO')