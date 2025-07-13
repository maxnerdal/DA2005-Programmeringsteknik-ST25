# √ 5.5.1 Uppgift 1: Definiera en klass för DNA-sekvenser
# √ 5.5.2 Uppgift 2: Läs in DNA-sekvenser från en fil
# √ 5.5.3 Uppgift 3: Hitta överlappningar mellan DNA-sekvenser
# √ 5.5.4 Uppgift 4: Hitta överlappningar mellan DNA-sekvenser 2
import dna

def main():
    """Main function to test the DNA sequence class and its methods. """
    print("")
    print("Testing the DnaSeq class:")
    dna.test_all()
    
    #dnafile = 'ex0.fa'
    dnafile = 'ex1.fa'
    #dnafile = 'ex2.fa'
    print("")

    dna_list = dna.read_dna(dnafile)

    print(f"Number of sequences in {dnafile}: {len(dna_list)}")
    for obj in dna_list:
        print("Checking DnaSeq objects in dna_list:")
        print(f"accession: {obj.accession}, seq: {obj.seq}")
    print("")
    
    dna_overlap_dict = dna.overlaps(dna_list, dna.check_exact_overlap)

    print("Printing the dna_overlap_dict:")
    for accession, overlap_dict in dna_overlap_dict.items():
        print(f"Accession: {accession}")
        for key, value in overlap_dict.items():
            print(f"    accession: {key}, overlap: {value}")
    print("")
if __name__ == "__main__":
    main()