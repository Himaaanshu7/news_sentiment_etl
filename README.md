# 📰 News Sentiment Analytics ETL Pipeline

A modular ETL pipeline that scrapes daily world news from Reuters, analyzes sentiment using NLP, and loads the data into MySQL for visualization.

---

## 📌 Project Highlights

* 🧱 Extract: Scrapes latest news headlines from [Reuters](https://www.reuters.com/world/)
* 🧹 Transform: Cleans headline text and analyzes sentiment using TextBlob
* 📂 Load: Loads processed data into a MySQL database
* 📊 Visualize: (Coming soon) Tableau dashboard for real-time sentiment trends
* 🧪 Orchestrate: Run modular ETL pipeline using main.ipynb and log every step

---

## 🛠️ Tech Stack

| Layer         | Tools Used                      |
| ------------- | ------------------------------- |
| Extract       | Python, requests, BeautifulSoup |
| Transform     | pandas, nltk, TextBlob          |
| Load          | MySQL, mysql-connector-python   |
| Orchestration | Jupyter Notebook (main.ipynb) |
| Logging       | Python logging module         |
| Storage       | CSV files + MySQL               |

---

## 📂 Project Structure

news_sentiment_etl/
├── etl/
│   ├── extract.py        # Web scraping logic
│   ├── transform.py      # Text cleaning and NLP
│   └── load.py           # Load data into MySQL
├── data/                 # Raw and transformed CSVs
├── logs/                 # ETL logs
├── main.ipynb            # ETL pipeline runner
└── README.md             # ← You're here


---

## 🚀 How to Run

### 1. Clone the Repository

bash
git clone https://github.com/yourusername/news_sentiment_etl.git
cd news_sentiment_etl


### 2. Install Requirements

bash
pip install -r requirements.txt
python -m textblob.download_corpora


### 3. Set MySQL Credentials

Update your MySQL username/password in load.py.

### 4. Run the Pipeline

Open main.ipynb and run all cells to:

* Extract → Transform → Load
* Logs stored in logs/etl.log
* Data saved in data/

---

📊 Sample Output

| Title                    | Sentiment | Label    |
| ------------------------ | --------- | -------- |
| "China resumes imports…" |  0.3     | Positive |
| "UN warns of famine…"    | -0.5    | Negative |

---

## 📈 Dashboard

---

📌 Author

Himanshu Mishra

