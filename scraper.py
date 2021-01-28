
from bs4 import BeautifulSoup
import requests


def scrape():
    shayries = []
    for i in range(1, 40):
        r = requests.get(
            f'http://www.shayaribazar.com/english/Romantic-Shayari?page={i}')
        soup = BeautifulSoup(r.text, 'html.parser')
        divs = soup.find_all('div', {"class": "main_body_1"})
        for div in divs:
            data = div.find("p")
            for br in data.select("br"):
                br.replace_with("\n")
            shayri = ""
            for d in data.text.split("\n"):
                shayri += d.strip() + "\n"
            shayries.append(shayri)
    with open("shayri.txt", "w", encoding="utf-8") as file:
        for shayri in shayries:
            print(shayri, file=file)


scrape()
