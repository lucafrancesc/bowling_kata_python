class Bowling:
    def __init__(self):
        self._frames = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: [], 12: []}
        self._current_roll = 1
        self._points = 0

    # def _populate_frames(self):
    #     for frame in range(1, 13):
    #         self._frames[frame] = []

    def roll(self, pins):
        if len(self._frames[self._current_roll]) == 0:
            if pins == 10:
                self._next_frame(pins)
            else:
                self._frames[self._current_roll].append(pins)
        else:
            self._next_frame(pins)

    def score(self):
        for i in range(1, 11):
            if sum(self._frames[i]) < 10:
                self._points += sum(self._frames[i])
            elif sum(self._frames[i]) == 10 and len(self._frames[i]) == 2:
                self._points += (sum(self._frames[i]) + self._frames[i+1][0])
            else:
                if len(self._frames[i+1]) > 1:
                    self._points += (sum(self._frames[i]) + sum(self._frames[i+1]))
                else:
                    if len(self._frames[i+2]) > 1:
                        self._points += (sum(self._frames[i]) + sum(self._frames[i+1]) + self._frames[i+2][0])
                    else:
                        self._points += (sum(self._frames[i]) + sum(self._frames[i+1]) + sum(self._frames[i+2]))

        return(self._points)


    def _next_frame(self, pins):
        self._frames[self._current_roll].append(pins)
        self._current_roll += 1
