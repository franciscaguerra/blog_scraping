from flask import Flask, request, abort
from utils.scraper.scraper import search_articles_by_category, search_one_article, search_all_categories
from utils.googlesheet.sheet import write_in_googlesheet
import requests
import os
from dotenv import load_dotenv
from selenium import webdriver


app = Flask(__name__)
load_dotenv()

@app.route('/search-category', methods=['POST'])
def search_all_articles():
    category, webhook = request.args.get("category"), request.args.get("webhook")
    if not category: raise abort(400, "El parametro categoria no se encuentra.")
    if not webhook: raise abort(400, "El parametro webhook no se encuentra.")
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    driver = webdriver.Chrome(options)
    if category.lower() == "bonus": blogs_found = search_all_categories(driver)
    else:
        links = search_articles_by_category(driver, category)
        blogs_found = search_one_article(driver, links)
    write_in_googlesheet(blogs_found)
    requests.post(webhook, data={"url_googlesheet": os.getenv("SPREADSHEET_URL"), "mail": "fxguerra@uc.cl"})
    return("Blogs buscados correctamente")


if __name__ == '__main__':
    app.run(debug=True, port=4000)