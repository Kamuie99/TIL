# 아래에 코드를 작성하시오.
from conf.settings import NAME, MAIN_URL
from utils.create_url import create_url

new_url = create_url(NAME, MAIN_URL)
print(new_url)