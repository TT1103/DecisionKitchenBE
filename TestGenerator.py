import random

def combine_categories(restraunt_categories, user_categories):
    # Returns an array of values for tensors to be made out of
    combined = []
    for i in zip(restraunt_categories, user_categories):
        combined.append(i[0] * i[1])
    return combined

def make_test_vectors(amount, num_categories):
    # Vector format: [[American, Indian, Chinese, Sushi, Mongolian], Price, Rating, Rating_Count]
    # Return [vector ... vector]
    tests = []
    for i in range(amount):
        test = []
        categories = []
        for i in range(num_categories):
            categories.append(random.randint(0,1))
        test.append(categories)
        test.append(random.randint(1,4))
        test.append(random.randint(1,5))
        test.append(random.randint(1,1000))
        tests.append(test)
    return tests

