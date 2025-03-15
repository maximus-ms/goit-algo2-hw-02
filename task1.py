from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[Dict], constraints: Dict) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """

    class ThePrinter:
        def __init__(self, max_volume, max_items):
            self.max_volume = max_volume
            self.max_items = max_items
            self.total_time = 0
            self.current_times = [0]
            self.job_queue = []
            self.execute()

        def execute(self):
            self.total_time += max(self.current_times)
            self.current_free_volume = self.max_volume
            self.current_free_items = self.max_items
            self.current_times = [0]

        def add_job(self, job):
            if job['volume'] > self.max_volume: raise ValueError('Volume is too big')
            if job['volume'] > self.current_free_volume or self.current_free_items == 0:
                self.execute()
            self.job_queue.append(job['id'])
            self.current_times.append(job['print_time'])
            self.current_free_volume -= job['volume']
            self.current_free_items -= 1

        def get_statistics(self):
            self.execute()
            return {
                "print_order": self.job_queue,
                "total_time": self.total_time,
            }

    printer = ThePrinter(constraints['max_volume'], constraints['max_items'])
    jobs_to_print = len(print_jobs)
    current_priority = 0

    while jobs_to_print > 0:
        current_priority += 1
        for job in print_jobs:
            if job['id'] in printer.job_queue: continue
            if job["priority"] > current_priority: continue
            printer.add_job(job)
            jobs_to_print -= 1
            if jobs_to_print == 0: break

    return printer.get_statistics()

# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        {"id": "M1", "volume": 100, "priority": 1, "print_time": 120},
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},
        {"id": "M3", "volume": 120, "priority": 1, "print_time": 150}
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        {"id": "M1", "volume": 100, "priority": 2, "print_time": 120},  # лабораторна
        {"id": "M2", "volume": 150, "priority": 1, "print_time": 90},  # дипломна
        {"id": "M3", "volume": 120, "priority": 3, "print_time": 150}  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        {"id": "M1", "volume": 250, "priority": 1, "print_time": 180},
        {"id": "M2", "volume": 200, "priority": 1, "print_time": 150},
        {"id": "M3", "volume": 180, "priority": 2, "print_time": 120}
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")

if __name__ == "__main__":
    test_printing_optimization()

