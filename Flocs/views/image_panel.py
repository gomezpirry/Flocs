#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/02/2017

@author: Augusto Gomez
'''
import wx, os
import cv2

class ImagePanel(wx.Panel):
    """ Panel of Browser Files """
    def __init__(self, parent): 
        super(ImagePanel, self).__init__(parent)
        self.initUI()
     
    """ Init UI Componenets """
    def initUI(self): 
        # --------------------------------------
        # ----------    Create Sizers ----------
        # --------------------------------------  
        
        # Box Sizer for Panel
        panelBox = wx.BoxSizer() 
        # Box Sizer for  buttons
        buttonBox = wx.BoxSizer(wx.HORIZONTAL)
        # Box Sizer for buttons and List
        listButtonBox = wx.BoxSizer(wx.VERTICAL)        
        # Split Container for image and List 
        self.imageSplitter = wx.SplitterWindow(self, style = wx.SP_3DSASH|wx.SP_3DBORDER) 
        # panel for list image
        self.listPanel = wx.Panel(self.imageSplitter)
        # Static Box for Image and List
        imageBox = wx.StaticBox(self, wx.ID_ANY, u' Imágenes: ') 
        imageBoxSizer = wx.StaticBoxSizer(imageBox, wx.VERTICAL)     

        # --------------------------------------------------------
        # ------ Create Buttons, List and Image Container --------
        # --------------------------------------------------------
        
        #set dir for images
        dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images/'))
        
        # create bit map for Buttons
        bmpAddFolder = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'addFolder.png')))
        bmpAddFile = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'addFile.png')))
        bmpRemove = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'remove.png')))
        
        # Create Buttons
        
        # Add file button
        self.button_addFolder = wx.BitmapButton(self.listPanel, wx.ID_ANY, bitmap = bmpAddFolder, style = wx.BU_EXACTFIT)
        # Add Folder Button
        self.button_addFile = wx.BitmapButton(self.listPanel, wx.ID_ANY, bitmap = bmpAddFile, style = wx.BU_EXACTFIT)
        #remove button
        self.button_remove = wx.BitmapButton(self.listPanel, wx.ID_ANY, bitmap = bmpRemove, style = wx.BU_EXACTFIT)
        
        # tooltip for Button
        self.button_addFolder.SetToolTip(wx.ToolTip(u" Agregar Carpeta"))
        self.button_addFile.SetToolTip(wx.ToolTip(u" Agregar Archivo"))
        self.button_remove.SetToolTip(wx.ToolTip(u" Eliminar Carpeta o Archivo"))
        
        # Create File List
        self.list_files = wx.TreeCtrl(self.listPanel, wx.ID_ANY, style = wx.TR_DEFAULT_STYLE|wx.BORDER_SUNKEN)
       
        
        # Create Image Container
        self.imagePanel = wx.Panel(self.imageSplitter, wx.ID_ANY, style= wx.NO_BORDER)
        self.imagePanel.SetBackgroundColour('WHITE')
        
        # --------------------------------------------------------
        # -------------- Add Components to Sizers ----------------
        # -------------------------------------------------------- 
        
        buttonBox.Add(self.button_addFolder, 1, wx.ALIGN_CENTER)
        buttonBox.Add(self.button_addFile, 1, wx.ALIGN_CENTER)
        buttonBox.Add(self.button_remove, 1, wx.ALIGN_CENTER)
        
        listButtonBox.Add(buttonBox, 0, wx.ALIGN_TOP|wx.EXPAND)
        listButtonBox.Add(self.list_files, 1, wx.ALIGN_TOP|wx.EXPAND)
        
        self.listPanel.SetSizerAndFit(listButtonBox)
        
        
        # --------------------------------------------------------
        # --------------------  Add Sizers -----------------------
        # -------------------------------------------------------- 
        
        # Add list and image container to Sizer
        self.imageSplitter.SplitVertically(self.listPanel, self.imagePanel)
        self.imageSplitter.SetMinimumPaneSize(150) 
        
        # Add images Sizer to Panel Sizer
        imageBoxSizer.AddSpacer(10)
        imageBoxSizer.Add(self.imageSplitter, 1, wx.EXPAND, border = 20)
        panelBox.Add(imageBoxSizer, 1, wx.EXPAND, border = 20)
        
        # Add Sizer to panel
        self.SetSizerAndFit(panelBox)
                
    # --------------------------------------------------------
    # --------------------  Add Getters ----------------------
    # -------------------------------------------------------- 
    
     



    
    def onView(self, path):
        img = cv2.imread(path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        h, w = img.shape[:2]
        self.width = w
        self.height = h   
        rgbBmp = wx.BitmapFromBuffer(self.width, self.height, img)
        self.image = self.scale_bitmap(rgbBmp, self.width/4, self.width/4)
        self.imageCtrl.SetBitmap(self.image)
        self.Refresh()
        self.Update()
        
    def scale_bitmap(self, bitmap, width, height):
        image = wx.ImageFromBitmap(bitmap)
        image = image.Scale(width, height, wx.IMAGE_QUALITY_HIGH)
        result = wx.BitmapFromImage(image)
        return result    

