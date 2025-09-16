from constants import *

class Cell:

    def __init__(self, position_x, position_y, mark=EMPTY):
        self.position_x = position_x
        self.position_y = position_y

        self.mark = mark

    def set_mark(self, new_mark:int) -> None:
        if not new_mark in (ZERO, CROSS): raise ValueError("")
        if not self.is_empty(): raise Exception("")

        self.mark = new_mark

    def clear_mark(self) -> None:
        self.mark = EMPTY

    def is_empty(self) -> bool:
        return self.mark == EMPTY


class Field:


    def __init__(self):
        self.size_x = 3
        self.size_y = 3
        self.cells = []

    def build(self):
        # TODO: Do home
        pass

    def make_move(self, x:int, y:int, mark:int) -> None:
        # TODO: Do home
        pass

    def can_move(self, x: int, y: int) -> bool:
        if not x <= 3: raise ValueError("")
        if not y <= 3: raise ValueError("")

        if Cell(x,y).is_empty == True:
            return True
        else:
            return False
        
    def clear(self) -> None:
        # TODO: Do home
        pass