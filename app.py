from modelos.restaurante import Restaurante

restaurante_labu = Restaurante('podrão do Labu', 'Podrões')
restaurante_labu.receber_avaliacao('João', 5)
restaurante_labu.receber_avaliacao('Maria', 4)
restaurante_labu.receber_avaliacao('José', 5)
restaurante_labu.alternar_status()
restaurante_candinho = Restaurante('pastelaria do Candinho', 'Pastéis')
restaurante_candinho.receber_avaliacao('Greg', 4.9)
restaurante_novais = Restaurante('restaurante do Novais', 'Comida Caseira')

def main():
    Restaurante.listar_restaurantes()
    print(restaurante_labu)

if __name__ == '__main__':
    main()
