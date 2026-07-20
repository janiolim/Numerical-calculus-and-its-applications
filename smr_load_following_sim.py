import numpy as np
import matplotlib.pyplot as plt

"""
Regional Nuclear Energy System (SENR)
Module: Grid Integration & Operations
Script: Daily Load Following Simulator for SMRs
"""

def generate_daily_demand(max_power, min_power_pct, steps=240):
    """
    Simulates a 24-hour power demand curve with morning and evening peaks.
    Uses Gaussian distributions to model the peaks over a baseline load.
    """
    time_hours = np.linspace(0, 24, steps)
    
    # Calculate absolute baseline and variable margin
    base_power = max_power * (min_power_pct / 100)
    variable_margin = max_power - base_power
    
    # Morning peak around 08:00
    peak_morning = np.exp(-0.5 * ((time_hours - 8) / 2.0)**2)
    
    # Evening peak around 19:00 (usually higher demand)
    peak_evening = np.exp(-0.5 * ((time_hours - 19) / 2.5)**2)
    
    # Combine peaks (weights: 40% morning, 80% evening to scale within margin)
    demand = base_power + variable_margin * (0.45 * peak_morning + 0.85 * peak_evening)
    
    # Ensure it doesn't exceed 100% max power just in case
    demand = np.clip(demand, base_power, max_power)
    
    return time_hours, demand

if __name__ == "__main__":
    print("--- SENR: SMR Load Following Simulator ---")
    
    try:
        p_max = float(input("SMR Maximum Electrical Power (MWe) [e.g., 60]: "))
        p_min_pct = float(input("Minimum Operational Power Level (%) [e.g., 40]: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        exit(1)
        
    # Generate the 24h operational data
    hours, smr_output = generate_daily_demand(p_max, p_min_pct)
    
    # Plotting the load following curve
    plt.figure(figsize=(12, 6))
    
    # Plot the power output line
    plt.plot(hours, smr_output, label='SMR Power Output', color='#F57C00', linewidth=3)
    
    # Add a baseline reference
    plt.axhline(y=p_max * (p_min_pct / 100), color='#757575', linestyle='--', linewidth=1.5, label='Minimum Base Load')
    plt.axhline(y=p_max, color='#D32F2F', linestyle=':', linewidth=1.5, label='Maximum Rated Capacity')
    
    plt.title('SENR - 24-Hour Load Following (Flexible SMR Operation)', fontsize=14, fontweight='bold')
    plt.xlabel('Time of Day (Hours)', fontsize=12)
    plt.ylabel('Electrical Power (MWe)', fontsize=12)
    
    # Configure X-axis to show specific hours nicely
    plt.xticks(np.arange(0, 25, 2), [f"{h:02d}:00" for h in range(0, 25, 2)])
    
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Fill the area under the curve to represent total energy generated (MWh)
    plt.fill_between(hours, smr_output, color='#F57C00', alpha=0.15)
    
    plt.legend(loc='upper left')
    
    # Save output
    output_filename = 'load_following_profile.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"\nGraph successfully saved as '{output_filename}'. Close the plot window to exit.")
    
    plt.show()
