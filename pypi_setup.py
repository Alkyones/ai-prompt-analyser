#!/usr/bin/env python3
"""
PyPI Setup script for AI Prompt Analyzer and Optimizer
"""

from setuptools import setup, find_packages

# Read README for long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "AI Prompt Analyzer and Optimizer - A Python tool for analyzing and optimizing AI prompts"

# Read requirements
try:
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]
except FileNotFoundError:
    requirements = []

setup(
    name="ai-prompt-analyzer",
    version="1.0.0",
    author="Developer",
    author_email="your.email@example.com",
    description="A Python application that analyzes user-provided prompts for AI models and provides optimized versions with detailed feedback",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/username/ai-prompt-analyser",
    project_urls={
        "Bug Tracker": "https://github.com/username/ai-prompt-analyser/issues",
        "Documentation": "https://github.com/username/ai-prompt-analyser#readme",
        "Source Code": "https://github.com/username/ai-prompt-analyser",
        "Changelog": "https://github.com/username/ai-prompt-analyser/blob/main/CHANGELOG.md",
    },
    packages=find_packages(),
    py_modules=["main", "prompt_analyzer", "prompt_optimizer", "utils"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.900",
        ],
        "enhanced": [
            "colorama>=0.4.4",
            "rich>=12.0.0",
            "click>=8.0.0",
            "nltk>=3.7",
            "textstat>=0.7.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "prompt-analyzer=main:main",
            "ai-prompt-analyzer=main:main",
        ],
    },
    keywords=[
        "ai", "prompt-engineering", "nlp", "text-analysis", 
        "artificial-intelligence", "prompt-optimization", 
        "machine-learning", "python", "cli-tool", "automation",
        "language-models", "prompt-design", "ai-tools", "nlp-tools"
    ],
    include_package_data=True,
    package_data={
        "": ["*.md", "*.txt", "*.json", "examples/*"],
    },
    zip_safe=False,
)
