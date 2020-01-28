import requests

base_url = 'https://pokeapi.co/api/v2/'
endpoint_url = 'version/'
game_name = 'red'


def test_get_game_status():
    resp = requests.get(base_url+endpoint_url+game_name)
    assert resp.status_code == 200, "Status 200"

def test_get_game_wrong():
    resp = requests.get(base_url + endpoint_url + 'm')
    assert resp.status_code == 404, "Status 404"

def test_get_game_content_type():
    resp = requests.get(base_url + endpoint_url + game_name)
    assert resp.headers['Content-Type'] == 'application/json; charset=utf-8', "Content-Type correto"

def test_get_game_name():
    resp = requests.get(base_url+endpoint_url+game_name)
    response_body = resp.json()
    assert response_body['name'] == game_name, "Nome do jogo retornou correto"