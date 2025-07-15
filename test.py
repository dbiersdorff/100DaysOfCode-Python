from prettytable import PrettyTable, from_csv
table = PrettyTable()

table.field_names = ["name", "age"]
table.add_row(["Dawson", 24])
table.add_row(["Bailee", 25])

print(table)
