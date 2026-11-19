import numpy as np
from data import allenamenti



# allenamenti filtrati
def calcolo_durata_calorie(allenamenti):
    durata = allenamenti[:, 0]
    calorie = allenamenti[:, 2]
    filtrati = allenamenti[(durata > 45) & (calorie > 70)]
    return filtrati



# media delle metriche
def somma_media_metriche(allenamenti):
    return np.mean(allenamenti, axis=0)

def differenza_prestazioni(allenamenti):
    primo_allenamento = allenamenti[0, :]
    ultimo_allenamento = allenamenti[-1, :]
    return ultimo_allenamento - primo_allenamento


def stampa_report(allenamenti):

    medie = somma_media_metriche(allenamenti)

    max_calorie_index = np.argmax(allenamenti[:, 2])
    max_fc_index = np.argmax(allenamenti[:, 3])

    filtrati = calcolo_durata_calorie(allenamenti)

    differenze = differenza_prestazioni(allenamenti)

    print("\n" + "=" * 45)
    print("     REPORT ALLENAMENTI:")
    print("=" * 45)

    print("\n--- MEDIE ---")
    print(f"Durata: {medie[0]:.2f}")
    print(f"Distanza: {medie[1]:.1f}")
    print(f"Calorie: {medie[2]:.1f}")
    print(f"Frequenza Cardiaca: {medie[3]:.1f}")

    print("\n--- MIGLIORI RISULTATI ---")
    print(f"Massimo consumo calorico: {max_calorie_index + 1}")
    print(f"Calorie: {allenamenti[max_calorie_index, 2]}")

    print(f"\nFrequenza cardiaca massima: Allenamento {max_fc_index + 1}")
    print(f"BPM: {allenamenti[max_fc_index, 3]}")

    print("\n--- ALLENAMENTI FILTRATI ---")

    if filtrati.size > 0:
        for allenamento in filtrati:
            print(allenamento)
    else:
        print("Nessun allenamento trovato.")

    print("\n--- DIFFERENZA PRESTAZIONI ---")
    print(differenze)

    print("=" * 45)
