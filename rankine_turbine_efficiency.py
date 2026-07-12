import numpy as np
import matplotlib.pyplot as plt

"""
Regional Nuclear Energy System (SENR)
Module: Power Conversion & Thermodynamics
Script: Rankine Cycle Turbine Efficiency Simulator
"""

def calculate_efficiency(t_cold_c, t_hot_min_c, t_hot_max_c, plant_factor, steps=200):
    """
    Calculates the Ideal (Carnot) and Real (Rankine estimation) thermal efficiencies.
    Temperatures are internally converted from Celsius to Kelvin.
    """
    # Convert temperatures to Kelvin
    t_cold_k = t_cold_c + 273.15
    t_hot_min_k = t_hot_min_c + 273.15
    t_hot_max_k = t_hot_max_c + 273.15
    
    # Create an array of turbine inlet temperatures
    t_hot_array_k = np.linspace(t_hot_min_k, t_hot_max_k, steps)
    t_hot_array_c = t_hot_array_k - 273.15 # For plotting in Celsius
    
    # Calculate efficiencies (in percentage)
    carnot_efficiency = (1 - (t_cold_k / t_hot_array_k)) * 100
    rankine_efficiency = carnot_efficiency * plant_factor
    
    return t_hot_array_c, carnot_efficiency, rankine_efficiency

if __name__ == "__main__":
    print("--- SENR: Turbine Efficiency Simulator (Rankine Cycle) ---")
    
    try:
        t_cold = float(input("Condenser Temperature (°C) [e.g., 30]: "))
        t_hot_min = float(input("Min Turbine Inlet Temperature (°C) [e.g., 250]: "))
        t_hot_max = float(input("Max Turbine Inlet Temperature (°C) [e.g., 350]: "))
        # Standard SMRs operate with a practical efficiency factor of around 0.65 to 0.75 relative to Carnot
        factor = float(input("Plant Efficiency Factor (0.0 to 1.0) [e.g., 0.70]: "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        exit(1)
        
    # Generate data
    inlet_temps, carnot_eff, rankine_eff = calculate_efficiency(t_cold, t_hot_min, t_hot_max, factor)
    
    # Terminal output for the maximum temperature provided
    print(f"\nAt a peak inlet temperature of {t_hot_max}°C:")
    print(f"-> Theoretical Max Efficiency (Carnot): {carnot_eff[-1]:.2f}%")
    print(f"-> Estimated Practical Efficiency (Rankine): {rankine_eff[-1]:.2f}%")
    
    # Plotting the curves
    plt.figure(figsize=(10, 6))
    plt.plot(inlet_temps, carnot_eff, label='Ideal Efficiency (Carnot)', color='#9E9E9E', linestyle='--', linewidth=2)
    plt.plot(inlet_temps, rankine_eff, label='Practical Efficiency (Rankine)', color='#E64A19', linewidth=3)
    
    plt.title('SENR - Turbine Thermal Efficiency vs Inlet Temperature', fontsize=14, fontweight='bold')
    plt.xlabel('Turbine Inlet Temperature (°C)', fontsize=12)
    plt.ylabel('Thermal Efficiency (%)', fontsize=12)
    
    # Adding a subtle fill to highlight the gap (thermodynamic losses)
    plt.fill_between(inlet_temps, rankine_eff, carnot_eff, color='#9E9E9E', alpha=0.15, label='Thermodynamic Losses')
    
    plt.grid(True, linestyle=':', alpha=0.8)
    plt.legend(loc='lower right')
    
    # Save output
    output_filename = 'turbine_efficiency_curve.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"\nGraph successfully saved as '{output_filename}'. Close the plot window to exit.")
    
    plt.show()
