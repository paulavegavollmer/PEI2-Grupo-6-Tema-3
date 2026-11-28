# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider

# # 1. Definición de la función de integración por trapecio
# def trapezoid_integral(y, x):
#     dx = x[1] - x[0]
#     return dx * (0.5 * (y[0] + y[-1]) + np.sum(y[1:-1]))

# # 2. Configuración inicial de los datos
# t_vuelo = np.linspace(0, 60, 1200)

# # Parámetros iniciales del cohete
# V_MAX_INIT = 800
# EXP_INIT = -0.02

# def calcular_v_vuelo(v_max, exp_coef):
#     return v_max * np.sin(np.pi * t_vuelo / 60) * np.exp(exp_coef * t_vuelo)

# v_vuelo = calcular_v_vuelo(V_MAX_INIT, EXP_INIT)
# altitud = trapezoid_integral(v_vuelo, t_vuelo)

# # 3. Configuración de la gráfica y la interfaz
# fig, ax = plt.subplots(figsize=(8, 6))
# plt.subplots_adjust(bottom=0.25)  # Espacio para los sliders en la parte inferior

# # Graficar la curva y rellenar el área bajo la curva (la integral)
# linea, = ax.plot(t_vuelo, v_vuelo, 'b-', label='Velocidad (v_vuelo)')
# area_sombreada = ax.fill_between(t_vuelo, v_vuelo, color='skyblue', alpha=0.4, label='Altitud (Integral)')

# # Configuración de los ejes y el título dinámico
# ax.set_xlabel('Tiempo (s)')
# ax.set_ylabel('Velocidad (m/s)')
# titulo = ax.set_title(f'Perfil de Velocidad y Altitud Apogeo: {altitud:.2f} m')
# ax.grid(True)
# ax.legend(loc='upper right')

# # 4. Creación de los Sliders interactivos
# ax_v_max = plt.axes([0.15, 0.1, 0.65, 0.03])    # [izquierda, abajo, ancho, alto]
# ax_exp = plt.axes([0.15, 0.05, 0.65, 0.03])

# slider_v_max = Slider(ax_v_max, 'V Max', 100.0, 1500.0, valinit=V_MAX_INIT, valfmt='%1.0f m/s')
# slider_exp = Slider(ax_exp, 'Amortig. (exp)', -0.1, 0.0, valinit=EXP_INIT, valfmt='%1.3f')

# # 5. Función de actualización cuando cambia un slider
# def actualizar(val):
#     # Obtener valores actuales de los sliders
#     v_max_actual = slider_v_max.val
#     exp_actual = slider_exp.val
    
#     # Recalcular velocidad e integral
#     v_vuelo_nuevo = calcular_v_vuelo(v_max_actual, exp_actual)
#     altitud_nueva = trapezoid_integral(v_vuelo_nuevo, t_vuelo)
    
#     # Actualizar la línea y el área rellena de la gráfica
#     linea.set_ydata(v_vuelo_nuevo)
    
#     global area_sombreada
#     area_sombreada.remove()  # Elimina el sombreado anterior para evitar superposiciones
#     area_sombreada = ax.fill_between(t_vuelo, v_vuelo_nuevo, color='skyblue', alpha=0.4)
    
#     # Actualizar título y límites del eje Y de forma dinámica
#     titulo.set_text(f'Perfil de Velocidad y Altitud Apogeo: {altitud_nueva:.2f} m')
#     ax.set_ylim(0, max(v_vuelo_nuevo) * 1.1)
    
#     fig.canvas.draw_idle()  # Redibuja la gráfica eficientemente

# # Vincular los sliders a la función de actualización
# slider_v_max.on_changed(actualizar)
# slider_exp.on_changed(actualizar)

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider

# # 1. Función de integración por trapecio
# def trapezoid_integral(y, x):
#     dx = x[1] - x[0]
#     return dx * (0.5 * (y[0] + y[-1]) + np.sum(y[1:-1]))

# # 2. Configuración de datos iniciales
# t_vuelo = np.linspace(0, 60, 1200)
# V_MAX = 800
# EXP_INIT = -0.02

# # Función para generar el perfil de velocidad
# def calcular_v_vuelo(exp_coef):
#     return V_MAX * np.sin(np.pi * t_vuelo / 60) * np.exp(exp_coef * t_vuelo)

# v_vuelo = calcular_v_vuelo(EXP_INIT)
# altitud = trapezoid_integral(v_vuelo, t_vuelo)

# # 3. Interfaz de la gráfica
# fig, ax = plt.subplots(figsize=(8, 5.5))
# plt.subplots_adjust(bottom=0.2)  # Espacio inferior para el único slider

# linea, = ax.plot(t_vuelo, v_vuelo, 'b-', label='Velocidad (v_vuelo)')
# area_sombreada = ax.fill_between(t_vuelo, v_vuelo, color='skyblue', alpha=0.4, label='Altitud (Integral)')

# ax.set_xlabel('Tiempo (s)')
# ax.set_ylabel('Velocidad (m/s)')
# titulo = ax.set_title(f'Perfil de Velocidad y Altitud Apogeo: {altitud:.2f} m')
# ax.grid(True)
# ax.set_ylim(0, 900)

# # 4. Creación de un ÚNICO Slider
# ax_slider = plt.axes([0.15, 0.05, 0.65, 0.03])  # Posición en pantalla
# slider_exp = Slider(ax_slider, 'Amortiguación', -0.1, 0.0, valinit=EXP_INIT, valfmt='%1.3f')

# # 5. Función que actualiza la gráfica al mover el slider
# def actualizar(val):
#     exp_actual = slider_exp.val
    
#     # Recalcular datos
#     v_vuelo_nuevo = calcular_v_vuelo(exp_actual)
#     altitud_nueva = trapezoid_integral(v_vuelo_nuevo, t_vuelo)
    
#     # Modificar la curva existente
#     linea.set_ydata(v_vuelo_nuevo)
    
#     # Reemplazar el sombreado del área
#     global area_sombreada
#     area_sombreada.remove()
#     area_sombreada = ax.fill_between(t_vuelo, v_vuelo_nuevo, color='skyblue', alpha=0.4)
    
#     # Actualizar texto del título
#     titulo.set_text(f'Perfil de Velocidad y Altitud Apogeo: {altitud_nueva:.2f} m')
    
#     fig.canvas.draw_idle()

# # Conectar el slider con la función
# slider_exp.on_changed(actualizar)

# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import Slider

# # 1. Tu función de integración trapezoidal
# def trapezoid_integral(y, x):
#     dx = x[1] - x[0]
#     return dx * (0.5 * (y[0] + y[-1]) + np.sum(y[1:-1]))

# # 2. Datos estrictos del intervalo solicitado (0 a 60 segundos)
# t_vuelo = np.linspace(0, 60, 1200)
# V_MAX = 800
# EXP_INIT = -0.02

# def calcular_v_vuelo(exp_coef):
#     return V_MAX * np.sin(np.pi * t_vuelo / 60) * np.exp(exp_coef * t_vuelo)

# v_vuelo = calcular_v_vuelo(EXP_INIT)
# altitud = trapezoid_integral(v_vuelo, t_vuelo)

# # 3. Inicialización del gráfico dentro del intervalo fijo
# fig, ax = plt.subplots(figsize=(8, 5.5))
# plt.subplots_adjust(bottom=0.2)

# linea, = ax.plot(t_vuelo, v_vuelo, 'b-', label='Velocidad (v_vuelo)')
# area_sombreada = ax.fill_between(t_vuelo, v_vuelo, color='skyblue', alpha=0.4, label='Altitud (Integral)')

# ax.set_xlabel('Tiempo (s)')
# ax.set_ylabel('Velocidad (m/s)')
# titulo = ax.set_title(f'Perfil de Velocidad y Altitud Apogeo: {altitud:.2f} m')
# ax.grid(True)

# # Límites del eje X estricto de tu intervalo
# ax.set_xlim(0, 60)
# # Límite del eje Y adaptado al valor inicial
# ax.set_ylim(0, max(v_vuelo) * 1.1)

# # 4. Un solo slider para la amortiguación exponencial
# ax_slider = plt.axes([0.15, 0.05, 0.65, 0.03])
# slider_exp = Slider(ax_slider, 'Amortiguación', -0.1, 0.0, valinit=EXP_INIT, valfmt='%1.3f')

# # 5. Función de actualización interactiva
# def actualizar(val):
#     exp_actual = slider_exp.val
    
#     # Recalcular velocidad e integral sobre el intervalo fijo (0-60)
#     v_vuelo_nuevo = calcular_v_vuelo(exp_actual)
#     altitud_nueva = trapezoid_integral(v_vuelo_nuevo, t_vuelo)
    
#     # Actualizar trazado y relleno
#     linea.set_ydata(v_vuelo_nuevo)
    
#     global area_sombreada
#     area_sombreada.remove()
#     area_sombreada = ax.fill_between(t_vuelo, v_vuelo_nuevo, color='skyblue', alpha=0.4)
    
#     # Actualizar textos
#     titulo.set_text(f'Perfil de Velocidad y Altitud Apogeo: {altitud_nueva:.2f} m')
    
#     # Corregir la altura del eje Y para evitar que la curva se corte al cambiar la amortiguación
#     ax.set_ylim(0, max(v_vuelo_nuevo) * 1.1)
    
#     fig.canvas.draw_idle()

# slider_exp.on_changed(actualizar)
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 1. Tu función de integración trapezoidal
def trapezoid_integral(y, x):
    if len(x) < 2:
        return 0.0
    dx = x[1] - x[0]
    return dx * (0.5 * (y[0] + y[-1]) + np.sum(y[1:-1]))

# 2. Datos base del perfil completo (0 a 60 segundos con 1200 puntos)
t_completo = np.linspace(0, 60, 1200)
v_completo = 800 * np.sin(np.pi * t_completo / 60) * np.exp(-0.02 * t_completo)

# Estado inicial del slider (empezamos mostrando el intervalo completo a 60s)
T_INIT = 60.0

# Filtrar datos para el intervalo inicial
indices_iniciales = t_completo <= T_INIT
t_vuelo = t_completo[indices_iniciales]
v_vuelo = v_completo[indices_iniciales]
altitud = trapezoid_integral(v_vuelo, t_vuelo)

# 3. Inicialización del gráfico fijo de fondo
fig, ax = plt.subplots(figsize=(8, 5.5))
plt.subplots_adjust(bottom=0.2)

# Dibujamos una línea tenue de fondo para ver la trayectoria completa del cohete
ax.plot(t_completo, v_completo, color='gray', linestyle='--', alpha=0.5, label='Trayectoria total')

# Líneas dinámicas que cambiarán con el slider
linea, = ax.plot(t_vuelo, v_vuelo, 'b-', linewidth=2, label='Velocidad actual')
area_sombreada = ax.fill_between(t_vuelo, v_vuelo, color='skyblue', alpha=0.4, label='Altitud (Área)')

# Configuración estética fija de los ejes
ax.set_xlabel('Tiempo (s)')
ax.set_ylabel('Velocidad (m/s)')
titulo = ax.set_title(f'Tiempo: {T_INIT:.1f}s | Altitud Apogeo: {altitud:.2f} m')
ax.grid(True)
ax.set_xlim(0, 60)
ax.set_ylim(0, max(v_completo) * 1.1)
ax.legend(loc='upper right')

# 4. Creación del Slider para controlar el TIEMPO de corte
ax_slider = plt.axes([0.15, 0.05, 0.65, 0.03])
slider_tiempo = Slider(ax_slider, 'Tiempo (s)', 0.1, 60.0, valinit=T_INIT, valfmt='%1.1f s')

# 5. Función de actualización interactiva
def actualizar(val):
    t_limite = slider_tiempo.val
    
    # Filtrar el arreglo original en el nuevo intervalo dinámico [0, t_limite]
    indices = t_completo <= t_limite
    t_vuelo_nuevo = t_completo[indices]
    v_vuelo_nuevo = v_completo[indices]
    
    # Calcular la integral exacta hasta ese segundo con tu método
    altitud_nueva = trapezoid_integral(v_vuelo_nuevo, t_vuelo_nuevo)
    
    # Actualizar la gráfica en tiempo real
    linea.set_data(t_vuelo_nuevo, v_vuelo_nuevo)
    
    global area_sombreada
    area_sombreada.remove()
    area_sombreada = ax.fill_between(t_vuelo_nuevo, v_vuelo_nuevo, color='skyblue', alpha=0.4)
    
    # Actualizar los datos del título
    titulo.set_text(f'Tiempo: {t_limite:.1f}s | Altitud Apogeo: {altitud_nueva:.2f} m')
    
    fig.canvas.draw_idle()

slider_tiempo.on_changed(actualizar)
plt.show()
