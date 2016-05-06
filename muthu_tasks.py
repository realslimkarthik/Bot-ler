from textwrap import dedent
import telepot


def execute_task(msg_packet):
    response_text = ''
    content_type, chat_type, chat_id = telepot.glance(msg_packet)
    flavor = telepot.flavor(msg_packet)
    if content_type == 'text':
        message_packet_fragments = parse_message_packet(msg_packet)
        cmd_args = message_packet_fragments.get('arguments')
        text = message_packet_fragments.get('text')
        commands = message_packet_fragments.get('commands')
        command = commands[0]
        command_callback = command_mapper.get(command)
        if command_callback is not None:
            response_text = command_callback(command_arguments=cmd_args, chat_id=chat_id)

    return chat_id, response_text


def generate_help_msg(**kwargs):
    help_msg = dedent('''\
            Vanakam. My name is Muthu. I am inspired by the character who has my same name in the 1995 hit Tamil film Muthu \
            https://en.wikipedia.org/wiki/Muthu_(1995_film)
            I can help you with a lot of things. I've described them all below
        '''.strip())
    for command_desc_text in help_msgs:
        help_msg += '\n' + command_desc_text
    return help_msg


def set_home(**kwargs):
    
    pass


def set_work(**kwargs):
    return 'hello'


def create_new_trip(**kwargs):
    pass


def parse_message_packet(message_packet):
    parsed_msg = {}
    msg_text = message_packet.get('text')
    commands = None

    if message_packet.get('entities') and msg_text is not None:
        parsed_msg['text'] = msg_text
        commands_positions = [{'offset': entity['offset'], 'length':entity['length']} for entity in message_packet['entities'] \
                    if entity['type'] == 'bot_command']
        commands = [msg_text[cmd_pos['offset']:cmd_pos['offset'] + cmd_pos['length']] for cmd_pos in commands_positions]
    
    if commands is not None:
        parsed_msg['commands'] = commands
        arguments = ' '.join(msg_text.split()[1:])
        if arguments == '':
            arguments = None
        else:
            parsed_msg['arguments'] = arguments

    return parsed_msg


command_mapper = {
    '/start': generate_help_msg ,
    '/help': generate_help_msg,
    '/home': set_home,
    '/work': set_work,
    '/new_trip': create_new_trip
}

help_msgs = [
    '/home - set your home address',
    '/new_trip - create a new trip to be prompted on when to leave',
    '/work - set your work address'
]
