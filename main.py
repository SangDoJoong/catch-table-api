import pickle
from selenium import webdriver
import requests


def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def get_catch_table_cookie():
    driver = webdriver.Chrome()
    driver.get(catch_table_url)
    cookies = driver.get_cookies()
    for cookie in cookies:
        cookie_dict[cookie['name']] = cookie['value']
    driver.close()
    return cookie_dict


def get_catch_table_shop_data(url, cookie_dict):
    split = url.split("/")
    shop_alias = split[-1]

    response = requests.get(catch_table_api_dict["shop_detail"] + shop_alias)
    print(response.json())
    return response.json()


if __name__ == '__main__':
    print_hi('sangDoJoong')

    cookie_flag = False
    cookie_dict = {}
    catch_table_url = "https://app.catchtable.co.kr"

    catch_table_api_dict = {
        # 뒤에 shop_alias를 붙여서 사용
        "shop_detail": catch_table_url + "/api/v3/shop/detail/",
        "pre_check": catch_table_url + "/api/v3/reservation/preCheck",
    }

    if cookie_flag:
        cookie_dict = get_catch_table_cookie()
    else:
        ### 직접 넣기?
        cookie_dict = {
            '_gat_gtag_UA_117680739_4': '1',
            '_fbp': 'fb.2.1668996126603.1408447385',
            '_gid': 'GA1.3.577495696.1668996126',
            '_ga_95C07ZWW1T': 'GS1.1.1668996124.1.0.1668996133.51.0.0',
            '_ga': 'GA1.3.1341880208.1668996125',
            '_ga_9ENCGJ7C7P': 'GS1.1.1668996125.1.0.1668996125.0.0.0',
            'wcs_bt': 's_3c2cf433f210:1668996124',
            'JSESSIONID': '845F7A937771DE667495067FB7820310'
        }

    print(cookie_dict)

    ### url 입력받기
    ### shop detail
    demo_url = "https://app.catchtable.co.kr/ct/shop/Y2F0Y2hfQVpSSE9TN3R1QnhIUUZUenY4ZDN3UT09"
    shop_detail_response = get_catch_table_shop_data(demo_url, cookie_dict)
