
from modelos.restaurante4 import Restaurante


restaurante_praca=Restaurante('praça','gourmet')
restaurante_mexicano=Restaurante('mexican food','mexicana')
restaurante_japones=Restaurante('japa','japonesa')



restaurante_japones.alternar_estado()


# criando avaliações para o restaurante praça
restaurante_praca.receber_avaliacao('Albino',8)
restaurante_praca.receber_avaliacao('Berenice',5.5)





def main():
    
    Restaurante.listar_restaurantes()
    

if __name__=='__main__':
    main()