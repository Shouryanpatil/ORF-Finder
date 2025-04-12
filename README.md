# ORF Finder (Open Reading Frame Extractor)

This Python script identifies all **distinct candidate protein strings** from open reading frames (ORFs) in a DNA sequence. It reads a DNA string in FASTA format, processes all 6 possible reading frames (3 forward, 3 reverse complement), and outputs all possible protein strings that begin with a start codon and end at a stop codon.

---

## 🧬 Features
- Supports sequences up to 1kb in length.
- Analyzes all 6 reading frames.
- Uses Biopython for sequence handling and translation.
- Automatically removes Biopython warnings by trimming sequences.
- Outputs all unique protein strings.

---

## 📂 Files
- `orf_solver.py`: Main Python script.
- `input.txt`: Input DNA sequence in FASTA format.
- `output.txt`: Output file containing protein strings.

---

## 🚀 Usage

### 1. Install Requirements
```bash
pip install biopython
```

### 2. Add Input
Create a file called `input.txt` with a DNA sequence in FASTA format. Example:

```txt
>Example_DNA
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG
```

### 3. Run the Script
```bash
python orf_solver.py
```

### 4. Check Output
Open `output.txt` to see the resulting protein strings.

---

## 📖 How It Works
- Translates the input sequence in all six reading frames.
- Searches for every subsequence that starts with `M` (start codon) and ends at `*` (stop codon).
- Extracts and stores all unique protein strings.

---

## 🧠 Example Output
```
M
MGMTPRLGLESLLE
MLLGSFRLIPKETLIQVAGSSPCNLS
MTPRLGLESLLE
```

---

## 🧪 Tech Stack
- Python 3
- Biopython

---

## 📜 License
MIT License
