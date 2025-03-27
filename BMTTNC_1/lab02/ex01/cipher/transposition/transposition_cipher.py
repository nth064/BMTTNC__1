class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        """Mã hóa văn bản bằng thuật toán hoán vị."""
        encrypted_text = ""

        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key

        return encrypted_text

    def decrypt(self, text, key):
        """Giải mã văn bản được mã hóa bằng thuật toán hoán vị."""
        decrypted_text = [''] * key  # Tạo danh sách rỗng với số cột bằng key
        row, col = 0, 0

        for symbol in text:
            decrypted_text[col] += symbol
            col += 1

            # Kiểm tra nếu cần chuyển sang hàng mới
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0
                row += 1

        return "".join(decrypted_text)  # Nối danh sách thành chuỗi hoàn chỉnh
