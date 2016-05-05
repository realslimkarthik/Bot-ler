from textwrap import dedent
import telepot


def execute_task(msg_packet):
    content_type, chat_type, chat_id = telepot.glance(msg_packet)
    flavor = telepot.flavor(msg_packet)
    response_text = 'hello'

    if content_type == 'text':
        message_packet_fragments = parse_message_packet(msg_packet)
        chat_id = message_packet_fragments['chat_id']
        cmd_args = message_packet_fragments['arguments']
        text = message_packet_fragments['text']
        commands = message_packet_fragments['commands']
        command = commands[0]
        command_callback = command_mapper.get(command)
        if command_callback is not None:
            response_text = command_callback(cmd_args, chat_id)

    return chat_id, response_text


def send_help_msg(command_arguments, chat_id):
    help_msg = ''
    if command_arguments is None:
        help_msg = '''
            Hello
            My name is Muthu. I am inspired by the character who has my same name in the 1995 hit Tamil film Muthu \
            https://en.wikipedia.org/wiki/Muthu_(1995_film)
            I can help you with a lot of things. I've described them all below

        '''
        for command, command_text in help_msgs.items():
            help_msg += command + command_text + '\n'
    elif command_arguments:
        for command_argument in command_arguments:
            command_argument_text = help_msgs.get(command_argument)
            help_msg += command_argument_text
    help_msg = dedent(help_msg)
    return help_msg


def set_home(msg_packet):
    
    pass


def set_work(command_arguments, chat_id):
    return 'hello'


def create_new_trip(msg_packet):
    pass


def parse_message_packet(message_packet):
    msg_text = message_packet['text']
    commands_positions = [{'offset': entity['offset'], 'length':entity['length']} for entity in message_packet['entities'] \
                if entity['type'] == 'bot_command']
    commands = [msg_text[cmd_pos['offset']:cmd_pos['offset'] + cmd_pos['length']] for cmd_pos in commands_positions]
    arguments = ' '.join(msg_text.split()[1:])
    if message_packet.get('from'):
        chat_id = message_packet['from'].get('chat_id')
    
    return {'text': msg_text, 'chat_id': chat_id, 'arguments': arguments, 'commands':commands}


command_mapper = {
    '/start': send_help_msg ,
    '/help': send_help_msg,
    '/home': set_home,
    '/work': set_work,
    '/new_trip': create_new_trip
}

help_msgs = {
    '/home': ' - Set your home address for transit based tasks',
    '/work': '- Set your work address for transit based tasks',
    '/new_trip': '- Create a new trip to be prompted on when to leave and to try to get the best form of public transport',
    '/help_with_cmd': '- Repeat this message. You can also Type /help_with_cmd /<command> to get details about a specific command'
}
