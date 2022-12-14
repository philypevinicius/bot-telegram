import json
import requests


def pokedex(id_name):
    try:
        output= ""
        url = "https://pokeapi.co/api/v2/pokemon/{}/"
        #get request for API information retrieval
        final_url = url.format(id_name)
        response = requests.get(final_url)
        response = response.content
        #json to python dictionary convertion
        information=json.loads(response)
        #getting all the information 
        output += f"<b>ID:</b> {str(information['id'])} \n"
        output += f"<b>Nome:</b> {str(information['name'])}\n"
        
        all_types=information['types']
        types = ""
        for type_ in all_types:
            types += f"{type_['type']['name']} "
        
        output += f"<b>Tipo:</b> {str(types)} \n"
        all_moves=information['moves']

        moves = ""
        #getting 5 moves of the pokemon
        if len(all_moves) < 4:
            for i in range(len(all_moves)):
                moves += f"<b>{i+1}:</b> {all_moves[i]['move']['name']} \n"
        else:
            for i in range(4):
                moves += f"<b>{i+1}:</b> {all_moves[i]['move']['name']} \n"
        output += f"<b>Movimentos:\n</b> {moves}\n"

        if information['id'] <= 890:
            photo_url = f"https://pokeres.bastionbot.org/images/pokemon/{information['id']}.png"
        else:
            photo_url = None

    except json.decoder.JSONDecodeError:
        output = None
        photo_url = None
    return output,photo_url

