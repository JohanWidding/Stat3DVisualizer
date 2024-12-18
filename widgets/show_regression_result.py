import sys
import numpy as np
import pandas as pd
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QVBoxLayout, QPlainTextEdit
import statsmodels.api as sm

class RegressionResults(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set up layout
        layout = QVBoxLayout()

        # Use QPlainTextEdit for better fixed-width font rendering
        self.text_edit = QPlainTextEdit()
        self.text_edit.setReadOnly(True)
        self.text_edit.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.text_edit.setStyleSheet("font-family: 'Courier New', monospace; font-size: 12px;")

        layout.addWidget(self.text_edit)
        self.setLayout(layout)

    def updateResults(self, df):
        # Extract data
        x_data = df.iloc[:, [0, 1]].values
        z_data = df.iloc[:, 2].values

        # Add constant for intercept
        X = sm.add_constant(x_data)

        # Fit regression model using statsmodels
        model = sm.OLS(z_data, X)
        results = model.fit()

        # Get the summary table as text
        summary_text = results.summary().as_text()

        # Display in text edit with consistent formatting
        self.text_edit.setPlainText(summary_text)

