venv:
		python3 -m venv .venv

venv-exit:
		deactivate

install:
		pip install pyo
		pip install wxPython
		pip install osc-gen

uninstall:
		pip uninstall pyo
		pip uninstall wxPython
		pip uninstall osc-gen