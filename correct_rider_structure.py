import os
import shutil

ORIGEN_CT = '/home/roth/aaron/TFG/data/RIDER/CT/RIDER-Lung-CT-Original-Scans-for-Leonard-Wee-Feb-10-2020-/"RIDER Lung CT"'
ORIGEN_SEG = '/home/roth/aaron/TFG/data/RIDER/SEG/RIDER-Lung-CT-RTSTRUCTS-DICOM-SEGS-Leonard-Wee-Feb-10-2020/"RIDER Lung CT"'
DESTINO = '/home/roth/aaron/TFG/data-corrected-st/RIDER/DICOM'

for paciente in os.listdir(ORIGEN_CT):
    paciente_origen = os.path.join(ORIGEN_CT, paciente)

    if not os.path.isdir(paciente_origen):
        continue

    test_bool = True
    switcher = {True: 'TEST', False: 'RETEST'}
    
    for estudio in os.listdir(paciente_origen):
        estudio_path = os.path.join(paciente_origen, estudio)



        if not os.path.isdir(estudio_path):
            continue

        if len(os.listdir(estudio_path)) == 1:
            folder = os.listdir(estudio_path)[0]
            paciente_destino = os.path.join(DESTINO, switcher[test_bool], paciente, 'CT')
            shutil.copytree(os.path.join(estudio_path, folder), paciente_destino)
            test_bool = not test_bool
        elif len(os.listdir(estudio_path)) == 2:
            folder = os.listdir(estudio_path)[0]
            paciente_destino = os.path.join(DESTINO, 'TEST', paciente, 'CT')
            shutil.copytree(os.path.join(estudio_path, folder), paciente_destino)
            folder = os.listdir(estudio_path)[1]
            paciente_destino = os.path.join(DESTINO, 'RETEST', paciente, 'CT')
            shutil.copytree(os.path.join(estudio_path, folder), paciente_destino)

for paciente in os.listdir(ORIGEN_SEG):
    paciente_origen = os.path.join(ORIGEN_SEG, paciente)

    if not os.path.isdir(paciente_origen):
        continue

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
                    paciente_destino_alt = os.path.join(DESTINO, 'RETEST', paciente, 'SEG_alt')
                    shutil.copytree(carpeta_path, paciente_destino_alt)
                elif "TEST" in carpeta:
                    paciente_destino_alt = os.path.join(DESTINO, 'TEST', paciente, 'SEG_alt')
                    shutil.copytree(carpeta_path, paciente_destino_alt)
 
            else:
                if "RETEST" in carpeta:
                    paciente_destino = os.path.join(DESTINO, 'RETEST', paciente, 'SEG')
                    shutil.copytree(carpeta_path, paciente_destino)
                elif "TEST" in carpeta:
                    paciente_destino = os.path.join(DESTINO, 'TEST', paciente, 'SEG')
                    shutil.copytree(carpeta_path, paciente_destino)

