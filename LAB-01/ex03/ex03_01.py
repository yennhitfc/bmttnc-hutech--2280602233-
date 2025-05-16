def tinhtongsochan(lst):
    tong = 0
    for num in lst:
        if num % 2 == 0:
            tong += num
    return tong

input_list = input("nhap ds cac so, cach nhau bang dau phay: ")
numbers = list(map(int, input_list.split(',')))

tongchan = tinhtongsochan(numbers)
print("KQ la: ",tongchan)
