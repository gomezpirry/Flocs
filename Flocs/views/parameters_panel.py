#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/02/2017

@author: Augusto Gomez
'''

import wx, os
from views.browser_panel import BrowserPanel
from wx.lib.buttons import GenBitmapTextButton
from controller.validators import TextValidator, NumberValidator, BrowserValidator

class ParameterPanel(wx.Panel):
    """ Panel of Initial Parameters """
    def __init__(self,parent): 
        super(ParameterPanel, self).__init__(parent)  
        self.initUI()
        
    """ Init UI Componenets """
    def initUI(self):
        max_float = float("inf")
        min_float = float("-inf")
        
        # Create Validator Object
        self.validator_text = TextValidator()
        self.validator_number = NumberValidator()
        self.validator_browser = BrowserValidator()
        
        # --------------------------------------
        # ----------    Create Sizers ----------
        # --------------------------------------
        
        # Box Sizer for Panel
        panelBox = wx.BoxSizer(wx.VERTICAL) 
        # Grid Sizer for Parameters
        parameterSizer = wx.GridSizer(rows=13, cols=2, hgap=5, vgap=5)
        # Static Box for Parameters
        parameterBox = wx.StaticBox(self, wx.ID_ANY, u' Parámetros Iniciales: ') 
        parameterBoxSizer = wx.StaticBoxSizer(parameterBox, wx.VERTICAL)
        # Button Sizer
        buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # --------------------------------------
        # --- Create Init Button and browser ---
        # --------------------------------------
        
        # browser panel
        self.outputBrowser = BrowserPanel(self, u' Carpeta de Salida:', 'Carpeta de Salida')
        
        #set dir for images
        dir_image = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images/'))
    
        # Create bitmap for Buttons
        bmpPlay = wx.BitmapFromImage(wx.Image(os.path.join(dir_image, 'play.png')))
        
        # Init Button       
        self.initButton = GenBitmapTextButton(self, wx.ID_ANY, bitmap = bmpPlay, label= u' Iniciar')  
       
        
        # --------------------------------------------------------
        # ----------    Create Labels and Inputs Fields ----------
        # --------------------------------------------------------
        
        # Nombre de la Muestra (string)-(- , -)
        label_sampleName = wx.StaticText(self,  wx.ID_ANY, u' &Nombre de Muestra:')
        self.text_sampleName = wx.TextCtrl(self, wx.ID_ANY, style = wx.ALIGN_RIGHT, name = "Nombre de Muestra") 
        
        # Usuario (string)-(-,-)
        label_user = wx.StaticText(self,  wx.ID_ANY, u' &Usuario:')
        self.text_user = wx.TextCtrl(self, wx.ID_ANY, style = wx.ALIGN_RIGHT, name = "Usuario") 
        
        # Equipo de la muestra (string)-(-,-)
        label_equipment = wx.StaticText(self,  wx.ID_ANY, u' &Equipo de Muestreo:')
        self.text_equipment = wx.TextCtrl(self, wx.ID_ANY, style = wx.ALIGN_RIGHT, name = "Equipo de Muestra") 
        
        # Temperatura (Decimal)-(25.0, 80.0)
        label_temp = wx.StaticText(self,  wx.ID_ANY, u' &Temperatura (°C):')
        self.text_temp = wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="40", min = min_float, max = max_float, initial=40.0, inc=0.1, name = "Temperatura") 
        
        # Dilución (Decimal)-(0.0, 1.0)
        label_dilution = wx.StaticText(self,  wx.ID_ANY, u' &Dilución:')
        self.text_dilution =  wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="0", min = min_float, max = max_float, initial=0, inc=0.05, name = "Dilucion")
        
        # Fecha (Date)-()
        label_date = wx.StaticText(self,  wx.ID_ANY, u' &Fecha:')
        self.text_date = wx.DatePickerCtrl(self, wx.ID_ANY, style = wx.DP_DROPDOWN|wx.ALIGN_RIGHT, name = "Fecha") 
        
        # Volumen para toma de Imagenes (Decimal)-(0.5, 1000)
        label_volume = wx.StaticText(self,  wx.ID_ANY, u' &Volumen (ml):')
        self.text_volume =   wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="0.5", min = min_float, max = max_float, initial=0.5, inc=0.5, name = "Volumen")
        
        # Concentracion de contaminante (Decimal)-(0.0, 1000.0)
        label_contaminantConcentration = wx.StaticText(self,  wx.ID_ANY, u' &Concentración de contaminante:')
        self.text_contaminantConcentration = wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="0.5", min = min_float, max = max_float, initial=0.5, inc=0.5, name = "Contaminante")
        
        # Concentracion de cougalante estimado (Decimal)-(0.0, 1000.0)
        label_coagulantConcentration  = wx.StaticText(self,  wx.ID_ANY, u' &Concentración de coagulante:')
        self.text_coagulantConcentration = wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="0.5", min = min_float, max = max_float, initial=0.5, inc=0.5, name = "Coagulante") 
        
        # Objetivo X (Entero)-(10, 100)
        label_objectiveX = wx.StaticText(self,  wx.ID_ANY, u' &Objetivo X:')
        self.text_objectiveX = wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="10", min = min_float, max = max_float, initial=10, inc=1, name = "ObjetivoX") 
        
        # Area del Visual (Decimal)-(- , -)
        label_visualArea = wx.StaticText(self,  wx.ID_ANY, u' &Visual del área:')
        self.text_visualArea = wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="0", min = min_float, max = max_float, initial=0, inc=1, name = "Visual") 
        
        # Voltaje (Decimal)-(1.0, 10.0)
        label_volt = wx.StaticText(self,  wx.ID_ANY, u' &Voltaje (V):')
        self.text_volt = wx.SpinCtrlDouble(self, wx.ID_ANY, style=wx.SP_ARROW_KEYS|wx.ALIGN_RIGHT, value="1", min = min_float, max = max_float, initial=1, inc=0.1, name = "Voltaje") 
        
        # Observaciones (String)-()
        label_observations = wx.StaticText(self,  wx.ID_ANY, u' &Observaciones:')
        self.text_observations = wx.TextCtrl(self, wx.ID_ANY, size=(200,300), style = wx.TE_MULTILINE|wx.TE_LINEWRAP|wx.TE_PROCESS_ENTER, name = "Objetivos") 
        
        # --------------------------------------------------------
        # ----------  Add Labels and Inputs to Sizer -------------
        # --------------------------------------------------------        
        
        parameterSizer.Add(label_sampleName, 1, wx.EXPAND)
        parameterSizer.Add(self.text_sampleName, 1, wx.EXPAND)
        
        parameterSizer.Add(label_user, 1, wx.EXPAND)
        parameterSizer.Add(self.text_user, 1, wx.EXPAND)
        
        parameterSizer.Add(label_equipment, 1, wx.EXPAND)
        parameterSizer.Add(self.text_equipment, 1, wx.EXPAND)
        
        parameterSizer.Add(label_temp, 1, wx.EXPAND)
        parameterSizer.Add(self.text_temp, 1, wx.EXPAND)
        
        parameterSizer.Add(label_dilution, 1, wx.EXPAND)
        parameterSizer.Add(self.text_dilution, 1, wx.EXPAND)
        
        parameterSizer.Add(label_date, 1, wx.EXPAND)
        parameterSizer.Add(self.text_date, 1, wx.EXPAND)
        
        parameterSizer.Add(label_volume, 1, wx.EXPAND)
        parameterSizer.Add(self.text_volume, 1, wx.EXPAND)
        
        parameterSizer.Add(label_contaminantConcentration, 1, wx.EXPAND)
        parameterSizer.Add(self.text_contaminantConcentration, 1, wx.EXPAND)
        
        parameterSizer.Add(label_coagulantConcentration, 1, wx.EXPAND)
        parameterSizer.Add(self.text_coagulantConcentration, 1, wx.EXPAND)
        
        parameterSizer.Add(label_objectiveX, 1, wx.EXPAND)
        parameterSizer.Add(self.text_objectiveX, 1, wx.EXPAND)
        
        parameterSizer.Add(label_visualArea, 1, wx.EXPAND)
        parameterSizer.Add(self.text_visualArea, 1, wx.EXPAND)
        
        parameterSizer.Add(label_volt, 1, wx.EXPAND)
        parameterSizer.Add(self.text_volt, 1, wx.EXPAND)
        
        parameterSizer.Add(label_observations, 1, wx.EXPAND)
        parameterSizer.Add(self.text_observations, 0, wx.EXPAND)
        
        # --------------------------------------------------------
        # --------------------  Add Sizers -----------------------
        # --------------------------------------------------------  
        
        # Add Parameters Sizer to parameter Box
        parameterBoxSizer.AddSpacer(10)
        parameterBoxSizer.Add(parameterSizer, 1, wx.EXPAND, 20)
        
        # Add buttons to Sizer
        buttonSizer.Add(self.initButton, 1, wx.ALIGN_CENTER)
        buttonSizer.AddSpacer(10)        
        
        # Add browser and Parameters Sizer to Panel Sizer
        panelBox.Add(self.outputBrowser, 1, wx.EXPAND)
        panelBox.AddSpacer(15)
        panelBox.Add(wx.StaticLine(self), 1, wx.EXPAND)
        panelBox.AddSpacer(15)
        panelBox.Add(parameterBoxSizer, 1, wx.EXPAND, 20)
        panelBox.AddSpacer(10)
        panelBox.Add(wx.StaticLine(self), 1, wx.EXPAND)
        panelBox.AddSpacer(10)
        panelBox.AddSizer(buttonSizer, 0, wx.ALIGN_CENTER, 20)
        panelBox.AddSpacer(10)
        
        # Add panelSizer to Panel
        self.SetSizerAndFit(panelBox) 
    
    # Function for validating initial parameters
    def ValidateInputs(self):
        message = ""
        message = message + self.validator_browser.Validate(self.outputBrowser.fileText)
        message = message + self.validator_text.Validate(self.text_sampleName)
        message = message + self.validator_text.Validate(self.text_user)
        message = message + self.validator_number.Validate(self.text_temp, 25, 80)
        message = message + self.validator_number.Validate(self.text_dilution, 0, 1)
        message = message + self.validator_number.Validate(self.text_volume, 0.5, 1000)
        message = message + self.validator_number.Validate(self.text_contaminantConcentration, 0, 1000)
        message = message + self.validator_number.Validate(self.text_coagulantConcentration, 0, 1000)
        message = message + self.validator_number.Validate(self.text_objectiveX, 10, 100)
        message = message + self.validator_number.Validate(self.text_volt, 1, 10)
        return message
    
   

    
        
        