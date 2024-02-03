# Аналіз та Реалізація Алгоритмів на Графі

Цей документ описує роботу з графами за допомогою бібліотеки NetworkX у Python. Включено аналіз графа, алгоритми пошуку в глибину (DFS) та в ширину (BFS), а також реалізацію алгоритму Дейкстри для пошуку найкоротшого шляху.

## Завдання 1: Створення та Аналіз Графа

Було створено граф, який представляє модель транспортної мережі з 50 зупинками.

- Кількість вершин: 50
- Кількість ребер: 137
- Ступені вершин: {'Station1': 6, 'Station2': 10, 'Station3': 8, 'Station4': 5, 'Station5': 11, 'Station6': 5, 'Station7': 4, 'Station8': 6, 'Station9': 9, 'Station10': 4, 'Station11': 2, 'Station12': 5, 'Station13': 6, 'Station14': 6, 'Station15': 4, 'Station16': 7, 'Station17': 11, 'Station18': 6, 'Station19': 6, 'Station20': 8, 'Station21': 7, 'Station22': 4, 'Station23': 9, 'Station24': 3, 'Station25': 7, 'Station26': 4, 'Station27': 5, 'Station28': 8, 'Station29': 5, 'Station30': 1, 'Station31': 7, 'Station32': 3, 'Station33': 4, 'Station34': 7, 'Station35': 4, 'Station36': 4, 'Station37': 6, 'Station38': 2, 'Station39': 3, 'Station40': 2, 'Station41': 7, 'Station42': 5, 'Station43': 7, 'Station44': 5, 'Station45': 3, 'Station46': 4, 'Station47': 6, 'Station48': 2, 'Station49': 6, 'Station50': 5}
- Щільність графа: 0.11184
- Кількість компонентів зв'язності: 1
- Діаметр графа: 5
- Середній найкоротший шлях: 2.4637
- Середній кластерний коефіцієнт: 0.1339

## Завдання 2: Алгоритми DFS та BFS

### DFS Tree
- Порядок обходу: [('Station5', 'Station1'), ('Station1', 'Station2'), ('Station2', 'Station4'), ('Station4', 'Station35'), ('Station35', 'Station49'), ('Station49', 'Station17'), ('Station17', 'Station34'), ('Station34', 'Station8'), ('Station8', 'Station3'), ('Station3', 'Station9'), ('Station3', 'Station30'), ('Station9', 'Station20'), ('Station20', 'Station26'), ('Station26', 'Station50'), ('Station50', 'Station14'), ('Station14', 'Station12'), ('Station12', 'Station44'), ('Station44', 'Station32'), ('Station32', 'Station25'), ('Station25', 'Station27'), ('Station27', 'Station48'), ('Station27', 'Station43'), ('Station43', 'Station28'), ('Station28', 'Station23'), ('Station23', 'Station16'), ('Station16', 'Station21'), ('Station21', 'Station18'), ('Station18', 'Station40'), ('Station18', 'Station45'), ('Station18', 'Station13'), ('Station45', 'Station41'), ('Station41', 'Station36'), ('Station41', 'Station33'), ('Station36', 'Station38'), ('Station33', 'Station22'), ('Station13', 'Station6'), ('Station13', 'Station46'), ('Station6', 'Station47'), ('Station47', 'Station42'), ('Station47', 'Station39'), ('Station42', 'Station37'), ('Station37', 'Station19'), ('Station19', 'Station31'), ('Station19', 'Station11'), ('Station31', 'Station7'), ('Station7', 'Station24'), ('Station11', 'Station10'), ('Station46', 'Station29'), ('Station29', 'Station15')]

### BFS Tree
- Порядок обходу:  [('Station5', 'Station1'), ('Station5', 'Station7'), ('Station5', 'Station16'), ('Station5', 'Station17'), ('Station5', 'Station19'), ('Station5', 'Station47'), ('Station5', 'Station31'), ('Station5', 'Station9'), ('Station5', 'Station42'), ('Station5', 'Station14'), ('Station5', 'Station24'), ('Station1', 'Station2'), ('Station1', 'Station3'), ('Station1', 'Station10'), ('Station1', 'Station21'), ('Station7', 'Station50'), ('Station16', 'Station23'), ('Station16', 'Station43'), ('Station16', 'Station13'), ('Station16', 'Station28'), ('Station17', 'Station34'), ('Station17', 'Station49'), ('Station17', 'Station22'), ('Station17', 'Station46'), ('Station17', 'Station36'), ('Station17', 'Station29'), ('Station17', 'Station33'), ('Station19', 'Station37'), ('Station19', 'Station8'), ('Station19', 'Station11'), ('Station47', 'Station39'), ('Station47', 'Station6'), ('Station31', 'Station44'), ('Station31', 'Station25'), ('Station9', 'Station20'), ('Station9', 'Station45'), ('Station9', 'Station15'), ('Station14', 'Station12'), ('Station2', 'Station4'), ('Station3', 'Station18'), ('Station3', 'Station27'), ('Station3', 'Station30'), ('Station21', 'Station41'), ('Station50', 'Station26'), ('Station23', 'Station35'), ('Station43', 'Station32'), ('Station28', 'Station38'), ('Station44', 'Station48'), ('Station18', 'Station40')]

DFS та BFS показали різні порядки обходу графа, що відображає їх особливості: DFS занурюється настільки глибоко, наскільки це можливо, перш ніж повертатися, тоді як BFS відвідує всі сусідні вершини перед переходом на наступний рівень.

## Завдання 3: Алгоритм Дейкстри

Було використано алгоритм Дейкстри для знаходження найкоротшого шляху від 'Station1' до 'Station50' у графі з вагами ребер.

- Найкоротший шлях: ['Station1', 'Station3', 'Station34', 'Station41', 'Station50']
- Довжина шляху: 14

## Висновки

Робота з графами виявилася ефективним методом для представлення та аналізу складних мережевих структур. Алгоритми DFS та BFS мають різні характеристики та можуть бути корисними для різних завдань. Алгоритм Дейкстри ефективно знаходить найкоротші шляхи в графі, особливо корисно в мережах з різними вагами.
