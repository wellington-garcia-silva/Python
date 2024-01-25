import requests
try:
    url = "https://www.youtube.com/"
    response = requests.get(url)
    # Verifique se a requisição foi bem-sucedida (código 200)
    if response.status_code == 200:
        # Exiba o conteúdo da página
        print(response.text)
except:
    print('O site do youTube não está disponível no momento.')