import pandas as pd

def countMonths(months):
    month_list = [int(x[:x.find("/")]) for i in months for x in i]
    total = len(month_list)
    degree_dict = {}
    for month in range(1, 13):
        degree_dict[str(month)] = [month_list.count(month), round(month_list.count(month) / total * 100, 1)]
    return degree_dict

def findCommonMonths(d):
    common_months = []
    while len(common_months) < 3:
        max_val = [0, 0]
        max_key = ""
        for key, val in d.items():
            if val[0] > max_val[0]:
                max_val = val
                max_key = key
        common_months.append((max_key, max_val[1]))
        del d[max_key]
    return common_months

def main():
    months = pd.read_csv("astronauts.csv", skipinitialspace=True, usecols=["Birth Date"]).values.tolist()
    month_counts = countMonths(months)
    common_months = findCommonMonths(month_counts)
    for i, month in enumerate(common_months):
        print(f"{i+1}. leggyakoribb honapok: {month[0]}, {month[1]}%-os esellyel")

main()