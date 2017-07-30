import random

def combine_categories(restraunt_categories, user_categories):
    # Returns an array of values for tensors to be made out of
    combined = []
    for i in zip(restraunt_categories, user_categories):
        combined.append(i[0] * i[1])
    return combined

def make_test_vectors(amount, num_categories, COLUMNS):
    # Vector format: [[American, Indian, Chinese, Sushi, Mongolian], Price, Rating, Rating_Count, Correctness]
    # Return [vector ... vector]
    file = open("Tensor.txt", "rw")
    file.write(i + "," for i in COLUMNS)
    tests = []
    for i in range(amount):
        test = {}
        for i in range(num_categories):
            test[COLUMNS[i]] = random.randint(0,1)
        test[COLUMNS[num_categories]] = random.randint(1,4)
        test[COLUMNS[num_categories+1]] = random.randint(1,5)
        test[COLUMNS[num_categories+2]] = random.randint(1,1000)
        test[COLUMNS[num_categories+3]] = random.random()
        tests.append(test)
    return tests

print(make_test_vectors(4, 5, ["American", "Indian", "Chinese", "Sushi", "Mongolian", "Price", "Rating", "Rating_Count", "Correctness"]))