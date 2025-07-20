import requests


class Auth:
    # será usada pra autenticação
    def __init__(self):
        self.__base_url = 'http://fhao.pythonanywhere.com/api/v1/'
        self.__auth_url = f'{self.__base_url}authentication/token/'
        # essa url sera concatenada com a url de cima para realizar as autenticacões

    def get_token(self, username, password):
        # função que vai passar os dados do usuario e retornar os tokens
        auth_payload = {
            'username': username,
            'password': password
        }
        # recebe dados para login
        auth_response = requests.post(
            self.__auth_url,
            data=auth_payload
        )

        if auth_response.status_code == 200:
            ("Status Code:", auth_response.status_code)
            ("Response Text:", auth_response.text)
            return auth_response.json()
            # vai retornar a mesma resposta que recebiamos no postman o refres e o access com os tokens
        return {'error': f'Erro ao autenticar. Status code: {auth_response.content}'}
