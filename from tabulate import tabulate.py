from tabulate import tabulate
title  = ["Name","Age","Department"]
data = [["Ravi",25,"HR"],["haran",28,"sales"]]

print(tabulate(data,headers = title,tablefmt="plain"))


