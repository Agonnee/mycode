#!/usr/bin/env python3

dog_list = ["fido", "spot", "rover"]

cat_list = ["felix", "garfield", "shanks"]

dog_list.append(cat_list)

print(dog_list[0])

print(dog_list[3][1])

cat_dog_dict = {
        "first_dog" : dog_list[0],
        "second_cat" : dog_list[3][1]
        }

print(cat_dog_dict)

print(cat_dog_dict["first_dog"])

print(cat_dog_dict["second_cat"])
