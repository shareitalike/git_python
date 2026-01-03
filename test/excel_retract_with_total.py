import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import glob

# ==========================================
# 1. SETUP: FOLDER PATH
# ==========================================
SOURCE_FOLDER = r"F:\excel_python"   # <--- YAHAN APNA PATH DALEIN
OUTPUT_FOLDER = os.path.join(SOURCE_FOLDER, "Processed_With_Totals")

if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

print(f"📂 Reading files from: {SOURCE_FOLDER}")

# ==========================================
# 2. FILE PROCESSOR
# ==========================================
def process_file(file_path):
    filename = os.path.basename(file_path)
    print(f"--------------------------------------------------")
    print(f"🔍 Processing: {filename}")

    try:
        # --- SHEET SELECTION ---
        df = None
        try:
            df = pd.read_excel(file_path, sheet_name="List of trades")
        except ValueError:
            try:
                xls = pd.ExcelFile(file_path)
                if len(xls.sheet_names) >= 4:
                    sheet_name = xls.sheet_names[3] # 4th Sheet
                    df = pd.read_excel(file_path, sheet_name=sheet_name)
                else:
                    print(f"   ❌ Skipped: Sheet not found.")
                    return None
            except: return None

        if df is None: return None

        # --- DATA CLEANING ---
        df.columns = df.columns.str.strip()

        # Columns Identity
        date_col = next((c for c in df.columns if 'Date' in c or 'Time' in c), None)
        pnl_col = next((c for c in df.columns if 'Net P&L' in c or 'Profit' in c), None)
        type_col = next((c for c in df.columns if 'Type' in c), None)

        if not date_col or not pnl_col:
            print("   ❌ Error: Required columns missing.")
            return None

        # Filter 'Exit' only
        if type_col:
            df = df[df[type_col].astype(str).str.contains('Exit', case=False, na=False)].copy()

        # Date & Month
        df[date_col] = pd.to_datetime(df[date_col])
        df['Year'] = df[date_col].dt.year
        df['Month'] = df[date_col].dt.month_name()

        months = ['January', 'February', 'March', 'April', 'May', 'June',
                  'July', 'August', 'September', 'October', 'November', 'December']
        df['Month'] = pd.Categorical(df['Month'], categories=months, ordered=True)

        # --- MATRIX CREATION ---
        # FIX: observed=False added to silence warning
        matrix = df.groupby(['Year', 'Month'], observed=False)[pnl_col].sum().reset_index()
        pivot = matrix.pivot(index='Year', columns='Month', values=pnl_col).fillna(0)

        # ADD YEARLY TOTAL
        pivot['Yearly Total'] = pivot.sum(axis=1)
        # ADD GRAND TOTAL
        pivot.loc['Grand Total'] = pivot.sum(axis=0)

        # --- SAVE OUTPUTS ---
        base_name = os.path.splitext(filename)[0]

        # Save Excel Matrix
        out_path = os.path.join(OUTPUT_FOLDER, f"{base_name}_Matrix.xlsx")
        pivot.to_excel(out_path)
        print(f"   💾 Matrix Saved: {base_name}_Matrix.xlsx")

        # Save Heatmap (Without Totals)
        plt.figure(figsize=(12, 6))
        try:
            heatmap_data = pivot.drop(index='Grand Total', columns='Yearly Total', errors='ignore')
            sns.heatmap(heatmap_data, cmap='RdYlGn', center=0, annot=True, fmt=".0f")
            plt.title(f'P&L Heatmap - {filename}')
            plt.tight_layout()
            plt.savefig(os.path.join(OUTPUT_FOLDER, f"{base_name}_Heatmap.png"))
            plt.close()
        except: pass

        # Save Graph
        df = df.sort_values(date_col)
        df['Cumulative'] = df[pnl_col].cumsum()
        plt.figure(figsize=(10, 5))
        plt.plot(df[date_col], df['Cumulative'], label='Equity', color='blue')
        plt.title(f'Wealth Graph - {filename}')
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(os.path.join(OUTPUT_FOLDER, f"{base_name}_Graph.png"))
        plt.close()

        return df[[date_col, pnl_col, 'Year', 'Month']]

    except Exception as e:
        print(f"   ❌ Error: {e}")
        return None

# ==========================================
# 3. MASTER EXECUTION
# ==========================================
all_dfs = []
files = glob.glob(os.path.join(SOURCE_FOLDER, "*.xls*"))

if files:
    for f in files:
        if not f.startswith('~'):
            res = process_file(f)
            if res is not None:
                res.columns = ['Date', 'Net P&L', 'Year', 'Month']
                all_dfs.append(res)

if all_dfs:
    print("-" * 50)
    print("🔄 Combining Master Data...")
    full_df = pd.concat(all_dfs)

    # Master Matrix with Totals
    # FIX: observed=False added here too
    full_matrix = full_df.groupby(['Year', 'Month'], observed=False)['Net P&L'].sum().reset_index()
    full_pivot = full_matrix.pivot(index='Year', columns='Month', values='Net P&L').fillna(0)

    # Add Totals for Master
    full_pivot['Yearly Total'] = full_pivot.sum(axis=1)
    full_pivot.loc['Grand Total'] = full_pivot.sum(axis=0)

    full_pivot.to_excel(os.path.join(OUTPUT_FOLDER, "MASTER_Combined_Matrix.xlsx"))

    # Master Graph
    full_df = full_df.sort_values('Date')
    full_df['Total_Cumulative'] = full_df['Net P&L'].cumsum()

    plt.figure(figsize=(12, 6))
    plt.plot(full_df['Date'], full_df['Total_Cumulative'], color='green', linewidth=2)
    plt.title('MASTER Combined Wealth Growth')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_FOLDER, "MASTER_Combined_Graph.png"))
    plt.close()

    print(f"✅ DONE! Files saved in: {OUTPUT_FOLDER}")
else:
    print("❌ No files processed.")