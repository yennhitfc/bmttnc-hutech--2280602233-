def taotupletulist(lst):
    return tuple(lst)

input_list = input("nhap ds cac so: ")
numbers = list(map(int, input_list.split(',')))

mytuple = taotupletulist(numbers)
print("list: ", numbers)
print("tuple tu list: ", mytuple)

