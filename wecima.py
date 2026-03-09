# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://wecima.click/'

def show_categories(add_func):
    add_func('🎬 أفلام', BASE_URL + 'category/film', 'wecima_list', '')
    add_func('📺 مسلسلات', BASE_URL + 'category/series', 'wecima_list', '')
    add_func('🎬 أفلام أجنبي', BASE_URL + 'category/foreign-films', 'wecima_list', '')
    add_func('📺 مسلسلات أجنبي', BASE_URL + 'category/foreign-series', 'wecima_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'category/turkish', 'wecima_list', '')