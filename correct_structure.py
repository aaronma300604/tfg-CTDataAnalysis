import os
import shutil

ORIGEN = '/home/roth/aaron/TFG/data/NSCLC-Radiomics-Version-4-Oct-2020-NBIA-manifest/NSCLC-Radiomics'
DESTINO = '/home/roth/aaron/TFG/data-corrected-st/DICOM'

for paciente in os.listdir(ORIGEN):
    paciente_origen = os.path.join(ORIGEN, paciente)
    paciente_destino = os.path.join(DESTINO, paciente)

    if not os.path.isdir(paciente_origen):
        continue

    os.makedirs(paciente_destino, exist_ok=True)

    for estudio in os.listdir(paciente_origen):
        estudio_path = os.path.join(paciente_origen, estudio)

        if not os.path.isdir(estudio_path):
            continue

        carpeta_mas_archivos = None
        carpeta_segmentation = None

        for carpeta in os.listdir(estudio_path):
            carpeta_path = os.path.join(estudio_path, carpeta)

            if not os.path.isdir(carpeta_path):
                continue

            # Cuenta SOLO archivos
            num_archivos = sum(
                1 for f in os.listdir(carpeta_path)
                if os.path.isfile(os.path.join(carpeta_path, f))
            )

            if num_archivos > 1: 
                carpeta_mas_archivos = carpeta_path


            if "segmentation" in carpeta.lower():
                carpeta_segmentation = carpeta_path

        # Copia CT
        if carpeta_mas_archivos:
            destino_nn1 = os.path.join(paciente_destino, "CT")
            if not os.path.exists(destino_nn1):
                shutil.copytree(carpeta_mas_archivos, destino_nn1)

        # Copia SEG
        if carpeta_segmentation:
            destino_nn2 = os.path.join(paciente_destino, "SEG")
            if not os.path.exists(destino_nn2):
                shutil.copytree(carpeta_segmentation, destino_nn2)
