from classes import Dice, Person, Gender, Player, Match, Tournament

def main():

    hod = Dice.rool()
    print(hod)
    muz = Player("Adam", Gender.male)
    zena = Player("Eva", Gender.female)
    muz2 = Player("David", Gender.male)
    muz3 = Player("Abraham", Gender.male)


    print(muz)
    print(zena)
    # muz.count_of_games = 10
    # muz.wins = 3
    # print(muz.win_rate())
    # muz.score = {'plus': 10, 'minus': 5}
    # print(muz.overall_score())

    zapas1 = Match(zena, muz)
    zapas1.play()
    print(zapas1)
    print(zapas1.get_history())

    zapas2 = Match(zena, muz)
    zapas2.play()
    print(zapas2)
    print(zapas2.get_history())

    print(zena, " | ", zena.wins, " | ", zena.score)
    print(muz, " | ", muz.wins, " | ", muz.score)

    players = [muz, zena, muz2, muz3]
    turnaj = Tournament(players)
    turnaj.play()
    turnaj.results()

if __name__ == "__main__":
    main()

