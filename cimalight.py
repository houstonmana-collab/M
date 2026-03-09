# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://cimalight.com/'

def show_categories(add_func):
    add_func('🎬 1080p WEB-DL', BASE_URL + 'tag/1080p-web-dl', 'cimalight_list', '')
    add_func('🎬 1080p BluRay', BASE_URL + 'tag/1080p-bluray', 'cimalight_list', '')
    add_func('🎬 4k UHD', BASE_URL + 'tag/4k-uhd', 'cimalight_list', '')
    add_func('📺 مسلسلات 1080p', BASE_URL + 'tag/1080p-series', 'cimalight_list', '')
    add_func('📺 مسلسلات 4k', BASE_URL + 'tag/4k-series', 'cimalight_list', '')
    add_func('🇺🇸 افلام اجنبي', BASE_URL + 'foreign', 'cimalight_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'turkish', 'cimalight_list', '')