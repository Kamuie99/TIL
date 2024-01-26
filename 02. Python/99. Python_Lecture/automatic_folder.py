import os

def create_folder(folder_name):
    # 현재 작업 디렉토리에 새로운 폴더 생성
    folder_path = os.path.join(os.getcwd(), folder_name)
    os.makedirs(folder_path, exist_ok=True)
    
    # solution.py 파일 생성
    solution_file_path = os.path.join(folder_path, "solution.py")
    with open(solution_file_path, 'w', encoding='utf-8') as solution_file:
        # solution.py 파일에 필요한 코드 작성
        solution_code = """import sys\nsys.stdin = open('input.txt', 'r', encoding='utf-8')\n\n \n"""
        solution_file.write(solution_code)
    
    # input.txt 파일 생성
    input_file_path = os.path.join(folder_path, "input.txt")
    with open(input_file_path, 'w', encoding='utf-8') as input_file:
        input_file.write("")

if __name__ == "__main__":
    # 사용자로부터 폴더 이름 입력받기
    folder_name = input("폴더 이름을 입력하세요: ")
    
    # 폴더 생성 및 파일 생성 함수 호출
    create_folder(folder_name)
    
    print(f"폴더 '{folder_name}'가 생성되었습니다.")
