import os
import gspread
import json
from dotenv import load_dotenv


load_dotenv()


def write_in_googlesheet(data):
    if data == []: data = [['No se encontraron blogs asociados a esa categoria.']]
    credentials = {
        "type": os.getenv("TYPE"),
        "project_id": os.getenv("PROJECT_ID"),
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": os.getenv("AUTH_URI"),
        "token_uri": os.getenv("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.getenv("CLIENT_X509_CERT_URL"),
        "universe_domain": os.getenv("UNIVERSE_DOMAIN")
    }
    with open("/tmp/credentials.json", "w") as outfile:
        outfile.write(json.dumps(credentials))
    sa = gspread.service_account("/tmp/credentials.json")
    sh = sa.open_by_url(os.getenv("SPREADSHEET_URL"))
    wks = sh.worksheet(os.getenv("SHEET_URL"))
    wks.clear()
    wks.update([['Titular', 'Categoria', 'Autor', 'Tiempo de lectura', 'Fecha de publicacion' ]] + data)
    return


