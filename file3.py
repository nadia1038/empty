# Assignment : 03
# replace A by G in dna sequence of them whose age is greater than 20

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
box1=[]
arr1=[]
arr2=[]
string1 = ""
string2 = ""

for element in user_dna_sequence:
    if element[1]>20:
        box1.append(element[2])
print(box1)
for i in box1[0]:
    arr1.append(i)
print(arr1)
for i in arr1:
    if i == 'A':
        arr1[arr1.index(i)] = 'G'
print(arr1)

for i in arr1:
    string1 += i
print(string1)
    
for i in box1[1]:
    arr2.append(i)
print(arr2)
for i in arr2:
    if i == 'A':
        arr2[arr2.index(i)] = 'G'
print(arr2)

for i in arr2:
    string2 += i
print(string2)
          



          
    
