import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt

# File paths for datasets
DATA_PATH_CITY = "./data/GlobalLandTemperaturesByCity.csv"
DATA_PATH_COUNTRY = "./data/GlobalLandTemperaturesByCountry.csv"
DATA_PATH_MAJOR_CITY = "./data/GlobalLandTemperaturesByMajorCity.csv"
DATA_PATH_STATE = "./data/GlobalLandTemperaturesByState.csv"
DATA_PATH_GLOBAL = "./data/GlobalTemperatures.csv"

def load_data(file_path):
    """
    Loads a CSV file and returns a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(data, date_column, drop_columns=None):
    """
    General data cleaning operations:
    - Converts date column to datetime format.
    - Drops specified columns.
    - Drops rows with missing values.
    """
    data[date_column] = pd.to_datetime(data[date_column], errors='coerce')
    if drop_columns:
        data = data.drop(columns=drop_columns)
    data = data.dropna()
    return data

def plot_temperature_trend(data, label, title, output_file):
    """
    General function to plot temperature trends and save to file.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['dt'], data['AverageTemperature'], label=label, color='blue')
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)  # Save the plot as a PNG file
    print(f"Plot saved as {output_file}")

def analyze_city_trend(data, city):
    """
    Visualizes the temperature trend for a specific city.
    """
    city_data = data[data['City'] == city]
    if city_data.empty:
        print(f"Error: No data found for the city '{city}'.")
        return
    
    plot_temperature_trend(city_data, f'{city} Average Temperature', f'Temperature Trend in {city}', f'{city}_trend.png')

def analyze_country_trend(data, country):
    """
    Visualizes the temperature trend for a specific country.
    """
    country_data = data[data['Country'] == country]
    if country_data.empty:
        print(f"Error: No data found for the country '{country}'.")
        return
    
    plot_temperature_trend(country_data, f'{country} Average Temperature', f'Temperature Trend in {country}', f'{country}_trend.png')

def compare_trends(data, entity1, entity2, is_city=True):
    """
    Compares the temperature trends of two entities (city or country).
    """
    data1 = data[data['City' if is_city else 'Country'] == entity1]
    data2 = data[data['City' if is_city else 'Country'] == entity2]
    
    if data1.empty:
        print(f"Error: No data found for '{entity1}'.")
        return
    if data2.empty:
        print(f"Error: No data found for '{entity2}'.")
        return
    
    plt.figure(figsize=(12, 6))
    plt.plot(data1['dt'], data1['AverageTemperature'], label=f'{entity1} Average Temperature', color='blue')
    plt.plot(data2['dt'], data2['AverageTemperature'], label=f'{entity2} Average Temperature', color='red')
    plt.title(f'Comparison of Temperature Trends: {entity1} vs {entity2}')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.legend()
    plt.grid(True)
    output_file = f'Comparison_{entity1}_vs_{entity2}.png'
    plt.savefig(output_file)
    print(f"Comparison plot saved as {output_file}")

def analyze_global_trend(data):
    """
    Analyzes global temperature trends and plots them.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data['dt'], data['LandAverageTemperature'], label='Land Average Temperature', color='green')
    plt.plot(data['dt'], data['LandAndOceanAverageTemperature'], label='Land and Ocean Average Temperature', color='orange')
    plt.title('Global Temperature Trends')
    plt.xlabel('Year')
    plt.ylabel('Average Temperature (°C)')
    plt.legend()
    plt.grid(True)
    plt.savefig('Global_Temperature_Trend.png')
    print("Global temperature trend plot saved as Global_Temperature_Trend.png")

if __name__ == "__main__":
    # Load all datasets
    city_data = load_data(DATA_PATH_CITY)
    country_data = load_data(DATA_PATH_COUNTRY)
    major_city_data = load_data(DATA_PATH_MAJOR_CITY)
    state_data = load_data(DATA_PATH_STATE)
    global_data = load_data(DATA_PATH_GLOBAL)
    
    # Clean datasets
    city_data = clean_data(city_data, 'dt', drop_columns=['AverageTemperatureUncertainty'])
    country_data = clean_data(country_data, 'dt')
    major_city_data = clean_data(major_city_data, 'dt')
    state_data = clean_data(state_data, 'dt')
    global_data = clean_data(global_data, 'dt')
    
    # Ask the user for their desired analysis type
    print("\nAnalysis Options:")
    print("1. City temperature trend")
    print("2. Country temperature trend")
    print("3. Compare temperature trends between two cities")
    print("4. Global temperature trend")
    
    choice = int(input("Please choose an option (1/2/3/4): "))
    
    if choice == 1:
        city_name = input("Enter the name of the city: ").strip()
        analyze_city_trend(city_data, city_name)
    elif choice == 2:
        country_name = input("Enter the name of the country: ").strip()
        analyze_country_trend(country_data, country_name)
    elif choice == 3:
        city1 = input("Enter the name of the first city: ").strip()
        city2 = input("Enter the name of the second city: ").strip()
        compare_trends(city_data, city1, city2, is_city=True)
    elif choice == 4:
        analyze_global_trend(global_data)
    else:
        print("Invalid choice!")
