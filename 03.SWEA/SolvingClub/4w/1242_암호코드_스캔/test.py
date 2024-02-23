def is_valid_code(code):
    odd_sum = 0
    even_sum = 0
    for i in range(8):
        digit = int(code[i])
        if i % 2 == 0:
            odd_sum += digit
        else:
            even_sum += digit
    total_sum = (odd_sum * 3) + even_sum
    return total_sum % 10 == 0

def convert_to_binary(hex_string):
    binary_string = bin(int(hex_string, 16))[2:]
    return binary_string.zfill(4 * len(hex_string))

def decode_code(binary_code):
    decoded = ""
    for i in range(0, len(binary_code), 7):
        chunk = binary_code[i:i + 7]
        decoded += str(int(chunk, 2))
    return decoded

def scanner(input_data):
    T = int(input_data[0])
    current_line = 1

    for test_case in range(1, T + 1):
        N, M = map(int, input_data[current_line].split())
        current_line += 1

        codes = []
        for _ in range(N):
            hex_line = input_data[current_line].strip()
            current_line += 1
            binary_line = convert_to_binary(hex_line)
            for i in range(0, M * 4, 7):
                codes.append(binary_line[i:i + 7])

        valid_codes = []
        for code_start in range(0, len(codes) - 56 + 1, 56):
            code_candidate = "".join(codes[code_start:code_start + 56])
            if is_valid_code(code_candidate):
                decoded_code = decode_code(code_candidate)
                valid_codes.append(decoded_code)

        total_sum = sum(map(int, valid_codes))
        print(f"#{test_case} {total_sum}")

# 파일에서 입력 데이터 읽기
with open('input.txt', 'r') as file:
    input_data = file.read().splitlines()

# 코드 실행
scanner(input_data)
