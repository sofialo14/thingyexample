#Take a function The function best_two_keys should take a dictionary as input.
#The dictionary will have keys that are strings, and values associated with each
#of the keys that are integers. The function should return a tuple of the two
#key strings that have the two highest integer values.

#For test:
#- create a dictionary where you know what the two highest integer values are
#Corner cases for test:
#- test with 0 and negative numbers
#- test with an empty dictionary
#- test where dictionary has all same values or a tie for top 2 values
#- test where dictionary has only one key-value pair

#params: dictionary, where keys are strings and values are integers
#return: tuple containing string representing the key associated with the highest
        #integer values

def best_two_keys(my_dict):
    pass

#Example test:
def best_two_keys(my_dict):
    dict1 = {'one': 1, 'two': 2, 'three': 3}
    expected1 = ('one', 'two')
    dict2 = {"one": 1} # expected: exception
    dict3 = {"one": 1, "two": 2, "also_two": 2}
    expected3 = ("one", "also_two")
    dict4 = {1: "one"} # expected: exception


if best_two_keys(dict1) == expected1:
    passed += 1
else:
    failed +=1
    print('Failed test one')

#testing if code breaks properly
try:
    best_two_keys(dict2)
    failed += 1
    print("Failed test 2")
except:
    passed += 1
