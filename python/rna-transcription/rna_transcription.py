def to_rna(dna_strand):

# G -> C
# C -> G
# T -> A
# A -> U

    dict = {"G":"C", "C":"G", "T":"A", "A":"U" }

    rna = ""
    for i in range(0,len(dna_strand)):
        rna += dict[dna_strand[i]]

    return rna
