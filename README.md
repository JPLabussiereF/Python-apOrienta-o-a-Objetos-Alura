# Projeto de Restaurante
Este projeto Python implementa um sistema de gerenciamento de restaurantes com funcionalidades como cadastro, avaliações e exibição de status.
## Estrutura do Projeto
A organização dos arquivos do projeto é a seguinte:
```
/restaurante-projeto
├── desafios/               # Pasta com desafios do projeto
├── modelos/                # Módulos do projeto
│   ├── avaliacao.py         # Classe Avaliacao
│   ├── restaurante.py       # Classe Restaurante
├── app.py                  # Arquivo principal de execução
├── .gitignore               # Arquivo para ignorar arquivos desnecessários
├── README.md                # Documentação do projeto
```
## Dependências
O projeto é escrito em Python e não requer dependências adicionais. Basta ter Python instalado na máquina.
## Funcionalidades
### 1. Classe Restaurante
A classe `Restaurante` permite:
- Cadastro de restaurantes com nome e categoria.
- Alternar status entre aberto e fechado.
- Receber avaliações de clientes.
- Calcular a média das avaliações.
Exemplo de uso:
```
from modelos.restaurante import Restaurante

restaurante = Restaurante('Pizza do Chef', 'Pizzaria')
restaurante.receber_avaliacao('Carlos', 5)
restaurante.alternar_status()
print(restaurante)
```
### 2. Classe Avaliacao
A classe `Avaliacao` representa a avaliação de um cliente para um restaurante.
Exemplo de uso:
```
from modelos.avaliacao import Avaliacao

avaliacao = Avaliacao('Julia', 4.5)
print(avaliacao.cliente)
print(avaliacao.nota)
```
### 3. Execução Principal (`app.py`)
O arquivo app.py contém exemplos de uso do sistema, incluindo a criação de restaurantes e avaliações.
```
from modelos.restaurante import Restaurante

restaurante_labu = Restaurante('podrão do Labu', 'Podrões')
restaurante_labu.receber_avaliacao('João', 5)
restaurante_labu.alternar_status()

def main():
    Restaurante.listar_restaurantes()
    print(f'\n{restaurante_labu}')

if __name__ == '__main__':
    main()
```
## Como Executar o Projeto

1. Clone este repositório:
```
git clone https://github.com/seu-usuario/restaurante-projeto.git
```
2. Navegue até o diretório do projeto:
```
cd restaurante-projeto
```
3. Execute o arquivo principal:
```
python app.py
```

## Contribuição
Contribuições são bem-vindas! Caso tenha alguma ideia ou encontre um problema, fique à vontade para abrir uma issue ou enviar um pull request.

## Créditos
- Desenvolvido como parte do curso da Alura sobre Python.
