# Contributing to AI Prompt Analyzer and Optimizer

Thank you for your interest in contributing to the AI Prompt Analyzer and Optimizer! This document provides guidelines for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and constructive in all interactions.

## How to Contribute

### Reporting Issues

- Use the GitHub issue tracker to report bugs or request features
- Search existing issues before creating a new one
- Provide clear, detailed descriptions with steps to reproduce bugs
- Include your environment details (OS, Python version, etc.)

### Submitting Changes

1. **Fork the repository** and create your branch from `main`
2. **Make your changes** with clear, descriptive commit messages
3. **Add tests** for any new functionality
4. **Update documentation** if needed
5. **Ensure all tests pass** by running `python test.py`
6. **Submit a pull request** with a clear description of changes

### Development Setup

1. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/ai-prompt-analyser.git
   cd ai-prompt-analyser
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run tests:
   ```bash
   python test.py
   ```

### Code Style

- Follow PEP 8 Python style guidelines
- Use meaningful variable and function names
- Add docstrings to all functions and classes
- Keep functions focused and concise
- Add type hints where appropriate

### Commit Message Guidelines

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Example:
```
Add support for custom scoring weights

- Allow users to configure different weights for analysis criteria
- Update config.json with new scoring_weights section
- Add validation for weight values

Fixes #123
```

## Areas for Contribution

### High Priority
- Additional analysis criteria and scoring improvements
- Better prompt optimization strategies
- Enhanced output formatting options
- Performance optimizations

### Medium Priority
- Additional export formats (PDF, HTML)
- Integration with popular AI platforms
- Batch processing improvements
- Web interface development

### Documentation
- Tutorial improvements
- API documentation
- Example use cases
- Video tutorials

## Testing

- Add unit tests for new functions
- Ensure existing tests continue to pass
- Test with various prompt types and edge cases
- Include tests for error handling

## Questions?

Feel free to open an issue with the "question" label if you need help or clarification on anything related to contributing.

Thank you for contributing! 🚀
