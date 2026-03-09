# -*- coding: utf-8 -*-

class MovieFilters:
    """فلاتر متقدمة للأفلام والمسلسلات"""
    
    MOVIE_GENRES = {
        'اكشن': 'action', 'دراما': 'drama', 'كوميديا': 'comedy',
        'رعب': 'horror', 'خيال علمي': 'sci-fi', 'اثارة': 'thriller',
        'جريمة': 'crime', 'غموض': 'mystery', 'رومانسي': 'romance',
        'مغامرة': 'adventure', 'حرب': 'war', 'تاريخي': 'history',
        'سيرة ذاتية': 'biography', 'رياضة': 'sport', 'موسيقى': 'music',
        'عائلي': 'family', 'انمي': 'anime', 'كارتون': 'cartoon',
        'وثائقي': 'documentary', 'غرب امريكي': 'western', 'فانتازيا': 'fantasy'
    }
    
    SERIES_GENRES = {
        'دراما': 'drama', 'اكشن': 'action', 'كوميديا': 'comedy',
        'جريمة': 'crime', 'رعب': 'horror', 'خيال علمي': 'sci-fi',
        'اثارة': 'thriller', 'رومانسي': 'romance', 'غموض': 'mystery',
        'تاريخي': 'history', 'حربي': 'war', 'طبي': 'medical',
        'قانوني': 'legal', 'بوليسي': 'police', 'انمي': 'anime',
        'كارتون': 'cartoon', 'وثائقي': 'documentary'
    }
    
    COUNTRIES = {
        '🇪🇬 مصرية': 'egypt', '🇸🇦 سعودية': 'ksa', '🇰🇼 كويتية': 'kuwait',
        '🇦🇪 إماراتية': 'uae', '🇶🇦 قطرية': 'qatar', '🇧🇭 بحرينية': 'bahrain',
        '🇴🇲 عمانية': 'oman', '🇯🇴 أردنية': 'jordan', '🇱🇧 لبنانية': 'lebanon',
        '🇸🇾 سورية': 'syria', '🇮🇶 عراقية': 'iraq', '🇵🇸 فلسطينية': 'palestine',
        '🇱🇾 ليبية': 'libya', '🇹🇳 تونسية': 'tunisia', '🇩🇿 جزائرية': 'algeria',
        '🇲🇦 مغربية': 'morocco', '🇸🇩 سودانية': 'sudan', '🇾🇪 يمنية': 'yemen',
        '🇹🇷 تركية': 'turkish', '🇰🇷 كورية': 'korean', '🇯🇵 يابانية': 'japanese',
        '🇨🇳 صينية': 'chinese', '🇮🇳 هندية': 'indian', '🇺🇸 امريكية': 'american',
        '🇬🇧 بريطانية': 'british', '🇫🇷 فرنسية': 'french', '🇩🇪 المانية': 'german'
    }
    
    @classmethod
    def show_movie_genres(cls, add_func):
        for ar_name, en_name in cls.MOVIE_GENRES.items():
            add_func(f'🎬 {ar_name}', f'genre_{en_name}', 'genre_list', '')
    
    @classmethod
    def show_series_genres(cls, add_func):
        for ar_name, en_name in cls.SERIES_GENRES.items():
            add_func(f'📺 {ar_name}', f'series_genre_{en_name}', 'genre_list', '')
    
    @classmethod
    def show_countries(cls, add_func):
        for ar_name, en_name in cls.COUNTRIES.items():
            add_func(f'{ar_name}', f'country_{en_name}', 'country_list', '')
    
    @classmethod
    def show_gulf_series(cls, add_func):
        gulf = ['🇸🇦 سعودية', '🇰🇼 كويتية', '🇦🇪 إماراتية', '🇶🇦 قطرية', '🇧🇭 بحرينية', '🇴🇲 عمانية']
        for country in gulf:
            add_func(country, f'gulf_{cls.COUNTRIES[country]}', 'country_list', '')
    
    @classmethod
    def show_arab_series(cls, add_func):
        arab = ['🇪🇬 مصرية', '🇸🇾 سورية', '🇱🇧 لبنانية', '🇯🇴 أردنية', '🇮🇶 عراقية', '🇵🇸 فلسطينية']
        for country in arab:
            add_func(country, f'arab_{cls.COUNTRIES[country]}', 'country_list', '')

class YearFilters:
    YEARS = ['2025', '2024', '2023', '2022', '2021', '2020']
    DECADES = {'2020': 'عشرينات 2020', '2010': 'عقد 2010', '2000': 'عقد 2000'}
    
    @classmethod
    def show_years(cls, add_func):
        for year in cls.YEARS:
            add_func(f'📅 أفلام {year}', f'year_{year}', 'year_list', '')
    
    @classmethod
    def show_decades(cls, add_func):
        for decade, name in cls.DECADES.items():
            add_func(f'📅 {name}', f'decade_{decade}', 'year_list', '')