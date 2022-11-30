import csv

lista = []

with open("dados.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        custo = row["Cost"]
        custo = str(custo)
        custo = custo.replace(".", ",")
        row["Cost"] = custo
        lista.append(row)

with open("dados.csv", "w", newline="") as csvfile:
    fieldnames = ["Date", "SKU", "Product", "Cost", "Clicks", "Impressions"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in lista:
        writer.writerow(row)
