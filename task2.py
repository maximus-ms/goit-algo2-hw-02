from typing import List, Dict
from functools import lru_cache


def rod_cutting_memo(length: int, prices: List[int]):
    @lru_cache(None)
    def rod_cutting_memo_recur(length):
        if length == 0: return 0, []

        max_profit = 0
        best_cut = []
        for i in range(length):
            profit, cuts = rod_cutting_memo_recur(length - (i + 1))
            profit += prices[i]
            if profit > max_profit:
                max_profit = profit
                best_cut = [i + 1] + cuts

        return max_profit, best_cut

    max_profit, best_cut = rod_cutting_memo_recur(length)

    return {
        "max_profit": max_profit,
        "cuts": best_cut,
        "number_of_cuts": len(best_cut) - 1
    }

def rod_cutting_table(length: int, prices: List[int]):
    dp = [0] * (length + 1)
    cuts = [[] for _ in range(length + 1)]

    for n in range(1, length + 1):
        for i in range(1, n + 1):
            if i <= len(prices) and dp[n - i] + prices[i - 1] > dp[n]:
                dp[n] = dp[n - i] + prices[i - 1]
                cuts[n] = [i] + cuts[n - i]
    return {
        "max_profit": dp[length],
        "cuts": cuts[length],
        "number_of_cuts": len(cuts[length]) - 1
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        # Тест 1: Базовий випадок
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        # Тест 2: Оптимально не різати
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        # Тест 3: Всі розрізи по 1
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        # Тестуємо мемоізацію
        memo_result = rod_cutting_memo(test['length'], test['prices'])
        print("\nРезультат мемоізації:")
        print(f"Максимальний прибуток: {memo_result['max_profit']}")
        print(f"Розрізи: {memo_result['cuts']}")
        print(f"Кількість розрізів: {memo_result['number_of_cuts']}")

        # Тестуємо табуляцію
        table_result = rod_cutting_table(test['length'], test['prices'])
        print("\nРезультат табуляції:")
        print(f"Максимальний прибуток: {table_result['max_profit']}")
        print(f"Розрізи: {table_result['cuts']}")
        print(f"Кількість розрізів: {table_result['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()
