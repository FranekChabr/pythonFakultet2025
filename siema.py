import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


def initialize_grid(size):
    """Tworzy początkową losową siatkę z wartościami 0 i 1."""
    return np.random.choice([0, 1], size=size)


def apply_rule(grid):
    """Zastosuj regułę 30 do każdej komórki w siatce 2D (sąsiedztwo von Neumanna)."""
    rows, cols = grid.shape
    new_grid = np.zeros((rows, cols), dtype=int)

    for i in range(rows):
        for j in range(cols):
            # Pobranie sąsiadów von Neumanna (góra, dół, lewo, prawo)
            neighbors = [
                grid[i - 1, j] if i > 0 else 0,  # góra
                grid[i + 1, j] if i < rows - 1 else 0,  # dół
                grid[i, j - 1] if j > 0 else 0,  # lewo
                grid[i, j + 1] if j < cols - 1 else 0  # prawo
            ]

            pattern = sum(neighbors)  # Liczba aktywnych sąsiadów
            new_grid[i, j] = 1 if (pattern == 1 or pattern == 3) else 0  # Prosta zasada ewolucji

    return new_grid


def visualize(grid, step):
    """Wyświetla siatkę jako obraz binarny."""
    plt.figure(figsize=(6, 6))
    cmap = mcolors.ListedColormap(["white", "black"])
    plt.imshow(grid, cmap=cmap, interpolation='nearest')
    plt.axis("off")
    plt.title(f"Step {step}")
    plt.show()


def run_simulation(size=(50, 50), steps=30):
    """Uruchamia symulację automatu przez określoną liczbę kroków."""
    grid = initialize_grid(size)

    for step in range(steps):
        visualize(grid, step)
        grid = apply_rule(grid)


if __name__ == "__main__":
    run_simulation()