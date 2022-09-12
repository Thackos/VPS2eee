import time

from Functions import envoie_discord

DELAI = 2.75
NB_ARTICLES = 1
URL_FREE_BOT = "https://www.vinted.fr/vetements?brand_id[]=53&brand_id[]=12&brand_id[]=7&brand_id[]=15&brand_id[]=197478&brand_id[]=6005&brand_id[]=20&brand_id[]=255&brand_id[]=11493&brand_id[]=161&catalog[]=2050&price_from=1&currency=EUR&price_to=50&order=newest_first "
URL_TSHIRT_NIKE = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&brand_id[]=53&price_from=1&currency=EUR&price_to=10&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first"
URL_TSHIRT_LACOSTE = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=304&brand_id[]=677891&brand_id[]=268734&price_to=15"
URL_TSHIRT_RALPH = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=15&brand_id[]=88&brand_id[]=4273"
URL_TSHIRT_TNF = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=10&brand_id[]=2319"
URL_TSHIRT_TOMMY = "https://www.vinted.fr/vetements?size_id[]=208&size_id[]=209&size_id[]=207&catalog[]=76&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=10&brand_id[]=94&brand_id[]=352755"
URL_SWEAT_NIKE = "https://www.vinted.fr/vetements?brand_id[]=53&size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&price_from=1&currency=EUR&price_to=20&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first"
URL_SWEAT_LACOSTE = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=79&brand_id[]=304&brand_id[]=677891&brand_id[]=268734&price_from=1&currency=EUR&price_to=25&status[]=3&status[]=2&status[]=6&status[]=1&order=newest_first"
URL_SWEAT_RALPH = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&catalog[]=1812&price_from=1&currency=EUR&price_to=25.00&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=88&brand_id[]=4273"
URL_SWEAT_TNF = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&catalog[]=1812&price_from=1&currency=EUR&price_to=20.00&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=2319"
URL_SWEAT_TOMMY = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1811&catalog[]=267&catalog[]=1813&catalog[]=1814&catalog[]=1815&catalog[]=1825&catalog[]=1812&price_from=1&currency=EUR&price_to=20.00&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=94&brand_id[]=352755"
URL_SWEAT_NIKE_TECH = "https://www.vinted.fr/vetements?size_id[]=207&size_id[]=208&size_id[]=209&catalog[]=1812&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&brand_id[]=53&price_to=30"

URL_JEANS_CARHARTT = "https://www.vinted.fr/vetements?brand_id[]=362&catalog[]=257&price_from=1&currency=EUR&price_to=25&status[]=6&status[]=1&status[]=2&status[]=3&order=newest_first"
URL_VESTES_TNF = "https://www.vinted.fr/vetements?price_from=1&currency=EUR&status[]=6&status[]=1&status[]=2&status[]=3&order=newest_first&brand_id[]=2319&price_to=90&catalog[]=2051"
URL_BONNET_LACOSTE = "https://www.vinted.fr/vetements?brand_id[]=304&search_text=bonnets&search_id=6409038568&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=15"
URL_BONNET_RALPH = "https://www.vinted.fr/vetements?brand_id[]=88&brand_id[]=4273&search_id=6409038568&price_from=1&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_to=15&catalog[]=287"
URL_AF1 = "https://www.vinted.fr/vetements?search_id=6409172428&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&catalog[]=1242&price_from=1&search_text=air%20force%201&price_to=50"
URL_AJ1 = "https://www.vinted.fr/vetements?search_id=6409081644&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&price_from=1&search_text=Jordan%201&catalog[]=1242&price_to=100"
URL_AJ4 = "https://www.vinted.fr/vetements?search_id=6409092911&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&search_text=Jordan%204&catalog[]=1242&price_from=1&price_to=200"
URL_DUNK_LOW = "https://www.vinted.fr/vetements?search_id=6409177174&currency=EUR&status[]=3&status[]=2&status[]=1&status[]=6&order=newest_first&catalog[]=1242&price_from=1&search_text=dunk%20low&price_to=80"

WEBHOOK_URL_FREE_BOT = "https://discord.com/api/webhooks/1018306492945932358/fwE3Tl7Pi4JRRZggbZZmLWCE_2GmfEk8ydMAsiOn-VI56aIty5o6t4dYb9atyENxspwa"
WEBHOOK_URL_TSHIRT_NIKE = "https://discord.com/api/webhooks/1018270137813573673/hhJ3hyeB1rgSiDttwCc5JJfuA_kjhWq78rvn82gop3vNcjqDWogrDXViccUwCjpTBFc6"
WEBHOOK_URL_TSHIRT_LACOSTE = "https://discord.com/api/webhooks/1018270289538326558/9P02JKVuot6mJfQazwreqEyJGmx08bM-MQabQaS6sjaTIW-v2je95I-wAfbxShigfcPW "
WEBHOOK_URL_TSHIRT_RALPH = "https://discord.com/api/webhooks/1018270428239765635/oy-c4axgeQ4WsPmIH0lTI82uD_VTdXpo5U0m3Abiyz_kmkq3vto27WSqNWcoiUiza_e9 "
WEBHOOK_URL_TSHIRT_TNF = "https://discord.com/api/webhooks/1018297089274417263/m8kEN7TkYyNDYuwnwo547qtHgCRUT8xVlzUfok-fmR16ApqoDiZoF8z3pPrk9R_oM5UQ"
WEBHOOK_URL_TSHIRT_TOMMY = "https://discord.com/api/webhooks/1018297308204498994/rb5IT80uPy0QkeFnSUzXzmSQ8gLGG5LRVgJtrOI7LhViQfX3PYzxySfHjTIT43dEpBSt "
WEBHOOK_URL_SWEAT_NIKE = "https://discord.com/api/webhooks/1018191923258867762/_MOMwTTDfIp7W8HXa41nTB30Qju31Fgs5DKnG4PNNa7Z9-f9LA05gLvUlJb02Jn6I9y7 "
WEBHOOK_URL_SWEAT_LACOSTE = "https://discord.com/api/webhooks/1018192348154433617/eMvu99lOH0PIG-n6tHNuN-h_rJ0eCuBYSxPf6PlLjy4lmKIbZHGb4YwGbl0pHO6xj02i "
WEBHOOK_URL_SWEAT_RALPH = "https://discord.com/api/webhooks/1017532663231430727/2ZwyDA3C0nWmZ82J0UxvMHYPI37DzoFlAc5OMjWNmZTz8rU4kE-F8JFsZLSe5SSCUET0 "
WEBHOOK_URL_SWEAT_TNF = "https://discord.com/api/webhooks/1018297759352238141/O9gA4x2el3pY5kKkJxtMo_CA_UieuMJzfMYDzVK0sLtIeL_nZzSLhMc9G1W0TM0VMtp- "
WEBHOOK_URL_SWEAT_TOMMY = "https://discord.com/api/webhooks/1018297971223306321/x3CAb-qLS6dKZbwx27fhfSGkdvvHTmvlHykUaieAsyyrGDtTpMrXVZyZE0qDovxdwGah "
WEBHOOK_URL_SWEAT_NIKE_TECH = "https://discord.com/api/webhooks/1018597731977154630/B2qQgRTkkJztB8tJ0HJUDv8CBEe_JLjD8R_BetV59GADTqShFNrvgHxCYLVFAlGJBB52"

WEBHOOK_URL_JEAN_CARHARTT = "https://discord.com/api/webhooks/1018916033286897866/irp7nj4e05LTqSPBuGSceYqsMJJhsjoFuVL8-mGEtdlsI-DxoNo9NRS1F4-OFxWP1XTv"
WEBHOOK_URL_VESTE_TNF = "https://discord.com/api/webhooks/1018916290586484876/KoW5bIw1b4ltePQYFbHusuZML9syBG9zoCk-GTjQqgnw2v_A1olZSvS6SPLYYetdNZGA"
WEBHOOK_URL_BONNET_LACOSTE = "https://discord.com/api/webhooks/1018916883698831455/uYG107MCktN4UY8VHFMiiF-hYfzsuTb6U6Y94kuyB0GuSgn754T6JNxjoY4sx9livAzS"
WEBHOOK_URL_BONNET_RALPH = "https://discord.com/api/webhooks/1018917035679416360/xNM0i48zm7VoUvT0grgqoKfUJ06T1aG0LzdisTLS5XsBh1KDefqqzHACsQqlCKxOGFdx"
WEBHOOK_URL_AF1 = "https://discord.com/api/webhooks/1018916523940778024/tQWqlZdHj38axaqFtKpvQGzxqD6JLvHymevI6lTBYA8uWxIxoGhJaxK38zEaRJiX08Fz"
WEBHOOK_URL_AJ1 = "https://discord.com/api/webhooks/1018916645177147402/qM-YM4WuHT0S5OvX_RzkDKfrpnn5aEI_9QaRR7Ayj6XHkg0BRwpPFfwvA0zKErdiAqVc"
WEBHOOK_URL_AJ4 = "https://discord.com/api/webhooks/1018916748357029951/DtT4FxuMHY7QjYhWM14la5pZmwBPofyi2DruNR6bHPpHQ9AAW_EZBh2dztyxolEu21gv"
WEBHOOK_URL_DUNK_LOW = "https://discord.com/api/webhooks/1018916813637161000/CChuqQ01PQ4nzMj53kA4tnypscb25-6vB9_QZxZCbjWFenIALla1lML0Aki00ib_SUQ6"

while True:
    try:
        print("JEAN CARHARTT dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_JEANS_CARHARTT, WEBHOOK_URL_JEAN_CARHARTT)
        print("VESTE TNF dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_VESTES_TNF, WEBHOOK_URL_VESTE_TNF)
        print("BONNET LACOSTE dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_BONNET_LACOSTE, WEBHOOK_URL_BONNET_LACOSTE)
        print("BONNET RALPH dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_BONNET_RALPH, WEBHOOK_URL_BONNET_RALPH)
        print("AF1 dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_AF1, WEBHOOK_URL_AF1)
        print("AJ1 dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_AJ1, WEBHOOK_URL_AJ1)
        print("AJ4 dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_AJ4, WEBHOOK_URL_AJ4)
        print("DUNK LOW dans " + str(DELAI) + " secondes...")
        time.sleep(DELAI)
        envoie_discord(URL_DUNK_LOW, WEBHOOK_URL_DUNK_LOW)
    except Exception:
        pass