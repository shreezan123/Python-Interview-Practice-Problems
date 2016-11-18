def split_on_repeat(your_string):
    temp_list = list()
    temp_dict = dict()
    for char in set(your_string):
        temp_dict[char] = your_string.count(char)

    for key in temp_dict:
        if temp_dict[key] >= 2:
            repeat_index = your_string.rfind(key)
            temp_list.append((your_string[:repeat_index],your_string[repeat_index:]))

    return temp_list