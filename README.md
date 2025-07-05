# Finance Tracker Application

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-brightgreen.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)

A simple command-line application to track personal finances, including income and expenses, with visualization capabilities.

## Features

- 📅 Add transactions with date, amount, category (Income/Expense), and optional description
- 📊 View transactions within any date range
- 💰 See summary statistics including total income, expenses, and net savings
- 📈 Visualize income and expense trends over time with matplotlib graphs
- 💾 Automatic CSV file creation for data persistence

## Installation

1. Clone the repository

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

### Main Menu Options

1. **Add a new transaction**:
   - Enter transaction details (date defaults to today)
   - Specify amount (must be positive)
   - Choose category (Income/Expense)
   - Add optional description

2. **View Transactions and Summary**:
   - Enter a date range to view transactions
   - See summary statistics (total income, expenses, net savings)
   - Option to visualize data with a plot

3. **Quit**: Exit the application

## Data Storage

All transactions are stored in `finance_data.csv` with the following columns:
- Date (dd-mm-yyyy format)
- Amount (float)
- Category (Income/Expense)
- Description (optional text)

## Requirements

- Python 3.8+
- pandas
- matplotlib

All dependencies are listed in `requirements.txt`

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.
