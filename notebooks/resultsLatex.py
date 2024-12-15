import pandas as pd
import glob
import os

def generate_latex_table(filespec):
    # Find all directories matching the filespec
    directories = glob.glob(filespec)
    print(f"Matching directories: {directories}")  # Debugging: Show matching directories

    # Collect summary.dat files from matching directories
    summary_files = [
        os.path.join(d, "summary.dat")
        for d in directories if os.path.isfile(os.path.join(d, "summary.dat"))
    ]
    print(f"Found summary.dat files: {summary_files}")  # Debugging: Show found summary.dat files

    if not summary_files:
        raise FileNotFoundError("No summary.dat files found matching the filespec.")

    # Initialize an empty DataFrame
    all_data = pd.DataFrame()

    # Read each summary.dat file and append the data
    for summary_file in summary_files:
        data = pd.read_csv(summary_file)
        all_data = pd.concat([all_data, data])

    # Ensure example_file is a string before processing
    all_data['example_file'] = all_data['example_file'].astype(str)
    import pdb
    pdb.set_trace()
    # Extract the level from the example_file column (e.g., 'ce22.json' -> '2')
    all_data['Level'] = all_data['example_file'].str.extract(r'(\d).json')
    pdb.set_trace()
    
    # Group by model, tuning_n, and levels, and select the correct_true_fraction
    pivot_table = all_data.pivot_table(
        index=['model', 'tuning_n'], columns='Level', values='correct_true_fraction', aggfunc='first'
    )

    # Sort levels in numerical order
    numeric_levels = sorted(pivot_table.columns.astype(int).astype(str))  # Extract only numeric columns
    pivot_table = pivot_table.reindex(columns=numeric_levels)

    # Reset index for LaTeX output
    pivot_table.reset_index(inplace=True)

    # Create LaTeX table
    latex_table = pivot_table.to_latex(
        index=False,
        header=["Model", "Tuning"] + [f"L{i}" for i in numeric_levels],
        float_format="%.3f"
    )

    return latex_table


# Example usage:
filespec = "../results/gpt-4_ceVPill*N200*"  # Replace with your desired pattern


try:
    latex_code = generate_latex_table(filespec)
    print(latex_code)
except Exception as e:
    print(f"Error: {e}")
    
