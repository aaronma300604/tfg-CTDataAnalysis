import os
import shutil

ORIGEN_CT = '/home/roth/aaron/TFG/data/RIDER/CT/RIDER-Lung-CT-Original-Scans-for-Leonard-Wee-Feb-10-2020-/"RIDER Lung CT"'
ORIGEN_SEG = '/home/roth/aaron/TFG/data/RIDER/SEG/RIDER-Lung-CT-RTSTRUCTS-DICOM-SEGS-Leonard-Wee-Feb-10-2020/"RIDER Lung CT"'
DESTINO = '/home/roth/aaron/TFG/data-corrected-st/RIDER/DICOM'

for paciente in os.listdir(ORIGEN_CT):
    paciente_origen = os.path.join(ORIGEN_CT, paciente)
    paciente_destino = os.path.join(DESTINO, paciente, 'CT')

    if not os.path.isdir(paciente_origen):
        continue

    os.makedirs(paciente_destino, exist_ok=True)

    test_bool = True
    switcher = {True: 'TEST', False: 'RETEST'}
    
    for estudio in os.listdir(paciente_origen):
        estudio_path = os.path.join(paciente_origen, estudio)



        if not os.path.isdir(estudio_path):
            continue

        if len(os.listdir(estudio_path)) == 1:
            folder = os.listdir(estudio_path)[0]
            shutil.copytree(os.path.join(estudio_path, folder), os.path.join(paciente_destino, switcher[test_bool]))
            test_bool = not test_bool
        elif len(os.listdir(estudio_path)) == 2:
            folder = os.listdir(estudio_path)[0]
            shutil.copytree(os.path.join(estudio_path, folder), os.path.join(paciente_destino, 'TEST'))
            folder = os.listdir(estudio_path)[1]
            shutil.copytree(os.path.join(estudio_path, folder), os.path.join(paciente_destino, 'RETEST'))

for paciente in os.listdir(ORIGEN_SEG):
    paciente_origen = os.path.join(ORIGEN_SEG, paciente)
    paciente_destino = os.path.join(DESTINO,paciente, 'SEG')
    paciente_destino_alt = os.path.join(DESTINO, paciente, 'SEG_alt')

    if not os.path.isdir(paciente_origen):
        continue

    os.makedirs(paciente_destino, exist_ok=True)

    for estudio in os.listdir(paciente_origen):
        estudio_path = os.path.join(paciente_origen, estudio)

        if not os.path.isdir(estudio_path):
            continue

        for carpeta in os.listdir(estudio_path):
            carpeta_path = os.path.join(estudio_path, carpeta)

            if not os.path.isdir(carpeta_path):
                continue
            if "RIDER" in carpeta:
                if "RETEST" in carpeta:
                    shutil.copytree(carpeta_path, os.path.join(paciente_destino_alt, 'RETEST'))
                elif "TEST" in carpeta:
                    shutil.copytree(carpeta_path, os.path.join(paciente_destino_alt, 'TEST'))
 
            else:
                if "RETEST" in carpeta:
                    shutil.copytree(carpeta_path, os.path.join(paciente_destino, 'RETEST'))
                elif "TEST" in carpeta:
                    shutil.copytree(carpeta_path, os.path.join(paciente_destino, 'TEST'))

