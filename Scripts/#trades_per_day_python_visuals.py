import matplotlib.pyplot as plt
import pandas as pd
import math
from matplotlib.ticker import FuncFormatter

def clean_trades(val):
    """Handles financial shorthand (M, K) and converts to numeric."""
    if isinstance(val, str):
        v = val.upper().replace('M', 'e6').replace('K', 'e3').replace(',', '')
        return pd.to_numeric(v, errors='coerce')
    return pd.to_numeric(val, errors='coerce')

def trade_formatter(x, pos):
    """Formats Y-axis labels for readability."""
    if x >= 1e6:
        return f'{x / 1e6:g}M'
    return f'{x:g}'

def plot_trade_frequency(sheet_range, title_prefix, chart_color, marker_style=None):
    # 1. Load Data
    raw_trades = xl(sheet_range, headers=True)
    df = pd.DataFrame(raw_trades)

    # 2. Process Dates & Index
    df.iloc[:, 0] = pd.to_datetime(df.iloc[:, 0], errors='coerce')
    df = df[df.iloc[:, 0].notna()] 
    df.set_index(df.columns[0], inplace=True)
    df.index = df.index.strftime('%Y-%m-%d')

    # 3. Filter Tickers
    tickers = [t for t in df.columns if t and "Unnamed" not in str(t) and "NUM_TRA" not in str(t)]
    rows = math.ceil(len(tickers) / 3)
    fig, axes = plt.subplots(rows, 3, figsize=(18, 5 * rows))
    axes = axes.flatten()

    # 4. Plotting Loop
    for i, ticker in enumerate(tickers):
        data = df[ticker].apply(clean_trades).fillna(0)
        axes[i].plot(df.index, data.values, color=chart_color, marker=marker_style, linewidth=2)
        axes[i].set_title(f"{title_prefix}: {ticker}", fontsize=12, fontweight='bold')
        axes[i].yaxis.set_major_formatter(FuncFormatter(trade_formatter))
        axes[i].xaxis.set_major_locator(plt.MaxNLocator(10))
        axes[i].tick_params(axis='x', rotation=45, labelsize=8)
        axes[i].grid(True, axis='y', alpha=0.3)

    # 5. Remove empty slots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    return fig

# Execute for Global X
# plot_trade_frequency("'Inputs_#trades_per_day'!A3:D41", "GX Trades", "#003366")

# Execute for BetaPro
# plot_trade_frequency("'Inputs_#trades_per_day'!A46:D84", "BetaPro Trades", "#1a73e8", marker_style='s')
