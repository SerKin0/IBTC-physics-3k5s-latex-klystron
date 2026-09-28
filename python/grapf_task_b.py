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

# 1. U'отр = 40' В
urez1 = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
i1 = [0, 5, 17, 23, 28, 29, 28, 29, 29, 28, 18, 0]
lam1 = [10.58, 10.58, 10.58, 10.58, 10.58, 10.56, 10.55, 10.51, 10.51, 10.50, np.nan, np.nan]

# 2. U'отр = 37' В (данные для лямбды немного рваные, берем как есть)
urez2 = [30, 40, 50, 60, 70, 80, 90]
i2 = [0, 25, 30, 30, 32, 34, 0]
lam2 = [np.nan, 10.56, 10.57, 10.5, 10.57, 10.56, 10.56]

# --- Построение графиков ---
fig, ax1 = plt.subplots(figsize=(10, 6))

# График 1: Ток детектора I(U'рез')
ax1.plot(urez1, i1, marker='o', linestyle='-', label=r"$U_{отр} = 40$ В")
ax1.plot(urez2, i2, marker='s', linestyle='--', label=r"$U_{отр} = 37$ В")
# ax1.set_title(r"Зависимость тока детектора $I$ от напряжения на резонаторе $U_{рез}$", fontsize=14)
ax1.set_xlabel(r"Напряжение на резонаторе $U_{рез}$, В", fontsize=12)
ax1.set_ylabel(r'Ток детектора $I$, делений', fontsize=12)
ax1.grid(True, which='both', linestyle='--', alpha=0.7)
ax1.legend(fontsize=10)



# Настройка тиков
ax1.set_xticks(np.arange(0, 100, 10))
plt.tight_layout()

# Сохранение в PDF
fig.savefig('./python/images/graph_task_b.pdf', bbox_inches='tight', dpi=300)
plt.close(fig)