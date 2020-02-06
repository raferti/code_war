"""

= EN =
A famous casino is suddenly faced with a sharp decline of their revenues.
They decide to offer Texas hold'em also online. Can you help them by writing
an algorithm that can rank poker hands?
Task

Create a poker hand that has a method to compare itself to another poker hand:
compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:
PokerHand("KS 2H 5C JD TD")

The characteristics of the string of cards are:
    Each card consists of two characters, where
        The first character is the value of the card:
            2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
        The second character represents the suit:
            S(pades), H(earts), D(iamonds), C(lubs)
    A space is used as card separator between cards
The result of your poker hand compare can be one of these 3 options:
[ "Win", "Tie", "Loss" ]

Notes
    - Apply the Texas Hold'em rules for ranking the cards.
    - Low aces are NOT valid in this kata.
    - There is no ranking for the suits.

= RU =

Известное казино неожиданно столкнулось с резким падением их доходов.
Они решают предложить Техасский Холдем также онлайн. Можете ли вы помочь им,
написав алгоритм, который может ранжировать покерные руки ?
задача

Создайте покерную комбинацию, в которой есть метод для сравнения себя с
другой покерной комбинацией:
сравнить_с собой (сам, другой_ручный)
В покерной руке есть конструктор, который принимает строку из 5 карт:
PokerHand ("KS 2H 5C JD TD")

Характеристики последовательности карт:
    Каждая карта состоит из двух символов, где
        Первый символ - это значение карты:
            2, 3, 4, 5, 6, 7, 8, 9, T (en), J (ack), Q (ueen), K (ing), A (ce)
        Второй символ представляет костюм:
            S (pades), H (earts), D (iamonds), C (lubs)
    Пробел используется как разделитель карт между картами

Результат вашей покерной руки может быть одним из следующих 3 вариантов:
["Win", "Tie", "Loss"]

Заметка:
    Примените правила Техасского Холдема для ранжирования карт.
    Низкие тузы НЕ действительны в этом слове.
    Там нет рейтинга для костюмов.

"""


class PokerHand(object):

    # Ценность каждой карты.
    card_value = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                  '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
                  }

    # Ценность комбинаций карт.
    COUPLE = 15
    TWO_COUPLE = 16
    SET = 17
    STREET = 18
    FLASH = 19
    FULL_HOUSE = 20
    KARE = 21
    STREET_FLASH = 22
    ROYAL_FLASH = 23

    # Возможные варианты результата игры.
    LOSS, TIE, WIN = 'Loss', 'Tie', 'Win'

    def __init__(self, hand):
        """ hand_value[] - ценность каждой из карт игрока.
        hand_color[] - цвет каждой из карт игрока.
        hand_couple - словарь содержащий только дубликаты карт, имеет вид:
        {ценность карты: её кол-во у игрока}

        """
        self.hand = hand.strip().split()
        self.hand_value = sorted([self.card_value[card[0]]
                                  for card in self.hand])

        self.hand_color = [card[1] for card in self.hand]

        self.hand_couple = {card: self.hand_value.count(card)
                            for card in self.hand_value
                            if self.hand_value.count(card) > 1}

    def get_high_card(self):
        """ Получет ценность самой высокой карты из имеющихся."""
        return self.hand_value[4]

    def is_color_all(self):
        """ Проверяет одинаковая ли масть у всех карт."""
        if len(set(self.hand_color)) == 1:
            return True
        else:
            return False

    def find_couple(self, quantity_card):
        """ Проверяет есть ли указанное кол-во одинаковых карт в словаре."""
        if self.hand_couple:
            for value in self.hand_couple.values():
                if quantity_card == value:
                    return True
        return False

    def is_couple(self):
        """ Проверяет есть ли в картах комбинация ПАРА."""
        return self.find_couple(2)

    def is_two_couple(self):
        """ Проверяет есть ли в картах комбинация ДВЕ ПАРЫ."""
        if self.hand_couple:
            count = 0
            for value in self.hand_couple.values():
                if value == 2:
                    count += 1
                if count == 2:
                    return True
        return False

    def is_set(self):
        """ Проверяет есть ли в картах комбинация СЕТ."""
        return self.find_couple(3)

    def is_street(self):
        """ Проверяет есть ли в картах комбинация СТРИТ."""
        hand_value_str = ''.join(map(str, self.hand_value))
        street_value = ''.join([str(i) for i in range(2, 15)])
        if hand_value_str in street_value:
            return True
        else:
            return False

    def is_full_house(self):
        """ Проверяет есть ли в картах комбинация ФУЛЛ ХАУС."""
        if self.is_couple() and self.is_set():
            return True
        return False

    def is_flash(self):
        """ Проверяет есть ли в картах комбинация ФЛЭШ."""
        return self.is_color_all()

    def is_kare(self):
        """ Проверяет есть ли в картах комбинация КАРЕ."""
        return self.find_couple(4)

    def is_street_flash(self):
        """ Проверяет есть ли в картах комбинация СТРИТ_ФЛЭШ."""
        if self.is_color_all() and self.is_street():
            return True
        return False

    def is_royal_flash(self):
        """ Проверяет есть ли в картах комбинация РОЯЛ_ФЛЭШ."""
        if self.is_street_flash() and 14 in self.hand_value:
            return True
        return False

    def equal_card_win(self, other):
        """ Детальное сравнивает ценности карт игрока и оппонента
        Если кол-во очков одинаково, последовательно сравнивает ценность
        каждой карты из отсортированного (от большего к меньшему) набора.

        """
        for card_index, card_value in enumerate(self.hand_value[::-1]):
            if card_value > other.hand_value[::-1][card_index]:
                return self.WIN
            elif card_value < other.hand_value[::-1][card_index]:
                return self.LOSS
        return self.TIE

    def check_hand(self):
        """ Проверяет совпала ли комбинация, если нет то берем старшую карту"""
        if self.is_royal_flash():
            return self.ROYAL_FLASH
        elif self.is_street_flash():
            return self.STREET_FLASH
        elif self.is_kare():
            return self.KARE
        elif self.is_full_house():
            return self.FULL_HOUSE
        elif self.is_flash():
            return self.FLASH
        elif self.is_street():
            return self.STREET
        elif self.is_set():
            return self.SET
        elif self.is_two_couple():
            return self.TWO_COUPLE
        elif self.is_couple():
            return self.COUPLE
        else:
            return self.get_high_card()

    def compare_with(self, other):
        """ Сравнивает ценность карт игрока и ценность карт опонента,
        если ценность равна, запускает более детальное сравнение.

        """
        player_hand = self.check_hand()
        enemy_hand = other.check_hand()

        if player_hand > enemy_hand:
            return self.WIN
        elif player_hand < enemy_hand:
            return self.LOSS
        elif player_hand == enemy_hand:
            return self.equal_card_win(other)
