# Start with 4 words “comfortable”, “round”, “support”, “machinery”, return a list of all possible 2 word combinations. 
# Example: ["comfortable round", "comfortable support", "comfortable machinery", .....]

list1 = ["comfortable", "round", "support", "machinery"]
list2 = []

def createNewList (list):
    
    newList = []

    for i in range (0, len(list)):

       for j in range (0, len(list)):

           if i != j:
               newList.append(list[i]+ " " + list[j])

    return newList


list2 = createNewList(list1)
print(list2)