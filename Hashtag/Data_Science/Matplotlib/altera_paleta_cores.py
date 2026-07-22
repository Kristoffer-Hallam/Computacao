import matplotlib.pyplot as plt
from cycler import cycler


def altera(mapa_de_cor:str):
    # definindo o ciclo de cores
    cores = plt.get_cmap(mapa_de_cor).colors
    ciclo_cores = cycler(color=cores)
    plt.rc('axes', prop_cycle=ciclo_cores)

    return cores