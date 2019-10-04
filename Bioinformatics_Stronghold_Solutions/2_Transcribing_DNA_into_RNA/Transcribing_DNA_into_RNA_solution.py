with open('sample_data.txt') as file:
    dna_sequence = file.read()
rna_sequence = dna_sequence.replace("T","U")
print(rna_sequence)