# Bourses Project

This project is designed to manage and analyze financial data related to stock markets and cryptocurrencies. The repository includes various Python scripts and configuration files to retrieve, process, and test financial data.

## Project Structure

### Directories

- **.github/workflows**:  
  Contains GitHub Actions workflows for CI/CD automation, ensuring tests run and code quality is maintained on each commit.

- **.idea**:  
  Stores project configuration files for JetBrains IDEs (e.g., PyCharm), including workspace settings and code style configurations.

- **API_bourses**:  
  Scripts related to retrieving and managing stock market data from various APIs.

- **API_crypto**:  
  Similar to `API_bourses`, but focused on cryptocurrency data retrieval and management.

- **data**:  
  Contains raw and processed datasets used by the project, including historical financial data.

### Python Scripts

- **Commentaires.py**:  
  Handles comments or logs, potentially used for debugging or maintaining a log of operations.

- **comm_test.py**:  
  A testing script for communication functions or data retrieval tests.

- **data_bourses.py**:  
  The main script for handling stock market data, including fetching, cleaning, and processing the data.

- **data_bourses_test.py**:  
  Test script for verifying the functionality of `data_bourses.py`.

- **main.py**:  
  The main entry point of the application, orchestrating the workflow and integrating various modules.

- **portefeuille.py**:  
  Manages financial portfolios, including calculations of returns, risks, and other metrics.

- **requete_data.py**:  
  Script for making API requests to external data sources and managing the retrieval of financial data.

- **test.py**:  
  General test script, possibly running a suite of unit tests across the project.

- **test_regression.py**:  
  A script for regression testing to ensure new changes don’t introduce bugs.

- **test_streamlit.py**:  
  Tests related to Streamlit, indicating the presence of a web interface for data visualization or interaction.

- **yfinance_structure.py**:  
  Script focused on retrieving and structuring financial data using the `yfinance` library.

### Configuration Files

- **requirements.txt**:  
  Lists all Python dependencies required to run the project, allowing for easy installation using `pip`.
