from modelos.avaliacao import Avaliacao

class Restaurante:

    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() # Método title() deixa a primeira letra de cada palavra maiúscula
        self._categoria = categoria.upper() # Método upper() deixa todas as letras maiúsculas
        self._status = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    @property
    def nome(self):
        return self._nome
    def categoria(self):
        return self._categoria

    def __str__(self):
        return f'Nome: {self._nome} | Categoria: {self._categoria} | Status: {self.status} | Avaliação: {self.media_avaliacoes}'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'\n| {'Nome:':<30} | {'Categoria:':<30} | {'Status:':<30} | {'Avaliação:':<30} |')
        for restaurante in cls.restaurantes:
            print(f'| {restaurante._nome:<30} | {restaurante._categoria:<30} | {restaurante.status:<30} | {restaurante.media_avaliacoes:<30} |') 

    @property
    def status(self):
        return 'Aberto' if self._status else 'Fechado'

    def alternar_status(self):
        self._status = not self._status
    
    def receber_avaliacao(self, cliente, nota):
        if nota < 0.0 or nota > 5.0:
            raise ValueError("A nota deve ser um valor entre 0.0 e 5.0!")
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return 'Restaurante sem Avaliações'
        soma_das_notas = sum(avaliacao.nota for avaliacao in self._avaliacao)
        quantidade_de_avaliacoes = len(self._avaliacao)
        media_das_notas = round(soma_das_notas / quantidade_de_avaliacoes, 1)
        return f'{'★' * int(media_das_notas)} {media_das_notas}'

