# import numpy as np
# import matplotlib.pyplot as plt

# # Parâmetros da partícula
# massa = 2.0       # kg
# forca = 10.0      # N
# tempo_total = 10  # segundos
# v0 = 0.0          # velocidade inicial (m/s)

# # Aceleração constante (segunda lei de Newton: F = m*a)
# aceleracao = forca / massa

# # Vetor de tempo
# tempos = np.linspace(0, tempo_total, 100)

# # Velocidade em função do tempo: v = v0 + a*t
# velocidades = v0 + aceleracao * tempos

# # Plotando o gráfico
# plt.style.use('seaborn-v0_8')
# plt.figure(figsize=(8, 5))
# plt.plot(tempos, velocidades, color='blue', linewidth=2)
# plt.title('Variação da Velocidade com o Tempo\n(m = 2 kg, F = 10 N, v₀ = 0)', fontsize=14)
# plt.xlabel('Tempo (s)', fontsize=12)
# plt.ylabel('Velocidade (m/s)', fontsize=12)
# plt.grid(True)
# plt.tight_layout()
# plt.show()

import numpy as np
import matplotlib
matplotlib.use('MacOSX')  # Use native MacOSX backend
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros físicos
massa = 2.0       # kg
forca = 10.0      # N
aceleracao = forca / massa
tempo_total = 10  # segundos
v0 = 0.0          # m/s
x0 = 0.0          # posição inicial

# Vetor de tempo
tempos = np.linspace(0, tempo_total, 100)
posicoes = x0 + v0 * tempos + 0.5 * aceleracao * tempos**2

# Configuração da figura
fig, ax = plt.subplots()
ax.set_xlim(0, max(posicoes) + 5)
ax.set_ylim(-1, 1)
ax.set_xlabel('Posição (m)')
ax.set_title('Movimento de uma partícula sob força constante')
particula, = ax.plot([], [], 'ro', markersize=10)

# Função de animação
def animar(i):
    particula.set_data([posicoes[i]], [0])
    return particula,

ani = animation.FuncAnimation(fig, animar, frames=len(tempos), interval=100, blit=False, repeat=True)
plt.show(block=True)
