# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://egybest.nl/'

def show_categories(add_func):
    add_func('🎬 افلام عربي', BASE_URL + 'arabic', 'egybest_list', '')
    add_func('📺 مسلسلات عربي', BASE_URL + 'series/arab', 'egybest_list', '')
    add_func('🎬 افلام اجنبي', BASE_URL + 'foreign', 'egybest_list', '')
    add_func('📺 مسلسلات اجنبي', BASE_URL + 'series/foreign', 'egybest_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'series/turkish', 'egybest_list', '')
    add_func('🇰🇷 مسلسلات كورية', BASE_URL + 'series/korean', 'egybest_list', '')
    add_func('⭐ الاكثر مشاهدة', BASE_URL + 'popular', 'egybest_list', '')
    add_func('⭐ الافضل تقييماً', BASE_URL + 'top-rated', 'egybest_list', '')