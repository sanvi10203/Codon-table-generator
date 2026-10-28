codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

print(codon_table)
print("Total number of codons:", len(codon_table))
print("Codons:", list(codon_table.keys()))
print("Amino acids:", list(codon_table.values()))

print("\nSTANDARD CODON TABLE")
print("--------------------")

for codon, amino_acid in codon_table.items():
    print(codon, ":", amino_acid)

sequence_type = input(
    "\nEnter sequence type (DNA or RNA): "
).upper().strip()

sequence = input("Enter your sequence: ").upper().strip()

if sequence_type == "RNA":
    sequence = sequence.replace("U", "T")

elif sequence_type != "DNA":
    print("Invalid sequence type. Enter DNA or RNA.")
    exit()

#Divide the sequence into codons
codons = []
for i in range(0, len(sequence), 3):
    codon = sequence[i:i + 3]
    codons.append(codon)

#Translate the codons
amino_acids = []
start_codons = []
stop_codons = []

for codon in codons:

     if len(codon) < 3:
         amino_acids.append("Incomplete codon")

     else:
         amino_acid = codon_table[codon]
         amino_acids.append(amino_acid)

     if codon == "ATG":
        start_codons.append(codon)
        
     elif codon == "TAA" or codon == "TAG" or codon == "TGA":
        stop_codons.append(codon)

#Check for incomplete codon
if len(sequence) % 3 != 0:
    print("Warning: Incomplete codon at the end.")
else:
 print("All codons contain three nucleotides.")


#Display the results
print("\n===== TRANSLATION RESULTS =====")
print("Sequence:", sequence)
print("Codons:", " - ".join(codons))
print("Amino acids:", " - ".join(amino_acids))


