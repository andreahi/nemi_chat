from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Any, List, Text

from rasa_nlu.components import Component
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.tokenizers import Tokenizer, Token
from rasa_nlu.training_data import Message
from rasa_nlu.training_data import TrainingData


class WhitespaceTokenizer(Tokenizer, Component):
    name = "" \
           ""
    numbermap = {
                 '0': 'null',
                 '1': 'en',
                 '2': 'to',
                 '3': 'tre',
                 '4': 'fire',
                 '5': 'fem',
                 '6': 'seks',
                 '7': 'sju',
                 '8': 'åtte',
                 '9': 'ni',
                '10': 'ti'
                 }
    provides = ["tokens"]

    def train(self, training_data, config, **kwargs):
        # type: (TrainingData, RasaNLUModelConfig, **Any) -> None

        for example in training_data.training_examples:
            example.set("tokens", self.tokenize(example.text))

    def process(self, message, **kwargs):
        # type: (Message, **Any) -> None

        message.set("tokens", self.tokenize(message.text))

    def tokenize(self, text):
        # type: (Text) -> List[Token]

        words = text.split()
        running_offset = 0
        tokens = []
        print(words)
        for word in words:
            word_offset = text.index(word, running_offset)
            word_len = len(word)
            running_offset = word_offset + word_len
            if word in self.numbermap:
                word = self.numbermap[word]
                print("ny word ", word)

            print("ny word ", word)
            tokens.append(Token(word, word_offset))
        print("tokens ", tokens)
        return tokens

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False