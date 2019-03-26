from LFSRGenerator import LFSR
from SSCGenerator import SSC
from PyQt5.QtWidgets import QGridLayout, QFileDialog, QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QVBoxLayout, QWidget, QMainWindow

class MainView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()
    
    def interface(self):

        lfsr_btn = QPushButton("&LFSR", self)
        exit_btn = QPushButton("&Wyjście", self)

        lfsr_btn.clicked.connect(self.start_lfsr)

        box_layout = QVBoxLayout()

        box_layout.addWidget(lfsr_btn)
        box_layout.addWidget(exit_btn)

        grid_layout = QGridLayout()
        grid_layout.addWidget(QLabel("Wybierz, co chcesz uczynić", self), 0, 0)
        grid_layout.addLayout(box_layout, 1, 0)

        self.setLayout(grid_layout)

        self.setGeometry(20, 20, 500, 300)
        self.setWindowTitle("Generatory")

    def start_lfsr(self):
        lfsr_view = LFSRView(self)
        lfsr_view.show()

class SSCView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):

        # etykiety
        polynomial_label = QLabel("Podaj wielomian (np 1001):", self)
        seed_label = QLabel("Podaj seed (np 1001):", self)
        self.file_label = QLabel("", self)
        result_label = QLabel("Wynik", self)

        # pola edycyjne
        self.polynomial_le = QLineEdit()
        self.seed_le = QLineEdit()
        self.result_pte = QPlainTextEdit()
        self.result_pte.setReadOnly(True)

        # przyciski
        file_btn = QPushButton("Wybierz plik", self)
        file_btn.clicked.connect(self.openFileNameDialog)

        box_layout = QHBoxLayout()

        encrypt_btn = QPushButton("&Szyfruj", self)
        encrypt_btn.clicked.connect(self.encrypt)
        decrypt_btn = QPushButton("&Deszyfruj", self)
        decrypt_btn.clicked.connect(self.decrypt)

        box_layout.addWidget(encrypt_btn)
        box_layout.addWidget(decrypt_btn)

        # przypisanie widgetów do układu tabelarycznego
        grid_layout = QGridLayout()
        grid_layout.addWidget(polynomial_label, 0, 0)
        grid_layout.addWidget(self.polynomial_le, 0, 1)
        grid_layout.addWidget(seed_label, 1, 0)
        grid_layout.addWidget(self.seed_le, 1, 1)
        grid_layout.addWidget(self.file_label, 2, 1)
        grid_layout.addWidget(file_btn, 2, 0)
        grid_layout.addWidget(result_label, 3, 0)
        grid_layout.addWidget(self.result_pte, 4, 0, 5, 2)

        grid_layout.addLayout(box_layout, 10, 0, 2, 2)

        # przypisanie utworzonego układu do okna
        self.setLayout(grid_layout)

        self.setGeometry(20, 20, 500, 300)
        self.setWindowTitle("Synchronous Stream Cipher")
    
    def openFileNameDialog(self):
        self.source_file_path = None
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.file_label.setText(fileName)
            self.source_file_path = fileName

    def saveFileDialog(self):
        self.destination_file_path = None
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.destination_file_path = fileName

    def read_last_n_bits(self, n, file_name):
        f = open(file_name, "rb")
        f.seek(-n, 2)
        bits = f.read(n)
        f.close()

        last_bits = ""
        get_bin = lambda x: format(x, '08b')

        for i in range(len(bits)):
            last_bits += str(get_bin(bits[i]))

        return last_bits

    def encrypt(self):
        self.saveFileDialog()
        if self.destination_file_path and self.source_file_path:
            ssc = SSC()
            lfsr = LFSR()
            blocks = lfsr.generate_blocks(self.polynomial_le.text(), self.seed_le.text())
            # ssc.encrypt_n_decrypt(blocks, self.source_file_path, self.destination_file_path)
            ssc.encrypt(blocks, self.source_file_path, self.destination_file_path)

            result = "Ostatnie bity z pliku zrodlowego:\n"
            result += self.read_last_n_bits(3, self.source_file_path) + "\n\n"
            result += "Ostatnie bity z pliku docelowego:\n"
            result += self.read_last_n_bits(3, self.destination_file_path)

            self.result_pte.setPlainText(result)
    
    def decrypt(self):
        self.saveFileDialog()
        if self.destination_file_path and self.source_file_path:
            ssc = SSC()
            lfsr = LFSR()
            blocks = lfsr.generate_blocks(self.polynomial_le.text(), self.seed_le.text())
            # ssc.encrypt_n_decrypt(blocks, self.source_file_path, self.destination_file_path)
            ssc.decrypt(blocks, self.source_file_path, self.destination_file_path)

            result = "Ostatnie bity z pliku zrodlowego:\n"
            result += self.read_last_n_bits(3, self.source_file_path) + "\n\n"
            result += "Ostatnie bity z pliku docelowego:\n"
            result += self.read_last_n_bits(3, self.destination_file_path)

            self.result_pte.setPlainText(result)

    def generate(self):
        #Todo: Sprawdzić, czy podany wielomian i seed jest w odpowiednim formacie.
        
        polynomial = self.polynomial_le.text()
        seed = self.seed_le.text()
        lfsr = LFSR()
        result = "\n".join(lfsr.generate_blocks(polynomial, seed))
        self.result_pte.setPlainText(result)

class LFSRView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interface()

    def interface(self):

        # etykiety
        polynomial_label = QLabel("Podaj wielomian (np 1001):", self)
        seed_label = QLabel("Podaj seed (np 1001):", self)
        result_label = QLabel("Wynik", self)

        # pola edycyjne
        self.polynomial_le = QLineEdit()
        self.seed_le = QLineEdit()
        self.result_pte = QPlainTextEdit()
        self.result_pte.setReadOnly(True)

        # przyciski
        generate_btn = QPushButton("&Generuj", self)
        generate_btn.clicked.connect(self.generate)

        # przypisanie widgetów do układu tabelarycznego
        grid_layout = QGridLayout()
        grid_layout.addWidget(polynomial_label, 0, 0)
        grid_layout.addWidget(self.polynomial_le, 0, 1)
        grid_layout.addWidget(seed_label, 1, 0)
        grid_layout.addWidget(self.seed_le, 1, 1)
        grid_layout.addWidget(result_label, 2, 0)
        grid_layout.addWidget(self.result_pte, 3, 0, 5, 2)
        grid_layout.addWidget(generate_btn, 9, 0)

        # przypisanie utworzonego układu do okna
        self.setLayout(grid_layout)

        self.setGeometry(20, 20, 500, 300)
        self.setWindowTitle("Generator LFSR")
    
    def generate(self):
        #Todo: Sprawdzić, czy podany wielomian i seed jest w odpowiednim formacie.
        
        polynomial = self.polynomial_le.text()
        seed = self.seed_le.text()
        lfsr = LFSR()
        result = "\n".join(lfsr.generate_blocks(polynomial, seed))
        self.result_pte.setPlainText(result)