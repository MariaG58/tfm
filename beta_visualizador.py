# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'beta_visualizador.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtGui, QtWidgets, QtCore
from PySide2.QtWidgets import QFileDialog, QVBoxLayout, QGroupBox
from PySide2.QtCore import Qt
import pydicom
import numpy as np
import glob
import os
import json
from mainwin_visualizador import Ui_MainWindow
import pathlib
import fnmatch
import time  
from math import log
# from utils.maxValue import calculateMaxVal
def jsonKeys2int(x):
    if isinstance(x, dict):
        return {int(k):v for k,v in x.items()}
    return x

def extractLat(dicom_file):

    name_parts = dicom_file.split("_")
    lat = name_parts[1]
    orientation = name_parts[2].split(".")[0]
    return lat, orientation


def organizeDicoms(dicomlist):
    dicomFilesordered = ["","","",""]
    for dim in dicomlist:
        # print(dim)
        later, ori = extractLat(dim)
        # print("----------ESTA ES LA LATERALIDAD--------------")
        # print(later, ori)
        
        if(later == "L" and ori == "CC"):
            dicomFilesordered[0] = dim
        if(later == "R" and ori == "CC"):
            dicomFilesordered[1] = dim
        if(later == "L" and ori == "ML"):
            dicomFilesordered[2] = dim
        if(later == "R" and ori == "ML"):
            dicomFilesordered[3] = dim
                
    return dicomFilesordered

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.dicomFiles = list()
        self.dicomPath = ""
        self.curDicom = -1
        # self.max_val = None
        self.qImg = None
        self.qImg_L_CC = None
        self.qImg_R_CC = None
        self.qImg_L_ML = None
        self.qImg_R_ML = None
        self.zoomInFlag = False
        self.zoomOutFlag = False
        self.figRect = False
        self.figCirc = False
        self.valorMaximoDicom = 2624
        self.imageList = [] 
        self.ROIsList = {}
        self.currenIndexTab = -1
        self.move_enabled = False
        self.moving = False
        self.current_list_pos=[]
        self.patients =[]
        self.pacientes = []
        self.list_dicom_roi = {}
        self.sample_DICOM = None
        self.dicom_name = None
        self.imageCounter = 0
        self.scaleFactor = 1.0
        self.izq_cc_image = 0
        self.context_menu = QtWidgets.QMenu(self)
        borrarRoi = self.context_menu.addAction("Borrar Roi")
        borrarRoi.triggered.connect(self.borrarROI)
        cambiarEtiqueta = self.context_menu.addAction("Cambiar Etiqueta")
        cambiarEtiqueta.triggered.connect(self.cambiarEtiqueta)
        zoomIn = self.context_menu.addAction("Zoom In")
        zoomIn.triggered.connect(self.zoomIn)
        zoomOut = self.context_menu.addAction("Zoom Out")
        zoomOut.triggered.connect(self.zoomOut)


        self.tabList = [self.L_CC, self.R_CC,self.L_ML,self.R_ML]

        self.left_cc_image = QtWidgets.QLabel()
        self.right_cc_image = QtWidgets.QLabel()
        self.left_ml_image = QtWidgets.QLabel()
        self.right_ml_image = QtWidgets.QLabel()
        
        self.labels =[self.left_cc_image, self.right_cc_image,self.left_ml_image, self.right_ml_image]
        self.scrollImages = [self.left_cc_scroll_image,self.right_cc_scroll_image, self.left_ml_scroll_image,self.right_ml_scroll_image]


        self.AbrirDICOM.clicked.connect(self.loadDICOMDirectory)
        self.nextDICOMButton.clicked.connect(self.nextPatient)
        self.prevDICOMButton.clicked.connect(self.prevPatient)
        self.zoomInButton.clicked.connect(self.zoomIn)
        self.zoomOutButton.clicked.connect(self.zoomOut)
        self.imageSelector.currentChanged.connect(self.paintEvent)

        self.opcionesVisualizacion.clicked.connect(self.show_group_box)
        self.checkbox.stateChanged.connect(self.loadCurrentPatient)
        self.checkbox1.stateChanged.connect(self.loadCurrentPatient)
        self.checkbox2.stateChanged.connect(self.loadCurrentPatient)
        self.slider.valueChanged.connect(self.loadCurrentPatient)
        
        #self.zoomINButton.clicked.connect(self.zoomIn)
        #self.zoomOutButton.clicked.connect(self.zoomOut)


    def loadDICOMDirectory(self):
        self.dicomPath = QFileDialog.getExistingDirectory(self)    
        #print(self.dicomPath)
        if not (os.path.exists(self.dicomPath)):
            print(f"Error:{self.dicomPath} no existe o es erróneo.")
            return
        if not os.path.isdir(self.dicomPath):
            print(f"Error:{self.dicomPath} no es un directorio.")
            return
        print("El valor máximo de los dicom es: "+ str(self.valorMaximoDicom))
        
        self.patients = []
        for patient in os.listdir(self.dicomPath):
            print(patient)
            patient_path = os.path.join(self.dicomPath, patient)
            print(patient_path)
            images = os.listdir(patient_path)
            contador = 0
            for image in images:
                if image.endswith(".dcm"):
                    contador+=1
                
            if(contador == 4):
                # print("---Paciente válido---")
                # print(patient)
                
                # print("----ORDENANDO PACIENTE----")

                self.patients.append(patient)
        #     print("El número de elementos es: "+str(contador))
        # print("El número de pacientes válidos es: "+str(len(self.patients)))
        # print(self.patients)
        # print(self.patients[0])

        if len(self.patients)>0:
            self.curPatient = 0
            self.loadCurrentPatient()
        else:
            self.curPatient = -1

        
    def loadCurrentPatient(self):
        self.PatientName.setText("Patient:"+self.patients[self.curPatient])
        patient_path = os.path.join(self.dicomPath, self.patients[self.curPatient])
        self.dicomFiles = glob.glob((patient_path) +'/*.dcm')
        
        print(self.dicomFiles)
        dicomFilesordered = organizeDicoms(self.dicomFiles)
        
        
        jsonLoaded = False
        if(os.path.exists(patient_path+"/Rois.json")):
            print("JSON CARGADO")
            with open(patient_path+'/Rois.json')as json_file:
                self.list_dicom_roi = json.load(json_file)
                self.list_dicom_roi = jsonKeys2int(self.list_dicom_roi)
                print("-----EL JSON HA SIDO CARGAD0-----")
                print(self.list_dicom_roi)
                jsonLoaded = True


        if len(dicomFilesordered)>0:
            self.curDicom = 0
            
        else:
            print("----Error: La lista de dicoms está vacía----")
            self.curDicom = -1

        self.imageList = []
        
        for dcm in dicomFilesordered:
            self.dicomImgs = {}
            
            self.dicom = pydicom.dcmread(dcm)
            print("-----NOMBRE DEL DICOM-----")
            print(dcm)
            self.dicom_name = os.path.basename(dcm)
            print(self.dicom_name)
            
            dicom_lat = self.dicom_name.split('_', 1)
            print(dicom_lat) 
            
            lat_orientation = dicom_lat[1].rsplit(".")[0]
            print(lat_orientation)
            
            print(self.dicom)
            self.dicom_img = self.dicom.pixel_array
            image = self.dicom_img

            image1 = image

            try:
                max_val = self.dicom[0x0028,0x0107].value   
                min_val = self.dicom[0x0028,0x0106].value 
            except KeyError:
                max_val = np.max(image)
                min_val = np.min(image)

            try:
                if(self.dicom[0x2050,0x0020]).value == 'INVERSE':
                    image1 = max_val - image
                image = (image1/max_val*255).astype(np.uint8)

            except KeyError:
                image = (image/max_val*255).astype(np.uint8)
    
            # if state == Qt.Checked:
            if self.checkbox.isChecked():
                lut = np.zeros(max_val+1)
                for i in range(max_val+1):
                    lut[i] = max_val - i
                negativo = lut[image1] 
                image = (negativo/max_val*255).astype(np.uint8)
            
            self.slider.setMaximum(1000)
            self.slider.setMinimum(30)
            # self.slider.setValue(100)

            if self.checkbox1.isChecked():    
                lut = np.zeros(max_val+1)
                
                gamma = self.slider.value()/150
                for i in range(max_val+1):
                    lut[i] = max_val*(((i-min_val)/(max_val-min_val))**gamma)
                potencia = lut[image1]
                image = (potencia/max_val*255).astype(np.uint8)

            if self.checkbox2.isChecked():
                lut = np.zeros(max_val+1)
                for i in range(max_val+1):
                    lut[i] = max_val*log(1+((i-min_val)/(max_val-min_val)))
                    # lut[i] = (exp(i / maximo) - 1) * (maximo - minimo) + minimo
                logaritmo = lut[image1]
                image = (logaritmo/max_val*255).astype(np.uint8)

            print("  ")
            print("-------LA SAMPLE---------")
            print(self.sample_DICOM)
            
            if(jsonLoaded == False):
                self.sample_DICOM = None
                print("-------AQUI CREA LA DICOM-------")
                self.sample_DICOM ={}
                self.sample_DICOM["Nombre"] = self.dicom_name
                self.sample_DICOM["Anotacion"]=[]
                self.list_dicom_roi[self.curDicom] = self.sample_DICOM
            self.imageCounter += 1
            if(self.imageCounter%25 == 0):
                self.copiaSeguridad()

            self.h, self.w = image.shape


            
            self.qImg = QtGui.QImage(image,self.w,self.h,QtGui.QImage.Format_Grayscale8)
            self.qImg.convertTo(QtGui.QImage.Format_RGB888)
            
            self.dicomImgs["Lateralidad"] = lat_orientation
            self.dicomImgs["Imagen"] = self.qImg
            
            self.imageList.append(self.dicomImgs)

            self.curDicom+=1
            self.update()


    
    def nextPatient(self):
        if self.curPatient > -1:
            self.curPatient += 1
            self.curPatient %= len(self.patients)
            print(self.curPatient)
            # if (self.checkbox.isChecked()):
            self.loadCurrentPatient()
            # else:
            #     self.loadCurrentPatient(Qt.Unchecked)

    def prevPatient(self):
        if self.curPatient > -1:
            self.curPatient -= 1
            print("--"+str(self.curPatient)+"--")
            if self.curPatient< 0:
                self.curPatient = len(self.patients) - 1
                print(self.curPatient)
            # if (self.checkbox.isChecked()):
            self.loadCurrentPatient()
            # else:
                # self.loadCurrentPatient(Qt.Unchecked)
    
            
    def mousePressEvent(self, mouse_event):
        if mouse_event.button() == QtCore.Qt.LeftButton:
            
            self.initial_mouse_pos = mouse_event.pos()
            print(self.initial_mouse_pos)
            # self.initial_mouse_pos *= self.scaleFactor
            areaScrollarea = self.scrollImages[self.currenIndexTab].geometry()
            
            pointArea = QtCore.QPoint(areaScrollarea.x(),areaScrollarea.y())

            pArea = self.scrollImages[self.currenIndexTab].mapTo(self,pointArea)
            newArea = QtCore.QRect(pArea.x(), pArea.y(), areaScrollarea.width(), areaScrollarea.height())
            

            if(newArea.contains(self.initial_mouse_pos,True)):
                print("------Esta dentro-------")
                self.move_enabled = True
            
        if mouse_event.button() == QtCore.Qt.RightButton:
            self.initial_mouse_pos_borrar = mouse_event.pos()
            # self.initial_mouse_pos_borrar *= self.scaleFactor



    def mouseReleaseEvent(self, mouse_event):
        if self.move_enabled:
            self.final_mouse_pos = mouse_event.pos()
            # self.final_mouse_pos *= self.scaleFactor
            areaScrollarea = self.scrollImages[self.currenIndexTab].geometry()
            pointArea = QtCore.QPoint(areaScrollarea.x(),areaScrollarea.y())
            # pointArea *= self.scaleFactor
            pArea = self.scrollImages[self.currenIndexTab].mapTo(self,pointArea)
            newArea = QtCore.QRect(pArea.x(), pArea.y(), areaScrollarea.width(), areaScrollarea.height())
            

            if(newArea.contains(self.final_mouse_pos,True)):
                print("----release----")
                if self.moving == True:
                    self.saveROI()
                    self.guardarJSON()
                self.move_enabled = False
                self.moving = False


    def mouseMoveEvent(self, mouse_event):
        if self.move_enabled:
            self.moving = True
            self.new_mouse_pos = mouse_event.pos()
            # self.new_mouse_pos *= self.scaleFactor
            self.update()



    def paintEvent(self, e):
        qp = QtGui.QPainter()  

        self.currenIndexTab = self.imageSelector.currentIndex()
        currentTab = self.tabList[self.currenIndexTab]
        for dcom in self.imageList:
            # time.sleep(0)
            if(dcom["Lateralidad"] == currentTab.objectName()):
                if dcom["Imagen"] is not None:
                    actual_tab_image=QtGui.QPixmap.fromImage(dcom["Imagen"])
                    # actual_tab_image = actual_tab_image.scaled(actual_tab_image.width() * self.scaleFactor, actual_tab_image.height() * self.scaleFactor,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                    
                    qp.begin(actual_tab_image)
                    if self.move_enabled and self.moving:
                        image_ini_pos = self.labels[self.currenIndexTab].mapFrom(self, self.initial_mouse_pos)
                        image_new_pos = self.labels[self.currenIndexTab].mapFrom(self, self.new_mouse_pos)
                        # image_ini_pos = self.labels[self.currenIndexTab].mapFromGlobal(self.initial_mouse_pos)
                        # image_new_pos = self.labels[self.currenIndexTab].mapFromGlobal(self.new_mouse_pos)
                        print("----DIMENSIONES DEL RECTANGULO  POSICION----")
                        print(image_ini_pos, image_new_pos)
                        pen = QtGui.QPen(QtCore.Qt.red)
                        pen.setWidth(5)
                        qp.setPen(QtGui.QPen(pen))

                        
                        x = min(image_ini_pos.x(), image_new_pos.x())
                        y = min(image_ini_pos.y(), image_new_pos.y())
                        w1 = abs(image_ini_pos.x()-image_new_pos.x())
                        h1 = abs(image_ini_pos.y()-image_new_pos.y())

                        x = x/self.scaleFactor
                        y = y/self.scaleFactor
                        w1 = w1/self.scaleFactor
                        h1 = h1/self.scaleFactor
                        if self.comboBox_4.currentText() == "Rectangulo":
                            qp.drawRect(x, y, w1, h1)
                        if self.comboBox_4.currentText() == "Circulo":
                            qp.drawEllipse(x,y,w1,h1)
                        # print(x,y,w1,h1)
                        
                        self.current_list_pos = [x,y,w1,h1]
                        print(self.current_list_pos)
                    if(len(self.list_dicom_roi)!=0):
                        if(len(self.list_dicom_roi[self.currenIndexTab]["Anotacion"])>=0):
                            actual_tab_image = self.paintAnotations(actual_tab_image, qp)
                    qp.end()
                    actual_tab_image = actual_tab_image.scaled(actual_tab_image.width() * self.scaleFactor, actual_tab_image.height() * self.scaleFactor,aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
                    
                    self.labels[self.currenIndexTab].setPixmap(actual_tab_image)
                    self.scrollImages[self.currenIndexTab].setWidget(self.labels[self.currenIndexTab])
            
        
    def contextMenuEvent(self, event):
        self.context_menu.exec_(event.globalPos())        


    def closeEvent(self, event: QtGui.QCloseEvent):

        confirmation = QtWidgets.QMessageBox.question(self, "Confirmacion", "¿Seguro que quieres cerrar la aplicacion?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        
        if confirmation == QtWidgets.QMessageBox.Yes:
            # self.guardarJSON()
            self.group_box.close()
            event.accept()  
            
        else:
            event.ignore()  


    def zoomIn(self):
        
        self.scaleFactor *= 1.25
        print("Factor de escala:"+str(self.scaleFactor))
        self.update()
    def zoomOut(self):
        
        future_image = self.labels[self.currenIndexTab].pixmap().scaled(self.labels[self.currenIndexTab].pixmap().width() * (self.scaleFactor), self.labels[self.currenIndexTab].pixmap().height()*(self.scaleFactor)) 
        print(future_image.height(),self.scrollImages[self.currenIndexTab].geometry().height())
        if(future_image.height() >= self.scrollImages[self.currenIndexTab].geometry().height()):
            self.scaleFactor /= 1.25
            print("Factor de escala:"+str(self.scaleFactor))
        self.update()
    def resetZoom(self):
        self.scaleFactor = 1.0

    def saveROI(self):
        sample_anot = {}
        sample_anot["DescripcionLesion"] = self.comboBox.currentText()
        sample_anot["PatronGlandular"] = self.comboBox_2.currentText()
        sample_anot["Categoria"] = self.comboBox_3.currentText()
        if self.comboBox_4.currentText() == "Rectangulo":
            sample_anot["Rectangulo"] =  self.current_list_pos   
        if self.comboBox_4.currentText() == "Circulo":
            sample_anot["Circulo"] = self.current_list_pos
        print(sample_anot)

        print(self.currenIndexTab)
        print(self.curDicom)
        print(self.list_dicom_roi)
        self.list_dicom_roi[self.currenIndexTab]["Anotacion"].append(sample_anot)
        self.update()


    def paintAnotations(self,izq_cc_image, qp):
        
        for anot in self.list_dicom_roi[self.currenIndexTab]["Anotacion"]:
            ###POSIBLE CHECKEO DE QUE NO ESTÉ VACIO
            if(len(anot)!=0):
                key = list(anot.keys())[3]
                catkey = list(anot.values())[0]
                
                if key == "Rectangulo":
                    x = anot["Rectangulo"][0]
                    y = anot["Rectangulo"][1]
                    w = anot["Rectangulo"][2]
                    h = anot["Rectangulo"][3]
                if key == "Circulo":
                    x = anot["Circulo"][0]
                    y = anot["Circulo"][1]
                    w = anot["Circulo"][2]
                    h = anot["Circulo"][3]
                pen = QtGui.QPen()
                if catkey == "Nodulo":
                    pen = QtGui.QPen(QtCore.Qt.green)
                elif catkey == "Distorsion_arq":
                    pen = QtGui.QPen(QtCore.Qt.blue)
                elif catkey == "Densidad_asim_foc":
                    pen = QtGui.QPen(QtCore.Qt.cyan)
                elif catkey == "Microcalcificaciones":
                    pen = QtGui.QPen(QtCore.Qt.yellow)
                elif catkey == "Calc_tip_benig":  
                    pen = QtGui.QPen(QtCore.Qt.magenta)
                pen.setWidth(5)
                font = QtGui.QFont()
                font.setPointSize(20)
                
                qp.setPen(pen)
                qp.setFont(font)
                if key == "Rectangulo":
                    qp.drawRect(x, y, w, h)
                if key == "Circulo":
                    qp.drawEllipse(x,y,w,h)
                # qp.drawRect(x, y, w, h)
                qp.drawText(x, y-5, anot["DescripcionLesion"])
                qp.drawText(x+w+5, y+(h-35), anot["PatronGlandular"])
                qp.drawText(x+w+5, y+(h-5), anot["Categoria"])
        return izq_cc_image
        
    def borrarROI(self):
        
        for anot in self.list_dicom_roi[self.currenIndexTab]["Anotacion"]:
            
            key = list(anot.keys())[3]
            
            if key == "Rectangulo":
                x = anot["Rectangulo"][0]
                y = anot["Rectangulo"][1]
                w = anot["Rectangulo"][2]
                h = anot["Rectangulo"][3]
            if key == "Circulo":
                x = anot["Circulo"][0]
                y = anot["Circulo"][1]
                w = anot["Circulo"][2]
                h = anot["Circulo"][3]

            x = x * self.scaleFactor
            y = y * self.scaleFactor
            w= w * self.scaleFactor
            h = h * self.scaleFactor
            image_ini_pos_borrar = self.labels[self.currenIndexTab].mapFrom(self, self.initial_mouse_pos_borrar)
            limite_x = image_ini_pos_borrar.x()
            limite_y = image_ini_pos_borrar.y() 

            if((limite_x>=x and limite_x<=x+w)and(limite_y>=y and limite_y<=y+h)):
                self.list_dicom_roi[self.currenIndexTab]["Anotacion"].remove(anot)   
                self.guardarJSON()
                print(self.list_dicom_roi[self.currenIndexTab]["Anotacion"])
                self.update()
        print("Borrar Roi Pinchado.")


    def cambiarEtiqueta(self):
        for anot in self.list_dicom_roi[self.currenIndexTab]["Anotacion"]:
            key = list(anot.keys())[3]
            
            if key == "Rectangulo":
                x = anot["Rectangulo"][0]
                y = anot["Rectangulo"][1]
                w = anot["Rectangulo"][2]
                h = anot["Rectangulo"][3]
            if key == "Circulo":
                x = anot["Circulo"][0]
                y = anot["Circulo"][1]
                w = anot["Circulo"][2]
                h = anot["Circulo"][3]


            x = x * self.scaleFactor
            y = y * self.scaleFactor
            w = w * self.scaleFactor
            h = h * self.scaleFactor


            image_ini_pos_borrar = self.labels[self.currenIndexTab].mapFrom(self, self.initial_mouse_pos_borrar)
            limite_x = image_ini_pos_borrar.x()
            limite_y = image_ini_pos_borrar.y()   
            
            if((limite_x>=x and limite_x<=x+w)and(limite_y>=y and limite_y<=y+h)):
                anot["DescripcionLesion"] = self.comboBox.currentText()
                anot["PatronGlandular"] = self.comboBox_2.currentText()
                anot["Categoria"] = self.comboBox_3.currentText()
                self.guardarJSON()
                self.update()

    def show_group_box(self, event: QtGui.QCloseEvent):
        self.group_box.setVisible(True)

    
    # def negativo(self, state):
    #     if state == Qt.Checked:
    #         print(self.image)
    #         lut = np.zeros(self.max_val+1)
    #         for i in range(self.max_val+1):
    #             lut[i] = self.max_val - i
    #         negativo = lut[self.dicom_img] 
    #         self.image = (negativo/self.max_val*255).astype(np.uint8)
    #         print(self.image)
    #     else: 
    #         print("Nada")
    #     self.update()
        

    def guardarJSON(self):
        file_path = os.path.join(os.path.join(self.dicomPath,self.patients[self.curPatient]), "Rois.json")
        with open(file_path, 'w') as jsdicom:
            json.dump(self.list_dicom_roi,jsdicom, indent=4)


    def copiaSeguridad(self):
        if not (os.path.exists("./seguridad_Rois")):
            print("El directorio no existe, creando el directorio...")
            os.mkdir("./seguridad_Rois")

        file_path = os.path.join("./seguridad_Rois", "Rois"+str(self.imageCounter)+".json")
        with open(file_path, 'w') as jsdicom:
            json.dump(self.list_dicom_roi,jsdicom, indent=4)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())