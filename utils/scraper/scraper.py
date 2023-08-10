from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import os
from unidecode import unidecode

url_blog = os.getenv('BLOG_URL')

#Busqueda con la lupita
def search_articles_by_word(driver, category): 
    driver.get(url_blog)
    WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ArticleSearch_search__KuXsU']/input[1]"))).send_keys(category)
    #Cambiar la parte de sleep por un until, VER COMO HACERLO
    time.sleep(2)
    results = driver.find_element(By.CLASS_NAME, "ArticleSearch_searchResults__1SzK9")
    links = list(set([elem.get_attribute('href') for elem in results.find_elements(By.TAG_NAME, 'a')]))
    return links


def search_one_article(driver, links):
    data_articles = []
    for link in links:
        driver.get(link)
        category = driver.find_element(By.CLASS_NAME, "text-primary-main").text
        title = driver.find_element(By.CLASS_NAME, "ArticleSingle_title__s6dVD").text
        time = driver.find_element(By.XPATH, "//div[@class='sc-fe594033-0 ioYqnu text-grey-600 Text_body__ldD0k']").text
        author = driver.find_element(By.CLASS_NAME, "Text_bodySmall__wdsbZ").text
        data_articles.append([title, category, author, time])
    return data_articles


def search_all_categories(driver):
    categories = ['emprendedores', 'pymes', 'corporativos', 'empresarios-exitosos', 'educacion-financiera', 'noticias']
    links = []
    for category in categories:
        driver.get(f'{url_blog}{category}')
        while True:
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-bf9c36a8-0 gVyddL Button_root__G_l9X Button_filled__GEop3 Button_medium__zCMU6']"))).click()
            except:
                break
        parent_node = driver.find_element(By.CLASS_NAME, "BlogArticlesPagination_articlesGridNormal__CYdsq")
        all_articles = parent_node.find_elements(By.XPATH, '*')
        for article in all_articles:
            href = article.find_elements(By.XPATH, '*')[0].find_elements(By.XPATH, '*')[0].get_attribute('href')
            links.append(href)
    data_articles = search_one_article(driver, links)
    return data_articles

#Busqueda por categoria
def search_articles_by_category(driver, category):
    links = []
    dict_categories = {
        'emprendedores': 'emprendedores',
        'pymes':'pymes',
        'corporativos': 'corporativos',
        'casos de exito': 'empresarios-exitosos',
        'educacion financiera': 'educacion-financiera',
        'xepelin': 'noticias'
    }
    if category in dict_categories.keys():
        driver.get(f'{url_blog}{dict_categories[unidecode(category.lower())]}')
        while True:
            try:
                WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='sc-bf9c36a8-0 gVyddL Button_root__G_l9X Button_filled__GEop3 Button_medium__zCMU6']"))).click()
            except:
                break
        parent_node = driver.find_element(By.CLASS_NAME, "BlogArticlesPagination_articlesGridNormal__CYdsq")
        all_articles = parent_node.find_elements(By.XPATH, '*')
        for article in all_articles:
            href = article.find_elements(By.XPATH, '*')[0].find_elements(By.XPATH, '*')[0].get_attribute('href')
            links.append(href)
        data_articles = search_one_article(driver, links)
    else: 
        return []
    return data_articles