# -*- coding: utf-8 -*-
import re
import requests

class AdBlocker:
    """حجب الإعلانات من المواقع"""
    
    AD_DOMAINS = [
        'doubleclick.net', 'googleadservices.com', 'googlesyndication.com',
        'google-analytics.com', 'googletagmanager.com', 'adservice.google.com',
        'adsrvr.org', 'adsymptotic.com', 'adnxs.com', 'rubiconproject.com',
        'criteo.com', 'outbrain.com', 'taboola.com', 'popads.net',
        'propellerads.com', 'exoclick.com', 'trafficfactory.biz', 'adf.ly',
        'sh.st', 'bc.vc', 'adsterra.com', 'adthrive.com', 'adpushup.com',
        'amazon-adsystem.com', 'bidswitch.net', 'casalemedia.com',
        'contextweb.com', 'crwdcntrl.net', 'demdex.net', 'exponential.com',
        'infolinks.com', 'intentmedia.com', 'media.net', 'mookie1.com',
        'mopub.com', 'openx.net', 'pubmatic.com', 'pulsepoint.com',
        'revcontent.com', 'rlcdn.com', 'serving-sys.com', 'sharethrough.com',
        'skimlinks.com', 'sovrn.com', 'spotxchange.com', 'tapad.com',
        'tremorhub.com', 'triplelift.com', 'turn.com', 'uidapi.com',
        'verve.com', 'vi.ai', 'videoadex.com', 'videoamp.com', 'visx.net',
        'w55c.net', 'weborama.com', 'xaxis.com', 'yieldmo.com', 'yldbt.com',
        'zedo.com'
    ]
    
    AD_PATTERNS = [
        r'<script[^>]*data-ad-client[^>]*>.*?</script>',
        r'<script[^>]*data-ad-slot[^>]*>.*?</script>',
        r'<ins[^>]*class="adsbygoogle"[^>]*>.*?</ins>',
        r'<div[^>]*id="div-gpt-ad[^>]*>.*?</div>',
        r'<iframe[^>]*src="[^"]*doubleclick[^"]*"[^>]*>.*?</iframe>',
        r'<iframe[^>]*src="[^"]*googlesyndication[^"]*"[^>]*>.*?</iframe>',
        r'<a[^>]*href="[^"]*adf\.ly[^"]*"[^>]*>.*?</a>',
        r'<div[^>]*class="[^"]*banner[^"]*"[^>]*>.*?</div>',
        r'<div[^>]*class="[^"]*advert[^"]*"[^>]*>.*?</div>',
        r'<div[^>]*class="[^"]*sponsor[^"]*"[^>]*>.*?</div>',
        r'<div[^>]*id="[^"]*banner[^"]*"[^>]*>.*?</div>',
        r'<div[^>]*id="[^"]*advert[^"]*"[^>]*>.*?</div>',
        r'<section[^>]*class="[^"]*banner[^"]*"[^>]*>.*?</section>',
        r'<aside[^>]*class="[^"]*advert[^"]*"[^>]*>.*?</aside>'
    ]
    
    @classmethod
    def clean_html(cls, html):
        """تنظيف HTML من الإعلانات"""
        if not html:
            return html
        for pattern in cls.AD_PATTERNS:
            html = re.sub(pattern, '', html, flags=re.DOTALL | re.IGNORECASE)
        return html
    
    @classmethod
    def is_ad_url(cls, url):
        """التحقق مما إذا كان الرابط إعلاناً"""
        if not url:
            return False
        url_lower = url.lower()
        for domain in cls.AD_DOMAINS:
            if domain in url_lower:
                return True
        return False
    
    @classmethod
    def get_clean_response(cls, url, timeout=10):
        """الحصول على استجابة نظيفة من موقع"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'ar,en-US;q=0.7,en;q=0.3',
                'DNT': '1',
                'Connection': 'keep-alive'
            }
            response = requests.get(url, headers=headers, timeout=timeout)
            if response.status_code == 200:
                response._content = cls.clean_html(response.text).encode('utf-8')
            return response
        except:
            return None