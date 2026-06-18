print("Quantidade de registros:", len(base_final))
print("Quantidade de fundos:", base_final[coluna_cnpj_fundos].nunique())

base_final[
    [
        'DENOM_SOCIAL',
        'VL_PATRIM_LIQ',
        'NR_COTST'
    ]
].head()


import matplotlib.pyplot as plt

plt.figure(figsize=(12,6))

plt.hist(
    base_final['VL_PATRIM_LIQ'],
    bins=50
)

plt.title(
    'Distribuição do Patrimônio Líquido dos Fundos'
)

plt.xlabel(
    'Patrimônio Líquido'
)

plt.ylabel(
    'Quantidade de Fundos'
)

plt.show()



plt.figure(figsize=(12,6))

plt.scatter(
    base_final['NR_COTST'],
    base_final['VL_PATRIM_LIQ'],
    alpha=0.4
)

plt.title(
    'Número de Cotistas x Patrimônio Líquido'
)

plt.xlabel(
    'Número de Cotistas'
)

plt.ylabel(
    'Patrimônio Líquido'
)

plt.show()


top15 = (
    base_final
    .sort_values(
        'VL_PATRIM_LIQ',
        ascending=False
    )
    .head(15)
    .copy()
)

# Converter para texto e tratar valores nulos
top15['DENOM_SOCIAL'] = (
    top15['DENOM_SOCIAL']
    .fillna('Sem nome')
    .astype(str)
)

plt.figure(figsize=(12,8))

plt.barh(
    top15['DENOM_SOCIAL'],
    top15['VL_PATRIM_LIQ']
)

plt.title(
    'Top 15 Fundos por Patrimônio Líquido'
)

plt.xlabel(
    'Patrimônio Líquido (R$)'
)

plt.tight_layout()

plt.show()



plt.figure(figsize=(10,6))

plt.boxplot(
    base_final['VL_PATRIM_LIQ']
)

plt.title(
    'Distribuição do Patrimônio Líquido'
)

plt.ylabel(
    'Patrimônio Líquido'
)

plt.show()