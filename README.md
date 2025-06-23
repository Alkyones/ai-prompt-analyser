# AI Prompt Analyzer and Optimizer

A Python application that analyzes user-provided prompts intended for AI models and provides optimized versions with detailed feedback.

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Prompt-Analyzer
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv ai-prompt-env
   # Windows
   ai-prompt-env\Scripts\activate
   # macOS/Linux
   source ai-prompt-env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python main.py --interactive
   ```

5. **Try a sample prompt**
   ```
   Enter: "Write a story about a robot"
   See the analysis and optimization results!
   ```

## Features

- **Comprehensive Analysis**: Evaluates prompts based on five key criteria:
  - **Clarity**: How clear and unambiguous the prompt is
  - **Specificity**: Level of detail and specific requirements
  - **Structure**: Organization and logical flow
  - **Context**: Background information and setting
  - **Creativity**: Encouragement of innovative responses

- **Smart Optimization**: Automatically improves prompts by:
  - Enhancing clarity and removing ambiguity
  - Adding specific requirements and constraints
  - Improving structure and organization
  - Providing context and background
  - Encouraging creative thinking

- **Detailed Feedback**: Provides:
  - Numerical scores (0-10) for each criterion
  - List of strengths in the original prompt
  - Identified weaknesses and areas for improvement
  - Actionable suggestions for future prompts

- **Multiple Usage modes**:
  - Interactive mode for real-time analysis
  - File processing for batch analysis
  - Command-line interface for single prompts
  - Export results in multiple formats (JSON, CSV, TXT)

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setting Up Virtual Environment (Recommended)

Using a virtual environment is highly recommended to avoid conflicts with other Python projects and to maintain clean dependencies.

#### Option 1: Using venv (Built-in Python module)

**Windows:**
```bash
# Navigate to the project directory
cd AI-Prompt-Analyzer

# Create virtual environment
python -m venv ai-prompt-env

# Activate virtual environment
ai-prompt-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

**macOS/Linux:**
```bash
# Navigate to the project directory
cd AI-Prompt-Analyzer

# Create virtual environment
python -m venv ai-prompt-env

# Activate virtual environment
source ai-prompt-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### Option 2: Using conda

```bash
# Create conda environment
conda create -n ai-prompt-env python=3.9

# Activate environment
conda activate ai-prompt-env

# Navigate to project directory
cd AI-Prompt-Analyzer

# Install dependencies
pip install -r requirements.txt
```

#### Option 3: Using virtualenv

```bash
# Install virtualenv if not already installed
pip install virtualenv

# Navigate to project directory
cd AI-Prompt-Analyzer

# Create virtual environment
virtualenv ai-prompt-env

# Activate virtual environment (Windows)
ai-prompt-env\Scripts\activate

# Activate virtual environment (macOS/Linux)
source ai-prompt-env/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Quick Installation (Without Virtual Environment)

If you prefer not to use a virtual environment:

1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Verifying Installation

To verify that everything is installed correctly:

```bash
# Test the installation
python main.py --help

# Run a quick test
python main.py --prompt "Test prompt" --verbose
```

### Deactivating Virtual Environment

When you're done working with the project:

```bash
# Deactivate the virtual environment
deactivate
```

### Reactivating Virtual Environment

Next time you want to use the project:

**Windows:**
```bash
cd AI-Prompt-Analyzer
ai-prompt-env\Scripts\activate
```

**macOS/Linux:**
```bash
cd AI-Prompt-Analyzer
source ai-prompt-env/bin/activate
```

## Usage

### Interactive Mode
```bash
python main.py --interactive
```

### Analyze a Single Prompt
```bash
python main.py --prompt "Your prompt here"
```

### Analyze Prompts from File
```bash
python main.py --file prompts.txt
```

### Save Analysis Report
```bash
python main.py --interactive --output report.json
python main.py --file prompts.txt --output report.csv
```

### Verbose Output
```bash
python main.py --prompt "Your prompt" --verbose
```

## Examples

### Example 1: Basic Prompt
**Original**: "Write a story about a robot."

**Optimized**: "Please write a comprehensive story about a robot who discovers emotions for the first time. 

Format: Please provide your response in a clear, structured format.

Length: Provide a comprehensive response with sufficient detail.

Context: You are an expert assistant helping with this task.

Purpose: This information will be used to provide accurate and helpful guidance.

Approach: Feel free to be creative and think of innovative solutions."

### Example 2: Business Query
**Original**: "Help me with my project."

**Optimized**: "Context: You are an expert assistant helping with this task.

Please help me with my web development project. I need specific guidance on technology selection and implementation best practices.

Format: Please provide your response in a clear, structured format.

Length: Provide a comprehensive response with sufficient detail.

Requirements:
- Be specific and detailed
- Include relevant examples
- Address all aspects of the request

Purpose: This information will be used to provide accurate and helpful guidance."

## File Structure

```
AI-Prompt-Analyzer/
├── main.py                 # Main application entry point
├── prompt_analyzer.py      # Core analysis logic
├── prompt_optimizer.py     # Optimization algorithms
├── utils.py               # Utility functions
├── config.json            # Configuration file (optional)
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── test.py               # Test cases
├── ai-prompt-env/        # Virtual environment (created during setup)
└── examples/             # Example prompts and outputs
    ├── sample_prompts.txt
    └── sample_analysis.json
```

## Troubleshooting

### Common Issues

#### 1. Python Version Compatibility
```bash
# Check Python version
python --version

# If you have multiple Python versions, try:
python3 --version
python3.9 --version
```

#### 2. Virtual Environment Issues

**Problem**: `python -m venv` command not found
**Solution**: 
```bash
# On Ubuntu/Debian
sudo apt-get install python3-venv

# On Windows, make sure Python was installed with pip and venv
```

**Problem**: Cannot activate virtual environment on Windows
**Solution**:
```bash
# Try using PowerShell instead of Command Prompt
# Or enable script execution:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

#### 3. Permission Issues

**Problem**: Permission denied when installing packages
**Solution**:
```bash
# Use --user flag to install in user directory
pip install --user -r requirements.txt

# Or on Windows, run command prompt as administrator
```

#### 4. Module Import Errors

**Problem**: "ModuleNotFoundError" when running the application
**Solution**:
```bash
# Make sure virtual environment is activated
# Check if you're in the correct directory
pwd  # or cd on Windows

# Reinstall requirements
pip install -r requirements.txt
```

### Getting Help

If you encounter issues:

1. **Check Python Version**: Ensure you have Python 3.7+
2. **Verify Virtual Environment**: Make sure it's activated (you should see `(ai-prompt-env)` in your terminal)
3. **Check Dependencies**: Run `pip list` to see installed packages
4. **Test Installation**: Use `python main.py --help` to verify the application loads
5. **Check File Paths**: Ensure you're in the correct directory

### Environment Variables

The application doesn't require environment variables, but you can optionally set:

```bash
# Optional: Set custom config file location
export AI_PROMPT_CONFIG=/path/to/your/config.json

# Windows
set AI_PROMPT_CONFIG=C:\path\to\your\config.json
```

## Analysis Criteria Explained

### Clarity (0-10)
- Measures how clear and unambiguous the prompt is
- Looks for specific language vs. vague terms
- Identifies ambiguous pronouns and complex sentences
- Rewards clear questions and direct instructions

### Specificity (0-10)
- Evaluates level of detail and specific requirements
- Checks for format, length, and style specifications
- Looks for examples and concrete criteria
- Rewards precise instructions and constraints

### Structure (0-10)
- Assesses organization and logical flow
- Checks for sections, bullet points, and headers
- Evaluates use of transition words and paragraphs
- Rewards well-organized, easy-to-follow prompts

### Context (0-10)
- Measures background information provided
- Looks for role definitions and purpose statements
- Checks for audience specification
- Rewards prompts that set clear expectations

### Creativity (0-10)
- Evaluates encouragement of innovative responses
- Looks for open-ended questions and multiple perspectives
- Balances constraints with creative freedom
- Rewards prompts that inspire original thinking

## Configuration

Create a `config.json` file to customize the analyzer:

```json
{
  "output_format": "text",
  "save_history": true,
  "verbose": false,
  "scoring_weights": {
    "clarity": 1.0,
    "specificity": 1.0,
    "structure": 1.0,
    "context": 1.0,
    "creativity": 1.0
  }
}
```

## Tips for Better Prompts

1. **Be Specific**: Include exact requirements, format, and constraints
2. **Provide Context**: Set the scene and define roles clearly
3. **Structure Well**: Use sections, bullet points, and clear organization
4. **Give Examples**: Show what you're looking for when helpful
5. **Define Terms**: Explain technical jargon or specific concepts
6. **Set Expectations**: Specify length, style, and audience
7. **Encourage Creativity**: Ask for alternatives and innovative approaches
8. **Test and Iterate**: Try different phrasings to see what works best

## Development

### Setting Up Development Environment

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd AI-Prompt-Analyzer
   ```

2. **Create development virtual environment**
   ```bash
   python -m venv ai-prompt-dev
   # Activate (Windows)
   ai-prompt-dev\Scripts\activate
   # Activate (macOS/Linux)
   source ai-prompt-dev/bin/activate
   ```

3. **Install development dependencies**
   ```bash
   pip install -r requirements.txt
   
   # Install optional development tools
   pip install pytest black flake8 mypy
   ```

4. **Run tests**
   ```bash
   python test.py
   # Or with pytest if installed
   pytest test.py
   ```

5. **Code formatting**
   ```bash
   # Format code with black
   black main.py prompt_analyzer.py prompt_optimizer.py utils.py
   
   # Check code style
   flake8 *.py
   
   # Type checking
   mypy *.py
   ```

### Project Architecture

- **main.py**: Entry point, handles CLI arguments and user interaction
- **prompt_analyzer.py**: Core analysis engine with scoring algorithms
- **prompt_optimizer.py**: Optimization logic and improvement suggestions
- **utils.py**: Helper functions for file I/O and configuration
- **config.json**: Configuration settings (optional)
- **test.py**: Unit tests and integration tests

### Adding New Features

1. **Analysis Criteria**: Add new scoring methods in `prompt_analyzer.py`
2. **Optimization Rules**: Add improvement patterns in `prompt_optimizer.py`
3. **Output Formats**: Extend export functionality in `utils.py`
4. **CLI Options**: Add new arguments in `main.py`

## Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Set up development environment (see Development section)
4. Make your changes
5. Run tests (`python test.py`)
6. Commit your changes (`git commit -m 'Add amazing feature'`)
7. Push to the branch (`git push origin feature/amazing-feature`)
8. Open a Pull Request

## License

This project is open source and available under the MIT License.
