# LLM Logs Viewer

A web interface for viewing and analyzing LLM conversation logs stored in SQLite databases.

## Features

- View conversation records in a scrollable list
- Display prompts and responses with full markdown rendering
- Categorize responses as ARBITER or MEMBER
- Real-time markdown preview using marked.js

## Setup

1. Clone the repository:
```bash
git clone https://github.com/irthomasthomas/llm-logs-viewer.git
cd llm-logs-viewer
```

2. Install requirements:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Configuration

The application expects an SQLite database at `~/.config/io.datasette.llm/logs.db`. This location can be modified in `app.py`.

## License

MIT License
