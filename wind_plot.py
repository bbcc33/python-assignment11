import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind(return_type='pandas')

print("First 10 rows:\n", df.head(10))
print("\nLast 10 rows:\n", df.tail(10))


def clean_strength(s):
    parts = s.split('-')
    if len(parts) == 2:
        try:
            low = float(parts[0].strip())
            high = float(parts[1].strip())
            return (low + high) / 2
        except ValueError:
            return None
    try:
        return float(s.strip())
    except ValueError:
        return None

df['strength'] = df['strength'].apply(clean_strength)

df.dropna(subset=['strength', 'frequency'], inplace=True)

fig = px.scatter(
    df,
    x='strength',
    y='frequency',
    color='direction',
    title='Wind Strength vs. Frequency',
    labels={'strength': 'Wind Strength', 'frequency': 'Frequency'},
)
fig.write_html('wind.html')

print("\nInteractive plot saved as 'wind.html'")
