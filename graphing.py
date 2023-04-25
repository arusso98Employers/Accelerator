import seaborn
 
 
seaborn.set(style='whitegrid')
exp = seaborn.load_dataset("exp")
 
seaborn.scatterplot(x="Number of Runs",
                    y="Execution Time",
                    data=exp)