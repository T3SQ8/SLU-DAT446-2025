# `gene_match` ([mars 2024](https://github.com/jyp/python-courses-exams/blob/main/2403/facit-vt24.org))




Write a function `gene_match(gene,genome)` that searches for a genetic
subsequence in a genome. The gene is given as a string. The genome is given as
a file name. Both the gene string and the genome file contents are comprised
only of the characters `A`, `C`, `G`, or `T`. The function should print all
the positions in the genome where the gene can be found. Print the starting
positions, indexed from zero. For example, if the gene contains `ACA` and the
genome file contains `GTACACAGT`, then both 2 and 4 should be printed.

For half credits, you can assume that the genome file can fit in memory. For
full credits, you must deal with files that cannot fit in memory. In both
cases, you can assume that the gene is smaller than the genome.

Hints:
- If `f` is a file, then `f.read(n)` reads `n` characters from `f` and returns
  them as a string.  If the file has `m` characters remaining to read and `m <
  n`, then only `m` characters will be read. In particular, at the end of the
  file, `f.read` always returns the string.
- Within the **Exam Sandbox, Question 2**, you can open the file "genome.txt".
  It has the contents `GTACACAGT`. You can use this file for testing.

