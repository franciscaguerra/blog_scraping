from flask import Flask, request, abort
from utils.scraper.scraper import search_articles_by_category, search_one_article, search_all_categories
from utils.googlesheet.sheet import write_in_googlesheet
import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
from selenium.common.exceptions import TimeoutException


app = Flask(__name__)

@app.route('/search-category', methods=['POST'])
def search_all_articles():
    category, webhook = request.args.get("category"), request.args.get("webhook")
    print(category)
    print(webhook)
    if not category: raise abort(400, "El parametro categoria no se encuentra.")
    if not webhook: raise abort(400, "El parametro webhook no se encuentra.")
    print("Antes de ChromOptions")
    options = webdriver.ChromeOptions()
    print("Despues de ChromOptions")
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--dns-prefetch-disable")
    try:
        driver = webdriver.Chrome(options)
    except TimeoutException as ex:
        print(ex.Message)
        print("Despues del driver")
    if category.lower() == "bonus": blogs_found = search_all_categories(driver)
    else:
        links = search_articles_by_category(driver, category)
        print("En app despues de los links")
        blogs_found = search_one_article(driver, links)
        print("En app despues de search_one_article")
    write_in_googlesheet(blogs_found)
    requests.post(webhook, data={"url_googlesheet": os.getenv("SPREADSHEET_URL"), "mail": "fxguerra@uc.cl"})
    return("Blogs buscados correctamente")


if __name__ == '__main__':
    app.run(debug=True, port=4000)