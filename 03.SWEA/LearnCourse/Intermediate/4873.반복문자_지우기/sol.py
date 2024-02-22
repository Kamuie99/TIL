import sys
sys.stdin = open('input.txt')

def zarugi(string):
    input_s = string
    input_len = len(string)
    count = 0
    for i in range(input_len-1):
        if input_s[i] == input_s[i+1]:
            count += 1
        elif count > 0 and input_s[i] != input_s[i+1]:
            return zarugi(input_s[:i-1]+input_s[i+1:])
    if count > 0:
        return input_s[:input_len-count-1]
    else:
        return input_s

T = int(input())

for test_case in range(1, T+1):
    what = str(input())
    new_what = zarugi(what)
    print(f'#{test_case} {len(new_what)}')