# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://bluray4k.net/'

def show_categories(add_func):
    add_func('🎬 4k BluRay افلام', BASE_URL + '4k-bluray', 'bluray4k_list', '')
    add_func('🎬 1080p BluRay افلام', BASE_URL + '1080p-bluray', 'bluray4k_list', '')
    add_func('📺 4k BluRay مسلسلات', BASE_URL + 'series-4k', 'bluray4k_list', '')
    add_func('📺 1080p BluRay مسلسلات', BASE_URL + 'series-1080p', 'bluray4k_list', '')
    add_func('🎬 افلام عربي', BASE_URL + 'arabic', 'bluray4k_list', '')
    add_func('🎬 افلام اجنبي', BASE_URL + 'foreign', 'bluray4k_list', '')
    add_func('🎬 افلام حديثة', BASE_URL + 'latest', 'bluray4k_list', '')
    add_func('⭐ افلام IMDB عالي', BASE_URL + 'top-imdb', 'bluray4k_list', '')