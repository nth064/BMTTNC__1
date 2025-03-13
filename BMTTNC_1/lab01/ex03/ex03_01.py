def tinh_tong_so_chan(lst):
    total = 0
    
    for num in lst:
        if num % 2 == 0:
            total += num
    
    return total

input_list = input("Nhap danh sach so, cach nhau bang dau phay:")
numbers = list(map(int, input_list.split(',')))
result = tinh_tong_so_chan(numbers)
print(f"Tổng các số chẵn trong danh sách là: {result}")
