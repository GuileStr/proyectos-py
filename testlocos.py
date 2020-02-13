# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 14:50:45 2020

@author: palar
"""

import webbrowser
#Abrir pagina nueva
webbrowser.open("http://www.python.org", new=2, autoraise=True)
#Pestaña nueva
webbrowser.open_new_tab("https://www.python.org/psf-landing/")
#Pagina nueva en navegador preferido
nav1 = webbrowser.get("Opera")
nav1.open("www.elpais.es")

#CMD 
#python -m webbrowser -t "http://www.python.org"