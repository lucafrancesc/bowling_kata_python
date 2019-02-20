class Bowling:
    def __init__(self):
        self._points = 0

    def score(self):
        return self._points

    def roll(self, pins):
        self._points += pins
