import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

flights_df = pd.read_csv("flights.csv")

print("Колонки в flights_df:")
for col in flights_df.columns:
    print(repr(col))

airline_delays = flights_df.groupby('AIRLINE')['DEPARTURE_DELAY'].mean().sort_values(ascending=False)

print("\n=== Средняя задержка по авиакомпаниям (AIRLINE) ===")
print(airline_delays.head(10))  # Покажем Топ-10

plt.figure(figsize=(10, 5))
airline_delays.head(10).plot(kind='bar', color='skyblue')
plt.title("Топ-10 авиакомпаний по средней задержке вылета")
plt.xlabel("Код авиакомпании")
plt.ylabel("Средняя задержка (мин.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

airport_delays = flights_df.groupby('ORIGIN_AIRPORT')['DEPARTURE_DELAY'].mean().sort_values(ascending=False)

print("\n=== Средняя задержка по аэропортам (ORIGIN_AIRPORT) ===")
print(airport_delays.head(10))

plt.figure(figsize=(10, 5))
airport_delays.head(10).plot(kind='bar', color='orange')
plt.title("Топ-10 аэропортов по средней задержке вылета")
plt.xlabel("Код аэропорта вылета")
plt.ylabel("Средняя задержка (мин.)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

if 'DAY_OF_WEEK' in flights_df.columns:
    dow_delays = flights_df.groupby('DAY_OF_WEEK')['DEPARTURE_DELAY'].mean().sort_values(ascending=False)
    print("\n=== Средняя задержка по дням недели ===")
    print(dow_delays)

    plt.figure(figsize=(8, 4))
    dow_delays.plot(kind='bar', color='green')
    plt.title("Средняя задержка по дням недели")
    plt.xlabel("День недели (1=Пн, 7=Вс)")
    plt.ylabel("Средняя задержка (мин.)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
else:
    print("\n[Нет столбца 'DAY_OF_WEEK' в данных — пропускаем этот шаг.]")

if 'MONTH' in flights_df.columns:
    month_delays = flights_df.groupby('MONTH')['DEPARTURE_DELAY'].mean().sort_values(ascending=False)
    print("\n=== Средняя задержка по месяцам ===")
    print(month_delays)

    plt.figure(figsize=(8, 4))
    month_delays.plot(kind='line', marker='o')
    plt.title("Средняя задержка по месяцам")
    plt.xlabel("Месяц (1-12)")
    plt.ylabel("Средняя задержка (мин.)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
else:
    print("\n[Нет столбца 'MONTH' в данных — пропускаем этот шаг.]")

if 'SCHEDULED_DEPARTURE' in flights_df.columns:
    flights_df['SCHEDULED_DEPARTURE'] = flights_df['SCHEDULED_DEPARTURE'].fillna(0).astype(int)
    flights_df['DEP_HOUR'] = flights_df['SCHEDULED_DEPARTURE'] // 100

    hour_delays = flights_df.groupby('DEP_HOUR')['DEPARTURE_DELAY'].mean().sort_values(ascending=False)
    print("\n=== Средняя задержка по часу вылета ===")
    print(hour_delays.head(24))  # Всего 24 часа

    plt.figure(figsize=(10, 5))
    sns.lineplot(x=hour_delays.index, y=hour_delays.values, marker='o')
    plt.title("Средняя задержка в зависимости от часа вылета")
    plt.xlabel("Час вылета (0-23)")
    plt.ylabel("Средняя задержка (мин.)")
    plt.xticks(range(0, 24))
    plt.grid(True)
    plt.tight_layout()
    plt.show()

print("\n=== КРАТКИЕ ВЫВОДЫ ===")
print("2. Видим, какие авиакомпании и аэропорты имеют наибольшие задержки (см. Топ-10).")
print("3. Анализируем задержки по дням недели, месяцам, часу вылета (см. графики).")
