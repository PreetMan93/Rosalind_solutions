#variables for translation mapping
bases = 'ATCG'
complementary_bases = 'TAGC'

#open and read sample data
with open('sample_data.txt') as file:
    dna_strand = file.read()

#reverse the dna_strand
reverse_strand = (dna_strand[::-1])

#create translation mapping
translation_mapping = reverse_strand.maketrans(bases,complementary_bases)

#use translation map to create complement strand
complement_strand = reverse_strand.translate(translation_mapping)

print(complement_strand)
