# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://akwam.to/'

def show_categories(add_func):
    add_func('🎬 أفلام', BASE_URL + 'movies', 'akwam_list', '')
    add_func('📺 مسلسلات', BASE_URL + 'series', 'akwam_list', '')
    add_func('🎬 أفلام أجنبي', BASE_URL + 'movies/foreign', 'akwam_list', '')
    add_func('📺 مسلسلات أجنبي', BASE_URL + 'series/foreign', 'akwam_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'series/turkish', 'akwam_list', '')
    add_func('🇰🇷 مسلسلات كورية', BASE_URL + 'series/korean', 'akwam_list', '')