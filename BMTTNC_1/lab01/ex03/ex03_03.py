def list_to_tuple(lst):
    return tuple(lst)

input_list = input("Nhap danh sach so, cach nhau bang dau phay:")
numbers = list(map(int, input_list.split(',')))

my_tuple = list_to_tuple(numbers)
print("List: ", numbers)
print("Tuple tu list: ", my_tuple)

