import json, requests, os, webbrowser

AUTH_URL = 'https://accounts.spotify.com/api/token'
BASE_URL = 'https://api.spotify.com/v1/'
spotify_user_id = 'rauby2rakh67zr9304hy081ja'
path_base = os.path.dirname(os.path.abspath(__file__))
header_auth = None

def auth(client_id = 'a652b62ed1fe4a889bf0405a6eef69b9', client_secret = '62315385f9c64b56bc5f8e5de9d52473'):
    global header_auth
    # auth_data = {
    #     'grant_type': 'client_credentials',
    #     'client_id': client_id,
    #     'client_secret': client_secret,
    #     'username': 'UserTest'
    # }
    # auth_response = requests.post(AUTH_URL, auth_data)

    # if auth_response.status_code == 200:
    #     token = auth_response.json()['access_token']
    #     print(token)
    #     header_auth = {'Authorization': f'Bearer {token}'}
    #     return True
    # https://developer.spotify.com/console/post-playlists/?user_id=&body=%7B%22name%22%3A%22New%20Playlist%22%2C%22description%22%3A%22New%20playlist%20description%22%2C%22public%22%3Afalse%7D
    token = 'BQBxvzHGSSZK_wuG-Dcks5qVlRHN-Znc7FbwNAx7Ha4nCRnckAfm_0HkhGqGqT2qX8hEWXsqRrwwMhZgJGIK3XVFtNCugd-dqnk-Ax8Us7XwnUR_wTTy6CgYQtExA2QspxskhpSNynbiWfYFsH3TREPG6ZcS3fZ6v0tc0vcM-zbdT1Snvmv7JGK8_gH-j-REaC-yO7A-Ho9OlqLv5-5n43JiXTyo0cVs3AX-60IVzsztwwQbHBevaoM'
    header_auth = {'Authorization': f'Bearer {token}'}
    return True

def get_album(album_id='4aawyAB9vmqN3uQ7FjRGTy', save = False):
    r = requests.get(f'{BASE_URL}albums/{album_id}', headers=header_auth)
    if r.status_code != 200:
        return None
    data = r.json()
    if save:
        with open(f'{path_base}/{album_id}.json', 'w',  encoding='UTF-8') as f:
            f.write(json.dumps(data, indent=4))
    return data

def new_playlist(name, description = '', public = False):
    data = {
        'name': name,
        'description': description,
        'public': public
    }
    r = requests.post(f'{BASE_URL}users/{spotify_user_id}/playlists', headers=header_auth, json=data)
    print(r.status_code)
    print(r.json())

def get_user_playlists(user):
    r = requests.get(f'{BASE_URL}users/{user}/playlists', headers=header_auth)
    if r.status_code != 200:
        print(r.json())
        return []
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

if not auth():
    exit(-1)

# new_playlist('Desde Python')
playlists = get_user_playlists(spotify_user_id)
for index, playlist in enumerate(playlists):
    print(f"{index+1} - {playlist['name']}")

try:
    playlist_index = int(input('Número de la lista: '))
except Exception:
    playlist_index = 1
playlist_index -= 1
playlist = playlists[playlist_index]
# print(f'Has seleccionado: {playlist["name"]}')

# album = get_album()
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

search = input('Buscar canción: ')
tracks = search_tracks(search)
if len(tracks) < 1:
    exit(0)
track = tracks[0]

r = add_track_to_playlist(track['uri'], playlist['id'])
if r:
    print('Canción añadida')
else:
    print('Fallo')