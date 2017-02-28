#!/usr/bin/env python
'''
Created on 18/02/2017

@author: Augusto Gomez
'''

import wx 

class BrowserPanel(wx.Panel):
    """ Panel of Browser Files """
    def __init__(self, parent, label, name): 
        super(BrowserPanel, self).__init__(parent)
        self.label = label
        self.name = name
        self.initUI()
    
    """ Init UI Componenets """
    def initUI(self):
        
        # --------------------------------------
        # ----------    Create Sizers ----------
        # --------------------------------------
        
        # Create Sizer for Panel
        panelBox = wx.BoxSizer(wx.VERTICAL) 
        
        # Create BoxSizer 
        browserBox = wx.StaticBox(self, wx.ID_ANY, label = self.label) 
        browserBoxSizer = wx.StaticBoxSizer(browserBox, wx.VERTICAL)
        
        # Create Sizer for widgets
        browserSizer = wx.BoxSizer()
  
        # ------------------------------------------
        # --- Create Input Text and Searh Button ---
        # ------------------------------------------
        
        # Create Input Text
        self.fileText = wx.TextCtrl(self, wx.ID_ANY, style = wx.ALIGN_LEFT, name = self.name) 
        # Create Button for Search
        self.browserButton = wx.Button(self, wx.ID_ANY, 'Buscar... ')
        
        # --------------------------------------------------------
        # ----------  Add Input and Button to Sizer -------------
        # -------------------------------------------------------- 
        
        # Add Text Input to sizer
        browserSizer.Add(self.fileText, 1, wx.EXPAND,10) 
        browserSizer.AddSpacer(5)
        # Add Button To Sizer
        browserSizer.Add(self.browserButton, 0, wx.EXPAND,10)
        
        #  Add Sizer to Panel
        browserBoxSizer.Add(browserSizer,1, wx.EXPAND)
        panelBox.Add(browserBoxSizer, 0, wx.EXPAND, 10)
        
        # Add Panel Sizer
        self.SetSizerAndFit(panelBox)
        
    
    
        
      
        
        