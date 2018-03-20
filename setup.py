#pyinstaller.exe --onefile --windowed --hidden-import pyexcel_io.readers.csvr --hidden-import pyexcel_io.readers.csvz --hidden-import pyexcel_io.readers.tsv --hidden-import pyexcel_io.readers.tsvz --hidden-import pyexcel_io.writers.csvw --hidden-import pyexcel_io.readers.csvz --hidden-import pyexcel_io.readers.tsv --hidden-import pyexcel_io.readers.tsvz --hidden-import pyexcel_io.database.importers.django --hidden-import pyexcel_io.database.importers.sqlalchemy --hidden-import pyexcel_io.database.exporters.django --hidden-import pyexcel_io.database.exporters.sqlalchemy --hidden-import pyexcel_xlsx --hidden-import pyexcel_xlsx.xlsxr --hidden-import pyexcel_xlsx.xlsxw --hidden-import pyexcel_xls --hidden-import pyexcel_xls.xlsr --hidden-import pyexcel_xls.xlsw POS.py

#cx_Freeze
import sys
import os
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'


# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = dict(
    packages = ["tkinter", "os", "xlrd", "xlsxwriter", "xlwt", "lxml" , "docx", "et_xmlfile", "openpyxl", "lml", "pyexcel_io", "pyexcel", "xlrd", "xlwt", "pyexcel_xls"],
    includes = ["pyexcel_io.readers.csvr",
    	"pyexcel_io.readers.csvz",
    	"pyexcel_io.readers.tsv",
    	"pyexcel_io.readers.tsvz",
    	"pyexcel_io.writers.csvw",
    	"pyexcel_io.readers.csvz",
    	"pyexcel_io.readers.tsv",
    	"pyexcel_io.readers.tsvz",
    	"pyexcel_io.database.importers.django",
    	"pyexcel_io.database.importers.sqlalchemy",
    	"pyexcel_io.database.exporters.django",
    	"pyexcel_io.database.exporters.sqlalchemy",
    	"pyexcel_xls",
    	"pyexcel_xls.xlsr",
    	"pyexcel_xls.xlsw"],
    excludes = [],
    include_files=[r'C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll',
    	r'C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll',
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\jdcal.py",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\texttable.py",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\datetime.py",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\easy_install.py",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pythoncom.py",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyWin32.chm",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pywin32.chm",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pywin32.pth",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pywin32_system32\pythoncom36.dll",
    	r"C:\Users\hedce\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\pywin32_system32\pywintypes36.dll"])

base = None 
if sys.platform=='win32':
	base = "Win32GUI"

setup(name='POS',
	version='1.1',
	description='Fixed bugs wherein packages haven\'t been fully imported',
    options = dict(build_exe = build_exe_options),
    executables = [Executable("POS.py", base = base)])


"""
datetime
time
win32com.client

"""