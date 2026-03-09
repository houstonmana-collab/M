# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://mycima.sbs/'

def show_categories(add_func):
    add_func('🎬 أفلام عربي', BASE_URL + 'category/افلام-عربي', 'mycima_list', '')
    add_func('📺 مسلسلات عربية', BASE_URL + 'category/مسلسلات-عربية', 'mycima_list', '')
    add_func('🎬 أفلام أجنبي', BASE_URL + 'category/افلام-اجنبي', 'mycima_list', '')
    add_func('📺 مسلسلات أجنبية', BASE_URL + 'category/مسلسلات-اجنبية', 'mycima_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'category/مسلسلات-تركية', 'mycima_list', '')