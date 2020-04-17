import pandas as pd

#help(pd.read_html)
df = pd.read_html("https://www.espncricinfo.com/series/19304/scorecard/1187027/india-vs-australia-1st-odi-australia-tour-of-india-2019-20")

print(df[0].columns)
print(df[0]["WD"])
print(df[2])