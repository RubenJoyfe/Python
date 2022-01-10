# import spotipy
import os, json, webbrowser
import requests
from requests.api import head

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
spotify_user_id = 'rauby2rakh67zr9304hy081ja'
path_base = os.path.dirname(os.path.abspath(__file__))
header_auth = None

def auth(client_id='a652b62ed1fe4a889bf0405a6eef69b9', client_secret='62315385f9c64b56bc5f8e5de9d52473'):
    global header_auth
    # auth_data  =  {
    #     'grant_type': 'client_credentials',
    #     'client_id': client_id,
    #     'client_secret': client_secret
    # }

    # auth_response = requests.post(AUTH_URL, auth_data)

    # # print(auth_response.status_code)
    # # print(auth_response.text)

    # if auth_response.status_code == 200:
    #     token = auth_response.json()['access_token']
    #     print(token)
    #     header_auth = {'Authorization': f'Bearer {token}'}
    #     return True
    # return False
    # https://developer.spotify.com/console/post-playlists/?user_id=&body=%7B%22name%22%3A%22New%20Playlist%22%2C%22description%22%3A%22New%20playlist%20description%22%2C%22public%22%3Afalse%7D
    token = 'BQBwtnObQ0on2EQnCzT7FzHMAufeQnyomDPzRTriTDsi2HakKQbAgOoPr3qP4CT8O1J0zjpXGRnt-bbbRKw5FOh03fzoTkGVd45_PN-Y5-uQ_QAXmyXF5Ye9lOX1QWQNb6cKYTyYGnk8dcoLHqzQJMzIXb58B-wvOKD9zJKHlZBA-PpWUPENCm5fwzVWwsUE8WF5nVO3gHE8eLgC_bI0dlWCUlK5sptAlJVQUeBdqdSTv_Rnmtr1EY08NgM1ZZHWLP0cF0f-ARjzqM7PAg'
    header_auth = {'Authorization': f'Bearer {token}'}
    return True

def get_album(album_id = '4aawyAB9vmqN3uQ7FjRGTy', save=False):
    r = requests.get(f'{BASE_URL}albums/{album_id}', headers=header_auth)
    if r.status_code != 200:
        print("Fallo")
        return None
    data = r.json()
    print(data)
    if save:
        with open(f'{path_base}/{album_id}.json', 'w',  encoding='UTF-8') as f:
            f.write(json.dumps(data, indent=4))
    return data

def new_playlist(name, description, privacy):
    data = {
        'name': name,
        'description': description,
        'public': privacy
    }
    r = requests.post(f'{BASE_URL}users/{spotify_user_id}/playlists', headers=header_auth, json=data)
    print(r.status_code)
    print(r.text)
    print(header_auth)

def get_user_playlists(user, write):
    r = requests.get(f'{BASE_URL}users/{user}/playlists', headers=header_auth)
    if r.status_code != 200:
        print(r.json())
        return []
    if write:
        with open(f'{path_base}/playlists.json', 'w',  encoding='UTF-8') as f:
            f.write(json.dumps(r.json()['items'], indent=4))
    return r.json()['items']

def add_track_to_playlist(track_uri, playlist_id):
    data = {
        'position': 0,
        'uris': [track_uri]
    }
    r = requests.post(
        f'{BASE_URL}playlists/{playlist_id}/tracks',
        headers=header_auth,
        json=data
    )
    if r.status_code != 201:
        return False
    return True

def search_tracks(search):
    params = {
        'q': search,
        'type': 'track'
    }
    r = requests.get(
        f'{BASE_URL}search',
        headers=header_auth,
        params=params
    )
    if r.status_code != 200:
        return []
    return r.json()['tracks']['items']

if not auth(): #se podrían pasar parametros
    exit(-1)

#AÑADIR UNA CANCION A SPOTIFY
playlists = get_user_playlists(spotify_user_id, False)
for index, playlist in enumerate(playlists):
    print(f"{index+1} - {playlist['name']}")

try:
    playlist_index = int(input('Número de la lista: '))
except Exception:
    playlist_index = 1
playlist_index -= 1
playlist = playlists[playlist_index]
print(f'Has seleccionado: {playlist["name"]}')

##BUSCA ALBUM Y TE MUESTRA LOS RESULTADOS
# album = get_album('0JGOiO34nwfUdDrD612dOp', False) #HTE
# album = get_album('0S0KGZnfBGSIssfF54WSJh', False) #WWAFAWDWG
# tracks = []
# for item in album['tracks']['items']:
#     dic = {'name': item['name'], 'uri': item['uri']}
#     tracks.append(dic)
    
# for index, track in enumerate(tracks):
#     print(f"{index+1} - {track['name']}")

# try:
#     track_index = int(input('Número de la canción: '))
# except Exception:
#     track_index = 1
# track_index -= 1
# track = tracks[track_index]
# print(f'La canción seleccionada es: {track["name"]}')


##BUSCA CANCION
search = input('Buscar canción: ')
tracks = search_tracks(search)
if len(tracks) < 1:
    exit(0)
track = tracks[0]

#AÑADE PISTA A PLAYLIST
r = add_track_to_playlist(track['uri'], playlist['id'])

if r:
    print('Canción añadida')
else:
    print('Fallo')



# new_playlist('BE','shhhh',False)
# playlists = get_user_playlists(spotify_user_id, False) #True para guardar en fichero playlists.json
# print(playlists)


### get_album("0JGOiO34nwfUdDrD612dOp", True) #BILLIE






# #HACER LISTA CON CANCIONES Y ABRIRLAS EN WEB

# with open(f'{path_base}/spotipy.json', 'r',  encoding='UTF-8') as f:
#     data = f.read()

# data = json.loads(data)
# ##urls = []
# ## info = {}
# tracks = []

# for item in data['tracks']['items']:
#     dic = {'name':item['name'], 'url':item['external_urls']['spotify']}
#     tracks.append(dic)
#     ## urls.append(item['external_urls']['spotify'])
#     ## info[item['name']] = item['external_urls']['spotify']

# for i, song in enumerate(tracks):
#     print(f'{i+1}-{song["name"]}')

# try:
#     select = int(input('Número de la canción: '))
# except Exception:
#     select = 1

# select-=1
# track = tracks[select]
# webbrowser.open_new(track['url'])

# print(info)
# print(urls)








# result = requests.get('https://google.com')

# if result.status_code == 200:
#     with open(f'{path_base}/google.html', 'w', encoding=result.encoding):
#         file.write(result.text)
#     print('Correcto')
# else:
#     print('Conexión fallida, compruebe su conexión a internet o inténtelo más tarde.')