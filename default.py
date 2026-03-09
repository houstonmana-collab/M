# -*- coding: utf-8 -*-
import sys
import xbmc
import xbmcgui
import xbmcplugin
import xbmcaddon
from urllib.parse import parse_qs

# استيراد جميع المواقع
from resources.lib import wecima
from resources.lib import akwam
from resources.lib import mycima
from resources.lib import arabseed
from resources.lib import shahed
from resources.lib import almstba
from resources.lib import egybest
from resources.lib import waqt
from resources.lib import cimalight
from resources.lib import cima4ever
from resources.lib import egyshare
from resources.lib import cimaclub
from resources.lib import arabseed4k
from resources.lib import fourkarab
from resources.lib import bluray4k

# استيراد المكتبات المساعدة
from resources.lib import adblocker
from resources.lib import highquality
from resources.lib import filters
from resources.lib import favorites
from resources.lib import history
from resources.lib import trailer
from resources.lib import imdb
from resources.lib import subtitles

# معلومات الإضافة
addon = xbmcaddon.Addon()
addon_handle = int(sys.argv[1])
base_url = sys.argv[0]
args = parse_qs(sys.argv[2][1:])

def build_url(query):
    """بناء رابط داخلي للإضافة"""
    return base_url + '?' + query

def add_menu_item(name, url, mode, icon='', is_folder=True):
    """إضافة عنصر قائمة"""
    try:
        url = build_url(f'mode={mode}&url={url}&name={name}')
        li = xbmcgui.ListItem(name)
        li.setArt({'thumb': icon, 'icon': icon})
        
        if not is_folder:
            li.setProperty('IsPlayable', 'true')
            li.setInfo('video', {'title': name, 'mediatype': 'video'})
        
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=is_folder)
    except:
        pass

def add_video_item(name, url, icon, plot='', year=''):
    """إضافة عنصر فيديو (فيلم أو حلقة)"""
    try:
        url = build_url(f'mode=play&url={url}&name={name}')
        li = xbmcgui.ListItem(name)
        li.setArt({'thumb': icon, 'icon': icon})
        
        info = {'title': name, 'mediatype': 'video', 'plot': plot}
        if year:
            info['year'] = int(year)
        
        li.setInfo('video', info)
        li.setProperty('IsPlayable', 'true')
        xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=False)
    except:
        pass

def play_video(url, title, thumb, site):
    """تشغيل الفيديو مع تحديث السجل"""
    try:
        history.add_to_history(title, url, site, 0)
        play_item = xbmcgui.ListItem(title, path=url)
        play_item.setArt({'thumb': thumb, 'icon': thumb})
        play_item.setInfo('video', {'title': title, 'mediatype': 'video'})
        play_item.setProperty('IsPlayable', 'true')
        xbmcplugin.setResolvedUrl(addon_handle, True, play_item)
    except:
        pass

def get_clean_content(url, timeout=10):
    """الحصول على محتوى نظيف من موقع مع حجب الإعلانات"""
    response = adblocker.AdBlocker.get_clean_response(url, timeout)
    if response and response.status_code == 200:
        return response.text
    return ''

def show_movie_details(title, url, thumb, site, year=''):
    """عرض تفاصيل الفيلم مع خيارات متقدمة"""
    try:
        imdb_rating, imdb_plot = imdb.get_imdb_rating(title, year)
        dialog = xbmcgui.Dialog()
        options = ['▶️ مشاهدة', '🎬 إعلان تشويقي', '⭐ إضافة للمفضلة', '📝 ترجمة']
        
        selected = dialog.select(f'🎬 {title}', options)
        
        if selected == 0:
            play_video(url, title, thumb, site)
        elif selected == 1:
            trailer.play_trailer(title, year)
        elif selected == 2:
            favorites.add_to_favorites(title, url, thumb, site)
        elif selected == 3:
            subs = subtitles.search_subtitles(title, year)
            if subs:
                sub_list = [s['name'] for s in subs]
                sub_choice = dialog.select('اختر ترجمة', sub_list)
                if sub_choice >= 0:
                    xbmcgui.Dialog().notification('ترجمة', 'تم اختيار الترجمة', xbmcgui.NOTIFICATION_INFO, 2000)
    except:
        pass

def show_main_menu():
    """عرض القائمة الرئيسية"""
    # مواقع الجودة العالية
    add_menu_item('🎬 [4K] وقت الافلام', 'waqt', 'site_menu', '')
    add_menu_item('🎬 [4K] 4k عرب', '4karab', 'site_menu', '')
    add_menu_item('🎬 [BluRay] بلو راي 4k', 'bluray4k', 'site_menu', '')
    add_menu_item('🎬 [WEB-DL] سيما لايت', 'cimalight', 'site_menu', '')
    add_menu_item('🎬 سيما فور ايفر', 'cima4ever', 'site_menu', '')
    add_menu_item('🎬 ايجي شير', 'egyshare', 'site_menu', '')
    add_menu_item('🎬 سيما كلوب', 'cimaclub', 'site_menu', '')
    add_menu_item('🎬 عرب سيد 4k', 'arabseed4k', 'site_menu', '')
    
    # مواقع عامة
    add_menu_item('📺 وي سيما', 'wecima', 'site_menu', '')
    add_menu_item('📺 أكوام', 'akwam', 'site_menu', '')
    add_menu_item('📺 ماي سيما', 'mycima', 'site_menu', '')
    add_menu_item('📺 عرب سيد', 'arabseed', 'site_menu', '')
    add_menu_item('📺 شاهد', 'shahed', 'site_menu', '')
    add_menu_item('📺 المصطبة', 'almstba', 'site_menu', '')
    add_menu_item('📺 ايجي بست', 'egybest', 'site_menu', '')
    
    add_menu_item('', '', 9999, '')  # فاصل
    
    # فلاتر شاملة
    add_menu_item('🎬 تصفح الأفلام حسب النوع', 'global', 'global_movie_genres', '')
    add_menu_item('📺 تصفح المسلسلات حسب النوع', 'global', 'global_series_genres', '')
    add_menu_item('🌍 تصفح المسلسلات حسب الدولة', 'global', 'global_countries', '')
    add_menu_item('🇪🇬 مسلسلات مصرية', 'global', 'global_egyptian', '')
    add_menu_item('🇸🇾 مسلسلات سورية', 'global', 'global_syrian', '')
    add_menu_item('🇹🇷 مسلسلات تركية', 'global', 'global_turkish', '')
    add_menu_item('🇰🇷 مسلسلات كورية', 'global', 'global_korean', '')
    add_menu_item('🇮🇳 مسلسلات هندية', 'global', 'global_indian', '')
    add_menu_item('🏝️ مسلسلات خليجية', 'global', 'global_gulf', '')
    add_menu_item('🌍 مسلسلات عربية', 'global', 'global_arab', '')
    
    add_menu_item('', '', 9999, '')  # فاصل
    
    add_menu_item('📅 أفلام حسب السنة', 'global', 'global_years', '')
    add_menu_item('📅 أفلام حسب العقد', 'global', 'global_decades', '')
    
    add_menu_item('', '', 9999, '')  # فاصل
    
    add_menu_item('🔍 بحث في كل المواقع', '', 'search_all', '')
    add_menu_item('⭐ المفضلة', '', 'favorites', '')
    add_menu_item('📜 آخر المشاهدات', '', 'history', '')
    add_menu_item('⚙️ إعدادات', '', 'settings', '')
    
    xbmcplugin.endOfDirectory(addon_handle)

def main():
    """الدالة الرئيسية"""
    mode = args.get('mode', [None])[0]
    
    if mode is None:
        show_main_menu()
    
    elif mode == 'site_menu':
        site = args.get('url', [''])[0]
        if site == 'wecima':
            wecima.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'akwam':
            akwam.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'mycima':
            mycima.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'arabseed':
            arabseed.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'shahed':
            shahed.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'almstba':
            almstba.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'egybest':
            egybest.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'waqt':
            waqt.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'cimalight':
            cimalight.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'cima4ever':
            cima4ever.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'egyshare':
            egyshare.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'cimaclub':
            cimaclub.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'arabseed4k':
            arabseed4k.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == '4karab':
            fourkarab.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        elif site == 'bluray4k':
            bluray4k.show_categories(lambda n, u, m, i: add_menu_item(n, u, m, i))
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_movie_genres':
        filters.MovieFilters.show_movie_genres(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_series_genres':
        filters.MovieFilters.show_series_genres(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_countries':
        filters.MovieFilters.show_countries(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_egyptian':
        add_menu_item('🇪🇬 مسلسلات مصرية', 'egypt', 'egyptian_series', '')
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_syrian':
        add_menu_item('🇸🇾 مسلسلات سورية', 'syria', 'syrian_series', '')
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_turkish':
        add_menu_item('🇹🇷 مسلسلات تركية', 'turkey', 'turkish_series', '')
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_korean':
        add_menu_item('🇰🇷 مسلسلات كورية', 'korea', 'korean_series', '')
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_indian':
        add_menu_item('🇮🇳 مسلسلات هندية', 'india', 'indian_series', '')
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_gulf':
        filters.MovieFilters.show_gulf_series(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_arab':
        filters.MovieFilters.show_arab_series(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_years':
        filters.YearFilters.show_years(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'global_decades':
        filters.YearFilters.show_decades(add_menu_item)
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'favorites':
        favs = favorites.load_favorites()
        for item in favs:
            add_video_item(item['title'], item['url'], item['thumb'])
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'history':
        recent = history.get_recently_watched()
        for item in recent:
            title = item['title']
            if item['progress'] > 0:
                title += f' [{item["progress"]}%]'
            add_video_item(title, item['url'], '')
        xbmcplugin.endOfDirectory(addon_handle)
    
    elif mode == 'search_all':
        search_text = xbmcgui.Dialog().input('بحث في كل المواقع:', type=xbmcgui.INPUT_ALPHANUM)
        if search_text:
            xbmc.executebuiltin('Container.Update(%s)' % build_url(f'mode=search_results&query={search_text}'))
    
    elif mode == 'settings':
        addon.openSettings()
    
    elif mode == 'play':
        url = args.get('url', [''])[0]
        name = args.get('name', [''])[0]
        play_item = xbmcgui.ListItem(name, path=url)
        play_item.setProperty('IsPlayable', 'true')
        xbmcplugin.setResolvedUrl(addon_handle, True, play_item)

if __name__ == '__main__':
    main()