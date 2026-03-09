# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://cima4ever.tv/'

def show_categories(add_func):
    add_func('🎬 1080p افلام', BASE_URL + 'category/1080p', 'cima4ever_list', '')
    add_func('🎬 720p افلام', BASE_URL + 'category/720p', 'cima4ever_list', '')
    add_func('📺 مسلسلات 1080p', BASE_URL + 'category/series-1080p', 'cima4ever_list', '')
    add_func('🎬 افلام اجنبي', BASE_URL + 'foreign-movies', 'cima4ever_list', '')
    add_func('🎬 افلام عربي', BASE_URL + 'arabic-movies', 'cima4ever_list', '')
    add_func('📺 مسلسلات تركية', BASE_URL + 'turkish-series', 'cima4ever_list', '')
    add_func('📺 مسلسلات كورية', BASE_URL + 'korean-series', 'cima4ever_list', '')
    add_func('⭐ افلام IMDB عالي', BASE_URL + 'top-imdb', 'cima4ever_list', '')