def dao_nguoc_list(lst):
    return lst[::-1]


input_list = input("Nhap danh sach so, cach nhau bang dau phay:")
numbers = list(map(int, input_list.split(',')))
reversed_numbers = dao_nguoc_list(numbers)
print(f"Danh sách sau khi đảo ngược: {reversed_numbers}")
