from .treinadores import TreinadoresApi

def initialize_routes(api):
    api.add_resource(TreinadoresApi, '/treinadores')