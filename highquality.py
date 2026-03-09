# -*- coding: utf-8 -*-

class QualityManager:
    """إدارة جودة الفيديو"""
    
    QUALITIES = {
        '4k': {'name': '4K UHD', 'priority': 5, 'patterns': ['4k', '2160', 'uhd']},
        '1080p': {'name': '1080p Full HD', 'priority': 4, 'patterns': ['1080', 'full hd', 'fhd']},
        '720p': {'name': '720p HD', 'priority': 3, 'patterns': ['720', 'hd']},
        '480p': {'name': '480p SD', 'priority': 2, 'patterns': ['480', 'sd']},
        '360p': {'name': '360p', 'priority': 1, 'patterns': ['360']}
    }
    
    @classmethod
    def detect_quality(cls, title, url=''):
        """اكتشاف جودة الفيديو من العنوان أو الرابط"""
        text = f"{title} {url}".lower()
        detected_quality = '360p'
        detected_priority = 1
        
        for quality, info in cls.QUALITIES.items():
            for pattern in info['patterns']:
                if pattern in text:
                    if info['priority'] > detected_priority:
                        detected_quality = quality
                        detected_priority = info['priority']
                    break
        return detected_quality, cls.QUALITIES[detected_quality]['name']
    
    @classmethod
    def sort_by_quality(cls, items):
        """ترتيب العناصر حسب الجودة (الأعلى أولاً)"""
        return sorted(items, 
                     key=lambda x: cls.QUALITIES.get(cls.detect_quality(x.get('title', ''), x.get('url', ''))[0], 
                                                     cls.QUALITIES['360p'])['priority'], 
                     reverse=True)