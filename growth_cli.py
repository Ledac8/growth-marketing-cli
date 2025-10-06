import pandas as pd

def funnel_analyze(file_path):
    """
    Analyzes a user event funnel from a CSV file.
    Assumes columns are sequential steps (e.g., step_1, step_2).
    """
    df = pd.read_csv(file_path)
    # Identify funnel steps (columns starting with 'step_')
    steps = [col for col in df.columns if col.startswith('step_')]
    
    if not steps:
        print("Error: No funnel steps found in the file.")
        return

    # Calculate starting users (Total)
    total_starters = df[steps[0]].sum()
    
    funnel_data = []
    previous_count = 0
    
    for i, step in enumerate(steps):
        current_count = df[step].sum()

        if i == 0:
            step_conversion = 1.0 # 100% conversion from 'start'
            overall_conversion = 1.0
        else:
            # Step-to-step conversion
            step_conversion = current_count / previous_count if previous_count > 0 else 0
            # Overall conversion (from step 1)
            overall_conversion = current_count / total_starters if total_starters > 0 else 0
            
        funnel_data.append({
            'Step': step,
            'Users': current_count,
            'Step Conv. Rate': f"{step_conversion * 100:.2f}%",
            'Overall Conv. Rate': f"{overall_conversion * 100:.2f}%"
        })
        
        previous_count = current_count

    # Display results
    print("\n--- 📈 Funnel Analysis Results ---")
    results_df = pd.DataFrame(funnel_data)
    
    # Calculate drop-off
    results_df['Drop-off'] = results_df['Users'].diff().fillna(0).astype(int) * -1
    results_df['Drop-off'] = results_df['Drop-off'].apply(lambda x: 0 if x < 0 else x)
    
    # Format and print the final table
    print(results_df[['Step', 'Users', 'Drop-off', 'Step Conv. Rate', 'Overall Conv. Rate']].to_markdown(index=False))

# --- Run the function with the sample data ---
funnel_analyze('user_events.csv')

# growth_cli.py (This is the file your README references)
import pandas as pd
import argparse
import sys # Import sys to handle command line arguments

# --- CORE FUNNEL ANALYSIS FUNCTION ---
def funnel_analyze(file_path):
    """
    Analyzes a user event funnel from a CSV file.
    Assumes columns are sequential steps (e.g., step_1, step_2).
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1) # Exit if file not found

    # Identify funnel steps (columns starting with 'step_')
    steps = [col for col in df.columns if col.startswith('step_')]

    if not steps:
        print("Error: No funnel steps found in the file.")
        return

    # Calculate starting users (Total)
    total_starters = df[steps[0]].sum()

    funnel_data = []
    previous_count = 0

    for i, step in enumerate(steps):
        current_count = df[step].sum()

        if i == 0:
            step_conversion = 1.0 # 100% conversion from 'start'
            overall_conversion = 1.0
        else:
            # Step-to-step conversion
            step_conversion = current_count / previous_count if previous_count > 0 else 0
            # Overall conversion (from step 1)
            overall_conversion = current_count / total_starters if total_starters > 0 else 0

        funnel_data.append({
            'Step': step,
            'Users': current_count,
            'Step Conv. Rate': f"{step_conversion * 100:.2f}%",
            'Overall Conv. Rate': f"{overall_conversion * 100:.2f}%"
        })

        previous_count = current_count

    # Display results
    print("\n--- 📈 Funnel Analysis Results ---")
    results_df = pd.DataFrame(funnel_data)

    # Calculate drop-off
    # Using .diff() is simpler for the calculation
    results_df['Drop-off'] = results_df['Users'].diff().fillna(0).astype(int) * -1
    results_df['Drop-off'] = results_df['Drop-off'].apply(lambda x: 0 if x < 0 else x)

    # Format and print the final table using markdown format
    print(results_df[['Step', 'Users', 'Drop-off', 'Step Conv. Rate', 'Overall Conv. Rate']].to_markdown(index=False))

# --- CLI STRUCTURE (The 'argparse' part) ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Growth Marketing Command Line Interface (CLI)")
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Subparser for funnel-analyze
    funnel_parser = subparsers.add_parser('funnel-analyze', help='Analyze a user event funnel.')
    funnel_parser.add_argument('--file', required=True, help='Path to the user events CSV file.')

    args = parser.parse_args()

    if args.command == 'funnel-analyze':
        funnel_analyze(args.file)

    # You will add other commands (keyword-suggest, ab-test-significance) here later.