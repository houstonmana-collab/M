# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://arabseed.ink/'

def show_categories(add_func):
    add_func('🎬 أفلام عربي', BASE_URL + 'movie', 'arabseed_list', '')
    add_func('📺 مسلسلات عربي', BASE_URL + 'series', 'arabseed_list', '')
    add_func('🎬 أفلام أجنبي', BASE_URL + 'category/foreign', 'arabseed_list', '')
    add_func('📺 مسلسلات أجنبي', BASE_URL + 'category/series-foreign', 'arabseed_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'category/turkish-series', 'arabseed_list', '')
    add_func('🇰🇷 مسلسلات كورية', BASE_URL + 'category/korean-series', 'arabseed_list', '')