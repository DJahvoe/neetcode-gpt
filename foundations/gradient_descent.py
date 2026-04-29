class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        cur = init
        for i in range(0, iterations):
            derivative = 2 * cur
            delta = learning_rate * derivative
            cur -= delta
        return round(cur, 5)