import numpy as np
import matplotlib.pyplot as plt

"""
Regional Nuclear Energy System (SENR)
Module: Techno-Economic Viability
Script: Levelized Cost of Energy (LCOE) Calculator
"""

def calculate_lcoe(capital_cost, om_cost, fuel_cost, energy_generated, discount_rate, plant_life):
    """
    Calculates the Levelized Cost of Energy (LCOE) over the plant's lifetime.
    Returns the final LCOE value and the breakdown of discounted costs.
    """
    # Arrays to store yearly discounted values
    years = np.arange(1, plant_life + 1)
    discount_factor = (1 + discount_rate) ** years
    
    # In a simplified model, capital cost is applied at year 0 (not discounted here for simplicity of the base model)
    # O&M and Fuel costs are annual
    discounted_om = np.sum(om_cost / discount_factor)
    discounted_fuel = np.sum(fuel_cost / discount_factor)
    discounted_energy = np.sum(energy_generated / discount_factor)
    
    total_cost = capital_cost + discounted_om + discounted_fuel
    lcoe = total_cost / discounted_energy
    
    return lcoe, capital_cost, discounted_om, discounted_fuel

if __name__ == "__main__":
    print("--- SENR: LCOE Financial Simulator ---")
    
    # Input parameters for the simulation
    try:
        # Example values for a small reactor: 
        # Capital: 1e9 ($1B), O&M: 5e7 ($50M/yr), Fuel: 1e7 ($10M/yr), Energy: 2e6 MWh/yr
        capital = float(input("Total Capital Investment ($): "))
        om_annual = float(input("Annual Operation & Maintenance Cost ($/year): "))
        fuel_annual = float(input("Annual Fuel Cost ($/year): "))
        energy_annual = float(input("Annual Energy Generation (MWh/year): "))
        rate = float(input("Discount Rate (e.g., 0.05 for 5%): "))
        life = int(input("Plant Operational Life (years): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        exit(1)
        
    # Run calculation
    final_lcoe, cap_cost, om_cost, f_cost = calculate_lcoe(capital, om_annual, fuel_annual, energy_annual, rate, life)
    
    print(f"\nResult: The LCOE for the SENR plant is ${final_lcoe:.2f} per MWh.")
    
    # Plotting a Pie Chart to show the cost breakdown (Nuclear usually has high capital, low fuel)
    labels = ['Capital Investment', 'O&M (Discounted)', 'Fuel (Discounted)']
    sizes = [cap_cost, om_cost, f_cost]
    colors = ['#1976D2', '#FFB300', '#D32F2F']
    explode = (0.05, 0, 0)  # slightly separate the capital cost slice
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140)
    plt.title('SENR - Lifetime Cost Breakdown', fontsize=14, fontweight='bold')
    
    # Save the graph
    output_filename = 'lcoe_cost_breakdown.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Graph successfully saved as '{output_filename}'. Close the plot window to exit.")
    
    plt.show()
