class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # Método title() deixa a primeira letra de cada palavra maiúscula
        self._categoria = categoria.upper() # Método upper() deixa todas as letras maiúsculas
        self._status = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'Nome: {self.nome} Categoria: {self.categoria} Status: {self.status}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'\n| {'Nome:':<30} | {'Categoria:':<30} | {'Status:':<30}')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante.nome:<30} | {restaurante.categoria:<30} | {restaurante.status:<30}') 

    @property
    def status(self):
        return 'Aberto' if self._status else 'Fechado'

restaurante_labu = Restaurante('podrão do Labu', 'Podrões')
restaurante_candinho = Restaurante('pastelaria do Candinho', 'Pastéis')

Restaurante.listar_restaurantes()

