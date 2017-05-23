from skyscanner.skyscanner import FlightsCache
import pandas as pd
import collections

flights_cache_service = FlightsCache('on537611765613459512552361233511')
result = flights_cache_service.get_cheapest_quotes(
    market='UK',
    currency='EUR',
    locale='en-GB',
    originplace='AMS',
    destinationplace='BCN',
    outbounddate='2017-06',
    inbounddate='2017-07').parsed

def flatten(d, parent_key='', sep='_'):
    # http://stackoverflow.com/questions/6027558/flatten-nested-python-dictionaries-compressing-keys
    items = []
    for k, v in d.items():
        new_key = parent_key + sep + k if parent_key else k
        if isinstance(v, collections.MutableMapping):
            items.extend(flatten(v, new_key, sep=sep).items())
        else:
            items.append((new_key, v))
    return dict(items)

dct = result['Quotes']
df = pd.DataFrame([flatten(x) for x in dct])

print(df)