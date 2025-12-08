# mama-ai Patch v1.1.1

This patch adds:

- Absolute imports (`from src...`) to avoid relative-import issues.
- Run scripts for API and UI:
  - `run_api.sh`, `run_ui.sh` (macOS / Linux)
  - `run_api.bat`, `run_ui.bat` (Windows)
- A basic `tests/` folder with `pytest` sanity checks for the model.

## Running the demo

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the API

On macOS / Linux:

```bash
./run_api.sh
```

On Windows:

```bat
run_api.bat
```

The API will start at `http://127.0.0.1:8000`.  
Open `http://127.0.0.1:8000/docs` to try `/predict`.

### 3. Run the Streamlit UI

On macOS / Linux:

```bash
./run_ui.sh
```

On Windows:

```bat
run_ui.bat
```

A browser window will open. Type any text and hit **Run demo** to see the
Hugging Face sentiment model in action.

### 4. Run tests

```bash
pytest
```
