arquivo = open('README.txt', 'w')

arquivo.write('Curso Python\n')
arquivo.write('Esses README foi criado no arquivo "TesteGravar"\nOs códigos desse repositório são de um curso que realizei para me introduzir na linguagem Python!')
arquivo.close()

leitura = open('README.txt', 'r')
print(leitura.read())
leitura.close()