import requests
from bs4 import BeautifulSoup
from ranking_line import RankingLine

response = requests.get('https://districtfoot85.fff.fr/competitions/?id=385358&poule=4&phase=1&type=ch&tab=ranking')

unparsed = BeautifulSoup(response.content, "html.parser")
unparsed.prettify()

table_ranking = unparsed.find('table', attrs={'class' : "ranking-tab"})
table_lines = table_ranking.findChildren("tr", recursive=True)

for line in table_lines:
  data = line.findChildren("td", recursive=True)
  raw = []
  raw.extend(data)
  if(len(raw) > 0):
    temp = RankingLine(raw[0].text, raw[1].text)
    print("Place ",temp.position , " : " , temp.teamName)
