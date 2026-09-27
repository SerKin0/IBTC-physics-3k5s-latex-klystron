import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

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

# 1. Оптимальный режим (опт) Uрез = 90
u1 = [11, 12, 14, 16, 17, 20, 29, 30, 31, 32, 33, 35, 36, 37]
i1 = [0, 10, 20, 15, 5, 0, 0, 19, 27, 29, 30, 30, 28, 0]

# 2. Режим (опт + 20V) Uрез = 110 (или 38*3)
u2 = [2, 3, 4, 5, 6, 10, 11, 12, 13, 14, 15, 16, 18, 32, 34, 37]
i2 = [0, 7, 8, 8, 0, 0, 14, 26, 27, 21, 23, 22, 0, 0, 36, 28]

# 3. Режим (опт - 20V) Uрез = 70
u3 = [2, 6, 7, 10, 12, 14, 16, 18, 29, 30, 36, 39, 40]
i3 = [0, 5, 0, 0, 25, 27, 20, 0, 0, 17, 32, 17, 0]

# --- Построение графика ---
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(u1, i1, marker='o', linestyle='-', label=r'$U_{рез} = 100$')
ax.plot(u3, i3, marker='^', linestyle='-.', label=r'$U_{рез} = 120$')
ax.plot(u2, i2, marker='s', linestyle='--', label=r'$U_{рез} = 140$')

# Настройки графика
# ax.set_title(r'Зависимость тока детектора $I$ от напряжения на отражателе $U_{\text{отр}}$')s
ax.set_xlabel(r'Напряжение на отражателе $U_{отр}$, В')
ax.set_ylabel(r'Ток детектора $I$, мкА')
ax.grid(True, which='both', linestyle='--', alpha=0.7)
ax.legend()
ax.set_xticks(range(0, 45, 5))
ax.set_yticks(range(0, 40, 5))

# Сохранение в PDF
fig.savefig('./python/images/graph_task_a.pdf', bbox_inches='tight', dpi=300)
plt.close(fig)
