import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget,
    QTableWidgetItem, QComboBox
)
from PyQt5.QtCore import Qt


class MahasiswaApp(QWidget):
    def __init__(self):  # Perbaikan: __init__ bukan _init_
        super().__init__()
        self.setWindowTitle("MAHASISWA")
        self.setGeometry(100, 100, 800, 500)
        self.setupUI()

    def setupUI(self):
        layout = QVBoxLayout()

        # Label Judul
        title_label = QLabel("MAHASISWA")
        title_label.setStyleSheet("font-size: 18pt; font-weight: bold; background-color: lightcyan;")
        title_label.setFixedHeight(40)
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Form input
        grid = QGridLayout()
        self.inputs = {}

        # Data input yang pakai QLineEdit
        line_fields = ["NPM", "NAMA LENGKAP", "NAMA PANGGILAN", "TELEPON", "EMAIL"]
        for i, label in enumerate(line_fields):
            lbl = QLabel(label)
            line_edit = QLineEdit()
            self.inputs[label] = line_edit
            grid.addWidget(lbl, i, 0)
            grid.addWidget(line_edit, i, 1)

        # Data input yang pakai QComboBox
        combo_fields = {
            "KELAS": ["A", "B", "C", "D"],
            "MATAKULIAH": ["Pemrograman", "Jaringan", "Basis Data", "AI"],
            "LOKASI KAMPUS": ["Kampus A", "Kampus B", "Kampus C"]
        }

        for i, (label, options) in enumerate(combo_fields.items(), len(line_fields)):
            lbl = QLabel(label)
            combo = QComboBox()
            combo.addItems(options)
            self.inputs[label] = combo
            grid.addWidget(lbl, i, 0)
            grid.addWidget(combo, i, 1)

        layout.addLayout(grid)

        # Tombol aksi
        button_layout = QHBoxLayout()
        btn_tambah = QPushButton("TAMBAH")
        btn_ubah = QPushButton("UBAH")
        btn_hapus = QPushButton("HAPUS")
        btn_batal = QPushButton("BATAL")

        btn_tambah.clicked.connect(self.tambah_data)

        for btn in (btn_tambah, btn_ubah, btn_hapus, btn_batal):
            button_layout.addWidget(btn)

        layout.addLayout(button_layout)

        # Tabel
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "NPM", "NAMA LENGKAP", "NAMA PANGGILAN", "NO HP",
            "EMAIL", "KELAS", "MATKUL", "LOKASI KAMPUS"
        ])
        layout.addWidget(self.table)

        self.setLayout(layout)

    def tambah_data(self):
        row = self.table.rowCount()
        self.table.insertRow(row)

        keys = ["NPM", "NAMA LENGKAP", "NAMA PANGGILAN", "TELEPON", "EMAIL", "KELAS", "MATAKULIAH", "LOKASI KAMPUS"]
        for i, key in enumerate(keys):
            if isinstance(self.inputs[key], QLineEdit):
                value = self.inputs[key].text()
            elif isinstance(self.inputs[key], QComboBox):
                value = self.inputs[key].currentText()
            else:
                value = ""
            self.table.setItem(row, i, QTableWidgetItem(value))


if __name__ == "__main__":  # Perbaikan: nama == "__main__"
    app = QApplication(sys.argv)
    window = MahasiswaApp()
    window.show()
    sys.exit(app.exec_())
