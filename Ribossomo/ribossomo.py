RNAm = 'GGC.CGA.UUA.AUG.CUU.AAA.UGC.GGC.CUA.AAU.UAU'

print('\nRNA mensageiro a ser comparado com o codigo genetico:\n-> {}'.format(RNAm))

geneticCode = {
'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L',
'UCU':'S', 'UCC':'S', 'UCA':'L', 'UCG':'L',
'UAU':'Y', 'UAC':'Y', 'UAA':'ST', 'UAG':'ST',
'UGU':'C', 'UGC':'C', 'UGA':'ST', 'UGG':'W',
'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L',
'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q',
'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R',
'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M',
'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K',
'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R',
'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V',
'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E',
'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G'
}

rnaStr = RNAm.split('.')

ribossomo = ''

for codon in rnaStr:    # Para cada codon do RNA mensageiro
    for i in geneticCode.keys():    # Para cada uma das chaves do dicionario
        if (i == codon):
            ribossomo += geneticCode.get(i) # Se forem iguais, adiciona-se o valor na variavel ribossomo
            break

print('\n\nRibossomo resultante:\n-> {}\n\n'.format(ribossomo))