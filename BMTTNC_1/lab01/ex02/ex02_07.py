print("Nhap cac dong van ban (nhap done de ket thuc): ")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\nCac dong da nhap sau khi chuyen thanh du lieu in hoa: ")
for line in lines:
    print(lines.upper())