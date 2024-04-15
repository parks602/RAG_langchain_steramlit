import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
import time


def extract_links_with_keyword(url, keyword):
    # HTML 가져오기
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 링크 추출
    links = soup.find_all('a', href=True)
    
    # 키워드를 포함하는 링크 추출
    keyword_links = []
    for link in links:
        if keyword in link['href']:
            keyword_links.append(link['href'])
    
    return keyword_links
    
def create_pdf(screenshots, output_filename):
    c = canvas.Canvas(output_filename, pagesize=letter)
    for screenshot in screenshots:
        c.drawImage(screenshot, 0, 0, width=letter[0], height=letter[1])
        c.showPage()
    c.save()
    
if __name__ == "__main__"    :
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')  # 화면 없이 실행
    chrome_options.add_argument('--start-maximized')  # 창을 최대화
    
    
    url = "https://www.tukorea.ac.kr/sites/tukorea/index.do"
    keyword = "tukorea.ac.kr"

    
    file_dir = "D:\\langchain\\crawl\\tukorea"
    print(file_dir)
    os.makedirs(file_dir)

    keyword_links = extract_links_with_keyword(url, keyword)
    keyword_links = list(set(keyword_links))
    screenshots = []
 
    
    for i, url in enumerate(keyword_links):
        if i == 100:
            break
        try:
            # 크롬 드라이버 실행
            driver = webdriver.Chrome(options=chrome_options)
            print(url)
            driver.get(url)
            # 페이지 전체 높이 측정
            scroll_height = driver.execute_script("return document.body.scrollHeight;")
            # 브라우저 창 크기 설정 (최대화)
            driver.set_window_size(1920, scroll_height)
            time.sleep(1)
            shot_num = 1
            scroll_step = 1000  # 스크롤할 거리
            scroll_position = 0  # 초기 스크롤 위치   
            
            screenshot_filename = "{}/screenshot{}-{}.png".format(file_dir, i, shot_num)
            driver.save_screenshot(screenshot_filename)
            screenshots.append(screenshot_filename)
            
            while scroll_position < scroll_height:
                shot_num =+ 1
                # 페이지를 아래로 스크롤
                driver.execute_script(f"window.scrollBy(0, {scroll_step});")
                scroll_position += scroll_step
                time.sleep(0.5)  # 스크롤을 하고 나면 충분한 시간을 줍니다.

                # 스크린샷 캡처
                screenshot_filename = "{}/screenshot{}-{}.png".format(file_dir, i, shot_num)
                driver.save_screenshot(screenshot_filename)
                screenshots.append(screenshot_filename)
        except:
            shot_num =+ 1
        driver.quit()
    
    # PDF 생성
    output_pdf = "output.pdf"
    create_pdf(screenshots, output_pdf)
    print("PDF 파일이 생성되었습니다:", output_pdf)