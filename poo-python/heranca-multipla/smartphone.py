from eletronico import *
from log import LogMixin
### Classe de login foi inserida para ser herdada também no smartphone:
class Smartphone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            info = f'{self._nome} não está ligado!'
            print(info)
            self.log_info(info)
            return
        if self._conectado:
            error = f'{self._nome} JÁ ESTÁ CONECTADO!'
            self.log_error(error)
            return
        info = f'{self._nome} ESTÁ CONECTADO!'
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._conectado:
            error = f'{self._nome} NÃO ESTÁ CONECTADO.'
            print(error)
            self.log_error(error)
            return

        info = f'{self._nome} está desligado.'
        print(info)
        self.log_info(info)
        self._conectado = False

