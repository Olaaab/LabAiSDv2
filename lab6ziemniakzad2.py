from collections import deque

def ziemniak(names, num_iterations):
    queue = deque(names)

    while len(queue) > 1:
        for _ in range(num_iterations):
            # Przekazanie ziemniaka
            queue.append(queue.popleft())

        # Usunięcie uczestnika z początku kolejki
        eliminated = queue.popleft()
        print(f"{eliminated} odpada z gry.")

    winner = queue.pop()
    print(f"Zwycięzca: {winner}")
    return winner


uczestnicy = ["Ola", "Bartek", "Hubert", "Dorota", "Zuzia", "Dawid"]
liczba_operacji = 3

zwyciezca = ziemniak(uczestnicy, liczba_operacji)
