def compute_gc_content(fasta_file):
    with open(fasta_file) as fasta_file:
        max_id , max_gc = '', 0

        #Read ID of first sequence
        formatted_fasta = fasta_file.readline().rstrip()
        while formatted_fasta:

            #Curr_sequence = ID of sequence, sequence is empty
            curr_sequence , sequence = formatted_fasta[1:], ''

            #Read sequence
            formatted_fasta = fasta_file.readline().rstrip()

            #While the line isn't an ID , add it to the sequence
            while formatted_fasta and not formatted_fasta[0] == '>':
                sequence = sequence + formatted_fasta
                formatted_fasta = fasta_file.readline().rstrip()
            
            #compute GC content of sequence, and compare to max gc content
            curr_gc_content = (sequence.count('C') + sequence.count('G')) / len(sequence)
            if curr_gc_content > max_gc:
                max_id , max_gc = curr_sequence, curr_gc_content

    #print te max GC content, and the ID that it belongs to            
    print('%s\n%.6f%%' % (max_id, max_gc * 100))

compute_gc_content('sample_data.txt')