from matplotlib.backends.backend_pdf import PdfPages

import matplotlib.pyplot as plt
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

# --- Данные для Задания 4б (Зависимость длины волны от Uрез) ---

# 1. Uотр = 40 В
urez1 = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
lam1 = [10.58, 10.58, 10.58, 10.58, 10.58, 10.56, 10.55, 10.51, 10.51, 10.50, np.nan, np.nan]

# 2. Uотр = 37 В
urez2 = [30, 40, 50, 60, 70, 80, 90]
lam2 = [np.nan, 10.56, 10.57, 10.57, 10.57, 10.56, 10.56]

def plot_with_nan(ax, x, y, label, marker, linestyle):
    # Создаем маски для валидных данных
    x_arr = np.array(x)
    y_arr = np.array(y)
    mask = ~np.isnan(y_arr)
    
    # Строим график только по валидным точкам
    ax.plot(x_arr[mask], y_arr[mask], marker=marker, linestyle=linestyle, label=label)

# --- Построение графика ---
fig, ax = plt.subplots(figsize=(10, 6))

plot_with_nan(ax, urez1, lam1, r'$U_{отр} = 40$ В', 'o', '-')
plot_with_nan(ax, urez2, lam2, r'$U_{отр} = 37$ В', 's', '--')

# Настройки графика
ax.set_title(r'Зависимость длины волны $\lambda$ от напряжения на резонаторе $U_{рез}$')
ax.set_xlabel(r'Напряжение на резонаторе $U_{рез}$, В')
ax.set_ylabel(r'Длина волны $\lambda$, см')
ax.grid(True, which='both', linestyle='--', alpha=0.7)
ax.legend()


# Сохранение в PDF
fig.savefig('./python/images/graph_task_b_lambda.pdf', bbox_inches='tight', dpi=300)
plt.close(fig)

