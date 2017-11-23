import requests
import json

twitch_client_id = "lczmfwmcxe7cv8xozsfnqxdrn1e6x9"

def set_game(game, api, token):
    print('Setting to: ' + game)
    twitch_game_dict = {'channel': {'game': game}}
    twitch_game_headers = {'Content-Type': 'application/json', 'Client-ID': twitch_client_id, 'Authorization': 'OAuth ' + token}
    twitch_request = requests.put(api, headers=twitch_game_headers, data=json.dumps(twitch_game_dict))

def lambda_handler(event, context):
    twitch_user = event['twitch_user']
    twitch_channel_api = "https://api.twitch.tv/kraken/channels/" + twitch_user
    twitch_oath_token = event['twitch_oath_token']
    twitch_game = event['twitch_game']
    set_game(twitch_game, twitch_channel_api, twitch_oath_token)
