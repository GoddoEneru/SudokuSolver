class SudokuSolver:
    def __init__(self, problem_grid):
        self.problem_grid = problem_grid

    def verify_if_value_is_valid(self, index, value):
        # verif zone
        ir = (index[0] // 3) * 3
        ic = (index[1] // 3) * 3
        for n in range(ir, ir + 3):
            for k in range(ic, ic + 3):
                if self.problem_grid[(n, k)] == value and (n != index[0] or k != index[1]):
                    return False
        # verif row
        for ic in range(0, 9):
            if self.problem_grid[(index[0], ic)] == value and ic != index[1]:
                return False
        # verif col
        for ir in range(0, 9):
            if self.problem_grid[(ir, index[1])] == value and ir != index[0]:
                return False
        return True

    def solve(self):
        # verif s'il y a une case modifiable
        number_row = self.problem_grid.shape[0]
        number_col = self.problem_grid.shape[1]
        for ir in range(0, number_row):
            for ic in range(0, number_col):
                if self.problem_grid[(ir, ic)] == 0:
                    index = (ir, ic)
                elif ic == 0 and ir == 0:
                    return True

        # test les valeurs de 1 à 9 dans la case modifiable et passe à la case suivante si une valeur est valide
        for i in range(1, 10):
            if self.verify_if_value_is_valid(index, i):
                self.problem_grid[index] = i
                if self.solve():
                    return True

        # réinitialise la case si aucune valeur est valide et retourne sur la précédente case
        self.problem_grid[index] = 0
        return False

        # # verif si une case est modifiable ou non
        # mod = False
        # for ir in range(0, 9):
        #     for ic in range(0, 9):
        #         if self.problem_grid[(ir, ic)] == 0:
        #             index = (ir, ic)
        #             mod = True
        #
        # # boucle si la case est modifiable pour trouver une valeur valid
        # while mod:
        #     # recupere la valeur actuelle
        #     value_act = self.problem_grid[index]
        #     # reinitialise la case au cas ou il n'y a plus de valeur valid pour pouvoir modifier la precedente
        #     self.problem_grid[index] = 0
        #     # test que les valeurs suivantes à la valeur actuelle
        #     for i in range(value_act + 1, 10):
        #         if self.verify_if_value_is_valid(index, i) and i != value_act:
        #             self.problem_grid[index] = i
        #             break
        #     # retourne sur la case precedente si aucune valeur valid a ete trouve
        #     if self.problem_grid[index] == 0:
        #         return False
        #
        #     if self.solve():
        #         return True
        # # Permet de quitter la recursive une fois le sudoku rempli
        # return True

    def __str__(self):
        return f"Le problème est :\n{self.problem_grid}"
