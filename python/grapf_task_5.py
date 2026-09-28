import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# Устанавливаем шрифт CMU Serif
plt.rcParams['font.family'] = 'CMU Serif'
plt.rcParams['mathtext.fontset'] = 'cm'
plt.rcParams['font.size'] = 14
plt.rcParams['axes.titlesize'] = 16
plt.rcParams['axes.labelsize'] = 15
plt.rcParams['xtick.labelsize'] = 13
plt.rcParams['ytick.labelsize'] = 13
plt.rcParams['legend.fontsize'] = 12

# --- Данные из таблиц ---

# 1. U'отр = 6' В
ip1 = [8, 10, 12, 14, 16, 18, 20, 9, 11, 13, 15, 17, 19]
id1 = [0, 3, 12, 16, 15, 8, 0, 3, 6, 16, 14, 11, 0]

# 2. U'отр = 14' В
ip2 = [14, 15, 16, 17, 18, 19, 20, 21, 13]
id2 = [3, 22, 23, 24, 24, 24, 22, 22, 0]

# 3. U'отр = 36' В
ip3 = [15, 16, 17, 18, 19, 20, 21]
id3 = [0, 15, 23, 25, 27, 28, 29]

# --- Функция для сортировки и построения ---
def plot_sorted(ax, x, y, label, marker, linestyle):
    # Сортируем данные по оси X
    sorted_pairs = sorted(zip(x, y))
    x_sorted, y_sorted = zip(*sorted_pairs)
    ax.plot(x_sorted, y_sorted, marker=marker, linestyle=linestyle, label=label)

# --- Построение графика ---
fig, ax = plt.subplots(figsize=(10, 6))

plot_sorted(ax, ip1, id1, r"$U_{отр} = 6$ В", 'o', '-')
plot_sorted(ax, ip2, id2, r"$U_{отр} = 14$ В", 's', '--')
plot_sorted(ax, ip3, id3, r"$U_{отр} = 36$ В", '^', '-.')

# Настройки
# ax.set_title(r"Зависимость тока детектора $I_д$ от тока пучка $I_п$ ($U_{рез} = 40$ В)", fontsize=14)
ax.set_xlabel(r"Ток пучка $I_п$, мА", fontsize=12)
ax.set_ylabel(r"Ток детектора $I_д$, делений", fontsize=12)
ax.grid(True, which='both', linestyle='--', alpha=0.7)
ax.legend(fontsize=10)

# Диапазоны осей (подобраны под данные)
ax.set_xticks(np.arange(6, 23, 2))
ax.set_yticks(np.arange(0, 35, 5))

plt.tight_layout()

# Сохранение в PDF
fig.savefig('./python/images/graph_task_5.pdf', bbox_inches='tight', dpi=300)
plt.close(fig)