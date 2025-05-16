def solanxuathien(lst):
count_dict = {}
for item in lst:
    if item in count_dict:
    count_dict[item] += 1
    else:
        count_dict[item] = 1
        return count_dict

input_string = input("nhapds: ")
word_list = input_string.split()


solan= solanxuathien(word_list)

print("KQ la: ", solanxuathien)


