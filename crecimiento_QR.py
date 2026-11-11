import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("detalles_pagos2.csv",sep = ";")
df.columns=df.columns.str.strip()
df["Serie"] =df["Serie"].str.strip()
df["Mes"] = pd.to_datetime(df["Mes"],format="%Y-%m-%d")

print ("Base de datos leída")
print ("\n",df.shape)
print(df.head())
print(df.dtypes)

es_qr = df["Serie"].isin(["Niubiz QR","Izipay QR"])
qr = df[es_qr]

resumen_qr=qr.groupby("Mes",as_index=False)[["Operaciones","S/"]].sum()
print(resumen_qr.tail())

resumen_qr["Monto promedio por pago"] = resumen_qr["S/"]/resumen_qr["Operaciones"]

print (resumen_qr.head())

x = resumen_qr["Mes"]
y = resumen_qr["Operaciones"]

plt.plot(x, y)

plt.title("Pagos QR mensuales de Niubiz e Izipay")
plt.xlabel("Meses")
plt.ylabel("Millones de operaciones")
plt.savefig("pagos_qr_mensuales.png", dpi=200, bbox_inches="tight")


plt.show()

