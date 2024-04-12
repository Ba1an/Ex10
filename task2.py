class NavalBattle:
    playing_field = []
    final = [['~'] * 10 for _ in range(10)]
    def __init__(self, mark):
        self.mark = mark

    def shot(self, x, y):
        if NavalBattle.playing_field[y-1][x-1] == 1:
            self.final[y-1][x-1] = self.mark
            print('попал')
        else:
            self.final[y-1][x-1] = 'o'
            print('мимо')

    @staticmethod
    def show():
        for z in NavalBattle.final:
            print(*z)


NavalBattle.playing_field = [[0, 1, 1, 1, 0, 0, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                             [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],
                             [1, 1, 1, 0, 0, 1, 0, 0, 1, 0],
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 1, 1, 0, 0, 1, 0, 0]]
player1 = NavalBattle("#")
player2 = NavalBattle("*")
NavalBattle.show()
print(' ')
player1.shot(6, 2)
player1.shot(6, 1)
player2.shot(6, 3)
player2.shot(6, 4)
player2.shot(6, 5)
player2.shot(3, 3)
player2.show()
print('')
player1.shot(1, 1)
NavalBattle.show()
