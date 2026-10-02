.PHONY: help run run-verbose test clean format lint install

help:
	@echo "Parking Space Management System - Available Commands"
	@echo "======================================================"
	@echo ""
	@echo "Usage: make [command]"
	@echo ""
	@echo "Commands:"
	@echo "  make help          - Display this help message"
	@echo "  make run           - Run the parking management system"
	@echo "  make run-verbose   - Run the system with verbose output"
	@echo "  make test          - Run unit tests (placeholder)"
	@echo "  make clean         - Remove temporary files and cache"
	@echo "  make format        - Format code using black"
	@echo "  make lint          - Lint code using flake8"
	@echo "  make install       - Install development dependencies"
	@echo ""

run:
	@python3 main.py

run-verbose:
	@python3 -v main.py

test:
	@echo "Running tests..."
	@echo "Note: Test suite not yet implemented"

clean:
	@echo "Cleaning up temporary files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name ".DS_Store" -delete 2>/dev/null || true
	@rm -rf .pytest_cache 2>/dev/null || true
	@echo "Clean complete!"

format:
	@echo "Formatting code with black..."
	@python3 -m black . --exclude='.venv|.git' 2>/dev/null || echo "Note: Install black with: pip install black"

lint:
	@echo "Linting code with flake8..."
	@python3 -m flake8 . --exclude='.venv,.git,__pycache__' --max-line-length=100 2>/dev/null || echo "Note: Install flake8 with: pip install flake8"

install:
	@echo "Installing development dependencies..."
	@pip install black flake8 pytest -q
	@echo "Dependencies installed successfully!"
