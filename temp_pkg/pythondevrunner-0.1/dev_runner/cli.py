
import argparse
import os
from dev_runner.core import DevRunner, load_config

def main():
    parser = argparse.ArgumentParser(description="PythonDevRunner - Auto-reload Python apps on file changes.")
    parser.add_argument('--entry', type=str, help='Entry point Python file (e.g. main.py)', default='main.py')
    parser.add_argument('--watch-ext', type=str, nargs='+', default=['.py'], help='Extensions to watch')
    parser.add_argument('--exclude', type=str, nargs='+', default=[], help='Paths to exclude from watching')
    parser.add_argument('--debounce', type=float, default=0.5, help='Delay before restart (in seconds)')
    parser.add_argument('--config', type=str, help='Path to config JSON file')
    parser.add_argument('--quiet', action='store_true', help='Disable verbose output')

    args = parser.parse_args()

    if args.config:
        config = load_config(args.config)
        runner = DevRunner(
            entry=config.get('entry', 'main.py'),
            watch_exts=config.get('watch_ext', ['.py']),
            exclude=config.get('exclude', []),
            debounce=config.get('debounce', 0.5),
            verbose=not config.get('quiet', False)
        )
    else:
        runner = DevRunner(
            entry=args.entry,
            watch_exts=args.watch_ext,
            exclude=args.exclude,
            debounce=args.debounce,
            verbose=not args.quiet
        )

    runner.start()
