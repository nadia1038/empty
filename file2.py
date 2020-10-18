# Assignment : 02
# count dna_elements in everyone's dna.
# for example
# "ATTGGCCAA" in this DNA contains A->3 times, T->2 times and C->2 times
# and G->2 times

user_dna_sequence = [
[
"Roksana Kozlova", 18, "GTTAGCCGACTTGGCXCTTT"
],
[
"Roza Kiseleva", 19, "ATTTGGCGAATTGGCCTTT"
],
[
"Kliment Volkov", 27, "ATTTGACCAATTGZGCAAA"
],
[
"Afanas Morozov", 22, "ATTTGACCGATTNGGCAA"
],
]

dna_elements = ["A", "T", "G", "C"]

countA = 0
countT = 0
countC = 0
countG = 0

for i in user_dna_sequence[0][2]:
    if i == 'A':
        countA+=1

for i in user_dna_sequence[0][2]:
    if i == 'T':
        countT += 1

for i in user_dna_sequence[0][2]:
    if i == 'C':
        countC += 1

for i in user_dna_sequence[0][2]:
    if i == 'G':
        countG += 1

print(user_dna_sequence[0][2] , "in this DNA contains" , "A->",countA,"times;", "T->",countT,"times;","C->",countC,"times;","G->",countG,"times")

