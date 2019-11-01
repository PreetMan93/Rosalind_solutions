with open('sample_data.txt') as dna_sequences:
    a, b = [seq.strip() for seq in dna_sequences]
    
print(sum ( a[i] != b[i] for i in range(len(a))))