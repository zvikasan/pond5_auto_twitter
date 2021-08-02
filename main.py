

from selenium import webdriver
import random
import time
import private_details

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
# driver.maximize_window()

driver.get("https://twitter.com/login")
time.sleep(3)

username = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
username.send_keys(private_details.TWITTER_EMAIL)
password = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(private_details.TWITTER_PASSWORD)
login_button = driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div')
login_button.click()

time.sleep(3)

driver.get("https://www.pond5.com/artist/gregbrave#1/2063")
# driver.implicitly_wait(10)

time.sleep(3)

# Finds the total number of pages in my portfolio
total_pages = driver.find_element_by_class_name('js-paginationCount')
# chooses a random page in my portfolio

random_page = random.randint(1, int(total_pages.text)-1)

for x in range(1, 12):  # set here how many videos I want to tweet.

    driver.get(f"https://www.pond5.com/artist/gregbrave#{random_page}/2063")
    driver.refresh()
    time.sleep(3)

    # makes list of all video thumbnails (with links obviously) on that random page
    videos = driver.find_elements_by_class_name('js-searchResultItem')
    # by default total number of videos on a page is 48, but on the last page it can be different, so I'm not using the last page
    random_video = random.randint(0, 47)
    # print(f'RANDOM VIDEO ON PAGE {random_page} is {random_video}')
    videos[random_video].click()  # navigates to the chosen random video

    # print(driver.current_url) # this shows the current url

    # gets the current url for constructing the tweet link
    raw_url_material = driver.current_url

    parts = raw_url_material.split('item/')
    # extracts the video id that is needed for the tweet link
    video_id = parts[1].split('-')[0]
    # print(f'VIDEOID IS VIDEO ID IS {video_id}')

    time.sleep(3)

    video_title = driver.find_element_by_xpath(
        '//*[@id="main"]/div/div[1]/div[4]/div[2]/div/div/div/div[2]/div[2]/div/div[1]/header/h1/span')  # extracts the video title from the video page. Needed for tweet link construction

    # print(video_title.text)

    # replaces all the spaces in the video title with pluses for tweet link construction
    formatted_video_title = video_title.text.replace(' ', '+')

    # final constructed tweet url
    # constructed_tweet_url = (
    #     f'https://twitter.com/intent/tweet?url=https://www.pond5.com/item/{video_id}&text={formatted_video_title}+-+Stock+Footage&via=pond5')

    constructed_tweet_url = (
        f'https://twitter.com/intent/tweet?url=https://www.pond5.com/item/{video_id}?ref=gregbrave&text={formatted_video_title}+-+Stock+Footage&via=pond5')

    # print(constructed_tweet_url)

    driver.get(constructed_tweet_url)

    time.sleep(3)

    tweet_button = driver.find_element_by_xpath(
        '/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]/div')

    tweet_button.click()

    time.sleep(1)

driver.quit()
