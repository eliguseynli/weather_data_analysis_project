
# Weather Data Analysis

## **About the Project**
This project is designed to analyze global temperature data over time, providing insights into climate trends at various levels such as **cities**, **countries**, and **global averages**. The project is written in Python and uses data visualization libraries to generate insightful temperature trend graphs.  

Users can choose from **four analysis options** to explore temperature data. Additionally, users can visualize the generated plots directly in the terminal or save them for further use.  

---

## **Features**
1. **City Temperature Trend**  
   Analyze temperature trends for a specific city over time.  
   Example: *How has New York's average temperature changed over the years?*  

2. **Country Temperature Trend**  
   Explore the temperature trends of an entire country.  
   Example: *What is the average temperature trend in the USA?*  

3. **Compare Trends Between Two Cities**  
   Compare temperature trends of two different cities on the same graph.  
   Example: *How does Paris compare to London in terms of temperature changes?*  

4. **Global Temperature Trend**  
   Analyze global temperature data, including both land and ocean averages.  

---

## **Project Structure**
```
weather-data-analysis/
│
├── data/                       # Contains temperature datasets
│   ├── GlobalLandTemperaturesByCity.csv
│   ├── GlobalLandTemperaturesByCountry.csv
│   ├── GlobalLandTemperaturesByMajorCity.csv
│   └── GlobalTemperatures.csv
│
├── scripts/
│   └── data_processing.py      # Main script to process and visualize data
│
├── results/                    # Generated plots (if saved)
│
└── README.md                   # Project description
```

---

## **How to Run**
### **Prerequisites**
1. Python 3.9+ installed on your system.
2. Required Python libraries:
   - pandas
   - matplotlib
   - numpy

Install them using pip:
```bash
pip install pandas matplotlib numpy
```

---

### **Steps to Run**
1. Clone the repository:
   ```bash
   git clone https://github.com/eliguseynli/weather-data-analysis.git
   cd weather-data-analysis
   ```

2. Run the main script:
   ```bash
   python scripts/data_processing.py
   ```

3. Follow the prompts in the terminal to select an analysis option:
   - **Option 1**: Enter the name of the city (e.g., *"New York"*).  
   - **Option 2**: Enter the name of the country (e.g., *"United States"*).  
   - **Option 3**: Enter the names of two cities for comparison (e.g., *"Paris"* and *"London"*).  
   - **Option 4**: Select global trend analysis.  

---

## **Example Visuals**
### **City Temperature Trend**
![City Temperature Example](https://via.placeholder.com/600x400?text=Example+Graph+for+City+Trend)

### **Global Temperature Trend**
![Global Trend Example](https://via.placeholder.com/600x400?text=Example+Graph+for+Global+Trend)

---

## **Data Sources**
The datasets used in this project are sourced from [Kaggle's Global Temperature Data](https://www.kaggle.com/datasets/berkeleyearth/climate-change-earth-surface-temperature-data).  

---

## **Future Improvements**
- Support for more advanced statistical analysis.
- Integration with a web dashboard for real-time data visualization.
- Dynamic data fetching from online sources.

---

## **Contributors**
- **Eli Guseynli**  
  [GitHub Profile](https://github.com/eliguseynli)

---

## **Acknowledgements**
Special thanks to the course instructor for guidance and feedback.  
