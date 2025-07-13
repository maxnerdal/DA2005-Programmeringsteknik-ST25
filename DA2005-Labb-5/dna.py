class DnaSeq:
    def __init__(self, accession, seq):
        """Initializes a DnaSeq object with an accession number and a sequence."""
        # Ensure that both accession and seq are non-empty strings
        if not accession or not seq:
            raise ValueError("Both accession and seq must be non-empty")
        # Check that accession and seq are ia able to be converted to strings
        try:
            self.accession = str(accession)
            self.seq = str(seq)
        except Exception as e:
            raise ValueError("Both accession and seq must be non-empty strings")

    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return f'<DnaSeq accession={self.accession}>'



def read_dna(filename):
    """
    takes a filename as input and returns a list of dna objects
    """
    result = []
    try:
        with open(filename, 'r') as infile:
            accession = None
            seq = None
            for line in infile:
                line = line.strip()
                if line.startswith('>'):
                    accession = line[1:]  # set accession to line without '>' character
                elif accession is not None: # if accession is set, it means we are reading a sequence
                    seq = line
                    result.append(DnaSeq(accession, seq)) # create a new DnaSeq object and append it to the result list
                    accession = None  # Reset for next pair
        return result
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return []


def check_exact_overlap(dnaobj1, dnaobj2, min_overlap = 10):
    """ Check if two DnaSeq objects have an exact overlap at the end of the first sequence """
    i = min(dnaobj1.__len__(), dnaobj2.__len__())  # Get the length of the shorter sequence
    overlap_count = 0
    while i > 0:
        if dnaobj1.seq[dnaobj1.__len__() - i:] == dnaobj2.seq[:i]:  # Check if the end of dnaobj1.seq overlaps with the start of dnaobj2.seq
            overlap_count = i
            break
        i -= 1
    return overlap_count if overlap_count >= min_overlap else 0



def overlaps(dna_list,function):
    """    
        Takes a list of DnaSeq objects and a function to check for overlaps.
        Returns a dictionary where the keys are accession numbers and the values are dictionaries of overlapping sequences.
    """
    d_overlaps = {}
    for obj1 in dna_list: # Iterate through each DnaSeq object in the list
        for obj2 in dna_list: # Iterate through each DnaSeq object in the list again
            if not obj1.accession == obj2.accession:  # Skip self-comparison
                overlap = function(obj1, obj2)  # Call the function to check for overlap
                if overlap:  # If there is an overlap
                    if obj1.accession not in d_overlaps:  # if obj1 not in d_overlaps, create a new dict for it
                        d_overlaps[obj1.accession] = {}
                    d_overlaps[obj1.accession][obj2.accession] = overlap  # add the overlap length to the dict
    return d_overlaps

#
# Testing code. You should not change any line after this one!
#
def test_class_DnaSeq():
    s1 = DnaSeq('s1', 'ACGT')
    s2 = DnaSeq('s2', 'ATGTTTGTTTTTCTTGTTTTATTGCCACTAGTCTCTAGTCAGTGTGTTAATCTTACAACCAGAACTCAAT')
    assert len(s1) == 4, 'Your length method (__len__) is not correct.'
    assert len(s2) == 70, 'Your length method (__len__) is not correct.'

    assert str(s1) == '<DnaSeq accession=s1>', 'The __str__ method is not following the specification.'
    assert str(s2) == '<DnaSeq accession=s2>', 'The __str__ method is not following the specification.'

    # The rest of this function is verifying that we are indeed raising an exception.
    status = 0
    try:
        s3 = DnaSeq('', 'ACGT')
    except ValueError:
        status += 1
    try:
        s3 = DnaSeq('s3', None)
    except ValueError:
        status += 1

    try:
        s3 = DnaSeq(None, '')
    except ValueError:
        status += 1
    if status != 3:
        raise Exception('class DnaSeq does not raise a ValueError '
                        'exception with initialised with empty '
                        'accession and sequence.')
    print('DnaSeq passed')


def test_reading():
    dna1 = read_dna('ex1.fa')
    assert len(dna1) == 6, 'The file "ex1.fa" has exactly 6 sequences, but your code does not return that.'
    assert list(map(lambda x: x.accession, dna1)) == [f's{i}' for i in range(6)], 'The accessions are not read correctly'
    print('read_dna passed')

def test_overlap():
    s0 = DnaSeq('s0', 'AAACCC')
    s1 = DnaSeq('s1', 'CCCGGG')
    s2 = DnaSeq('s2', 'TTTTCC')
    data1 = [s0, s1, s2]
    assert check_exact_overlap(s0, s1, 2) == 3
    assert check_exact_overlap(s0, s1) == 0
    assert check_exact_overlap(s1, s2, 2) == 0
    assert check_exact_overlap(s2, s1, 2) == 2

    res0 = overlaps(data1, lambda s1, s2: check_exact_overlap(s1, s2, 2))
    assert len(res0) == 2, 'You get the wrong number of overlaps'
    assert res0 == {'s0': {'s1': 3}, 's2': {'s1': 2}}

    dna_data = read_dna('ex1.fa')
    res1 = overlaps(dna_data, check_exact_overlap)
    assert len(res1) == 5
    for left, right in [('s0', 's1'), ('s1', 's2'), ('s2', 's3'), ('s3', 's4'), ('s4', 's5')]:
        assert res1[left][right], f'Missing overlap of {left} and {right} (in that order)'
    print('overlap code passed')



def test_all():
    test_class_DnaSeq()
    test_reading()
    test_overlap()
    print('Yay, all good')
