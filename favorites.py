# -*- coding: utf-8 -*-
import os
import json
import xbmc
import xbmcgui
import xbmcaddon

addon = xbmcaddon.Addon()
profile_path = xbmc.translatePath(addon.getAddonInfo('profile'))
favorites_file = os.path.join(profile_path, 'favorites.json')

def load_favorites():
    try:
        if os.path.exists(favorites_file):
            with open(favorites_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return []

def save_favorites(favorites):
    try:
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)
        with open(favorites_file, 'w', encoding='utf-8') as f:
            json.dump(favorites, f, ensure_ascii=False, indent=2)
    except:
        pass

def add_to_favorites(title, url, thumb, site):
    favorites = load_favorites()
    for item in favorites:
        if item['url'] == url:
            xbmcgui.Dialog().notification('المفضلة', 'العنصر موجود بالفعل', xbmcgui.NOTIFICATION_INFO, 2000)
            return
    favorites.append({'title': title, 'url': url, 'thumb': thumb, 'site': site})
    save_favorites(favorites)
    xbmcgui.Dialog().notification('المفضلة', 'تمت الإضافة', xbmcgui.NOTIFICATION_INFO, 2000)