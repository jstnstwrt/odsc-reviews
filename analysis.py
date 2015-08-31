import sqlite3
import pandas as pd

import matplotlib as plt
import numpy as np
# matplotlib.style.use('ggplot')

con = sqlite3.connect("user_frequency.db")
df = pd.read_sql_query("select * from username_counts", con)

plt.()


con.close()