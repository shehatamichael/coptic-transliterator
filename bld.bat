conda install -c conda-forge pynini
"%PYTHON%" setup.py install
if errorlevel 1 exit 1