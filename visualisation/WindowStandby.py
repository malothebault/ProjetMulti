# -*- coding: utf-8 -*-
# Fonctions permettant de mettre en pause et redémarer la fenêtre graphique Qt
#Elle devient inaccessible pendant que la fenêtre de visualisation est active


def PauseWindow(MyWidget, movie):
        MyWidget.Label_loader.setMovie(movie)
        MyWidget.Label_loader.show()
        print("Hey")
        movie.start()
        print("Yo")
        MyWidget.setEnabled(0)
        
        
def RestartWindow(MyWidget, movie):
        movie.stop()
        print("Yop")
        MyWidget.Label_loader.hide()
        MyWidget.setEnabled(1)        