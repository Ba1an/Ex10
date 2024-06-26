import random

class NavalBattle:
    """
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
    - new_game(): Initializes a new game by randomly placing ships on the playing field.
    - check_around(x, y): Checks if there are any ships around the specified coordinates.
    - show(): Displays the final state of the playing field.
    """
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
        if NavalBattle.playing_field == []:
            print('игровое поле не заполнено')
        elif NavalBattle.final[y - 1][x - 1] != '~':
            print('ошибка')
        elif NavalBattle.playing_field[y-1][x-1] == 1:
            self.final[y-1][x-1] = self.mark
            print('попал')
        else:
            self.final[y-1][x-1] = 'o'
            print('мимо')

    @staticmethod
    def new_game():
        """
        Initializes a new game by randomly placing ships on the playing field.
        """
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        ships = {'4': 1, '3': 2, '2': 3, '1': 4}
        for ship_size, count in ships.items():
            for i in range(count):
                k = 0
                while k != count:
                    ship_size = int(ship_size)
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    direction = random.choice(['вверх', 'вправо', 'вниз', 'влево'])
                    if direction == 'вправо':
                        if x + ship_size <= 10 and NavalBattle.playing_field[y][x - 1] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y][x + i] != 0 or
                                        NavalBattle.check_around(x - i, y) != True):
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y][x + i] = 1
                                k += 1
                                break
                    if direction == 'влево':
                        if x - ship_size >= 0 and NavalBattle.playing_field[y][min(x + 1, 9)] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y][x - i] != 0 or
                                        NavalBattle.check_around(x+i, y)!=True):
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y][x - i] = 1
                                k += 1
                                break
                    if direction == 'вверх':
                        if y + ship_size <= 10 and NavalBattle.playing_field[y-1][x] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y + i][x] != 0 or
                                        NavalBattle.check_around(x, y+i) != True):
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y + i][x] = 1
                                k += 1
                                break
                    if direction == 'вниз':
                        if y - ship_size >= 0 and NavalBattle.playing_field[min(y + 1, 9)][x] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y - i][x] != 0 or
                                        NavalBattle.check_around(x, y - i) != True):
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y - i][x] = 1
                                k += 1
                                break

    @staticmethod
    def check_around(x, y):
        """
        Checks if there are any ships around the specified coordinates.

        Parameters
        ----------
        - x: int, X coordinate.
        - y: int, Y coordinate.
        """

        for i in range(max(x - 1, 0), min(x + 2, 10)):
            for j in range(max(y - 1, 0), min(y + 2, 10)):
                if (i != x and j != y) and NavalBattle.playing_field[j][i] == 1:
                    return False
                elif (i != x or j != y) and NavalBattle.playing_field[j][i] == 1:
                    return False
        return True

    @staticmethod
    def show():
        """
        Displays the final state of the playing field.
        """
        for z in NavalBattle.final:
            print(*z)

player1 = NavalBattle('#')
player1.shot(6, 2)
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
player1.shot(6, 2)
player1.shot(6, 2)
NavalBattle.show()
player1.shot(1,1)
player1.shot(1,1)
NavalBattle.new_game()
NavalBattle.show()
player1.shot(6, 2)