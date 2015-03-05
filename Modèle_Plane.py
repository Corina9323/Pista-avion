import re
import operator
import os
import sys 
from PyQt4.QtCore import * 
from PyQt4.QtGui import *

class MyTableModel(QAbstractTableModel): 
    def __init__(self, datain, headerdata, projection, parent=None, *args): 
        
        QAbstractTableModel.__init__(self, parent, *args) 
        self.projection = projection
        self.arraydata = datain
        self.headerdata = headerdata
 
    def rowCount(self, parent): 
        return len(self.arraydata) 
 
    def columnCount(self, parent): 
        return len(self.projection)
    def triggerDataChanging(self):
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
    def triggerDataChanged(self):
        self.emit(SIGNAL("layoutChanged()"))
    def data(self, index, role): 
        if not index.isValid(): 
            return None 
        elif role != Qt.DisplayRole: 
            return None 
        return (getattr(self.arraydata[index.row()], self.projection[index.column()])) 

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return (self.headerdata[col])
        return None

    def sort(self, Ncol, order):
        
        self.emit(SIGNAL("layoutAboutToBeChanged()"))
        self.arraydata = sorted(self.arraydata, key=projection[Ncol])        
        if order == Qt.DescendingOrder:
            self.arraydata.reverse()
        self.emit(SIGNAL("layoutChanged()"))
