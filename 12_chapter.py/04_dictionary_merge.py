def merge():
    dict1 = {'a': 1, 'b': 2} 
    dict2 = {'b': 3, 'c': 4} 
    merged = dict1 | dict2 
    print(merged)  # Output: {'a': 1, 'b': 3, 'c': 4} 
merge()

def update():
    dict1 = {'a': 1, 'b': 2} 
    dict2 = {'b': 3, 'c': 4} 

    dict1.update(dict2)
    print(dict1)

update()