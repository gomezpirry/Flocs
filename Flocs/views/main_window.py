#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 18/02/2017

@author: Augusto Gomez
'''
import wx, os
from views.initial_panel import InitialPanel
from wx._windows_ import Frame_CreateToolBar

class MainWindow(wx.Frame):
    """ Main Window for the Application """
    def __init__(self,parent): 
        super(MainWindow, self).__init__(parent)  
        self.initUI() 
        
    """ Init UI Componenets """
    def initUI(self):
        
        # --------------------------------------------------------
        # -----------------  Create App Panels -------------------
        # --------------------------------------------------------
        
        # PanelNotebook
        self.panel_initial = InitialPanel(self, style = wx.BORDER_SUNKEN) 
        self.SetTitle('Floc Size ') 
        self.Centre() 
        
        # A Statusbar in the bottom of the window
        self.CreateStatusBar() 
    
        # --------------------------------------------------------
        # -------------------  Create Menus ----------------------
        # --------------------------------------------------------
        
        fileMenu = wx.Menu()
        editMenu = wx.Menu()
        helpMenu = wx.Menu()
        
        # --------------------------------------------------------
        # -------------------  Create Toolbar --------------------
        # --------------------------------------------------------
         
        self.toolbar = self.CreateToolBar()
        
        # --------------------------------------------------------
        # ------------------  Add items to Menu ------------------
        # --------------------------------------------------------
            
        # Add fileMenu items
        self.fMenuOpen = wx.MenuItem(fileMenu, wx.ID_ANY, "&Abrir", " Seleccionar Folder de Imagenes")
        self.fMenuOpen.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_MENU, (16, 16)))
        self.fMenuExit = wx.MenuItem(fileMenu, wx.ID_ANY, "&Salir", " Salir del Programa")
        self.fMenuExit.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_MENU, (16, 16)))
        
        fileMenu.AppendItem(self.fMenuOpen)
        fileMenu.AppendSeparator()
        fileMenu.AppendItem(self.fMenuExit)

        # Add editMenu items
        self.eMenuCopy = wx.MenuItem(editMenu, wx.ID_ANY, "&Copiar", " Copiar")
        self.eMenuCopy.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_COPY, wx.ART_MENU, (16, 16)))
        self.eMenuCut = wx.MenuItem(editMenu, wx.ID_ANY, "&Cortar", " Cortar")
        self.eMenuCut.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_CUT, wx.ART_MENU, (16, 16)))
        self.eMenuPaste = wx.MenuItem(editMenu, wx.ID_ANY, "&Pegar", " Pegar")
        self.eMenuPaste.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_PASTE, wx.ART_MENU, (16, 16)))        
        
        editMenu.AppendItem(self.eMenuCopy)
        editMenu.AppendItem(self.eMenuCut)
        editMenu.AppendItem(self.eMenuPaste)
        
        # Add helpMenu items
        self.hMenuHelp = wx.MenuItem(helpMenu, wx.ID_ANY, "&Ayuda", " Abrir Dialogo de Ayuda")
        self.hMenuHelp.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP, wx.ART_MENU, (16, 16)))
        self.hMenuAbout = wx.MenuItem(helpMenu, wx.ID_ANY, "&Acerca de", " Abrir Dialogo Acerce de la Aplicacion")
        self.hMenuAbout.SetBitmap(wx.ArtProvider.GetBitmap(wx.ART_HELP_BOOK, wx.ART_MENU, (16, 16)))
        
        helpMenu.AppendItem(self.hMenuHelp)
        helpMenu.AppendSeparator()
        helpMenu.AppendItem(self.hMenuAbout) 
        
        # --------------------------------------------------------
        # -----------------  Add items to toolbar ----------------
        # --------------------------------------------------------
        
        # Directory for image bitmap
        dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'images/'))
        
        # Create bitmap for toolbar icons
        bmpOpen = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'open.png')))
        bmpSave = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'save.png')))
        bmpStart = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'play.png')))
        bmpStop = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'stop.png')))
        bmpExit = wx.BitmapFromImage(wx.Image(os.path.join(dir, 'exit.png')))
        
        # Add toolbar items
        self.tool_open = self.toolbar.AddTool(101, bitmap = bmpOpen, shortHelpString = u' Abrir Sesión' )    
        self.tool_save = self.toolbar.AddTool(102, bitmap = bmpSave, shortHelpString = u' Guardar la Sesión') 
        self.toolbar.AddSeparator()
        self.tool_start = self.toolbar.AddTool(103, bitmap = bmpStart, shortHelpString = u' Iniciar Procesamiento') 
        self.tool_stop = self.toolbar.AddTool(104, bitmap = bmpStop, shortHelpString = u' Detener Procesamiento') 
        self.toolbar.AddSeparator()
        self.tool_exit = self.toolbar.AddTool(105, bitmap = bmpExit, shortHelpString = u' Salir de la Aplicación')   
                 
        # --------------------------------------------------------
        # ------------------  Add Bars to Window -----------------
        # --------------------------------------------------------
         
        # Creating the menuBar
        menuBar = wx.MenuBar()
        
        # Adding the Menus to the MenuBar
        menuBar.Append(fileMenu,"&Archivo") 
        menuBar.Append(editMenu,"&Editar")
        menuBar.Append(helpMenu,"&Ayuda")
             
        # Adding the MenuBar to the Frame content.
        self.SetMenuBar(menuBar) 
        
        #Add Toolbar
        self.toolbar.Realize()
        self.ToolBar = self.toolbar 
        
          
        
        
    
    
    

