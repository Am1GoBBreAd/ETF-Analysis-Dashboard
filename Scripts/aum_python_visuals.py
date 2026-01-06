import matplotlib.pyplot as plt
import pandas as pd
import math
from matplotlib.ticker import FuncFormatter

# Note: In a local environment, replace xl() with pd.read_excel()
raw_data = xl("Inputs_aum!A4:D17", headers=True)
df = pd.DataFrame(raw_data)

def clean_aum(val):
    """Converts financial strings (1M, 1B) to numeric values."""
    if isinstance(val, (int, float)): return val
    if isinstance(val, str):
        v = val.upper().replace('M', 'e6').replace('B', 'e9').replace('$', '').replace(',', '')
        return pd.to_numeric(v, errors='coerce')
    return pd.to_numeric(val, errors='coerce')

# Date Formatting
df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], errors='coerce')
df = df[df.iloc[:, 0].notna()] 
df.set_index(df.columns[0], inplace=True)
df.index = df.index.strftime('%Y-%m')

def millions_formatter(x, pos):
    return f'{x / 1e6:g}M'

# Dynamic Grid Logic
tickers = [t for t in df.columns if t and "Unnamed" not in str(t) and "Equity" in str(t)]
rows = math.ceil(len(tickers) / 3)
fig, axes = plt.subplots(rows, 3, figsize=(18, 5 * rows))
axes = axes.flatten()

for i, ticker in enumerate(tickers):
    data = df[ticker].apply(clean_aum).fillna(0)
    chart_color = '#003366' # Global X Brand Blue
    
    axes[i].plot(df.index, data.values, color=chart_color, marker='o', linewidth=2)
    axes[i].set_title(f"GX AUM Trend: {ticker}", fontsize=12, fontweight='bold')
    axes[i].yaxis.set_major_formatter(FuncFormatter(millions_formatter))
    axes[i].tick_params(axis='x', rotation=45, labelsize=8)
    axes[i].grid(True, axis='y', alpha=0.3)

# Cleanup: Delete unused subplot slots
for j in range(i + 1, len(axes)): 
    fig.delaxes(axes[j])

plt.tight_layout()
fig
