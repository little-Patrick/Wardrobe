<h1 align='center'>Wardrobe App</h1>

## About

Wardrobe App is a desktop application designed for e-commerce analytics and customer management. It provides tools for database management, customer churn prediction, and data visualization, all within a modern and user-friendly interface.

---

## App Overview


https://github.com/user-attachments/assets/7e08c8db-abe5-44df-8500-5a48c1c528ad



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

## Technologies Used

- **Python**: Core programming language.
- **PySide6**: For building the desktop application interface.
- **DuckDB**: Lightweight database management.
- **XGBoost**: Machine learning model for customer churn prediction.
- **pandas**: Data manipulation and analysis.
- **Jupyter Notebook**: For data exploration and model training.

---

## Road Map

### UI
- [ ] Make text consistant across pages
- [ ] Better navigation bar UX

### Models
- [ ] Impliment remaining 2 models at [Wardrobe_Models](https://github.com/little-Patrick/Wardrobe_Models)

### Analytics
- [ ] User defined graphs
- [ ] SQL injection to filter and sort databases

### Automated Customer Retention
- [ ] Automated customer emailing/notifications based on churn
- [ ] Track customers who repeatedly show up in model analytics
