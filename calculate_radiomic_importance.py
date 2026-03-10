from ast import arg

import pandas as pd
import pingouin as pg


def ordenar_por_importancia(radiomicas_csv,objetivos_csv, caracteristicas_a_evaluar, objetivo):
    df = pd.read_csv(radiomicas_csv)
    df_objetivos = pd.read_csv(objetivos_csv)
    df_objetivos.rename(columns={'PatientID': 'Patient'}, inplace=True)
    df = df.merge(df_objetivos, on='Patient')
    columnas = ['Patient'] + caracteristicas_a_evaluar + [objetivo]
    df_filtrado = df[columnas]
    res = {}
    for caracteristica in caracteristicas_a_evaluar:
        lm = pg.mediation_analysis(data=df_filtrado, x='Patient', m=caracteristica, y=objetivo)
        efecto_indirecto = lm.loc[lm['path'] == 'Indirect', 'coef'].values[0]
        res[caracteristica] = efecto_indirecto
    return pd.DataFrame.from_dict(dict(sorted(res.items(), key=lambda item: item[1], reverse=True)))

def main():
    arg.add_argument('--rad_csv', type=str, required=True, help='Path to the radiomic features CSV file')
    arg.add_argument('--obj_csv', type=str, required=True, help='Path to the objectives CSV file')
    arg.add_argument('--feats', nargs='+', required=True, help='List of radiomic features to evaluate')
    arg.add_argument('--obj', type=str, required=True, help='The target variable to evaluate the importance against')
    arg.parse_args()