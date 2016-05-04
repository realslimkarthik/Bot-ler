
citymapper_api_keys = ['']
telegram_bot_key = ''


def get_citymapper_api_key(seed):
    index = seed % len(api_keys)
    return api_keys[index]


def get_telegram_bot_api_key():
    return telegram_bot_key