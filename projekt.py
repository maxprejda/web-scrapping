import requests
from bs4 import BeautifulSoup

def collect(URL):
    r = requests.get(URL)

    

    data = BeautifulSoup(r.content, 'html.parser')
    tabulka = data.find('tbody')
    radky = tabulka.find_all('tr')

    for i in range(len(radky)):
        info = radky[i].find_all('td')

        cislo = info[0].text
        hrac = info[1].find('a').text
        pozice = info[2].text
        haze = info[3].text
        vyska = info[4].text
        vaha = info[5].text
        rok = info[6].text


        print(f'Číslo: {cislo} | Hráč: {hrac} | Pozice: {pozice} | Háže/Pálí: {haze} | Výška: {vyska} | Váha: {vaha} | Rok Narození: {rok}')

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27061")

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27059")

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27062")

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27060")

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27063")

collect("https://stats.baseball.cz/cs/events/2023-nadstavba-o-extraligu/teams/27064")