with open('sample_data.txt') as file:
    dna_sequence = file.read()
bases = dna_sequence.count('A'), dna_sequence.count('C'), dna_sequence.count('G'), dna_sequence.count('T')
print(bases[0], bases[1], bases[2], bases[3])