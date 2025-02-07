import json
import models as m
import exceptions as e


class DB:
    cards = []
    sessions = []

    def __init__(self):
        print(' * Initializing Database...')
        self.load_test_data()

    def post_card(self, _card: m.Card):
        self.cards.append(_card)

    def get_card(self, PAN: str):
        for card in self.cards:
            if card.PAN == PAN:
                return card
        else:
            return None

    def post_session(self, _session: m.Session):
        self.sessions.append(_session)

    def get_session(self, terminal_id: str):
        for session in self.sessions:
            if session.get_terminal_id() == terminal_id:
                return session
        else:
            return None

    def is_session_active(self, terminal_id):
        return terminal_id in [session.get_terminal_id() for session in self.sessions]

    def load_test_data(self):
        with open('test_data.json', 'r') as fout:
            data = json.load(fout)

            for card_json_key in data['cards']:
                card_json = data['cards'][card_json_key]
                self.post_card(m.Card(
                    card_json['PAN'],
                    card_json['exp_date'],
                    card_json['PIN'],
                    card_json['cardholder_name'],
                    card_json['balance'],
                ))

    def save_state(self):
        with open('test_data.json', 'w') as fin:
            obj = {"cards": {}}
            for i, card in enumerate(self.cards):
                obj['cards'].update({i: card.to_dict()})

            json.dump(obj, fin, ensure_ascii=False, indent=2, sort_keys=True)
