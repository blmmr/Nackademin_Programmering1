#övning 10_2
import pandas as pd

df = pd.read_csv("/Users/s/nackademin/programming_1/numbers.csv")

#print(df.to_string()) 
#print(pd.options.display.max_rows) hur många linjer är på skärmen
count_of_0 = df.iloc[:, 0].value_counts().get(0, 0)
count_of_1 = df.iloc[:, 0].value_counts().get(1, 0)
count_of_2 = df.iloc[:, 0].value_counts().get(2, 0)
count_of_3 = df.iloc[:, 0].value_counts().get(3, 0)
count_of_4 = df.iloc[:, 0].value_counts().get(4, 0)
count_of_5 = df.iloc[:, 0].value_counts().get(5, 0)
count_of_6 = df.iloc[:, 0].value_counts().get(6, 0)
count_of_7 = df.iloc[:, 0].value_counts().get(7, 0)
count_of_8 = df.iloc[:, 0].value_counts().get(8, 0)
count_of_9 = df.iloc[:, 0].value_counts().get(9, 0)

print("---------------")
print("- NUMANALYZER -")
print("---------------")
print(f"| 0 | {count_of_0}")
print(f"| 1 | {count_of_1}")
print(f"| 2 | {count_of_2}")
print(f"| 3 | {count_of_3}")
print(f"| 4 | {count_of_4}")
print(f"| 5 | {count_of_5}")
print(f"| 6 | {count_of_6}")
print(f"| 7 | {count_of_7}")
print(f"| 8 | {count_of_8}")
print(f"| 9 | {count_of_9}")
print("---------------")
