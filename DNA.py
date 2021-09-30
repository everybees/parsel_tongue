# method to read the nucleotide sequence file by passing file_name parameter

def read_dna_seq(file_name):
    # This method reads the dna sequence from the file downloaded from NCBI and crates a python dictionary.
    fil = open(file_name,'r')
    fil_list = fil.readlines()
    fil.close
    
    genome = {}
    gene_name = ''
    protein_name = ''
    gene_seq = ''
    for i in fil_list:
        if i[0] == '>':
            # Reads each line from the file and creates a dictionary with the following information for each
            # gene. {<'gene_name-1'>:[<protein_name>,nucleotide sequence],
            #        <'gene_name-2'>:[<protein_name>,nucleotide sequence],
            #        <'gene_name-2'>:[<protein_name>,nucleotide sequence]}
            if list(genome.keys()) != []:
                gene_seq = gene_seq.replace('\n','')
                genome[gene_name].append(gene_seq)
            gene_seq = ''
            g_st = i.find('[gene=')
            g_end = i[g_st:].find(']')
            p_st = i.find('[protein=')
            p_end = i[p_st:].find(']') 

            if g_st > 0 and g_end > 0:
                gene_name = i[g_st+1:g_st+g_end]
                genome[gene_name] = []
            
            if p_st > 0 and p_end > 0:
                protein_name = i[p_st+1:p_st+p_end]
                genome[gene_name].append(protein_name)
        else:
            gene_seq += i
    gene_seq = gene_seq.replace('\n','')
    genome[gene_name].append(gene_seq)    
    return genome