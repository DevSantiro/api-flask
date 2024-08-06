import os
import importlib

def register_routes(app):
    routes_dir = os.path.join(os.path.dirname(__file__))  # acessando o diretório
    # irá fazer a iteração para cada versão no diretorio "routes"
    for version in os.listdir(routes_dir):
        # Pega a versão (v1, v2, ...)
        version_path = os.path.join(routes_dir, version)
        # Verifica se é um diretório para poder prosseguir (irá ignorar arquivos)
        if os.path.isdir(version_path):
            # Para cada arquivo irá iterar sobre
            for filename in os.listdir(version_path):
                # Verifica se é da extensão ".py" e diferente do arquivo init
                if filename.endswith('.py') and filename != '__init__.py':
                    # Cria o padrão do nome do modulo
                    module_name = f'routes.{version}.{filename[:-3]}'
                    # Faz o import do modulo
                    module = importlib.import_module(f"app.{module_name}")
                    # Faz o Registro do modulo no blueprint com o arquivo de usuários
                    if hasattr(module, 'bp'):
                        app.register_blueprint(module.bp, url_prefix=f'/{version}')