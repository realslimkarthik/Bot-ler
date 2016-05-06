import unittest
from textwrap import dedent
import muthu_tasks


class MuthuTasksTest(unittest.TestCase):

    def test_parse_message_packet(self):
        regular_text_packet = {'date': 1462411171, 'text': '/help', 'from': {'id': 52355227, 'last_name': 'Hariharan', \
            'first_name': 'Karthik'}, 'chat': {'id': 52355227, 'last_name': 'Hariharan', 'first_name': 'Karthik', \
            'type': 'private'}, 'entities': [{'length': 5, 'offset': 0, 'type': 'bot_command'}], 'message_id': 10}
        tc_1_res = muthu_tasks.parse_message_packet(regular_text_packet)
        self.assertIsInstance(tc_1_res, dict)
        self.assertIsNotNone(tc_1_res.get('commands'))
        self.assertIsNotNone(tc_1_res.get('text'))
        self.assertIsNone(tc_1_res.get('arguments'))

        random_text_packet =  {'a': 'hello', 'b': 33, 46: 'forty six', 'arr': [{'r': 'new key'}]}
        tc_2_res = muthu_tasks.parse_message_packet(random_text_packet)
        self.assertIsInstance(tc_2_res, dict)
        self.assertIsNone(tc_2_res.get('commands'))
        self.assertIsNone(tc_2_res.get('text'))
        self.assertIsNone(tc_2_res.get('arguments'))



    def test_generate_help_msg(self):
        help_msg = dedent('''\
            Vanakam. My name is Muthu. I am inspired by the character who has my same name in the 1995 hit Tamil film Muthu \
            https://en.wikipedia.org/wiki/Muthu_(1995_film)
            I can help you with a lot of things. I've described them all below
        '''.strip())
        help_msg = dedent(help_msg.strip())
        tc_1_res = muthu_tasks.generate_help_msg()
        self.assertIsInstance(tc_1_res, str)
        self.assertTrue(tc_1_res.startswith(help_msg))



def main():
    unittest.main()


if __name__ == '__main__':
    main()