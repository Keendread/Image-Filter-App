import subprocess
import sys
import importlib

def auto_require(import_name, install_name = None):
    if install_name is None:
        install_name = import_name

    try:
        return importlib.import_module(import_name)
    except ImportError:
        print(f"[!] Module '{import_name}' missing. Attempting auto-installation of '{install_name}'")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", install_name])
            print(f"Successfully installed '{install_name}'.")
        except subprocess.CalledProcessError as e:
            print(f"[-] Failed to install package '{install_name}'. Error: {e}")
            raise
        
def startup():
    auto_require("cv2", "opencv-contrib-python")
    auto_require("numpy")
    auto_require("tkinter", "tkinter")
    auto_require("PIL", "Pillow")
    auto_require("Pyside6")

startup()

import cv2
import numpy as np
from tkinter import *  
from tkinter import filedialog  
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtCore import Qt, QFileInfo
from ui_mainwindow import Ui_MainWindow
from PIL import Image, ImageTk  


class ImageFilterApp:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Image Filter App")  

        # Widgets  
        self.load_btn = Button(root, text="Load Image", command=self.load_image)  
        self.filter_var = StringVar(value="Grayscale")  
        self.filter_menu = OptionMenu(root, self.filter_var, "Grayscale", "Gaussian Blur", "Canny Edge", command=self.apply_filter)  
        self.kernel_slider = Scale(root, from_=1, to=15, orient=HORIZONTAL, label="Kernel Size")  
        self.canvas_orig = Canvas(root, width=400, height=400)  
        self.canvas_filtered = Canvas(root, width=400, height=400)  

        # Layout  
        self.load_btn.pack()  
        self.filter_menu.pack()  
        self.kernel_slider.pack()  
        self.canvas_orig.pack(side=LEFT)  
        self.canvas_filtered.pack(side=RIGHT)  

    def load_image(self):  
        path = filedialog.askopenfilename()  
        self.image = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)  
        self.display_image(self.image, self.canvas_orig)  

    def apply_filter(self, _=None):  
        if not hasattr(self, 'image'): return  
        kernel = self.kernel_slider.get()  
        kernel = kernel + 1 if kernel % 2 == 0 else kernel  # Ensure odd kernel  

        choice = self.filter_var.get()  
        if choice == "Grayscale":  
            filtered = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)  
            filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)  
        elif choice == "Gaussian Blur":  
            filtered = cv2.GaussianBlur(self.image, (kernel, kernel), 0)  
        elif choice == "Canny Edge":  
            gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)  
            filtered = cv2.Canny(gray, 100, 200)  
            filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)  

        self.display_image(filtered, self.canvas_filtered)  

    def display_image(self, image, canvas):  
        image_pil = Image.fromarray(image)  
        image_tk = ImageTk.PhotoImage(image_pil)  
        canvas.create_image(0, 0, anchor=NW, image=image_tk)  
        canvas.image = image_tk  # Prevent garbage collection  
        

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.last_directory = ""
        
        # Connect slider value to apply_filter function and text label
        self.kernelSizeSlider.valueChanged.connect(self.snap_kernel_slider)
        self.kernelSizeSlider.valueChanged.connect(self.update_kernel_label)
        self.kernelSizeSlider.sliderReleased.connect(self.apply_filter)
        self.update_kernel_label(self.kernelSizeSlider.value())

        # Button connections (implement select_image and take_picture)
        self.selectImageButton.clicked.connect(self.select_image)        
        self.takeImageButton.clicked.connect(self.take_picture)
        
        # Connect filterSelector combobox to apply_filter function
        self.filterSelector.currentTextChanged.connect(self.apply_filter)

        # Setting up one scene per view
        self.sceneOriginal = QGraphicsScene(self)
        self.sceneFiltered = QGraphicsScene(self)
        self.graphicsViewOriginal.setScene(self.sceneOriginal)
        self.graphicsViewFilter.setScene(self.sceneFiltered)
     
    def snap_kernel_slider(self, value):
        value = value if value % 2 == 1 else value + 1
        self.kernelSizeSlider.setValue(value)    
        
    def update_kernel_label(self, value):
        value = value if value % 2 == 1 else value + 1
        self.kernelText.setText(f"Kernel Size: {value}")
        
    def select_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            self.last_directory,
            "Image Files (*.png *.jpg *.jpeg *.bmp)"
        ) 
        if file_path:
            self.last_directory = QFileInfo(file_path).absolutePath()
            self.image = cv2.cvtColor(cv2.imread(file_path), cv2.COLOR_BGR2RGB)
            self.display_image(self.image, self.sceneOriginal, self.graphicsViewOriginal)
            self.apply_filter()

    def display_image(self, cv_image, scene, view):
        height, width, channels = cv_image.shape
        bytes_per_line = channels*width

        q_image = QImage(cv_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_image)

        scene.clear()
        scene.addPixmap(pixmap)
        scene.setSceneRect(0, 0, width, height)

        view.fitInView(scene.sceneRect(), Qt.KeepAspectRatio)
    
    def apply_filter(self):
        if not hasattr(self, 'image'):
            return
        
        kernel = self.kernelSizeSlider.value()
        kernel = kernel if kernel % 2 == 1 else kernel + 1
        
        choice = self.filterSelector.currentText()
        match choice:
            case "Grayscale":
                filtered = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
                filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)
            case "Gaussian Blur":
                filtered = cv2.GaussianBlur(self.image, (kernel, kernel), 0)
            case "Canny Edge":
                gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
                filtered = cv2.Canny(gray, 100, 200)
                filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)
            case _:
                filtered = self.image
                
        self.display_image(filtered, self.sceneFiltered, self.graphicsViewFilter)
        
    def take_picture(self):
        ...

if __name__ == "__main__":
    #root = Tk()  
    #app = ImageFilterApp(root)  
    #root.mainloop()  

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())