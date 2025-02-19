#atribuições na função print()

print(23, 45 , 63)
print(13, 25 , 94, sep="-")
print(41, 12 , 36, sep='-', end='.')

#Posso usar tanto aspas simples ou aspas duplas para atribuir
#O 'sep="" ' é separação, é o que posso colocar entre as separações
#O 'end="" ' é o que posso colocar no final.

#\r\n -> CRLF   sistema de quebra de linha automatica do windows antigos.

#\n - > LF      sistema dequebra de linha automatica do mac os, linux e Windows 10 e superior.

print(23, 45 , 63, sep='\n')
print(234, 452 , 243, end='\n\n')
print(23123, 12345 , 65443, end='\n\n\n')