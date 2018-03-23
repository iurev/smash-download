from main import *

def test_get_month_page_url():
    assert get_month_page_url(2000, 6) == 'https://www.smashingmagazine.com/2000/05/desktop-wallpaper-calendars-june-2000'
    assert get_month_page_url(2000, 12) == 'https://www.smashingmagazine.com/2000/11/desktop-wallpaper-calendars-december-2000'
    assert get_month_page_url(2000, 1) == 'https://www.smashingmagazine.com/1999/12/desktop-wallpaper-calendars-january-2000'

def test_get_year():
    assert get_year([]) == now.year
    assert get_year(['20']) == now.year
    assert get_year(['2000']) == 2000

def test_get_month():
    assert get_month([]) == now.month
    assert get_month(['1']) == 1
    assert get_month(['12']) == 12
    assert get_month(['2000', '6']) == 6

def test_get_size():
    assert get_size([]) == '2560x1440'
    assert get_size(['320x480']) == '320x480'

def test_get_calendar():
    assert get_calendar([]) == True
    assert get_calendar(['no-calendar']) == False

def test_get_settings():
    s = {
        'year': 2000,
        'month': 12,
        'size': '1000x1000',
        'calendar': False
    }
    assert get_settings(['2000', '12', '1000x1000', 'no-calendar']) == s
    assert get_settings([]) == default_settings
