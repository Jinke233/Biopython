'''

Convert a dictionary to a sorted list.

-----------------------------------------------------------
(c) 2013 Allegra Via and Kristian Rother
    Licensed under the conditions of the Python License

    This code appears in section 8.3.5 of the book
    "Managing Biological Data with Python".
-----------------------------------------------------------
'''

dictionary = {1: 'a', 2: 'b', 4: 'd', 3: 'c',
              5: 't', 6: 'm', 36: 'z'}

# create a list of keys and go through them one by one
keys = list(dictionary)
keys.sort()
for key in keys:
    print dictionary[key]


# sort keys using the sorted() built-in function
keys = sorted(dictionary)
print keys
