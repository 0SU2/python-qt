import os
from pathlib import Path


def compile_ui(ui_folder, ui_compiled_folder):
    """ Compile all Qt *.ui files to Python files *.py """
    ui_files = list(ui_folder.rglob("*.ui"))
    for file in ui_files:
        py_path = str(Path(ui_compiled_folder, file.with_suffix('.py').name))
        os.system(f"pyside2-uic {str(file)} -o {py_path} --from-imports {str(ui_compiled_folder)}")
    return


def compile_qrc(ui_folder, ui_compiled_folder):
    """ Compile all Qt *.qrc files to Python files *.py """
    qrc_files = list(ui_folder.rglob("*.qrc"))
    for qrc_file in qrc_files:
        py_path = str(Path(ui_compiled_folder, qrc_file.stem + "_rc.py"))
        os.system(f"pyside2-rcc {str(qrc_file)} -o {py_path}")
    return
