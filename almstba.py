# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://almstba.tv/'

def show_categories(add_func):
    add_func('🎬 أفلام', BASE_URL + 'category/افلام', 'almstba_list', '')
    add_func('📺 مسلسلات', BASE_URL + 'category/مسلسلات', 'almstba_list', '')
    add_func('🎬 افلام اجنبية', BASE_URL + 'category/افلام-اجنبية', 'almstba_list', '')
    add_func('📺 مسلسلات اجنبية', BASE_URL + 'category/مسلسلات-اجنبية', 'almstba_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'category/مسلسلات-تركية', 'almstba_list', '')
    add_func('🇰🇷 مسلسلات كورية', BASE_URL + 'category/مسلسلات-كورية', 'almstba_list', '')