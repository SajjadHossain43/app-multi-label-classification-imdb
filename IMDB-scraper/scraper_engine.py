from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import pickle
import pandas as pd
import logging

logging.basicConfig(
    filename='log.txt',
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
)

def log_exception(e: Exception):
    logging.error(f"Exception: {e}", exc_info=True)

columns = ['game_title', 'description', 'genres']

def append_to_csv(game_record: dict):
    list = []
    list.append(game_record)
    df = pd.DataFrame(data=list, columns=columns)
    df.to_csv('TempGameData.csv', mode='a', header=not pd.io.common.file_exists('TempGameData.csv'), index=False)
    return

def scraper_engine() -> bool:
    options = Options()
    #options.add_argument('--headless')
    game_data = []
    site_url = 'https://www.imdb.com/search/title/?title_type=video_game&sort=user_rating,desc'
    webdriver_path = 'C:\\Users\\nsyfi\\Downloads\\chromedriver-win64-latest\\chromedriver-win64\\chromedriver.exe'
    service = Service(webdriver_path)
    site_driver = webdriver.Chrome(service=service, options=options)
    site_driver.get(site_url)
    games = []
    for i in range(0, 400):
        try:
            see_more_button = site_driver.find_element(By.CLASS_NAME, 'ipc-see-more__text')
            site_driver.execute_script('arguments[0].scrollIntoView(true);', see_more_button)
            ActionChains(site_driver).move_to_element(see_more_button).perform()
            element_to_hide = site_driver.find_element(By.CLASS_NAME, 'fRnQpT')#fCQWxZ
            site_driver.execute_script("arguments[0].style.display = 'none';", element_to_hide)
            element_to_hide = site_driver.find_element(By.CLASS_NAME, 'cCEHlh')
            site_driver.execute_script("arguments[0].style.display = 'none';", element_to_hide)
            see_more_button.click()
            time.sleep(3)
            games = list(site_driver.find_elements(By.CLASS_NAME, 'coKeKZ'))#coKeKZ ejavrk
        except Exception as e:
            log_exception(e)
            continue
    print(len(games))
    details_driver = webdriver.Chrome(service=service, options=options)
    for game in games:
        try:
            game_record = {}
            details_link = game.find_element(By.CLASS_NAME, 'ipc-title-link-wrapper').get_attribute('href')
            details_driver.get(details_link)
            details = details_driver.find_element(By.CLASS_NAME, 'ipc-chip-list__scroller')
            genres = details.find_elements(By.CLASS_NAME, 'ipc-chip__text')
            genres_list = [i.text for i in genres]
            game_record['genres'] = str(genres_list)
            plot = details_driver.find_element(By.CLASS_NAME, 'NPkNd')
            details_driver.execute_script('arguments[0].scrollIntoView(true);', plot)
            ActionChains(details_driver).move_to_element(plot).perform()
            description = details_driver.find_element(By.CSS_SELECTOR, "p[data-testid='plot']").text
            game_record['description'] = description
            game_title = details_driver.find_element(By.CLASS_NAME, 'hero__primary-text').text
            game_record['game_title'] = game_title
            game_data.append(game_record)
            append_to_csv(game_record)
        except Exception as e:
            with open('game_data.pkl', 'wb') as f:
                pickle.dump(game_data, f)
            log_exception(e)
            time.sleep(3)
        finally:
            continue
    final_df = pd.DataFrame(data=game_data, columns=columns)
    final_df.to_csv('GameData.csv', index=False)
    return True
    
if __name__ == '__main__':
    print('Initializing . . . .')
    print(f'successfully completed = {scraper_engine()}')