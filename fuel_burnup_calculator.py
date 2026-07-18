import numpy as np
import matplotlib.pyplot as plt

"""
Regional Nuclear Energy System (SENR)
Module: Core Neutronics & Fuel Cycle
Script: Fuel Burnup and Lifetime Calculator
"""

def calculate_burnup_curve(power_mw, mass_kg, capacity_factor, target_burnup, steps=500):
    """
    Calculates the accumulated burnup over time until the target is reached.
    """
    # Effective power taking into account plant availability
    effective_power = power_mw * capacity_factor
    
    # Calculate total days required to reach the target burnup
    total_days = (target_burnup * mass_kg) / effective_power
    total_years = total_days / 365.25
    
    # Create time arrays
    time_years = np.linspace(0, total_years, steps)
    time_days = time_years * 365.25
    
    # Calculate accumulated burnup array
    accumulated_burnup = (effective_power * time_days) / mass_kg
    
    return time_years, accumulated_burnup, total_years

if __name__ == "__main__":
    print("--- SENR: Fuel Burnup & Cycle Simulator ---")
    
    try:
        p_thermal = float(input("Reactor Thermal Power (MWt) [e.g., 200]: "))
        m_fuel = float(input("Total Initial Fuel Mass (kgU) [e.g., 15000]: "))
        target_bu = float(input("Target Maximum Burnup (MWd/kgU) [e.g., 45]: "))
        c_factor = float(input("Capacity Factor (0.0 to 1.0) [e.g., 0.92]: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        exit(1)
        
    # Generate data
    years, burnup_curve, cycle_length = calculate_burnup_curve(p_thermal, m_fuel, c_factor, target_bu)
    
    # Terminal output
    print(f"\nResult: To reach a burnup of {target_bu} MWd/kgU,")
    print(f"the SMR will operate for approximately {cycle_length:.2f} years without refueling.")
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(years, burnup_curve, label=f'Accumulated Burnup (CF = {c_factor*100:.0f}%)', color='#6A1B9A', linewidth=2.5)
    
    # Target line
    plt.axhline(y=target_bu, color='#D32F2F', linestyle='--', linewidth=1.5, label=f'Target Limit ({target_bu} MWd/kgU)')
    
    plt.title('SENR - Nuclear Fuel Burnup Over Time', fontsize=14, fontweight='bold')
    plt.xlabel('Time of Operation (Years)', fontsize=12)
    plt.ylabel('Burnup (MWd/kgU)', fontsize=12)
    
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.fill_between(years, burnup_curve, color='#6A1B9A', alpha=0.1)
    plt.legend(loc='lower right')
    
    # Save output
    output_filename = 'fuel_burnup_output.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"\nGraph successfully saved as '{output_filename}'. Close the plot window to exit.")
    
    plt.show()
