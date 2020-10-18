# Assignment : 05

# reverse those user's DNA whose age is greater than 18 and less than 25

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
array=[]
arra1=[]
arra2=[]
string1=""
string2=""

for element in user_dna_sequence:
    if element[1]>18 and element[1]<25:
        array.append(element[2])

for i in array[0]:
    arra1.append(i)
arra1.reverse()

for element in arra1:
    string1 += element
print(string1)
for i in array[1]:
    arra2.append(i)
arra2.reverse()

for element in arra2:
    string2 += element
print(string2)


# Assignment : 06

# Find the users whose DNA ends with A

arr1 = []
arr2 = []
arr3 = []
arr4 = []

for i in (user_dna_sequence[0][2]):
    arr1.append(i)
if arr1[len(arr1) - 1]== 'A':
    print(user_dna_sequence[0][0])

for i in (user_dna_sequence[1][2]):
    arr2.append(i)
if arr2[len(arr2) - 1]== 'A':
    print(user_dna_sequence[1][0])


for i in (user_dna_sequence[2][2]):
    arr3.append(i)
if arr3[len(arr3) - 1]== 'A':
    print(user_dna_sequence[2][0])


for i in (user_dna_sequence[3][2]):
    arr4.append(i)
if arr4[len(arr4) - 1]== 'A':
    print(user_dna_sequence[3][0])



    
 
       



