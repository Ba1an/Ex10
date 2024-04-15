class NavalBattle:
    '''
    It is a class representing a naval battle game.

    Attributes
    -----------
    - mark: str, Mark representing a ship on the playing field.

    Class Attributes
    ----------------
    - playing_field: list, A 2D list representing the playing field.
    - final: list, A 2D list representing the final state of the playing field after shots.

    Methods
    --------
    - shot(x, y): Performs a shot at the specified coordinates and updates the final state of the playing field.
    - show(): Displays the final state of the playing field.
    '''
    playing_field = []
    final = [['~'] * 10 for _ in range(10)]
    def __init__(self, mark):
        self.mark = mark

    def shot(self, x, y):
        """
        Performs a shot at the specified coordinates and updates the final state of the playing field.

        Parameters
        ----------
        - x: int, X coordinate of the shot.
        - y: int, Y coordinate of the shot.
        """
        if NavalBattle.playing_field[y-1][x-1] == 1:
            self.final[y-1][x-1] = self.mark
            print('попал')
        else:
            self.final[y-1][x-1] = 'o'
            print('мимо')

    @staticmethod
    def show():
        """
        Displays the final state of the playing field.
        """
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
