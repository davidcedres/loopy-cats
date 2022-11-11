import random


class OpenLoopController:
    def __init__(self):
        self.state = '1'
        self.transition_matrix = {
            '0': {
                '1': [
                    ['TIME', '1']
                ],
            },
            '1': {
                '1': [
                    ['FEED', '0'],
                ],
            },
        }

    def input(self, signal):
        possible_actions = self.transition_matrix[self.state][signal]
        output, state = possible_actions[0]
        self.state = state
        return output


class ClosedLoopController:
    def __init__(self):
        self.state = '0'
        self.transition_matrix = {
            '0': {
                'BEGS': [
                    ['FEED', '0']
                ],
                'PURRS': [
                    ['TIME', '0']
                ],
            },
        }

    def input(self, signal):
        possible_actions = self.transition_matrix[self.state][signal]
        output, state = possible_actions[0]
        self.state = state
        return output


class Cat:
    def __init__(self, type):
        self.state = 'HAPPY'

        self.transition_matrix = {
            'HAPPY': {
                'FEED': [
                    ['PUKES', 'HAPPY']
                ],
                'PET': [
                    ['PURRS', 'HAPPY']
                ],
                'TIME': [
                    ['BEGS', 'HUNGRY']
                ]
            },
            'HUNGRY': {
                'FEED': [
                    ['PURRS', 'HAPPY'],
                ] if type == 'Normal' else [
                    ['PURRS', 'HAPPY'],
                    ['BEGS', 'HUNGRY']
                ],
                'PET': [
                    ['BITES', 'HUNGRY']
                ],
                'TIME': [
                    [None, 'DEAD']
                ]
            },
            'DEAD': {}
        }

    def sprite(self):
        return self.state.lower()

    def input(self, signal):
        possible_actions = self.transition_matrix[self.state][signal]
        output, state = random.choice(possible_actions)
        self.state = state
        return output
