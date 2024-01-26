# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, repeat_count, string_to_repeat):
        for _ in range(repeat_count):
            print(string_to_repeat)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
