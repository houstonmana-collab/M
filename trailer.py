# -*- coding: utf-8 -*-
import xbmc
from urllib.parse import quote

def play_trailer(movie_name, year=''):
    try:
        search_query = quote(f"{movie_name} {year} trailer")
        youtube_url = f'plugin://plugin.video.youtube/search/?q={search_query}'
        xbmc.executebuiltin(f'PlayMedia({youtube_url})')
    except:
        pass