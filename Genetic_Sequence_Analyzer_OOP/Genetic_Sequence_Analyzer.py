class Sequence:
    def __init__(self, sequence_id, nucleotides):
        if not all(nucleotide in "ATGC" for nucleotide in nucleotides.upper()):
            raise ValueError("Invalid nucleotides: only A, T, G, C allowed")
        self.sequence_id = sequence_id
        self.nucleotides = nucleotides.upper()

    def gc_content(self):
        if len(self.nucleotides) == 0:
            return 0
        g_count = self.nucleotides.count('G')
        c_count = self.nucleotides.count('C')
        return ((g_count + c_count) / len(self.nucleotides)) * 100

    def is_stable(self):
        return self.gc_content() >= 50

    def get_info(self):
        return {
            "sequence_id": self.sequence_id,
            "nucleotides": self.nucleotides,
            "gc_content": self.gc_content(),
            "stable": self.is_stable()
        }


class MutatedSequence(Sequence):
    def __init__(self, sequence_id, nucleotides, mutation_description):
        super().__init__(sequence_id, nucleotides)
        self.mutation_description = mutation_description

    def get_info(self):
        info = super().get_info()
        info["mutation_description"] = self.mutation_description
        return info


class GeneBank:
    def __init__(self):
        self.sequences = []

    def add_sequence(self, sequence):
        if not isinstance(sequence, Sequence):
            return -1
        self.sequences.append(sequence)

    def list_sequences(self):
        return [sequence.get_info() for sequence in self.sequences]

    def count_stable(self):
        return sum(1 for sequence in self.sequences if sequence.is_stable())



seq1 = Sequence("SEQ001", "ATGCGTAC")
seq2 = Sequence("SEQ002", "ATATATAT")
seq3 = MutatedSequence("SEQ003", "GCGCGC", "Point mutation at position 3")
seq4 = MutatedSequence("SEQ004", "ATGCATGC", "Insertion mutation")
seq5 = Sequence("SEQ005", "GGCCGGCC")


gene_bank = GeneBank()
gene_bank.add_sequence(seq1)
gene_bank.add_sequence(seq2)
gene_bank.add_sequence(seq3)
gene_bank.add_sequence(seq4)
gene_bank.add_sequence(seq5)


print("All Sequences:")
for seq_info in gene_bank.list_sequences():
    print(seq_info)

print("\nNumber of stable sequences:", gene_bank.count_stable())
