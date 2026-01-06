import matplotlib.pyplot as plt
import pandas as pd
import math

def plot_volume_dashboard(sheet_range, title_prefix, color):
    """
    Generalized function to create volume dashboards from Excel data.
    """
    raw_data = xl(sheet_range, headers=True)
    df = pd.DataFrame(raw_data)

    # 1. Data Cleaning
    date_series = pd.to_datetime(df.iloc[:, 0], errors='coerce')
    df_clean = df[date_series.notna()].copy()
    df_clean.iloc[:, 0] = date_series[date_series.notna()].dt.strftime('%Y-%m-%d')
    df_clean.set_index(df_clean.columns[0], inplace=True)

    # 2. Grid Setup
    tickers = [t for t in df_clean.columns if t and "Unnamed" not in str(t) and "PX_VOLUME" not in str(t)]
    num_plots = len(tickers)
    cols = 3
    rows = math.ceil(num_plots / cols)

    fig, axes = plt.subplots(rows, cols, figsize=(18, 4 * rows))
    axes = axes.flatten()

    # 3. Plotting
    for i, ticker in enumerate(tickers):
        volume_values = pd.to_numeric(df_clean[ticker], errors='coerce').fillna(0)
        axes[i].plot(df_clean.index, volume_values.values, color=color)
        axes[i].set_title(f"{title_prefix}: {ticker}", fontsize=11, fontweight='bold')
        
        axes[i].xaxis.set_major_locator(plt.MaxNLocator(5))
        axes[i].tick_params(axis='x', rotation=45, labelsize=8)
        axes[i].grid(axis='y', linestyle='--', alpha=0.3)

    # Remove empty slots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    plt.tight_layout()
    return fig

# Execute for Global X
# plot_volume_dashboard("Inputs_volume!A3:D41", "GX total volume", "#0033
