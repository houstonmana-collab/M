# -*- coding: utf-8 -*-
import requests

def get_imdb_rating(movie_name, year=''):
    try:
        search_url = f'https://v2.sg.media-imdb.com/suggestion/{movie_name[0].lower()}/{movie_name.replace(" ", "_")}.json'
        response = requests.get(search_url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            if 'd' in data and len(data['d']) > 0:
                for item in data['d']:
                    if 'y' in item and year and str(item['y']) == str(year):
                        return item.get('i', [{}])[0], item.get('s', '')
    except:
        pass
    return '', 