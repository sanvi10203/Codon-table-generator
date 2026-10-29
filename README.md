# 🧬 Codon Table Generator

A beginner-friendly Python program that stores the **standard genetic code (all 64 codons)**, takes a **DNA or RNA sequence** from the user, splits it into **codons**, and translates each codon into its **amino acid**. It also reports **start codons**, **stop codons** and any **incomplete codon** at the end of the sequence.

---

## Background

| Term | Meaning |
|---|---|
| **DNA** | Sequence of the bases **A, T, G, C** |
| **RNA** | Same as DNA but **thymine (T)** is replaced by **uracil (U)** |
| **Codon** | A group of **3 nucleotides**; 4 × 4 × 4 = **64** possible codons |
| **Amino acid** | The building block of proteins; each codon codes for one |
| **Start codon** | `ATG` (`AUG` in RNA), codes for **Methionine** and starts translation |
| **Stop codons** | `TAA`, `TAG`, `TGA` (`UAA`, `UAG`, `UGA` in RNA); they end translation |

---

## Features

- ✅ Dictionary (`codon_table`) containing **all 64 codons** and their amino acids
- ✅ Prints the full codon table
- ✅ Accepts **DNA or RNA** input (RNA is converted by replacing `U` with `T`)
- ✅ Input is converted to upper case, so `atggct` works too
- ✅ Divides the sequence into **groups of three nucleotides**
- ✅ Translates each codon into its **amino acid**
- ✅ Identifies **start codon (ATG)** and **stop codons (TAA, TAG, TGA)**
- ✅ Detects and labels an **incomplete codon** at the end

---

## Requirements

- **Python 3.6 or later**
- No external libraries (standard library only)

---

## How to Run

1. Save the code as `python_project.py`.
2. Open a terminal in that folder and run:

```bash
python python_project.py
```

3. When prompted, enter:
   - the **sequence type**: `DNA` or `RNA`
   - the **sequence**, e.g. `ATGGCTTTTTAA`

---

## Example Runs

### 1. DNA sequence (the sample from the project brief)

```
Enter sequence type (DNA or RNA): DNA
Enter your sequence: ATGGCTTTTTAA
All codons contain three nucleotides.

===== TRANSLATION RESULTS =====
Sequence: ATGGCTTTTTAA
Codons: ATG - GCT - TTT - TAA
Amino acids: Methionine - Alanine - Phenylalanine - Stop
Start codon(s): ATG
Stop codon(s): TAA
```

### 2. RNA sequence with an incomplete codon

```
Enter sequence type (DNA or RNA): RNA
Enter your sequence: AUGGCUUAAGG
Warning: Incomplete codon at the end.

===== TRANSLATION RESULTS =====
Sequence: ATGGCTTAAGG
Codons: ATG - GCT - TAA - GG
Amino acids: Methionine - Alanine - Stop - Incomplete codon
Start codon(s): ATG
Stop codon(s): TAA
```

> The RNA input is converted to DNA internally (`U → T`), so the results are displayed with `T`.

### 3. Invalid sequence type

```
Enter sequence type (DNA or RNA): XYZ
Invalid sequence type. Enter DNA or RNA.
```

---

## How the Program Works

1. **Create the codon table** – a Python dictionary maps each of the 64 codons to an amino acid (or `"Stop"`).
2. **Display the table** – prints the dictionary, the total count (64), and every `codon : amino acid` pair.
3. **Read the input** – asks for the sequence type and the sequence; both are `.upper().strip()`-ed.
4. **Handle RNA** – if the type is `RNA`, every `U` is replaced with `T`, so one table works for both. Any type other than DNA/RNA stops the program.
5. **Split into codons** – a loop `for i in range(0, len(sequence), 3)` slices the sequence into triplets. The last piece may be shorter than 3.
6. **Translate** – for each codon:
   - fewer than 3 letters → labelled `"Incomplete codon"`
   - otherwise → looked up in `codon_table`
   - `ATG` is added to the start-codon list; `TAA`, `TAG`, `TGA` to the stop-codon list
7. **Check completeness** – if `len(sequence) % 3 != 0`, a warning is printed.
8. **Display results** – sequence, codons, amino acids, start codon(s) and stop codon(s).
