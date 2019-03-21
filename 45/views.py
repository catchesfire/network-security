from LFSRGenerator import LFSR
from PyQt5.QtWidgets import QGridLayout, QLabel, QLineEdit, QPlainTextEdit, QPushButton, QWidget


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
        self.show()
    
    def generate(self):
        #Todo: Sprawdzić, czy podany wielomian i seed jest w odpowiednim formacie.
        
        polynomial = self.polynomial_le.text()
        seed = self.seed_le.text()
        lfsr = LFSR()
        result = "\n".join(lfsr.generate_blocks(polynomial, seed))
        self.result_pte.setPlainText(result)