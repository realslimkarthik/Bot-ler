import telepot
from telepot.delegate import per_from_id, create_open
from credentials import get_telegram_bot_api_key


class UserTracker(telepot.helper.UserHandler):
    def __init__(self, seed_tuple, timeout):
        super(UserTracker, self).__init__(seed_tuple, timeout)

        # keep track of how many messages of each flavor
        self._counts = {'chat': 0,
                        'inline_query': 0,
                        'chosen_inline_result': 0}

        self._answerer = telepot.helper.Answerer(self.bot)

    def on_message(self, msg_packet):
        flavor = telepot.flavor(msg_packet)
        self._counts[flavor] += 1

        if flavor == 'chat':
            print(msg_packet)
            # command = msg_packet['text'].strip()



def set_home(msg_packet):
    
    pass


def set_work(msg_packet):
    pass


def set_dest(msg_packet):
    pass


command_mapper = {
    '/home': set_home,
    '/work': set_work,
    '/new_dest': set_dest
}



telegram_bot_api_key = get_telegram_bot_api_key()

bot = telepot.DelegatorBot(telegram_bot_api_key, [
    (per_from_id(), create_open(UserTracker, timeout=20)),
])
bot.message_loop(run_forever=True)