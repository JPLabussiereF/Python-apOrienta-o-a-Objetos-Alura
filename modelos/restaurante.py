from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # Método title() deixa a primeira letra de cada palavra maiúscula
        self._categoria = categoria.upper() # Método upper() deixa todas as letras maiúsculas
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} Categoria: {self.categoria} Status: {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'\n| {'Nome:':<30} | {'Categoria:':<30} | {'Status:':<30}')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome:<30} | {restaurante._categoria:<30} | {restaurante.status:<30}') 

    @property
    def status(self):
        return 'Aberto' if self._status else 'Fechado'

    def alternar_status(self):
        self._status = not self._status
    
    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

