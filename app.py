import requests
from bs4 import BeautifulSoup
from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api, reqparse
from ranking_line import RankingLine, RankingLineEncoder
from conf import conf
import json

app = Flask(__name__)

cors = CORS(app)
api = Api(app)

class Ranking(Resource):
  def get(self, token, phase, poule):
      if(token != conf().guid):
        return {'error': 'Invalid token'}, 401
      else :
        url = 'https://districtfoot85.fff.fr/competitions/?id=385358&poule={pouleId}&phase={phaseId}&type=ch&tab=ranking'.format(pouleId=poule, phaseId=phase)
        response = requests.get(url)
        if(response.status_code == 200):
          toExport = []
          unparsed = BeautifulSoup(response.content, "html.parser")
          unparsed.prettify()
          table_ranking = unparsed.find('table', attrs={'class' : "ranking-tab"})
          if(table_ranking):
            table_lines = table_ranking.findChildren("tr", recursive=True)
            for line in table_lines:
              data = line.findChildren("td", recursive=True)
              raw = []
              raw.extend(data)
              if(len(raw) > 0):
                temp = RankingLine(raw[0].text, raw[1].text, raw[2].text, raw[3].text, raw[4].text, raw[5].text, raw[6].text, raw[7].text, raw[8].text, raw[9].text, raw[10].text, raw[11].text)
                toExport.append(temp)
            return json.dumps(toExport, cls=RankingLineEncoder), 200
          else:
            return {'error': 'Invalid Parameters'}, 401
        else:
          return {'error': 'Invalid Parameters'}, 401
    
def tryParseInt(s):
    try:
        return int(s)
    except ValueError:
        return False    

api.add_resource(Ranking, '/ranking/<string:token>/<int:phase>/<int:poule>/')

@app.route('/')
def index():
    return "<h1>District85_webscrapper</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)