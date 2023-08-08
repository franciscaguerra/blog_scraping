import os
import gspread


def write_in_googlesheet(data):
    if data == []: data = [['No se encontraron blogs asociados a esa categoria.']]
    sa = gspread.service_account(filename = os.getenv('PATH_CREDS'))
    sh = sa.open_by_url(os.getenv('SPREADSHEET_URL'))
    wks = sh.worksheet(os.getenv('SHEET_URL'))
    wks.clear()
    wks.update([['Titular', 'Categoria', 'Autor', 'Tiempo de lectura', 'Fecha de publicacion' ]] + data)
    return
