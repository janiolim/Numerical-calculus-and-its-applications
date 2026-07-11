import numpy as np
import matplotlib.pyplot as plt

"""
Regional Nuclear Energy System (SENR)
Module: Radiation Protection & Safety
Script: Gamma Radiation Shielding Attenuation Simulator
"""

def calculate_attenuation(i0, mu, max_thickness, steps=500):
    """
    Calculates the radiation intensity after passing through a shield.
    Formula: I(x) = I0 * e^(-mu * x)
    """
    # Create a vector for thickness (in cm)
    thickness = np.linspace(0, max_thickness, steps)
    
    # Calculate intensity drop
    intensity = i0 * np.exp(-mu * thickness)
    
    return thickness, intensity

if __name__ == "__main__":
    print("--- SENR: Radiation Shielding Simulator ---")
    
    # Input parameters
    try:
        i0 = float(input("Initial Gamma Radiation Intensity (mSv/h): "))
        safe_limit = float(input("Target safe radiation limit (mSv/h): "))
        max_x = float(input("Max shield thickness to simulate (in cm): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        exit(1)
        
    # Approximate linear attenuation coefficients (mu) for 1 MeV gamma rays (in cm^-1)
    mu_lead = 0.77      # Lead (Chumbo)
    mu_concrete = 0.15  # Concrete (Concreto)
    
    # Generate data for both materials
    x_lead, i_lead = calculate_attenuation(i0, mu_lead, max_x)
    x_concrete, i_concrete = calculate_attenuation(i0, mu_concrete, max_x)
    
    # Plotting the curves for material comparison
    plt.figure(figsize=(10, 6))
    plt.plot(x_lead, i_lead, label='Lead Shielding (mu=0.77)', color='#424242', linewidth=2.5)
    plt.plot(x_concrete, i_concrete, label='Concrete Shielding (mu=0.15)', color='#9E9E9E', linewidth=2.5)
    
    # Target safety limit line
    plt.axhline(y=safe_limit, color='#388E3C', linestyle='--', linewidth=1.5, label=f'Safe Limit ({safe_limit} mSv/h)')
    
    plt.title('SENR - Radiation Shielding Attenuation Comparison', fontsize=14, fontweight='bold')
    plt.xlabel('Shield Thickness (cm)', fontsize=12)
    plt.ylabel('Radiation Intensity (mSv/h)', fontsize=12)
    
    # Using a logarithmic scale on the Y-axis is standard for radiation protection charts
    plt.yscale('log')
    
    plt.grid(True, which="both", linestyle='--', alpha=0.7)
    plt.legend()
    
    # Save output
    output_filename = 'shielding_attenuation_output.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"\nGraph successfully saved as '{output_filename}'. Close the plot window to exit.")
    
    plt.show()
