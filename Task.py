import heapq  # Імпортуємо модуль для роботи з мінімальною купою

def minCostToConnectCables(cables):
    # Ініціалізуємо мінімальну купу з довжинами кабелів
    heapq.heapify(cables)
    
    total_cost = 0  # Загальні витрати на з'єднання всіх кабелів
    
    # Поки в купі більше одного кабелю
    while len(cables) > 1:
        # Видаляємо два найменші кабелі з купи
        first_min = heapq.heappop(cables)
        second_min = heapq.heappop(cables)
        
        # Обчислюємо витрати на з'єднання цих двох кабелів
        cost = first_min + second_min
        total_cost += cost  # Додаємо витрати до загальної суми
        
        # Додаємо новий кабель, отриманий в результаті з'єднання, назад до купи
        heapq.heappush(cables, cost)
    
    # Повертаємо загальні витрати на з'єднання всіх кабелів
    return total_cost

# Приклад використання
cables = [8, 4, 6, 12]
print("Мінімальні витрати на з'єднання кабелів:", minCostToConnectCables(cables))