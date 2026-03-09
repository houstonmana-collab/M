# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://shahed4u.cam/'

def show_categories(add_func):
    add_func('🎬 أفلام', BASE_URL + 'category/افلام-عربي', 'shahed_list', '')
    add_func('📺 مسلسلات', BASE_URL + 'category/مسلسلات-عربية', 'shahed_list', '')
    add_func('🎬 أفلام اجنبي', BASE_URL + 'category/افلام-اجنبية', 'shahed_list', '')
    add_func('📺 مسلسلات اجنبية', BASE_URL + 'category/مسلسلات-اجنبية', 'shahed_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'category/مسلسلات-تركية', 'shahed_list', '')
    add_func('🇮🇳 افلام هندية', BASE_URL + 'category/افلام-هندية', 'shahed_list', '')