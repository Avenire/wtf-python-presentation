class __FeedableDoge:
    def feed(self, eatable):
        self._food.append(eatable)


class BadDoge(__FeedableDoge):
    def __init__(self, food=[]):
        self._food = food


class GoodDoge(__FeedableDoge):
    def __init__(self, food=[]):
        self._food = list(food)

