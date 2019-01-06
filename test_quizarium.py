import unittest
from quizarium import *


class TestGetQuestion(unittest.TestCase):
    def test_when_question_first_appears(self):
        message = '''Round 7/10
▶️ QUESTION  [Music Bands]
Name the 60s band from Manchester who had a hit with a song called "Jennifer Eccles"?
[   ○   ○       ○        ]'''
        expected = 'Name the 60s band from Manchester who had a hit with a song called "Jennifer Eccles"?'
        actual = get_question(message)
        self.assertEqual(expected, actual)


class TestGetHint(unittest.TestCase):
    def test_when_hint_not_given_yet(self):
        message = '''Round 7/10
▶️ QUESTION  [Music Bands]
Name the 60s band from Manchester who had a hit with a song called "Jennifer Eccles"?
[   ○   ○       ○        ]'''
        expected = None
        actual = get_hint(message)
        self.assertEqual(expected, actual)

    def test_when_hint_given1(self):
        message = '''Name the 60s band from Manchester who had a hit with a song called "Jennifer Eccles"?
Hint:  _ _ _ _ _ _ _
[••••   ○       ○        ]'''
        expected = '_ _ _ _ _ _ _'
        actual = get_hint(message)
        self.assertEqual(expected, actual)

    def test_when_hint_given2(self):
        message = '''Name the 60s band from Manchester who had a hit with a song called "Jennifer Eccles"?
Hint:  H _ _ l _ _ _
[••••••••       ○        ]'''
        expected = 'H _ _ l _ _ _'
        actual = get_hint(message)
        self.assertEqual(expected, actual)

    def test_when_no_hint(self):
        message = '''🐱🚀🌕 We (Quizarium devs) released a new iOS and Android puzzle game Catomic where cats go to space and colonize Mars. Check it out!
 🍏 App Store | 🤖 Google Play | 📲 catomic.on-5.com'''
        expected = None
        actual = get_hint(message)
        self.assertEqual(expected, actual)


class TestGetAnswer(unittest.TestCase):
    def test_when_guessed_correctly(self):
        message = '''✅ Yes, Hollies!

🏅 Hui Wen Wong +1

📢 Share the wisdom:  FB | TW
⚖ Rate this question:   👍 /good  or   👎 /bad ?'''
        expected = 'Hollies'
        actual = get_answer(message)
        self.assertEqual(expected, actual)

    def test_when_nobody_guessed(self):
        message = '''⛔️ Nobody guessed. The correct answer was Vietnam

📢 Share the wisdom:  FB (https://www.facebook.com/dialog/feed?app_id=444837735034&display=popup&link=https%3A%2F%2Ftelegram.me%2FQuizariumBot&name=%40QuizariumBot%20on%20Telegram&description=Coq%20Bang%20can%20be%20found%20in%20which%20country%20%E2%80%94%20Vietnam.%20Learn%20this%20and%20more%20with%20Telegram%20QuizariumBot!&picture=https%3A%2F%2Fs3.amazonaws.com%2Fon5%2Fqz%2FQ_avatar__.png) | TW (http://twitter.com/share?text=Coq%20Bang%20can%20be%20found%20in%20which%20country%20%E2%80%94%20Vietnam&url=https%3A%2F%2Ftelegram.me%2FQuizariumBot)
⚖️ Rate this question:   👍 /good  or   👎 /bad ?'''
        expected = 'Vietnam'
        actual = get_answer(message)
        self.assertEqual(expected, actual)

    def test_not_an_answer(self):
        message = '''Round 9/10
▶️ QUESTION  [myth]
Agrippa poisoned her husband/uncle who was he
[   ○   ○       ○        ]'''
        expected = None
        actual = get_answer(message)
        self.assertEqual(expected, actual)
