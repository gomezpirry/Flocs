#!/usr/bin/env python
'''
Created on 19/02/2017

@author: augusto
'''

import wx
from views.parameters_panel import ParameterPanel
from views.image_panel import ImagePanel

class InitialPanel(wx.Panel):
    """ Panel Group """
    def __init__(self, *args, **kwargs):
        """Create the DemoPanel."""
        wx.Panel.__init__(self, *args, **kwargs)  
        self.initUI() 
        
    """ Init UI Componenets """
    def initUI(self):
        
        # --------------------------------------
        # ----------    Create Sizers ----------
        # --------------------------------------
        
        # Create Panel Sizer
        panelSizer = wx.BoxSizer(wx.VERTICAL) 
        # Create Splitter Window for Parameters and Image
        self.paramatersAndImageSplitter = wx.SplitterWindow(self, style= wx.SP_3DSASH|wx.SP_3DBORDER)
        
        # -----------------------------------------
        # ----------    Create  Panels  -----------
        # -----------------------------------------
        
        # Create Paramter Panel
        self.parameters = ParameterPanel(self.paramatersAndImageSplitter)
        # Create Image Panel
        self.image = ImagePanel(self.paramatersAndImageSplitter) 
        
        # -------------------------------------------
        # ----------  Add Panels to Sizer -----------
        # -------------------------------------------
        self.paramatersAndImageSplitter.SplitVertically(self.image, self.parameters)
        #self.paramatersAndImageSplitter.SetMinimumPaneSize(20)       
        
        panelSizer.AddSpacer(10)
        panelSizer.AddSizer(self.paramatersAndImageSplitter , 1, wx.EXPAND,10)
        
        # Add Sizer to Panel
        self.SetSizerAndFit(panelSizer)
        
    # --------------------------------------------------------
    # --------------------  Add Getters ----------------------
    # --------------------------------------------------------  
    
    # Get Parameters Panel
        
    """ Get Sample Name """   
    def getSampleName(self):
        return self.parameters.text_sampleName.GetValue()
    
    """ Get User Name """   
    def getUser(self):
        return self.parameters.text_user.GetValue()
    
    """ Get Equipment """   
    def getEquipment(self):
        return self.parameters.text_equipment.GetValue()
    
    """ Get Temperature """   
    def getTemp(self):
        return self.parameters.text_sampleName.GetValue()
    
    """ Get Dilution """   
    def getDilution(self):
        return self.parameters.text_dilution.GetValue()
    
    """ Get Date """   
    def getDate(self):
        return self.parameters.text_date.GetValue()
    
    """ Get Volume """   
    def getVolume(self):
        return self.parameters.text_volume.GetValue()
    
    """ Get Contaminant Concentration """   
    def getContaminantConcentration(self):
        return self.parameters.text_contaminantConcentration.GetValue()
    
    """ Get Coagulant Concentration """   
    def getCoagulantConcentration(self):
        return self.parameters.text_coagulantConcentration.GetValue()
    
    """ Get Objective X"""   
    def getObjectiveX(self):
        return self.parameters.text_objectiveX.GetValue()
    
    """ Get Visual Area """   
    def getVisualArea(self):
        return self.parameters.text_visualArea.GetValue()
    
    """ Get Voltage """   
    def getVoltage(self):
        return self.parameters.text_volt.GetValue()
    
    """ Get Observations """   
    def getObservations(self):
        return self.parameters.text_observations.GetValue()
    
    # Get output Browser Panel
    """ Get Input Browser Text """
    def getOutput(self):
        return self.parameters.outputBrowser.fileText.GetValue()
    
    def getOutputButton(self):
        return self.parameters.outputBrowser.browserButton

    # Get Start and Restart Button
    def getStartButton(self):
        return self.parameters.initButton
    
    def getRestartButton(self):
        return self.parameters.resetButton
    
    # Get Image Panel
    """ Get Add Folder button """
    def getAddFolderButton(self):
        return self.image.button_addFolder
    
    """ Get Add File button """
    def getAddFileButton(self):
        return self.image.button_addFile

    """ Get remove button """
    def getRemoveButton(self):
        return self.image.button_remove
    
    
    
    # --------------------------------------------------------
    # --------------------  Add Setters ----------------------
    # --------------------------------------------------------  
    
    """ Get Sample Name """   
    def setSampleName(self, value):
        self.parameters.text_sampleName.SetValue()
    
    """ Set User Name """   
    def setUser(self, value):
        self.parameters.text_user.SetValue()
    
    """ Set Equipment """   
    def setEquipment(self, value):
        self.parameters.text_equipment.SetValue()
    
    """ Set Temperature """   
    def setTemp(self, value):
        self.parameters.text_sampleName.SetValue()
    
    """ Set Dilution """   
    def setDilution(self, value):
        self.parameters.text_dilution.SetValue()
    
    """ Set Date """   
    def setDate(self, value):
        self.parameters.text_date.SetValue()
    
    """ Set Volume """   
    def setVolume(self, value):
        self.parameters.text_volume.SetValue()
    
    """ Set Contaminant Concentration """   
    def setContaminantConcentration(self, value):
        self.parameters.text_contaminantConcentration.SetValue()
    
    """ Set Coagulant Concentration """   
    def setCoagulantConcentration(self, value):
        self.parameters.text_coagulantConcentration.SetValue()
    
    """ Set Objective X"""   
    def setObjectiveX(self, value):
        self.parameters.text_objectiveX.SetValue()
    
    """ Set Visual Area """   
    def setVisualArea(self, value):
        self.parameters.text_visualArea.SetValue()
    
    """ Set Voltage """   
    def setVoltage(self, value):
        self.parameters.text_volt.SetValue()
    
    """ Set Observations """   
    def setObservations(self, value):
        self.parameters.text_observations.SetValue()
    
    """ Set Input Browser Text """
    def setOutput(self, value):
        self.parameters.outputBrowser.fileText.SetValue(value)
     
    """ Set Size of Splitter of Image Panel and Parameters Panel """
    def setSplitterPanelSize(self, size):
        self.paramatersAndImageSplitter.SetSashPosition(size)
    
    """ Set Size of Splitter of Image Panel """
    def setSplitterImageSize(self, size):
        self.image.imageSplitter.SetSashPosition(size)
        
    
        
    
