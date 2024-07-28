marks = [92,93,94,94,95,95,97] #it is a list
print(marks)

print(marks[-1]) #piche se start hoga 

# print(marks[0:5])

# for score in marks:
#     print(score)

marks.append(7) #last me add krne ke liye
print(marks)

marks.insert(0,13) #first me add
print(marks)

print (13 in marks)

print(len(marks)) #length 

i=0
while i<len(marks):
    print(marks[i])
    i=i+1
    
marks.clear()
print(marks) 