# request the DNA sequence #
raw_sequence= input('raw_sequence: ')

# define the variables for start-end codons #
start_codon = 'ATG'
stop_codon = ['TAA','TAG','TGA']

# find the start codon 'ATG' #
start_codon_position = raw_sequence.find(start_codon)
print(start_codon_position)

# redefine the sequence #
codon_sequence = raw_sequence[(start_codon_position)::]
print(codon_sequence)

start_codon_newposition = codon_sequence.find(start_codon)
print(start_codon_newposition)

# find if an Open Reading Frame exists #
if start_codon_position != -1:
  for triplet in stop_codon: 
    stop_codon_position = codon_sequence.find(triplet)
    print(stop_codon_position)
    if (start_codon_newposition) < (stop_codon_position) and ((stop_codon_position) - (start_codon_newposition)) %3 == 0:         
      print("ORF found")    
    else: 
      print("ORF not found")
else:
  print("Coding sequence NOT found")
    



    