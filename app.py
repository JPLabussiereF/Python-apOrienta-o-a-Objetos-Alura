from modelos.restaurante import Restaurante

restaurante_labu = Restaurante('podrão do Labu', 'Podrões')
restaurante_labu.receber_avaliacao('João', 5)
restaurante_labu.receber_avaliacao('Maria', 4)
restaurante_labu.receber_avaliacao('José', 3)
# restaurante_labu.alternar_status()
# restaurante_candinho = Restaurante('pastelaria do Candinho', 'Pastéis')
# restaurnte_novais = Restaurante('restaurante do Novais', 'Comida Caseira')


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()