import numpy as np
import pandas as pd
from scipy.stats import entropy


# До обработки
df = pd.read_csv("lag_data.csv", delimiter=";")

# Доля пропущенных значений в каждом столбце
missing_rate = df.isnull().mean()
# Доля заполненных значений
completeness = 1 - missing_rate

print("Доля пропущенных значений:\n", missing_rate)
print("\nДоля заполненных значений:\n", completeness)


duplicate_rate = df.duplicated().mean()
# Доля уникальных строк
uniqueness = 1 - duplicate_rate

print("\nДоля дубликатов:", duplicate_rate)
print("Доля уникальных строк:", uniqueness)


# Проверим корректность объема растворителя
invalid_amount_count = df["liq_amount_mL"][df["liq_amount_mL"] > 5].count()
invalid_amount_rate = invalid_amount_count / len(df)

print("\nНекорректные значения объема:", invalid_amount_count)
print("Доля некорректных значений объема:", invalid_amount_rate)


class_distribution = df["API"].value_counts(normalize=True)
class_imbalance_ratio = class_distribution.min() / class_distribution.max()

print("\nРаспределение классов:\n", class_distribution)
print("Коэффициент дисбаланса классов:", class_imbalance_ratio)


# Энтропия для категориального столбца "class"
class_probs = df["API"].value_counts(normalize=True)
class_entropy = entropy(class_probs, base=2)

print("\nЭнтропия классов:", class_entropy)


# После обработки

df = pd.read_csv("lag_data_new.csv")

# Доля пропущенных значений в каждом столбце
missing_rate = df.isnull().mean()
# Доля заполненных значений
completeness = 1 - missing_rate

print("Доля пропущенных значений:\n", missing_rate)
print("\nДоля заполненных значений:\n", completeness)


duplicate_rate = df.duplicated().mean()
# Доля уникальных строк
uniqueness = 1 - duplicate_rate

print("\nДоля дубликатов:", duplicate_rate)
print("Доля уникальных строк:", uniqueness)


# Проверим корректность объема растворителя
invalid_amount_count = df["liq_amount_mL"][df["liq_amount_mL"] > 5].count()
invalid_amount_rate = invalid_amount_count / len(df)

print("\nНекорректные значения объема:", invalid_amount_count)
print("Доля некорректных значений объема:", invalid_amount_rate)


class_distribution = df["API"].value_counts(normalize=True)
class_imbalance_ratio = class_distribution.min() / class_distribution.max()

print("\nРаспределение классов:\n", class_distribution)
print("Коэффициент дисбаланса классов:", class_imbalance_ratio)


# Энтропия для категориального столбца "class"
class_probs = df["API"].value_counts(normalize=True)
class_entropy = entropy(class_probs, base=2)

print("\nЭнтропия классов:", class_entropy)
