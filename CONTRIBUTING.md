# Contributing to Technical Documentation Scraper & Multi-Level Content Rewriter

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Development Process

We use GitHub to host code, to track issues and feature requests, as well as accept pull requests.

## Pull Requests

Pull requests are the best way to propose changes to the codebase. We actively welcome your pull requests:

1. Fork the repo and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. If you've changed APIs, update the documentation.
4. Ensure the test suite passes.
5. Make sure your code lints.
6. Issue that pull request!

## Development Setup

### Prerequisites
- Python 3.8+
- Azure OpenAI access
- Git

### Setup Steps

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/your-username/technical-doc-rewriter.git
   cd technical-doc-rewriter
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   pip install -r requirements-dev.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI details
   ```

5. **Set up pre-commit hooks**
   ```bash
   pre-commit install
   ```

## Code Style

### Python Style Guide
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [flake8](https://flake8.pycqa.org/) for linting
- Use [mypy](https://mypy.readthedocs.io/) for type checking

### Running Code Quality Tools

```bash
# Format code
black .

# Lint code
flake8 .

# Type check
mypy .

# Run all pre-commit hooks
pre-commit run --all-files
```

### Documentation
- Add docstrings to all public functions and classes
- Use Google-style docstrings
- Update README.md for any user-facing changes

Example docstring:
```python
def scrape_sections(url: str) -> List[Dict[str, Any]]:
    """
    Scrape sections from a documentation webpage.
    
    Args:
        url: The URL to scrape
        
    Returns:
        List of dictionaries containing section data
        
    Raises:
        requests.RequestException: If the webpage cannot be fetched
        ValueError: If the URL is invalid
    """
```

## Testing

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/test_scraper.py

# Run tests with verbose output
pytest -v
```

### Writing Tests
- Write tests for all new functions
- Use descriptive test names
- Test both success and failure cases
- Mock external API calls

Example test:
```python
import pytest
from unittest.mock import Mock, patch
from src.scraper import scrape_sections

def test_scrape_sections_success():
    """Test successful scraping of sections."""
    with patch('requests.get') as mock_get:
        mock_response = Mock()
        mock_response.text = '<html><main><h1>Test</h1><p>Content</p></main></html>'
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response
        
        result = scrape_sections('https://example.com')
        
        assert len(result) == 1
        assert result[0]['title'] == 'Test'
```

## Issue Reporting

### Bug Reports
Use the bug report template and include:
- A quick summary and/or background
- Steps to reproduce
- What you expected would happen
- What actually happens
- Sample code (if applicable)
- Environment details

### Feature Requests
Use the feature request template and include:
- Clear description of the feature
- Why you want/need this feature
- Possible implementation approach
- Any alternative solutions considered

## Project Structure

```
technical-doc-rewriter/
├── src/
│   ├── __init__.py
│   ├── scraper.py          # Web scraping functionality
│   ├── analyzer.py         # Difficulty analysis
│   ├── rewriter.py         # Content rewriting
│   ├── summarizer.py       # Content summarization
│   └── utils.py            # Utility functions
├── tests/
│   ├── __init__.py
│   ├── test_scraper.py
│   ├── test_analyzer.py
│   ├── test_rewriter.py
│   └── test_summarizer.py
├── examples/
│   ├── basic_usage.py
│   ├── batch_processing.py
│   └── web_api_example.py
├── docs/
│   ├── api_reference.md
│   ├── configuration.md
│   └── troubleshooting.md
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│   │   └── release.yml
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
├── requirements.txt
├── requirements-dev.txt
├── setup.py
├── README.md
├── CONTRIBUTING.md
├── LICENSE
└── .gitignore
```

## Coding Guidelines

### Function Design
- Keep functions small and focused
- Use type hints for all parameters and return values
- Handle errors gracefully
- Use descriptive variable names

### Error Handling
```python
# Good
try:
    result = risky_operation()
except SpecificException as e:
    logger.error(f"Operation failed: {e}")
    raise ProcessingError(f"Failed to process: {e}") from e

# Bad
try:
    result = risky_operation()
except:
    pass
```

### Logging
```python
import logging

logger = logging.getLogger(__name__)

def process_document(url: str) -> Dict[str, Any]:
    """Process a document from URL."""
    logger.info(f"Starting to process document: {url}")
    
    try:
        # Processing logic
        logger.debug("Processing step completed")
        return result
    except Exception as e:
        logger.error(f"Failed to process document {url}: {e}")
        raise
```

## Release Process

1. Update version in `setup.py`
2. Update `CHANGELOG.md`
3. Create a pull request with changes
4. After merge, create a new release on GitHub
5. GitHub Actions will automatically:
   - Run tests
   - Build package
   - Publish to PyPI (if configured)

## Getting Help

- **Documentation**: Check the [docs/](docs/) directory
- **Examples**: Look at [examples/](examples/) directory
- **Issues**: Search existing [GitHub Issues](https://github.com/yourusername/technical-doc-rewriter/issues)
- **Discussions**: Start a [GitHub Discussion](https://github.com/yourusername/technical-doc-rewriter/discussions)

## Code of Conduct

### Our Pledge
We pledge to make participation in our project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards
Examples of behavior that contributes to creating a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community

### Enforcement
Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project team. All complaints will be reviewed and investigated promptly and fairly.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## References

This document was adapted from the open-source contribution guidelines for [Facebook's Draft](https://github.com/facebook/draft-js/blob/main/CONTRIBUTING.md).
