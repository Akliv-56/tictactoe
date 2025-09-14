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