from flask import Response, request
from ..banco.modelos import Treinadores
from flask_restful import Resource

class TreinadoresApi(Resource):

 def get(self):
  treinadores = Treinadores.objects().to_json()
  return Response(treinadores, mimetype="application/json", status=200)

 def post(self):
  body = request.get_json()
  treinador = Treinadores(**body).save()
  id = treinador.id
  return {'id': str(id)}, 200