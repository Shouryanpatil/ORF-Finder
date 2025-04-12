from Bio.Seq import Seq
from Bio import SeqIO

def find_orfs(seq):
    protein_set = set()
    stop_codons = ['TAA', 'TAG', 'TGA']
    seq_len = len(seq)

    for strand, nucleotide_seq in [('+', seq), ('-', seq.reverse_complement())]:
        for frame in range(3):
            # Trim to multiple of 3 to avoid warnings
            trimmed_seq = nucleotide_seq[frame:len(nucleotide_seq) - (len(nucleotide_seq) - frame) % 3]
            trans = trimmed_seq.translate(to_stop=False)
            aa_seq = str(trans)

            # Find all start codon positions (M)
            start_positions = [i for i, aa in enumerate(aa_seq) if aa == 'M']
            for start in start_positions:
                protein = ""
                for aa in aa_seq[start:]:
                    if aa == '*':  # Stop codon
                        break
                    protein += aa
                if protein:
                    protein_set.add(protein)
    return protein_set

def main():
    record = SeqIO.read("input.txt", "fasta")  # Make sure input.txt is in same folder
    sequence = record.seq
    proteins = find_orfs(sequence)
    
    with open("output.txt", "w") as f:
        for p in proteins:
            f.write(p + "\n")

if __name__ == "__main__":
    main()
