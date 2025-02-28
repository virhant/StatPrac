import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

def generate_normal_sample(n):
    """
    Генерирует выборку из двумерного нормального распределения
    с использованием модифицированного метода Box-Muller
    """
    # Генерация равномерных случайных чисел
    u1, u2 = np.random.rand(2, n)
    r = np.sqrt(-2 * np.log(u1))
    
    # Исключаем использование sin и cos
    z1 = r * (2 * u2 - 1) / np.sqrt((2 * u2 - 1)**2 + (1 - 2 * u1)**2)
    z2 = r * (1 - 2 * u1) / np.sqrt((2 * u2 - 1)**2 + (1 - 2 * u1)**2)
    
    return z1, z2

def transform_to_target_distribution(z1, z2, mu, Sigma):
    """
    Преобразует стандартное нормальное распределение в целевое
    """
    L = scipy.linalg.cholesky(Sigma, lower=True)  # Разложение Холецкого
    samples = L @ np.vstack((z1, z2)) + mu[:, np.newaxis]
    return samples

def plot_2d_histogram(samples):
    """
    Строит двумерную гистограмму распределения
    """
    plt.figure(figsize=(8, 6))
    plt.hist2d(samples[0], samples[1], bins=30, density=True, cmap="Blues")
    plt.colorbar(label="Density")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("2D Gaussian Distribution")
    plt.show()

def main():
    n = 1000  # Размер выборки
    mu = np.array([1, 2])  # Среднее значение
    Sigma = np.array([[20, -4], [-4, 5]])  # Ковариационная матрица
    
    # Генерация выборки
    z1, z2 = generate_normal_sample(n)
    samples = transform_to_target_distribution(z1, z2, mu, Sigma)
    
    # Вычисление эмпирических характеристик
    empirical_mean = np.mean(samples, axis=1)
    empirical_cov = np.cov(samples)
    
    # Построение гистограммы
    plot_2d_histogram(samples)
    
    # Вывод результатов
    print("Эмпирическое среднее:", empirical_mean)
    print("Эмпирическая ковариационная матрица:\n", empirical_cov)

if __name__ == "__main__":
    main()
