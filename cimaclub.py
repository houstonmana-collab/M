# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from resources.lib import adblocker
from resources.lib import highquality

BASE_URL = 'https://cimaclub.us/'

def show_categories(add_func):
    add_func('🎬 4k UHD', BASE_URL + 'category/4k-uhd', 'cimaclub_list', '')
    add_func('🎬 1080p WEB-DL', BASE_URL + 'category/1080p', 'cimaclub_list', '')
    add_func('🎬 1080p BluRay', BASE_URL + 'category/bluray-1080p', 'cimaclub_list', '')
    add_func('📺 مسلسلات 1080p', BASE_URL + 'category/series-1080p', 'cimaclub_list', '')
    add_func('📺 مسلسلات 4k', BASE_URL + 'category/series-4k', 'cimaclub_list', '')
    add_func('🎬 افلام عربي', BASE_URL + 'category/arabic', 'cimaclub_list', '')
    add_func('🎬 افلام اجنبي', BASE_URL + 'category/foreign', 'cimaclub_list', '')
    add_func('🇹🇷 مسلسلات تركية', BASE_URL + 'category/turkish', 'cimaclub_list', '')