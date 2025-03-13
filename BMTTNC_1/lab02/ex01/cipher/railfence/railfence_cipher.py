class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        # Tạo các rail (danh sách các danh sách rỗng)
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        
        # Lặp qua từng ký tự trong văn bản gốc (plain_text)
        for char in plain_text:
            rails[rail_index].append(char)
            
            # Thay đổi hướng di chuyển khi đạt tới rail đầu hoặc cuối
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        # Ghép các rail lại thành một chuỗi để tạo ra ciphertext
        cipher_text = ''.join(''.join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self, cipher_text, num_rails):
        # Tính số lượng ký tự vào mỗi rail
        rail_lengths = [0] * num_rails
        rail_index = 0
        direction = 1
        
        for _ in range(len(cipher_text)):
            rail_lengths[rail_index] += 1
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        # Chia ciphertext thành các rail
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length
        
        # Giải mã ciphertext bằng cách đọc các rail
        plain_text = []
        rail_index = 0
        direction = 1
        for _ in range(len(cipher_text)):
            plain_text.append(rails[rail_index].pop(0))
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        
        return ''.join(plain_text)
