import json

from scripts.pull_crypto import *


dict_obj = [('quote_USD_price', 7256.50763292), ('quote_USD_volume_24h', 18093249851.4391), ('quote_USD_percent_change_1h', 0.160725), ('quote_USD_percent_change_24h', 0.752455), ('quote_USD_percent_change_7d', -2.41726), ('quote_USD_market_cap', 131329632107.51352), ('quote_USD_last_updated', '2019-12-13T00:44:32.000Z')]

json_obj = json.loads(dict_obj)

print(dict_obj)