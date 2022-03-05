from random import shuffle

"""Q 8, 9"""


class DeckOfCards:
    suit = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self):
        self.deal = {}
        self.__all_cards = []

    def _shuffle_cards(self):
        cards = []
        for j in range(9):
            while True:
                shuffle(self.suit)
                shuffle(self.rank)
                new_card = f"{self.suit[0]}-{self.rank[0]}"
                if new_card not in self.__all_cards:
                    self.__all_cards.append(new_card)  # unique card container
                    cards.append(new_card)  # unique card insertion
                    break
        return cards

    def _show_deals(self):
        for k, v in self.deal.items():
            print(f">>{k}: {', '.join(v)} ")

    def solution(self):
        for i in range(1, len(self.suit)+1):
            cards = self._shuffle_cards()
            self.deal.update({f"user {i}": cards})
        self._show_deals()


if __name__ == '__main__':
    d = DeckOfCards()
    d.solution()
