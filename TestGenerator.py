def combine_categories(restraunt_categories, user_categories):
    combined = []
    for i in zip(restraunt_categories, user_categories):
        combined.append(i[0] * i[1])
    return combined

