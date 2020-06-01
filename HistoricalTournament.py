# -*- coding: utf-8 -*-
"""
Created on Fri May 29 06:19:17 2020

@author: aaron
"""

from PyQt5.QtCore import QDateTime, Qt, QTimer
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
        QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
        QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy, QLCDNumber,
        QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
        QVBoxLayout, QWidget)
from PyQt5.QtGui import QIcon


import pandas as pd
import numpy as np
import sys

rawBatting = pd.read_csv('Batting.csv')
rawPitching = pd.read_csv('Pitching.csv')

dataSet = pd.merge(rawBatting, rawPitching, on=["Season", "Team"])
dataSet['Overall'] = dataSet['bRank'] + dataSet['Rank']

years = ['Season','2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019']
teams = ['Team', 'Diamondbacks','Braves','Orioles','Red Sox','White Sox','Cubs','Reds','Indians','Rockies','Tigers','Astros','Royals','Angels','Dodgers','Marlins','Brewers','Twins','Yankees','Mets','Athletics','Phillies','Pirates','Padres','Giants','Mariners','Cardinals','Rays','Rangers','Blue Jays', 'Nationals']



class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.createMatch1Box()
        self.createMatch2Box()
        self.createMatch3Box()
        self.createMatch4Box()
        self.createMatch5Box()
        self.createMatch6Box()
        self.createMatch7Box()
 
        
        self.mainLayout = QGridLayout()
        self.mainLayout.addWidget(self.match1Box, 0, 1, 5, 5)
        self.mainLayout.addWidget(self.match2Box, 6, 1, 5, 5)
        self.mainLayout.addWidget(self.match3Box, 0, 24, 5, 5)
        self.mainLayout.addWidget(self.match4Box, 6, 24, 5, 5)
        self.mainLayout.addWidget(self.match5Box, 3, 6, 5, 5)
        self.mainLayout.addWidget(self.match6Box, 3, 19, 5, 5)
        self.mainLayout.addWidget(self.match7Box, 4, 14, 3, 5)
        
        self.champ = QLabel('Champion')
        self.champ.setStyleSheet("border-style: outset; border-width: 2px; border-radius: 3px; border-color: beige; font:  14px; padding: 6px;")
        self.btn = QPushButton('Simulate', self)
        self.btn.setStyleSheet("background-color: #007BF5; border-style: outset; border-width: 2px; border-radius: 3px; border-color: beige; font:  14px; min-width: 10em; padding: 6px;")
        self.mainLayout.addWidget(self.btn, 1, 16)
        self.btn.clicked.connect(self.buttonPressed)
        self.mainLayout.addWidget(self.champ, 1, 17)

        
        self.setLayout(self.mainLayout)
        self.setWindowTitle("Historical MLB Tournament Simulator")
        self.setWindowIcon(QIcon('mlblogo.png'))
        self.changeStyle('windowsvista')

    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        
    def createMatch1Box(self):
        self.match1Box = QGroupBox("Round 1 : Match 1")

        self.match1team1 = QLabel()
        self.match1team1.setText('Team 1 Select')
        
        
        self.match1team1y = QComboBox()
        self.match1team1y.addItems(years)
        self.match1team1t = QComboBox()
        self.match1team1t.addItems(teams)

        self.match1team2 = QLabel()
        self.match1team2.setText('Team 2 Select')
        
        self.match1team2y = QComboBox()
        self.match1team2y.addItems(years)
        self.match1team2t = QComboBox()
        self.match1team2t.addItems(teams)

        
        layout1 = QVBoxLayout()
        layout1.addWidget(self.match1team1)
        layout1.addWidget(self.match1team1y)
        layout1.addWidget(self.match1team1t)
        layout1.addWidget(self.match1team2)
        layout1.addWidget(self.match1team2y)
        layout1.addWidget(self.match1team2t)
        layout1.addStretch(1)
        self.match1Box.setLayout(layout1)   
        
    def createMatch2Box(self):
        self.match2Box = QGroupBox("Round 1 : Match 2")

        self.match2team1 = QLabel()
        self.match2team1.setText('Team 1 Select')
        
        self.match2team1y = QComboBox()
        self.match2team1y.addItems(years)
        self.match2team1t = QComboBox()
        self.match2team1t.addItems(teams)

        self.match2team2 = QLabel()
        self.match2team2.setText('Team 2 Select')
        
        self.match2team2y = QComboBox()
        self.match2team2y.addItems(years)
        self.match2team2t = QComboBox()
        self.match2team2t.addItems(teams)

        
        layout2 = QVBoxLayout()
        layout2.addWidget(self.match2team1)
        layout2.addWidget(self.match2team1y)
        layout2.addWidget(self.match2team1t)
        layout2.addWidget(self.match2team2)
        layout2.addWidget(self.match2team2y)
        layout2.addWidget(self.match2team2t)
        layout2.addStretch(1)
        self.match2Box.setLayout(layout2)  
        
    def createMatch3Box(self):
        self.match3Box = QGroupBox("Round 1 : Match 3")

        self.match3team1 = QLabel()
        self.match3team1.setText('Team 1 Select')
        
        self.match3team1y = QComboBox()
        self.match3team1y.addItems(years)
        self.match3team1t = QComboBox()
        self.match3team1t.addItems(teams)

        self.match3team2 = QLabel()
        self.match3team2.setText('Team 2 Select')
        
        self.match3team2y = QComboBox()
        self.match3team2y.addItems(years)
        self.match3team2t = QComboBox()
        self.match3team2t.addItems(teams)

        
        layout3 = QVBoxLayout()
        layout3.addWidget(self.match3team1)
        layout3.addWidget(self.match3team1y)
        layout3.addWidget(self.match3team1t)
        layout3.addWidget(self.match3team2)
        layout3.addWidget(self.match3team2y)
        layout3.addWidget(self.match3team2t)
        layout3.addStretch(1)
        self.match3Box.setLayout(layout3)
        
    def createMatch4Box(self):
        self.match4Box = QGroupBox("Round 1 : Match 4")

        self.match4team1 = QLabel()
        self.match4team1.setText('Team 1 Select')
        
        self.match4team1y = QComboBox()
        self.match4team1y.addItems(years)
        self.match4team1t = QComboBox()
        self.match4team1t.addItems(teams)

        self.match4team2 = QLabel()
        self.match4team2.setText('Team 2 Select')
        
        self.match4team2y = QComboBox()
        self.match4team2y.addItems(years)
        self.match4team2t = QComboBox()
        self.match4team2t.addItems(teams)

        
        layout4 = QVBoxLayout()
        layout4.addWidget(self.match4team1)
        layout4.addWidget(self.match4team1y)
        layout4.addWidget(self.match4team1t)
        layout4.addWidget(self.match4team2)
        layout4.addWidget(self.match4team2y)
        layout4.addWidget(self.match4team2t)
        layout4.addStretch(1)
        self.match4Box.setLayout(layout4)
        
    def createMatch5Box(self):
        self.match5Box = QGroupBox("Semifinals : Match 1")

        self.match5team1 = QLabel('Quarterfinal 1 Winner')
        self.match5team1.setAlignment(Qt.AlignCenter)
        
        self.vs = QLabel('Vs.')
        self.vs.setAlignment(Qt.AlignCenter)

        self.match5team2 = QLabel('Quarterfinal 2 Winner')
        self.match5team2.setAlignment(Qt.AlignCenter)
        
        
        layout5 = QVBoxLayout()
        layout5.addSpacing(20)
        layout5.addWidget(self.match5team1)
        layout5.addSpacing(40)
        layout5.addWidget(self.vs)
        layout5.addSpacing(40)
        layout5.addWidget(self.match5team2)
        layout5.addSpacing(20)


        self.match5Box.setLayout(layout5)
        
        
    def createMatch6Box(self):
        self.match6Box = QGroupBox("Semifinals : Match 2")

        self.match6team1 = QLabel('Quarterfinal 3 Winner')
        self.match6team1.setAlignment(Qt.AlignCenter)
        
        self.vs = QLabel('Vs.')
        self.vs.setAlignment(Qt.AlignCenter)

        self.match6team2 = QLabel('Quarterfinal 4 Winner')
        self.match6team2.setAlignment(Qt.AlignCenter)
        
        
        layout6 = QVBoxLayout()
        layout6.addSpacing(20)
        layout6.addWidget(self.match6team1)
        layout6.addSpacing(40)
        layout6.addWidget(self.vs)
        layout6.addSpacing(40)
        layout6.addWidget(self.match6team2)
        layout6.addSpacing(20)


        self.match6Box.setLayout(layout6)
        
        
    def createMatch7Box(self):
        self.match7Box = QGroupBox("Finals")
        self.match7Box.setStyleSheet("background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #C0D6D6, stop: 1 #FFFFFF);")

        self.match7team1 = QLabel('Semifinal 1 Winner')
        self.match7team1.setStyleSheet("border: 3px solid black;")
        self.match7team1.setAlignment(Qt.AlignCenter)
        
        self.vs = QLabel('Vs.')
        self.vs.setAlignment(Qt.AlignCenter)

        self.match7team2 = QLabel('Semifinal 2 Winner')
        self.match7team2.setStyleSheet("border: 3px solid black;")
        self.match7team2.setAlignment(Qt.AlignCenter)
     
        
        layout7 = QVBoxLayout()
        layout7.addSpacing(00)
        layout7.addWidget(self.match7team1)
        layout7.addSpacing(00)
        layout7.addWidget(self.vs)
        layout7.addSpacing(00)
        layout7.addWidget(self.match7team2)
        layout7.addSpacing(00)


        self.match7Box.setLayout(layout7)
        
    def buttonPressed(self):
        self.selectmatch1team1y = int(self.match1team1y.currentText())
        self.selectmatch1team1t = str(self.match1team1t.currentText())
        self.selectmatch1team2y = int(self.match1team2y.currentText())
        self.selectmatch1team2t = str(self.match1team2t.currentText())        
        
        self.m1t1Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch1team1y) & (dataSet['Team'] == self.selectmatch1team1t), 'Overall'].values[0] 
        self.m1t2Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch1team2y) & (dataSet['Team'] == self.selectmatch1team2t), 'Overall'].values[0] 

        print(self.m1t1Selection)
        print(self.m1t2Selection)
        
        if self.m1t1Selection < self.m1t2Selection:
            self.match5team1.setText(str(self.selectmatch1team1y) + ' ' + self.selectmatch1team1t)
            self.quarterfinal1winner = str(self.selectmatch1team1y) + ' ' + self.selectmatch1team1t
            self.quarterfinal1winnerscore = self.m1t1Selection

        else:
            self.match5team1.setText(str(self.selectmatch1team2y) + ' ' + self.selectmatch1team2t)
            self.quarterfinal1winner = str(self.selectmatch1team2y) + ' ' + self.selectmatch1team2t
            self.quarterfinal1winnerscore = self.m1t2Selection
            
            
        self.selectmatch2team1y = int(self.match2team1y.currentText())
        self.selectmatch2team1t = str(self.match2team1t.currentText())
        self.selectmatch2team2y = int(self.match2team2y.currentText())
        self.selectmatch2team2t = str(self.match2team2t.currentText())        
        
        self.m2t1Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch2team1y) & (dataSet['Team'] == self.selectmatch2team1t), 'Overall'].values[0] 
        self.m2t2Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch2team2y) & (dataSet['Team'] == self.selectmatch2team2t), 'Overall'].values[0] 

        print(self.m2t1Selection)
        print(self.m2t2Selection)
        
        if self.m2t1Selection < self.m2t2Selection:
            self.match5team2.setText(str(self.selectmatch2team1y) + ' ' + self.selectmatch2team1t)
            self.quarterfinal2winner = str(self.selectmatch2team1y) + ' ' + self.selectmatch2team1t
            self.quarterfinal2winnerscore = self.m2t1Selection
        else:
            self.match5team2.setText(str(self.selectmatch2team2y) + ' ' + self.selectmatch2team2t)
            self.quarterfinal2winner = str(self.selectmatch2team2y) + ' ' + self.selectmatch2team2t
            self.quarterfinal2winnerscore = self.m2t2Selection
            
            
        self.selectmatch3team1y = int(self.match3team1y.currentText())
        self.selectmatch3team1t = str(self.match3team1t.currentText())
        self.selectmatch3team2y = int(self.match3team2y.currentText())
        self.selectmatch3team2t = str(self.match3team2t.currentText())        
        
        self.m3t1Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch3team1y) & (dataSet['Team'] == self.selectmatch3team1t), 'Overall'].values[0] 
        self.m3t2Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch3team2y) & (dataSet['Team'] == self.selectmatch3team2t), 'Overall'].values[0] 

        print(self.m3t1Selection)
        print(self.m3t2Selection)
        
        if self.m3t1Selection < self.m3t2Selection:
            self.match6team1.setText(str(self.selectmatch3team1y) + ' ' + self.selectmatch3team1t)
            self.quarterfinal3winner = str(self.selectmatch3team1y) + ' ' + self.selectmatch3team1t
            self.quarterfinal3winnerscore = self.m3t1Selection
        else:
            self.match6team1.setText(str(self.selectmatch3team2y) + ' ' + self.selectmatch3team2t)
            self.quarterfinal3winner = str(self.selectmatch3team2y) + ' ' + self.selectmatch3team2t
            self.quarterfinal3winnerscore = self.m3t2Selection
            
            
        self.selectmatch4team1y = int(self.match4team1y.currentText())
        self.selectmatch4team1t = str(self.match4team1t.currentText())
        self.selectmatch4team2y = int(self.match4team2y.currentText())
        self.selectmatch4team2t = str(self.match4team2t.currentText())        
        
        self.m4t1Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch4team1y) & (dataSet['Team'] == self.selectmatch4team1t), 'Overall'].values[0] 
        self.m4t2Selection = dataSet.loc[(dataSet['Season'] == self.selectmatch4team2y) & (dataSet['Team'] == self.selectmatch4team2t), 'Overall'].values[0] 

        print(self.m4t1Selection)
        print(self.m4t2Selection)
        
        if self.m4t1Selection < self.m4t2Selection:
            self.match6team2.setText(str(self.selectmatch4team1y) + ' ' + self.selectmatch4team1t)
            self.quarterfinal4winner = str(self.selectmatch4team1y) + ' ' + self.selectmatch4team1t
            self.quarterfinal4winnerscore = self.m4t1Selection
        else:
            self.match6team2.setText(str(self.selectmatch4team2y) + ' ' + self.selectmatch4team2t)
            self.quarterfinal4winner = str(self.selectmatch4team2y) + ' ' + self.selectmatch4team2t
            self.quarterfinal4winnerscore = self.m4t2Selection         
            
        if self.quarterfinal1winnerscore < self.quarterfinal2winnerscore:
            self.match7team1.setText(self.quarterfinal1winner)
            self.semifinal1winner = self.quarterfinal1winner
            self.semifinal1winnerscore = self.quarterfinal1winnerscore
        else:
            self.match7team1.setText(self.quarterfinal2winner)
            self.semifinal1winner = self.quarterfinal2winner
            self.semifinal1winnerscore = self.quarterfinal2winnerscore
            
        if self.quarterfinal3winnerscore < self.quarterfinal4winnerscore:
            self.match7team2.setText(self.quarterfinal3winner)
            self.semifinal2winner = self.quarterfinal3winner
            self.semifinal2winnerscore = self.quarterfinal3winnerscore
            
        else:
            self.match7team2.setText(self.quarterfinal4winner)
            self.semifinal2winner = self.quarterfinal4winner
            self.semifinal2winnerscore = self.quarterfinal4winnerscore
        
        if self.semifinal1winnerscore < self.semifinal2winnerscore:
            self.champ.setText('Champion: ' + self.semifinal1winner)
        else:
            self.champ.setText('Champion: ' + self.semifinal2winner)

        
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet("QGroupBox { subcontrol-origin: margin; subcontrol-position: top center; background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ABD3FC, stop: 1 #FFFFFF); }")
    sim = Window()
    sim.show()
    sys.exit(app.exec_())