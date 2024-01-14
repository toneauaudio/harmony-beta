install:
		python3 -m venv .venv
		python3.9 -m pip install --upgrade pip
		pip install pyo
		pip install wxPython

uninstall:
		pip uninstall pyo
		pip uninstall wxPython
		deactivate