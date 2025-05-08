# PythonDevRunner

Auto-reload your Python app when source files change. Useful for development of web servers, CLI tools, or any script-driven workflow.

## 🚀 Features

- Watches for changes in `.py` files
- Automatically restarts your app
- Logs the **exact file** that triggered the restart
- Configurable via CLI or JSON file
- Cross-platform support

## 🛠 Installation

### 📦 From PyPI

```bash
pip install PythonDevRunner
```

### 🧪 From source

```bash
git clone https://github.com/mrjulesfletcher/PythonDevRunner.git
cd PythonDevRunner
pip install .
```

## 💡 Usage

### CLI

```bash
devrunner --entry main.py --watch-ext .py --exclude venv __pycache__ --debounce 0.5
```

### Config file

```bash
devrunner --config examples/config.json
```

## 🔧 Configuration Options

| Option       | CLI Flag       | Config Key   | Default    |
|--------------|----------------|--------------|------------|
| Entry script | `--entry`      | `entry`      | `main.py`  |
| Extensions   | `--watch-ext`  | `watch_ext`  | `[".py"]`  |
| Exclude      | `--exclude`    | `exclude`    | `[]`       |
| Debounce     | `--debounce`   | `debounce`   | `0.5`      |
| Verbose      | `--quiet`      | `quiet`      | `false`    |

## 📝 Example Output

```text
[Watcher] File changed: /myproject/chat_panel.py
[Runner] Restart triggered by: /myproject/chat_panel.py
[Runner] Launching main.py
```

## 📦 Packaging

Supports installation via `pip install .` or from [PyPI](https://pypi.org/project/PythonDevRunner/).

---

## License

MIT

---

### Author

Created with ❤️ by **Jules Le Masson**  
[github.com/mrjulesfletcher](https://github.com/mrjulesfletcher)