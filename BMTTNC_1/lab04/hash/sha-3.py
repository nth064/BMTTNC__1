from Crypto.Hash import SHA3_256

def sha3(message):
    """Tính toán giá trị hash SHA-3-256 từ dữ liệu đầu vào."""
    sha3_hash = SHA3_256.new()
    sha3_hash.update(message)
    return sha3_hash.digest()

def main():
    """Nhận chuỗi đầu vào từ người dùng, mã hóa bằng SHA-3-256 và hiển thị kết quả."""
    text = input("Nhập chuỗi văn bản: ").encode('utf-8')
    hashed_text = sha3(text)

    print("Chuỗi văn bản đã nhập:", text.decode('utf-8'))
    print("SHA-3 Hash:", hashed_text.hex())

if __name__ == "__main__":
    main()
