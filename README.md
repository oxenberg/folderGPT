# TO RUN SERVER
Open terminal from the root directory of the project and run the following commands:
## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

Use the package manager to install local package

```bash
pip install -e .
```

run server
```bash
cd API
python -m uvicorn app:app --reload
```