def access_tuple_elements(tpl):
    
    first_element = tpl[0]  
    last_element = tpl[-1]  
    return first_element, last_element


my_tuple = (10, 20, 30, 40, 50)
first, last = access_tuple_elements(my_tuple)

print(f"Phần tử đầu tiên: {first}")
print(f"Phần tử cuối cùng: {last}")
