# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://4karab.net/'

def show_categories(add_func):
    add_func('🎬 4k افلام', BASE_URL + '4k-movies', 'fourkarab_list', '')
    add_func('📺 4k مسلسلات', BASE_URL + '4k-series', 'fourkarab_list', '')
    add_func('🎬 4k افلام عربي', BASE_URL + 'arabic-4k', 'fourkarab_list', '')
    add_func('🎬 4k افلام اجنبي', BASE_URL + 'foreign-4k', 'fourkarab_list', '')
    add_func('🇹🇷 4k مسلسلات تركية', BASE_URL + 'turkish-4k', 'fourkarab_list', '')
    add_func('🇰🇷 4k مسلسلات كورية', BASE_URL + 'korean-4k', 'fourkarab_list', '')
    add_func('🎬 افلام 2025', BASE_URL + '2025', 'fourkarab_list', '')
    add_func('🎬 افلام 2024', BASE_URL + '2024', 'fourkarab_list', '')