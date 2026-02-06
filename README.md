# 🌍 Global Terrorism Database Analysis (1970–2017)

## 📌 Project Overview
This project is a comprehensive data analysis and visualization of the **Global Terrorism Database (GTD)**. The goal is to uncover historical patterns in terrorist activity, including frequency trends, regional hotspots, attack methods, and the rise and fall of major terrorist organizations over the last 50 years.

This repository includes:
1.  **Jupyter Notebook:** A deep-dive analysis answering 10 key analytical questions.
2.  **Streamlit Dashboard:** An interactive web application for exploring the data dynamically.
3.  **Visualizations:** Static and interactive charts illustrating the "Who, Where, When, and How" of global terrorism.

## 📂 Dataset
* **Source:** [Global Terrorism Database (GTD)](https://www.start.umd.edu/gtd/) via Kaggle.
* **Description:** The dataset contains over **180,000+** terrorist attacks worldwide from 1970 to 2017.
* **Key Features:** Dates, Locations (Latitude/Longitude), Attack Types, Weapons, Casualties (Killed/Wounded), and Group Names.
* **Note:** The dataset file (`globalterrorismdb_0718dist.csv`) is not included in this repo due to size limits. You can download it [here](https://www.kaggle.com/START-UMD/gtd).

## 🛠️ Tech Stack
* **Python 3.9+**
* **Data Manipulation:** `pandas`, `numpy`
* **Visualization:** `matplotlib`, `seaborn`, `plotly.express`
* **Web App Framework:** `streamlit`

## ⚙️ Installation & Setup

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/your-username/global-terrorism-analysis.git](https://github.com/your-username/global-terrorism-analysis.git)
    cd global-terrorism-analysis
    ```

2.  **Install Dependencies**
    Ensure you have Python installed, then run:
    ```bash
    pip install pandas matplotlib seaborn plotly streamlit nbformat protobuf
    ```

3.  **Add the Data**
    * Download the dataset from Kaggle.
    * Place the `globalterrorismdb_0718dist.csv` file in the root directory of this project.

## 🚀 How to Run

### 1. Run the Jupyter Notebook (Analysis)
To see the step-by-step analysis and all 10 visualizations:
```bash
jupyter notebook "Global Terrorism Analysis.ipynb"
```
### 2. Run the Streamlit Dashboard (Web App)
To launch the interactive dashboard:
```bash
streamlit run app.py
```
The dashboard will open automatically in your browser at http://localhost:8501.

## 📊 Key Analytical Questions Solved

1.  Global Trends: How has the frequency of attacks changed from 1970 to 2017?

2.  Geospatial Hotspots: Which regions suffer the most casualties?

3.  Attack Effectiveness: What is the distribution of casualties per attack?

4.  Major Groups: Which groups are responsible for the most incidents?

5.  Tactics: How have attack methods (Bombing vs. Assassination) evolved?

6.  Targets: Who are the primary targets (Civilians vs. Military)?

7.  Heatmap Analysis: Do specific regions prefer specific attack methods?

8.  Lifecycle of Groups: Visualizing the rise and fall of groups like ISIL and the Taliban.

9.  Success Rates: How often do attacks achieve their tactical goals?

10. Mapping Terror: An interactive map of high-casualty events.

## 📁 Project Structure

```bash
├── app.py                     # The Streamlit dashboard source code
├── Global Terrorism Analysis.ipynb  # The Jupyter Notebook with full analysis
├── archive
│   ├── globalterrorismdb_0718dist.csv   # The Dataset (Not included in repo)
├── README.md                   # Project documentation
└── requirements.txt            # List of dependencies
```
📜 Author
Name: Aravind Kagganti Anjinamurthy

Course: Final Project - Winter 2025/2026

Institution: University of Europe for Applied Sciences (UE)


Disclaimer: This project is for educational purposes only. The data deals with sensitive topics regarding global conflict and violence.

