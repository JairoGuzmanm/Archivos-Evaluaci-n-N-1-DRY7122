import json

with open ('/home/devasc/labs/devnet-src/parsing/myfile.json', 'r') as json_file:
    ourjson = json.load (json_file)
    print("El Token de acceso es: {}".format(ourjson['access_token']))
    print("El Token caduca en: {} segundos".format(ourjson['expires_in']))
    print("El Token de refresco es: {}".format(ourjson['refresh_token']))
    print("El Token caduca en: {} segundos".format(ourjson['refreshtokenexpires_in']))