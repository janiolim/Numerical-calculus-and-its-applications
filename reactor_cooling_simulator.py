import numpy as np
import matplotlib.pyplot as plt

"""
Regional Nuclear Energy System (SENR)
Module: Reactor Thermodynamics & Safety
Script: Reactor Core Cooling Simulator (Post-Shutdown)
"""

def simulate_cooling(t_initial, t_coolant, cooling_constant, max_time, steps=500):
    """
    Simulates the reactor core temperature drop over time using Newton's Law of Cooling.
    Formula: T(t) = T_coolant + (T_initial - T_coolant) * e^(-k * t)
    """
    # Create a time vector
    time_array = np.linspace(0, max_time, steps)
    
    # Apply Newton's Law of Cooling
    temperature_array = t_coolant + (t_initial - t_coolant) * np.exp(-cooling_constant * time_array)
    
    return time_array, temperature_array

if __name__ == "__main__":
    print("--- SENR: Reactor Core Cooling Simulator ---")
    
    # Input parameters for the simulation
    try:
        t0 = float(input("Initial core temperature (°C): "))
        t_env = float(input("Coolant/Environment temperature (°C): "))
        k = float(input("Cooling system constant 'k' (e.g., 0.05): "))
        simulation_time = float(input("Total simulation time (hours): "))
    except ValueError:
        print("Invalid input. Please enter numerical values.")
        exit(1)
        
    # Generating the cooling data
    times, temperatures = simulate_cooling(t0, t_env, k, simulation_time)
    
    # Terminal output
    final_temp = temperatures[-1]
    print(f"\nResult: After {simulation_time} hours, the core temperature will drop to approximately {final_temp:.2f} °C.")
    
    # Plotting the visual graph
    plt.figure(figsize=(10, 6))
    plt.plot(times, temperatures, label=f'Cooling Curve (k={k})', color='#1976D2', linewidth=2.5)
    
    # Adding a dashed line to represent the safe target temperature (coolant temp)
    plt.axhline(y=t_env, color='#388E3C', linestyle='--', linewidth=1.5, label=f'Coolant Temp ({t_env}°C)')
    
    plt.title('SENR - Post-Shutdown Reactor Cooling Curve', fontsize=14, fontweight='bold')
    plt.xlabel('Time (Hours)', fontsize=12)
    plt.ylabel('Core Temperature (°C)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.fill_between(times, temperatures, t_env, color='#1976D2', alpha=0.1)
    plt.legend()
    
    # Save the graph automatically to the repository folder
    output_filename = 'cooling_curve_output.png'
    plt.savefig(output_filename, dpi=300, bbox_inches='tight')
    print(f"Graph successfully saved as '{output_filename}'. Close the plot window to exit.")
    
    plt.show()
