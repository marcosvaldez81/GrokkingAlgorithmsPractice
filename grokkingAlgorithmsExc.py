

# this python script is all the practice problems I have to do in my book that I am reading: grokking algorithm

#Excercise 4.1


listt = [1,2,3,4]
print(listt[1:]) # this is simply showing what is after element 1 in list


def sum(arr):
    """this function prints sum of an array"""
    if arr == []:
        return 0
    
    return arr[0] + sum(arr[1:]) 


print(sum([1,2,3,4]))

#4.2 create a recursion function to count number of items in a list

def count(list):
    """this function counts how many items are in a list."""
    if list == []:
        return 0
    return 1 + count(list[1:]) #the counter is going by 1... if you put 2 instead, it will count by twos... so 
    # 1 + count(list[1:]) counts the list by 1  so list[1,2,3,4] is equal to 4
    # if it is 2 + count(list[1:) counts the list by twos, so list [1,2,3,4] is 2+2+2+2 = 8... get it? 

print(count([1,2,3,4]))


def max(list2):
    
    if len(list2) == 2:
        if list2[0] > list2[1]:
            return list2[0]
        else:
            return list2[1]
        
    sub_max = max(list2[1:])
    return list2[0] if list2[0] > sub_max else sub_max
    
print(max([8,2]))


# Quicksort
print()
print("Quicksort Function:")

def quickSort(array):
    if len(array) <2:
        return array 
    
    else:
        pivot = array[0]
        
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
 
        return quickSort(less) + [pivot] + quickSort(greater)
    
print(quickSort([10,5,2,3]))



            
