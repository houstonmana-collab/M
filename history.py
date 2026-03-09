# -*- coding: utf-8 -*-
import os
import json
import time
import xbmc
import xbmcaddon

addon = xbmcaddon.Addon()
profile_path = xbmc.translatePath(addon.getAddonInfo('profile'))
history_file = os.path.join(profile_path, 'history.json')

def add_to_history(title, url, site, progress=0):
    try:
        history = load_history()
        for i, item in enumerate(history):
            if item['url'] == url:
                history[i]['last_watch'] = time.time()
                history[i]['progress'] = progress
                save_history(history)
                return
        history.append({
            'title': title, 'url': url, 'site': site,
            'first_watch': time.time(), 'last_watch': time.time(),
            'progress': progress, 'watched_count': 1
        })
        save_history(history)
    except:
        pass

def load_history():
    try:
        if os.path.exists(history_file):
            with open(history_file, 'r', encoding='utf-8') as f:
                return json.load(f)
    except:
        pass
    return []

def save_history(history):
    try:
        if not os.path.exists(profile_path):
            os.makedirs(profile_path)
        with open(history_file, 'w', encoding='utf-8') as f:
            json.dump(history, f, ensure_ascii=False, indent=2)
    except:
        pass

def get_recently_watched(limit=20):
    history = load_history()
    history.sort(key=lambda x: x['last_watch'], reverse=True)
    return history[:limit]