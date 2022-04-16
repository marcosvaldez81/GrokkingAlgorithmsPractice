import collections 


# CREATING A CHAIN MAP

# Chain maps purpose is to handle multiple dictionaries as one unite.


# PRACTICE:

dict1 = {'Day 1': 'Monday', 'Day 2': 'Tuesday'}
dict2 = {"Day 3": "Wednesday", "Day 4": "Thursday"}

res = collections.ChainMap(dict1,dict2) # combines the two here to make 1 single dictionary

print(res.maps)
print()

print('Keys = {}'.format(list(res.keys()))) # how to print the keys of the res dictionary
print('Values = {}'.format(list(res.values())))
print()


# Print all elements in one go
print("Elements:")
for key,val in res.items():
    print("{} = {}".format(key,val))
print()

# Print certain value from the res dictionary

print('Day 3 in res: {}'.format(('Day 3' in res))) # true
print('Day 4 in res: {}'.format(('Day 5' in res))) # false



