# Disciplina: Bioinformática
# Professor: Luiz Cláudio Demes
# Aluno: Hilderlan

######### Programa que faz a transcrição de DNA para RNAm ##########

arq = open('input.txt', 'r')

dna = arq.read()

arq.close()

rna = ''

print('Molécula de DNA a ser transcrita: {}'.format(dna))

for i in dna:
    if (i == 'A'):
        rna += 'U'
    elif (i == 'T'):
        rna += 'A'
    elif (i == 'G'):
        rna += 'C'
    elif (i == 'C'):
        rna += 'G'
    else:
        rna += ''

print('̣O resultado da transcrição está no arquivo output.txt!')

arq = open ('output.txt', 'w')

arq.write(rna)

arq.close()