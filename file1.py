# Assignment : 01
# filter dna: remove invalid elements from all the DNA


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
t = []
arr1 = []
arr2 = []
arr3 = []
string1 = ""
string2 = ""
string3 = ""

for element in user_dna_sequence:
    for i in element[2]:
        if i not in dna_elements:
            t.append(element[2])
print(t)

for element in t[0]:
           arr1.append(element)

for i in arr1:
    if i not in dna_elements:
        index = arr1.index(i)
        print(index)
        arr1.pop(15)
        print(arr1)
        
for i in arr1:
    string1 += i
print(string1)

for element in t[1]:
           arr2.append(element)
           
for i in arr2:
    if i not in dna_elements:
        index = arr2.index(i)
        print(index)
        arr2.pop(13)
        print(arr2)
for i in arr2:
    string2 += i
print(string2)

for element in t[2]:
           arr3.append(element)

for i in arr3:
    if i not in dna_elements:
        index = arr3.index(i)
        print(index)
        arr3.pop(12)
        print(arr3)
        
for i in arr3:
    string3 += i
print(string3)

        

                


