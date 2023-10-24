import pandas as pd

from ydata_profiling import ProfileReport

df = pd.read_csv("StudentsPerformance.csv")

profile = ProfileReport(df, minimal=True)

profile.to_notebook_iframe()

profile.to_file("output_report.html")
