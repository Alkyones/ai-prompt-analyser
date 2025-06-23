#!/bin/bash

# GitHub Release Creation Script
# Make sure you have GitHub CLI installed: https://cli.github.com/

VERSION="1.0.0"
REPO_NAME="ai-prompt-analyser"

# Trending tags for maximum visibility
TAGS="ai prompt-engineering nlp artificial-intelligence machine-learning python cli-tool text-analysis automation prompt-optimization"

echo "🚀 Creating GitHub release..."

# Create the release using GitHub CLI
gh release create "v${VERSION}" \
    --title "🎉 AI Prompt Analyzer and Optimizer v${VERSION}" \
    --notes-file release_notes.md \
    --draft \
    --latest

echo "✅ Draft release created! Visit GitHub to review and publish."
echo "📋 Suggested trending tags to add manually:"
echo "   ${TAGS}"

# Instructions for manual steps
echo ""
echo "📝 Next steps:"
echo "1. Visit your GitHub repository releases page"
echo "2. Edit the draft release"
echo "3. Add trending tags in the description"
echo "4. Attach any additional files if needed"
echo "5. Publish the release"
echo ""
echo "🏷️ Recommended topics for your repository:"
echo "Go to your repo → Settings → General → Topics and add:"
echo "ai, prompt-engineering, nlp, artificial-intelligence, machine-learning, python, cli-tool, text-analysis, automation, prompt-optimization"
