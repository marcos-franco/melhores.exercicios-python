from municipio import Municipio
from distrito import Distrito

municipio1 = Municipio('Rio de Janeiro', 2000000, 80000)
print(municipio1.nome)

distrito1 = Distrito('rua papara ', 'caxias', 30000, 15000)
print(distrito1.enderecoPrefeitura)
print(distrito1.nome)
distrito1.area = 200000
print(distrito1.area)
