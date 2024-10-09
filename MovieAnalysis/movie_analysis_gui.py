import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QPushButton, QVBoxLayout, QWidget, QDialog, QTextEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from movieAnalysis import *

class ResultDialog(QDialog):
    def __init__(self, title, result):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 600, 400)
        
        layout = QVBoxLayout()
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setFont(QFont("Courier", 10))
        self.text_edit.setText(result)
        layout.addWidget(self.text_edit)
        
        self.setLayout(layout)

class MovieAnalysisGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movie Analysis")
        self.setGeometry(100, 100, 800, 600)

        # Create tab widget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create tabs
        self.eda_tab = QWidget()
        self.advanced_tab = QWidget()
        self.visualization_tab = QWidget()
        self.recommendation_tab = QWidget()

        # Add tabs to widget
        self.tabs.addTab(self.eda_tab, "EDA")
        self.tabs.addTab(self.advanced_tab, "Advanced Analysis")
        self.tabs.addTab(self.visualization_tab, "Visualization")
        self.tabs.addTab(self.recommendation_tab, "Recommendation")

        # Set up layouts for each tab
        self.setup_eda_tab()
        self.setup_advanced_tab()
        self.setup_visualization_tab()
        self.setup_recommendation_tab()

    
    # EDA Tab
    def setup_eda_tab(self):
        layout = QVBoxLayout()
        btn_avg_rating = QPushButton("Find Average Rating")
        btn_avg_rating.clicked.connect(self.show_avg_rating)
        layout.addWidget(btn_avg_rating)

        btn_top5 = QPushButton("Top 5 Movies")
        btn_top5.clicked.connect(self.show_top5_movies)
        layout.addWidget(btn_top5)

        btn_top5 = QPushButton("Distribution of Ratings")
        btn_top5.clicked.connect(self.show_rating_dist)
        layout.addWidget(btn_top5)

        btn_top5 = QPushButton("Most Popular Genre")
        btn_top5.clicked.connect(self.show_pop_genre)
        layout.addWidget(btn_top5)

        btn_top5 = QPushButton("Rating Trend by Year")
        btn_top5.clicked.connect(self.show_rating_trend_by_year)
        layout.addWidget(btn_top5)

        self.eda_tab.setLayout(layout)

    def show_result(self, title, result):
        dialog = ResultDialog(title, result)
        dialog.exec_()

    # EDA - Find Average Rating
    def show_avg_rating(self):
        result = findAvgRating()
        self.show_result("Average Ratings", result)

    # EDA - Top 5 Movies
    def show_top5_movies(self):
        result = top5Movies()
        self.show_result("Top 5 Movies", result)

    # EDA - Distribution of Ratings
    def show_rating_dist(self):
        result = rating_dist()
        self.show_result("Distribution of Ratings", str(result))

    # EDA - Most Popular Genre
    def show_pop_genre(self):
        result = pop_genre()
        self.show_result("Most Popular Genre", str(result))

    # EDA - Rating Trend by Year
    def show_rating_trend_by_year(self):
        result = rating_trend_by_year()
        self.show_result("Rating Trends By Year", result)

    def setup_advanced_tab(self):
        # Similar to setup_eda_tab, create buttons for advanced analysis functions
        pass

    def setup_visualization_tab(self):
        # Create buttons for visualization functions
        pass

    def setup_recommendation_tab(self):
        # Create interface for recommendation system
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MovieAnalysisGUI()
    window.show()
    sys.exit(app.exec_())