import pandas as pd

df = pd.read_csv("donnees_top14_1.csv")

print(df.head())     
print(df.shape)      
print(df.info())      

moyennes = df.groupby("victoire")["possession"].mean()
print(moyennes)

correlation = df["possession"].corr(df["victoire"])
print (f"Corrélation possession/victoire : {correlation}")

import matplotlib.pyplot as plt

df.boxplot(column="possession", by="victoire")
plt.title("Possession selon le résultat du match")
plt.suptitle("")  # enlève le titre automatique moche que matplotlib ajoute
plt.xlabel("Victoire (0 = défaite, 1 = victoire)")
plt.ylabel("Possession")
plt.show()

moyennes_occup = df.groupby("victoire")["occupation"].mean()
print(moyennes_occup)

correlation_occup = df["occupation"].corr(df["victoire"])
print (f"Corrélation occupation/victoire : {correlation_occup}")

import matplotlib.pyplot as plt

df.boxplot(column="occupation", by="victoire")
plt.title("Occupation selon le résultat du match")
plt.suptitle("")  # enlève le titre automatique moche que matplotlib ajoute
plt.xlabel("Victoire (0 = défaite, 1 = victoire)")
plt.ylabel("Occupation")
plt.show()

import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(10, 5))

df.boxplot(column="possession", by="victoire", ax=axes[0])
axes[0].set_title("Possession selon le résultat")
axes[0].set_xlabel("Victoire (0 = défaite, 1 = victoire)")

df.boxplot(column="occupation", by="victoire", ax=axes[1])
axes[1].set_title("Occupation selon le résultat")
axes[1].set_xlabel("Victoire (0 = défaite, 1 = victoire)")

plt.suptitle("")
plt.tight_layout()
plt.show()

toulouse = df[df["equipe"] == "Stade Toulousain"].mean()
print (toulouse)
