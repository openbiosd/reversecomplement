'''
Find reverse-complement of a strand of DNA
'''

alt_map = {'ins':'0'}
complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'} 

def reverse_complement(seq):    
    for k,v in alt_map.items():
        seq = seq.replace(k,v)
    bases = list(seq) 
    bases = reversed([complement.get(base,base) for base in bases])
    bases = ''.join(bases)
    for k,v in alt_map.items():
        bases = bases.replace(v,k)
    return bases
   
f_inname = input('Enter file name: ')
try:
    f_inhandle = open(f_inname, 'r')
except:
    print('File cannot be opened: ', f_inname)
    exit() 
seq = f_inhandle.read() # TCGGinsGGCC

f_outname = 'reverse_complement.txt'
try:
    f_outhandle = open(f_outname, 'x')
except:
    print('Generated file cannot be created: ', f_outhandle)
    exit()
    
seq_revcomp = f_outhandle.write(reverse_complement(seq))
