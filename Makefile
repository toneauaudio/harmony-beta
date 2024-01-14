install:
		python3 -m venv .venv
		pip install pyo
		pip install wxPython

uninstall:
		pip uninstall pyo
		pip uninstall wxPython
		deactivate