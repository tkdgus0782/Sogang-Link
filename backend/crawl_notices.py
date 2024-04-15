import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyperclip  # 클립보드 사용을 위해

from urllib import parse
from datetime import datetime
import pytz

import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

django.setup()
from notices.models import Notice




def scrape_links(url):
    driver = webdriver.Chrome()
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "table")))

    # 첫 번째 행을 찾아 클릭
    first_row = driver.find_element(By.CSS_SELECTOR, "table tr:nth-child(1) td:nth-child(1)")
    # first_row = first_row.find_element(By.XPATH, "//*[@id='__nuxt']/html/div/main/div/div[3]/div[1]/table/tbody/tr[1]")
    driver.execute_script("arguments[0].click();", first_row)
    collected_data = []  # 제목과 링크를 저장할 리스트

    for _ in range(5):  # 10번 반복
        # 새 페이지 로딩 대기
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.cursor-pointer")))
        
        # 링크 아이콘 클릭
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'set-alt-image')))
        # find element by id
        time.sleep(1)  # 클립보드 복사를 위한 충분한 시간 확보
        title = driver.find_element(By.ID, 'set-alt-image').text
        
        # 게시물 시간
        date = driver.find_element(By.XPATH, "//*[@id='__nuxt']/html/div/main/div/div[2]/div[2]/div[1]/div[2]/div[3]").text
        
        seoul_tz = pytz.timezone('Asia/Seoul')
        # 날짜와 시간을 파싱할 때 사용할 형식 지정
        input_format = '%Y.%m.%d %H:%M:%S'
        django_format = '%Y-%m-%d %H:%M:%S'

        # 입력된 문자열을 datetime 객체로 변환
        parsed_date_time = datetime.strptime(date, input_format)
        # Django가 요구하는 형식의 문자열로 변환
        # date_time = parsed_date_time.strftime(django_format)
        date_time = seoul_tz.localize(parsed_date_time)

        link_icon = driver.find_element(By.CSS_SELECTOR, "img[alt='link']")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(link_icon))
        # WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='link']")))
        ActionChains(driver).move_to_element(link_icon).click().perform()

        # driver.execute_script("arguments[0].scrollIntoView(true);", link_icon)
        driver.execute_script("arguments[0].click();", link_icon)
        
        # 클립보드에서 링크 가져오기
        # time.sleep(1)  # 클립보드 복사를 위한 충분한 시간 확보
        link_url = pyperclip.paste()

        # decode url
        link_url = parse.unquote(link_url)


        print("title: ", title, " link: ", link_url, " date: ", date_time)
        collected_data.append({'title': title, 'link': link_url, 'date': date_time})

        # 이전 페이지 버튼 클릭
        span = driver.find_element(By.XPATH, "//span[text()='이전 페이지']")
        span.click()
    driver.quit()
    return collected_data


def crawl_by_board(board_name):
    '''
    게시판별로 크롤링하는 함수
    '''

    base_url = "https://sogang.ac.kr/ko/"
    if(board_name == "일반공지"):
        extracted_links = scrape_links(base_url + "story/notification-general")
        
    elif(board_name == "학사공지"):
        extracted_links = scrape_links(base_url + "academic-support/notices")
    elif(board_name == "장학공지"):
        extracted_links = scrape_links(base_url + "scholarship-notice")

    existing_links = Notice.objects.values_list('url', flat=True)
    # existing_links = existing_links.order_by('-id')[:3]
    new_links = [link for link in extracted_links if link['link'] not in existing_links]
    
    Notice.objects.bulk_create([Notice(
        board=board_name,
        title=link['title'], 
        url=link['link'],
        date=link['date']
    ) for link in new_links])

# 결과 출력
if __name__ == "__main__":
    crawl_by_board("일반공지")
    # extracted_links = scrape_links()
    # print("========== Extracted Links ==========")
    # for link in extracted_links:
    #     print(link)