def sum_ages(person_list):
    """
    Given a list of dictionaries with 'name' and 'age' keys, 
    return a dictionary with unique ages as keys and the sum of ages as values.
    """
    dic = {}
    
    for person in person_list:
        if person["age"] in dic:
            dic[person["age"]] += person["age"]
        else:
            dic[person["age"]] = person["age"]

    return dic

# Example usage:
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 25},
    {'name': 'David', 'age': 30},
    {'name': 'Eva', 'age': 25},
    {'name': 'Eva', 'age': 20},
    {'name': 'Eva', 'age': 20},
    {'name': 'Eva', 'age': 20},
    {'name': 'Eva', 'age': 20},
    {'name': 'Eva', 'age': 100},
    {'name': 'Eva', 'age': 100},
    {'name': 'Eva', 'age': 100},
    {'name': 'Eva', 'age': 100},
]

result = sum_ages(people)
print(result)
