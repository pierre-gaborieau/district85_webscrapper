from base64 import encode
from encodings import utf_8
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api
from ranking_line import RankingLine, RankingLineEncoder
from conf import conf
import json

#Configuration des paramètres de l'application
app = Flask(__name__)
cors = CORS(app)
api = Api(app)

#Classe qui gère l'accès au classment
class Ranking(Resource):
  def get(self, token, phase, poule):
    #On vérifie que le token est valide
      if(token != conf().guid):
        return {'error': 'Invalid token'}, 401
      else :
        #On génère l'url de la page avec les paramètres d'entrés
        url = 'https://districtfoot85.fff.fr/competitions/?id=385358&poule={pouleId}&phase={phaseId}&type=ch&tab=ranking'.format(pouleId=poule, phaseId=phase)
        #On charge la page
        response = requests.get(url)
        if(response.status_code == 200):
          toExport = []
          #On récupère le code html de la page
          unparsed = BeautifulSoup(response.content, "html.parser")
          unparsed.prettify()
          #On récupère le tableau de classement
          table_ranking = unparsed.find('table', attrs={'class' : "ranking-tab"})
          if(table_ranking):
            #On récupère chaque ligne du tableau
            table_lines = table_ranking.findChildren("tr", recursive=True)
            for line in table_lines:
              #On transforme les cellules en tableau
              data = line.findChildren("td", recursive=True)
              raw = []
              raw.extend(data)
              #On créé un objet pour chaque ligne sauf la première (le header du tableau)
              if(len(raw) > 0):
                temp = RankingLine(raw[0].text, raw[1].text, raw[2].text, raw[3].text, raw[4].text, raw[5].text, raw[6].text, raw[7].text, raw[8].text, raw[9].text, raw[10].text, raw[11].text)
                toExport.append(temp)
            #On encode en json et retourne le résultat
            return json.dumps(toExport, cls=RankingLineEncoder, skipkeys=True)
          else:
            return {'error': 'Invalid Parameters'}, 401
        else:
          return {'error': 'Invalid Parameters'}, 401

#On ajoute la classe aux chemins de l'applications
api.add_resource(Ranking, '/ranking/<string:token>/<int:phase>/<int:poule>/')

#Racine de l'application
@app.route('/')
def index():
    return "<h1>District85_webscrapper</h1>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)