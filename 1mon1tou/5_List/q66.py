fruits = ['orange', 'apple', 'banana', 'pineapple', 'lemon', 'apple', 'banana']
favorites = ['like', 'like', 'dislike', 'dislike', 'like']
for fruit, favorite in zip(fruits, favorites):
    print("I {} {}".format(favorite, fruit))