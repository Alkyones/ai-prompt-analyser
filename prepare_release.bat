@echo off
REM GitHub Release Preparation Script for AI Prompt Analyzer (Windows)
REM This script helps prepare and create a GitHub release with trending tags

echo.
echo 🚀 GitHub Release Preparation for AI Prompt Analyzer and Optimizer
echo ================================================================
echo.

REM Project configuration
set PROJECT_NAME=AI Prompt Analyzer and Optimizer
set VERSION=1.0.0
set REPO_NAME=ai-prompt-analyser

REM Check if we're in a git repository
if not exist ".git" (
    echo ❌ Error: Not in a git repository
    echo Please run this script from the root of your git repository
    pause
    exit /b 1
)

echo ✅ Git repository detected

REM Check for uncommitted changes
git status --porcelain > temp_status.txt
for /f %%i in ("temp_status.txt") do set size=%%~zi
del temp_status.txt

if %size% gtr 0 (
    echo ⚠️  Warning: There are uncommitted changes
    git status --porcelain
    echo.
    set /p continue="Do you want to continue anyway? (y/n): "
    if /i not "%continue%"=="y" (
        echo Aborting release preparation
        pause
        exit /b 1
    )
)

echo 📋 Creating release information...

REM Generate release notes
(
echo # 🎉 AI Prompt Analyzer and Optimizer v%VERSION%
echo.
echo ## 🚀 What's New
echo.
echo Transform your AI prompts from good to great! This powerful Python tool analyzes and optimizes prompts for AI models, providing detailed feedback and suggestions.
echo.
echo ## ✨ Key Features
echo.
echo ### 🧠 Intelligent Analysis
echo - **5-Criteria Scoring System**: Clarity, Specificity, Structure, Context, and Creativity
echo - **Smart Pattern Recognition**: Detects ambiguous language, missing context, and optimization opportunities
echo - **Detailed Feedback**: Get specific strengths, weaknesses, and actionable suggestions
echo.
echo ### 🔧 Powerful Optimization
echo - **Automatic Improvements**: Enhances clarity, adds structure, provides context
echo - **Preserves Intent**: Maintains your original message while making it more effective
echo - **Customizable**: Configure scoring weights and optimization preferences
echo.
echo ### 💻 Flexible Usage
echo - **Interactive Mode**: Real-time prompt analysis and optimization
echo - **Batch Processing**: Analyze multiple prompts from files
echo - **Command Line**: Perfect for automation and scripting
echo - **Multiple Formats**: Export to JSON, CSV, or formatted text
echo.
echo ## 🎯 Perfect For
echo - **AI Engineers** optimizing model interactions
echo - **Content Creators** crafting better AI prompts
echo - **Researchers** studying prompt effectiveness
echo - **Educators** teaching prompt engineering
echo - **Developers** integrating prompt optimization
echo.
echo ## 🏷️ Trending Tags
echo `#ai` `#prompt-engineering` `#nlp` `#artificial-intelligence` `#machine-learning` `#python` `#cli-tool` `#text-analysis` `#automation` `#prompt-optimization`
echo.
echo ## 🚀 Quick Start
echo.
echo ```bash
echo # Interactive mode
echo python main.py --interactive
echo.
echo # Analyze a single prompt
echo python main.py --prompt "Your prompt here"
echo.
echo # Batch process from file
echo python main.py --file prompts.txt --output report.json
echo ```
echo.
echo ## 🛠️ Technical Highlights
echo - **Zero Dependencies**: Uses only Python standard library
echo - **Cross-Platform**: Works on Windows, macOS, and Linux
echo - **Python 3.7+**: Compatible with modern Python versions
echo - **Well-Tested**: Comprehensive test suite included
echo - **Extensible**: Modular architecture for easy customization
echo.
echo ---
echo.
echo **Ready to transform your AI prompts?** Download now and start creating more effective AI interactions! 🎯
) > release_notes.md

echo ✅ Release notes generated

REM Create GitHub CLI release command
(
echo @echo off
echo REM GitHub Release Creation Script
echo REM Make sure you have GitHub CLI installed: https://cli.github.com/
echo.
echo set VERSION=1.0.0
echo set REPO_NAME=ai-prompt-analyser
echo.
echo echo 🚀 Creating GitHub release...
echo.
echo REM Create the release using GitHub CLI
echo gh release create "v%%VERSION%%" --title "🎉 AI Prompt Analyzer and Optimizer v%%VERSION%%" --notes-file release_notes.md --draft --latest
echo.
echo echo ✅ Draft release created! Visit GitHub to review and publish.
echo echo 📋 Suggested trending tags to add manually:
echo echo    ai prompt-engineering nlp artificial-intelligence machine-learning python cli-tool text-analysis automation prompt-optimization
echo.
echo echo.
echo echo 📝 Next steps:
echo echo 1. Visit your GitHub repository releases page
echo echo 2. Edit the draft release
echo echo 3. Add trending tags in the description
echo echo 4. Attach any additional files if needed
echo echo 5. Publish the release
echo.
echo pause
) > create_release.bat

echo ✅ Release creation script generated

echo.
echo 📋 Release Preparation Complete!
echo ================================
echo.
echo Files created:
echo   📝 release_notes.md - Comprehensive release description
echo   🚀 create_release.bat - GitHub CLI release creation script
echo.
echo Next steps:
echo 1. Review the generated files
echo 2. Push all changes to GitHub
echo 3. Run: create_release.bat
echo 4. Follow the instructions for complete release process
echo.
echo 🏷️ Trending tags ready for maximum visibility!
echo.
echo Happy releasing! 🎉
echo.
pause
