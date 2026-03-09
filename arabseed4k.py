# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://arabseed4k.net/'

def show_categories(add_func):
    add_func('🎬 4k افلام', BASE_URL + '4k-movies', 'arabseed4k_list', '')
    add_func('🎬 1080p افلام', BASE_URL + '1080p-movies', 'arabseed4k_list', '')
    add_func('📺 4k مسلسلات', BASE_URL + '4k-series', 'arabseed4k_list', '')
    add_func('📺 1080p مسلسلات', BASE_URL + '1080p-series', 'arabseed4k_list', '')
    add_func('🎬 افلام 2025', BASE_URL + 'movies-2025', 'arabseed4k_list', '')
    add_func('🎬 افلام 2024', BASE_URL + 'movies-2024', 'arabseed4k_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'turkish-4k', 'arabseed4k_list', '')
    add_func('🇺🇸 افلام اجنبي 4k', BASE_URL + 'foreign-4k', 'arabseed4k_list', '')