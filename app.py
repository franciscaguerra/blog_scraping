from flask import Flask, request, abort
from utils.scraper.scraper import search_articles_by_category, search_all_categories
from utils.googlesheet.sheet import write_in_googlesheet
import requests
import os
from selenium import webdriver
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/search-category', methods=['POST'])
def search_all_articles():
    category, webhook = request.args.get("category"), request.args.get("webhook")
    if not category: raise abort(400, "El parametro categoria no se encuentra.")
    if not webhook: raise abort(400, "El parametro webhook no se encuentra.")
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--dns-prefetch-disable")
    driver = webdriver.Remote(os.getenv("CHROMEDRIVER"), options=options)
    if category.lower() == "bonus": blogs_found = search_all_categories(driver)
    else:
        blogs_found = search_articles_by_category(driver, category)
    write_in_googlesheet(blogs_found)
    requests.post(webhook, json={"url_googlesheet": os.getenv("SPREADSHEET_URL"), "mail": os.getenv("MAIL")})
    
    return("Blogs buscados correctamente")


if __name__ == '__main__':
    app.run(debug=True, port=4000)