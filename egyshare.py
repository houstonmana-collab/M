# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://egyshare.net/'

def show_categories(add_func):
    add_func('🎬 4k افلام', BASE_URL + '4k', 'egyshare_list', '')
    add_func('🎬 1080p افلام', BASE_URL + '1080p', 'egyshare_list', '')
    add_func('🎬 720p افلام', BASE_URL + '720p', 'egyshare_list', '')
    add_func('📺 1080p مسلسلات', BASE_URL + 'series-1080p', 'egyshare_list', '')
    add_func('📺 4k مسلسلات', BASE_URL + 'series-4k', 'egyshare_list', '')
    add_func('🇺🇸 افلام اجنبي', BASE_URL + 'foreign', 'egyshare_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'turkish', 'egyshare_list', '')
    add_func('🇰🇷 مسلسلات كورية', BASE_URL + 'korean', 'egyshare_list', '')