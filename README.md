# Wardrobe App

Wardrobe App is a desktop application designed for e-commerce analytics and customer management. It provides tools for database management, customer churn prediction, and data visualization, all within a modern and user-friendly interface.

---

## Features

- **Database Management**: Import CSV files, manage DuckDB databases, and view database contents.
- **Customer Churn Prediction**: Predict customer churn using an XGBoost model and visualize results with interactive graphs.
- **Analytics Dashboard**: Access detailed analytics for customer behavior and trends.
- **Modular Design**: Easily extendable to include additional models like item return prediction and loan approval analytics.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/little-Patrick/Wardrobe.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Wardrobe
   ```
3. Install dependencies using [Poetry](https://python-poetry.org/):
   ```bash
   poetry install
   ```
4. Run the application:
   ```bash
   poetry run python main.py
   ```

---

## Usage

1. **Add a File**: Import CSV files into the database.
2. **Manage Databases**: View and manage DuckDB databases.
3. **Run Churn Model**: Select a database and run the customer churn prediction model.
4. **View Analytics**: Explore detailed analytics and graphs for customer behavior.

---

## Screenshots

_Add screenshots or GIFs of the app in action here._

---

## Technologies Used

- **Python**: Core programming language.
- **PySide6**: For building the desktop application interface.
- **DuckDB**: Lightweight database management.
- **XGBoost**: Machine learning model for customer churn prediction.
- **pandas**: Data manipulation and analysis.
- **Jupyter Notebook**: For data exploration and model training.

---

## Future Plans

- Add an item return prediction model using Random Forest.
- Develop a loan approval analytics model.
- Enhance the analytics dashboard with more visualizations.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Acknowledgments

- Inspired by the need for better e-commerce analytics tools.
- Special thanks to the open-source community for providing the tools and libraries used in this project.
