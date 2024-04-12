import random

class NavalBattle:
    playing_field = []
    final = [['~'] * 10 for _ in range(10)]
    def __init__(self, mark):
        self.mark = mark

    def shot(self, x, y):
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
        NavalBattle.playing_field = [[0] * 10 for _ in range(10)]
        ships = {'4': 1, '3': 2, '2': 3, '1': 4}
        for ship_size, count in ships.items():
            print(ship_size, count, '-')
            for i in range(count):
                k = 0
                while k != count:
                    print('')
                    print('Gonna place one', ship_size)
                    print('')
                    ship_size = int(ship_size)
                    x = random.randint(0, 9)
                    y = random.randint(0, 9)
                    direction = random.choice(['вверх', 'вправо', 'вниз', 'влево'])
                    print(x, y, direction)
                    if direction == 'вправо':
                        if x + ship_size <= 9 and NavalBattle.playing_field[y][x-1] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y][x + i] != 0 or
                                        NavalBattle.check_around(x-i, y, 'вправо')!=True):
                                    print('no way(')
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y][x + i] = 1
                                k += 1
                                print('k=', k)
                                for z in NavalBattle.playing_field:
                                    print(*z)
                                print('')
                                break
                        print(x, y, 'out of range')
                    if direction == 'влево':
                        if x - ship_size >= 0 and NavalBattle.playing_field[y][x+1] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y][x - i] != 0 or
                                        NavalBattle.check_around(x+i, y, 'влево')!=True):
                                    print('no way(')
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y][x - i] = 1
                                k += 1
                                print('k=', k)
                                for z in NavalBattle.playing_field:
                                    print(*z)
                                print('')
                                break
                        print(x, y, 'out of range')
                    if direction == 'вверх':
                        if y + ship_size <= 9 and NavalBattle.playing_field[y-1][x] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y + i][x] != 0 or
                                        NavalBattle.check_around(x, y+1, 'вверх') != True):
                                    print('no way(')
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y + i][x] = 1
                                k += 1
                                print('k=', k)
                                for z in NavalBattle.playing_field:
                                    print(*z)
                                print('')
                                break
                        print(x, y, 'out of range')
                    if direction == 'вниз':
                        if y - ship_size >= 0 and NavalBattle.playing_field[y+1][x] == 0:
                            for i in range(ship_size):
                                if (NavalBattle.playing_field[y - i][x] != 0 or
                                        NavalBattle.check_around(x, y-i, 'вниз') != True):
                                    print('no way(')
                                    break
                            else:
                                for i in range(ship_size):
                                    NavalBattle.playing_field[y - i][x] = 1
                                k += 1
                                print('k=', k)
                                for z in NavalBattle.playing_field:
                                    print(*z)
                                print('')
                                break
                        print(x, y, 'out of range')
                else:
                    print('')
                    print('Finished all', ship_size)
                    print('')

    @staticmethod
    def check_around(x, y, destination):
        if destination == 'верх':
            for i in range(x-1, x+2):
                for j in range(y, y+2):
                    if i < 10 and j < 10:
                        if NavalBattle.playing_field[j][i] == 1:
                            return False
                        else:
                            print('for', x, y, 'this', i, j, 'is fine')
            return
        if destination == 'вниз':
            for i in range(x-1, x+2):
                for j in range(y-1, y+1):
                    if i < 10 and j < 10:
                        if NavalBattle.playing_field[j][i] == 1:
                            return False
                        else:
                            print('for', x, y, 'this', i, j, 'is fine')
            return True
        if destination == 'влево':
            for i in range(x-1, x+1):
                for j in range(y-1, y+2):
                    if i < 10 and j < 10:
                        if NavalBattle.playing_field[j][i] == 1:
                            return False
                        else:
                            print('for', x, y, 'this', i, j, 'is fine')
            return True
        if destination == 'вправо':
            for i in range(x, x+2):
                for j in range(y-1, y+2):
                    if i < 10 and j < 10:
                        if NavalBattle.playing_field[j][i] == 1:
                            return False
                        else:
                            print('for', x, y, 'this', i, j, 'is fine')
            return True

    @staticmethod
    def show():
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