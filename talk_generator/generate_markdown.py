#%%
import pandas as pd
import datetime as dt

TEMPLATE = """+++
title = "{title}"
presenter = "{speaker}"
affiliation = "{affiliation}"
start_time = {time_start:%Y-%m-%dT%H:%M:%S+00:00}
end_time = {time_end:%Y-%m-%dT%H:%M:%S+00:00}
session = {session}
is_break = {is_break}
+++

{abstract}
"""

df = pd.read_csv("talks.csv", sep=";")
df["abstract"] = df["abstract"].fillna("")

def get_start_and_end_time(session, time, duration):
    if session <= 2:
        session_offset = dt.datetime(2023, 7, 3)
    else:
        session_offset = dt.datetime(2023, 7, 4)
    h, m = map(int, time.split(":"))
    start_time = session_offset + dt.timedelta(hours=h, minutes=m)
    end_time = start_time + dt.timedelta(minutes=duration)
    return start_time, end_time

for i, row in df.iterrows():
    r = row.to_dict()
    r["time_start"], r["time_end"] = get_start_and_end_time(r["session"], r["time"], r["duration"])
    del r["time"]
    fname = r["speaker"].replace(" ", "_").lower() + ".md"
    fname = fname.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
    with open(f"../content/talks/{fname}", "w") as f:
        f.write(TEMPLATE.format(**r))

# %%
