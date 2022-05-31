import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from ranking_line import RankingLine
from conf import conf

app = Flask(__name__)

cors = CORS(app)
api = Api(app)

class Ranking(Resource):
  def get(self):
    parser = reqparse.RequestParser()
    parser.add_argument('name')   
    args = parser.parse_args()
    return "Bienvenue sur le " + args['name'], 200
  def post(self):
    return "Impossible de post", 405
    
def tryParseInt(s):
    try:
        return int(s)
    except ValueError:
        return False    

api.add_resource(Ranking, '/ranking')

@app.route('/')
def index():
    return "<h1>District85_webscrapper</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

# response = requests.get('https://districtfoot85.fff.fr/competitions/?id=385358&poule=4&phase=1&type=ch&tab=ranking')
# toExport = []

# unparsed = BeautifulSoup(response.content, "html.parser")
# unparsed.prettify()

# table_ranking = unparsed.find('table', attrs={'class' : "ranking-tab"})
# table_lines = table_ranking.findChildren("tr", recursive=True)

# for line in table_lines:
#   data = line.findChildren("td", recursive=True)
#   raw = []
#   raw.extend(data)
#   if(len(raw) > 0):
#     temp = RankingLine(raw[0].text, raw[1].text, raw[2].text, raw[3].text, raw[4].text, raw[5].text, raw[6].text)
#     toExport.append(temp)
   
