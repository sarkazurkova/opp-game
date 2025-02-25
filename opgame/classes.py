from random import randrange
from enum import Enum
from _datetime import datetime
from tabulate import tabulate


class Dice:
    @staticmethod
    def rool(max_value=6):
        if max_value < 4 or max_value > 9:
            raise ValueError("Maximální hodnota musí být v rozmezí 4 až 9")
        return randrange(1, max_value + 1)


class Gender(Enum):
    male = 'man'
    female = 'woman'


class Person:
    def __init__(self, nickname: str, gender: Gender):
        self.nickname = nickname
        self.gender = gender
        self._birth = datetime.now()

    def __str__(self):
        return f"Nickname: {self.nickname}, [{self.gender.value}], birth: {self._birth.year}"

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, Gender):
            self._gender = gender
        else:
            raise ValueError("Gender není platná hodnota.")

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        if len(nickname) <= 10:
            self._nickname = nickname
        else:
            raise ValueError("Nickname nesmi přesáhnout 10 znaků.")

    def get_seconds_from_birth(self):
        return (datetime.now() - self._birth).total_seconds()

class Player(Person):
    def __init__(self, nickname: str, gender: Gender, state: str = "CZE"):
        super().__init__(nickname, gender)
        self.state = state
        self.count_of_games = 0
        self.wins = 0
        self.score = {'plus': 0, 'minus': 0}

    def __str__(self):
        return f"{super().__str__()}, state: {self.state}"

    @property
    def wins(self):
        return self._wins

    @wins.setter
    def wins(self, wins):
        if wins >= 0:
            self._wins = wins
        else:
            raise ValueError("Počet výher nesmí být záporné číslo.")

    def win_rate(self):
        return round(self.wins / self.count_of_games * 100, 2) if self.count_of_games > 0 else 0

    def overall_score(self):
        return self.score['plus'], self.score['minus']


class Match:
    def __init__ (self, hp: Player, gp: Player):
        self.h_player = hp
        self.g_player = gp
        self._datetime = datetime.now()
        self.hp_points = 0
        self.gp_points = 0
        self._history = []

    def __str__(self):
        return f"{self.h_player.nickname} - {self.g_player.nickname} {self.score()}"

    def __roll(self):
        while True:
            hp = Dice.rool()
            gp = Dice.rool()
            if hp != gp:
                break
        return 0 if hp > gp else 1


    def play(self):
        while self.hp_points < 10 and self.gp_points < 10:
            if self.__roll() == 0:
                self.hp_points += 1
            else:
                self.gp_points += 1
            self._history.append(self.score())
        self.h_player.count_of_games += 1
        self.g_player.count_of_games += 1

        self.h_player.score['plus'] += self.hp_points
        self.g_player.score['plus'] += self.gp_points

        self.h_player.score['minus'] += self.gp_points
        self.g_player.score['minus'] += self.hp_points

        if self.hp_points > self.gp_points:
            self.h_player.wins += 1
        else:
            self.g_player.wins += 1

    def score(self):
        return self.hp_points, self.gp_points

    def get_history(self):
        return self._history


class Tournament:
    def __init__(self, players: list):
        self.players = players
        self.matches_history = []

    def play(self):
        for i in range(len(self.players)):
            for j in range(i + 1, len(self.players)):
                player1 = self.players[i]
                player2 = self.players[j]

                # Vytvoření a spuštění zápasu mezi hráči
                match = Match(player1, player2)
                match.play()
                self.matches_history.append(match)

    def results(self):
        table_data = []
        for match in self.matches_history:
            table_data.append([match.h_player.nickname, match.g_player.nickname, match.hp_points, match.gp_points])

        # Vytvoření tabulky
        headers = ["Player 1", "Player 2", "Player 1 Score", "Player 2 Score"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))