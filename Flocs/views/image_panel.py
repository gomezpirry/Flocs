#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/02/2017

@author: Augusto Gomez
'''
import wx, os, re


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
        dir_image = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images/'))
        
        # create bit map for Buttons
        bmpAddFolder = wx.BitmapFromImage(wx.Image(os.path.join(dir_image, 'addFolder.png')))
        bmpAddFile = wx.BitmapFromImage(wx.Image(os.path.join(dir_image, 'addFile.png')))
        bmpRemove = wx.BitmapFromImage(wx.Image(os.path.join(dir_image, 'remove.png')))
        
        # create image for TreeCtrl items 
        self.image_list = wx.ImageList(16, 16)
        self.imageSample = self.image_list.Add(wx.Image(os.path.join(dir_image, 'sample.png'), wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        self.imagePhoto  = self.image_list.Add(wx.Image(os.path.join(dir_image, 'image.png'), wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        
        # Create Buttons
        
        # Add file button
        self.button_addFolder = wx.BitmapButton(self.listPanel, wx.ID_ANY, bitmap = bmpAddFolder)
        # Add Folder Button
        self.button_addFile = wx.BitmapButton(self.listPanel, wx.ID_ANY, bitmap = bmpAddFile)
        self.button_addFile.Disable()
        #remove button
        self.button_remove = wx.BitmapButton(self.listPanel, wx.ID_ANY, bitmap = bmpRemove)
        self.button_remove.Disable()
        
        # tooltip for Button
        self.button_addFolder.SetToolTip(wx.ToolTip(u" Agregar Carpeta"))
        self.button_addFile.SetToolTip(wx.ToolTip(u" Agregar Archivo"))
        self.button_remove.SetToolTip(wx.ToolTip(u" Eliminar Carpeta o Archivo"))
        
        # Create File List
        self.list_files = wx.TreeCtrl(self.listPanel, wx.ID_ANY, style = wx.TR_DEFAULT_STYLE|wx.BORDER_SUNKEN|wx.TR_HIDE_ROOT|wx.TR_MULTIPLE)
        
        ### Add Root ### ----- CORREGIR
        self.root = self.list_files.AddRoot('Images')
        
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
    # ----------------  Auxiliar Functions -------------------
    # -------------------------------------------------------- 
    
    # Verify if parent Item (Sample Time) don't have images path 
    def verifyEmptySamples(self, item = None):
        itemList = []
        if item is None: 
            item = self.list_files.GetRootItem() 
        (child1 ,cookie1) = self.list_files.GetFirstChild(item) 
        while child1.IsOk(): 
            (child2,cookie2) = self.list_files.GetFirstChild(child1)
            # add item to list if parent Item (Sample Time) don't have children 
            if not child2:
                itemList.append(int(re.findall('\d+', self.list_files.GetItemText(child1))[0]))
            (child1, cookie1) = self.list_files.GetNextChild(item, cookie1)
        return itemList
     
    # Traverse TreeCtrl for obtaining only Parent Items (Sample Time)  
    def traverseRootTree(self, item = None): 
        itemList = []
        if item is None: 
            item = self.list_files.GetRootItem() 
        (child ,cookie) = self.list_files.GetFirstChild(item) 
        while child.IsOk(): 
            itemList.append(int(re.findall('\d+', self.list_files.GetItemText(child))[0]))
            (child, cookie) = self.list_files.GetNextChild(item, cookie)
        return itemList
     
    # Traverse TreeCtrl for obtaining all Items    
    def traverseTree(self, isRoot, item = None):
        itemList = []
        if item is None: 
            item = self.list_files.GetRootItem() 
        (child1 ,cookie1) = self.list_files.GetFirstChild(item) 
        # traverse Parent Items 
        while child1.IsOk(): 
            if isRoot:
                itemList.append(int(re.findall('\d+', self.list_files.GetItemText(child1))[0]))
            (child2 ,cookie2) = self.list_files.GetFirstChild(child1) 
            # traverse path images items
            while child2.IsOk():
                itemList.append(self.list_files.GetItemText(child2))
                (child2, cookie2) = self.list_files.GetNextChild(item, cookie2)
            (child1, cookie1) = self.list_files.GetNextChild(item, cookie1)
        return itemList
    
    # Add Items to TreeCtrl
    def addItem(self, root, paths):
        for path in paths:
            item = self.list_files.AppendItem(root, path ) 
            self.list_files.SetItemPyData(item, None)      
            self.list_files.SetItemImage(item, self.imagePhoto, wx.TreeItemIcon_Normal)
    
    # Load Image In ImagePanel
    def onView(self, path):
        panelWidth, panelHeight = self.imagePanel.GetSizeTuple()
        self.image = wx.Image(path, wx.BITMAP_TYPE_ANY).Rescale(panelWidth, panelHeight, wx.IMAGE_QUALITY_HIGH).ConvertToBitmap()
        wx.StaticBitmap(self.imagePanel, wx.ID_ANY, self.image)
        self.imagePanel.Refresh()
    
    # Set White Background to ImagePanel
    def removeImage(self):
        panelWidth, panelHeight = self.imagePanel.GetSizeTuple()
        image_blank = wx.EmptyBitmapRGBA(panelWidth, panelHeight, red=255, blue= 255, green= 255) 
        wx.StaticBitmap(self.imagePanel, wx.ID_ANY, image_blank)
        self.imagePanel.Refresh()
