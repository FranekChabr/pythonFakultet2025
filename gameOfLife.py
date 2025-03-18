import numpy as np
import os
import time

def initialize_grid(size, density=0.2):
    """Tworzy początkową siatkę z losowo rozmieszczonymi komórkami."""
    return np.random.choice([0, 1], size=size, p=[1 - density, density])


def apply_game_of_life_rule(grid):
    """Zastosuj reguły Game of Life do całej siatki."""
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)

    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            neighbors = np.sum(grid[i - 1:i + 2, j - 1:j + 2]) - grid[i, j]

            if grid[i, j] == 1 and (neighbors == 2 or neighbors == 3):
                new_grid[i, j] = 1
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    return new_grid


def visualize(grid):
    """Wyświetla siatkę jako obraz ASCII w terminalu."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Czyszczenie terminala
    print("\n".join("".join("█" if cell else " " for cell in row) for row in grid))


def run_simulation(size=(20, 20), steps=60):
    """Uruchamia symulację Game of Life."""
    grid = initialize_grid(size)

    for step in range(steps):
        visualize(grid)
        time.sleep(0.2)  # Opóźnienie między krokami
        grid = apply_game_of_life_rule(grid)


if __name__ == "__main__":
    run_simulation()
