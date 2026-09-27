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

# --- Данные для Задания 4а (Зависимость длины волны от Uотр) ---

# 1. (опт) Uрез = 120 В
uotr1 = [2, 6, 7, 10, 12, 14, 16, 18, 29, 30, 36, 39, 40]
lam1  = [np.nan, 10.54, np.nan, np.nan, 10.61, 10.58, 10.54, np.nan, np.nan, 10.62, 10.57, 10.54, np.nan]

# 2. (опт - 20V) Uрез = 100 В
uotr2 = [11, 12, 14, 16, 17, 20, 29, 30, 31, 32, 33, 35, 36, 37]
lam2  = [np.nan, 10.60, 10.58, 10.54, 10.53, np.nan, np.nan, 10.60, 10.60, 10.59, 10.58, 10.57, 10.56, np.nan]

# 3. (опт + 20V) Uрез = 140 В
uotr3 = [2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 18, 32, 34, 37]
lam3  = [np.nan, 10.55, 10.54, 10.53, np.nan, np.nan, 10.65, 10.61, 10.60, 10.58, 10.57, 10.56, np.nan, np.nan, 10.6, 10.35]

def plot_with_nan(ax, x, y, label, marker, linestyle):
    # Создаем маски для валидных данных
    x_arr = np.array(x, dtype=float)
    y_arr = np.array(y, dtype=float)
    mask = ~np.isnan(y_arr)
    
    # Строим график только по валидным точкам
    ax.scatter(x_arr[mask], y_arr[mask], marker=marker, linestyle=linestyle, label=label)

# --- Построение графика ---
fig, ax = plt.subplots(figsize=(10, 6))

plot_with_nan(ax, uotr1, lam1, r'$U_{рез} = 120$ В (опт)', 'o', '-')
plot_with_nan(ax, uotr2, lam2, r'$U_{рез} = 100$ В (опт - 20)', 's', '--')
plot_with_nan(ax, uotr3, lam3, r'$U_{рез} = 140$ В (опт + 20)', '^', '-.')

# Настройки графика
ax.set_title(r'Зависимость длины волны $\lambda$ от напряжения на отражателе $U_{отр}$')
ax.set_xlabel(r'Напряжение на отражателе $U_{отр}$, В')
ax.set_ylabel(r'Длина волны $\lambda$, см')
ax.grid(True, which='both', linestyle='--', alpha=0.7)
ax.legend()

# Настройка диапазонов осей (подбираем под данные, чтобы не было пустот)
ax.set_xlim(0, 45)
ax.set_ylim(10.30, 10.70)

# Сохранение в PDF
# Убедитесь, что папка ./python/images/ существует, или измените путь
fig.savefig('./python/images/graph_task_a_lambda.pdf', bbox_inches='tight', dpi=300)
plt.close(fig)