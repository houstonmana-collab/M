# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://waqtelafilam.com/'

def show_categories(add_func):
    add_func('🎬 4K افلام', BASE_URL + '4k', 'waqt_list', '')
    add_func('🎬 1080p افلام', BASE_URL + '1080p', 'waqt_list', '')
    add_func('🎬 720p افلام', BASE_URL + '720p', 'waqt_list', '')
    add_func('📺 4k مسلسلات', BASE_URL + 'series-4k', 'waqt_list', '')
    add_func('📺 1080p مسلسلات', BASE_URL + 'series-1080p', 'waqt_list', '')
    add_func('🎬 افلام عربي', BASE_URL + 'arabic-movies', 'waqt_list', '')
    add_func('🎬 افلام اجنبي', BASE_URL + 'foreign-movies', 'waqt_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'turkish-series', 'waqt_list', '')
    add_func('⭐ الافضل تقييماً', BASE_URL + 'top-imdb', 'waqt_list', '')