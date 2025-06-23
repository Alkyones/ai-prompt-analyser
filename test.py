#!/usr/bin/env python3
"""
Test script for the AI Prompt Analyzer and Optimizer
"""

from prompt_analyzer import PromptAnalyzer
from prompt_optimizer import PromptOptimizer
from utils import create_sample_prompts, validate_prompt


def test_analyzer():
    """Test the prompt analyzer"""
    print("Testing Prompt Analyzer...")
    analyzer = PromptAnalyzer()
    
    test_prompts = [
        "Write a story about a robot.",
        "Please write a comprehensive 500-word story about a robot who discovers emotions for the first time. The story should be written for a young adult audience, include dialogue, and follow a clear three-act structure.",
        "Help me with my project.",
        "As an expert consultant, help me develop a detailed project plan for launching a mobile app. Include timeline, resources, budget considerations, and risk management strategies."
    ]
    
    for i, prompt in enumerate(test_prompts, 1):
        print(f"\nTest {i}: {prompt[:50]}...")
        analysis = analyzer.analyze(prompt)
        print(f"Scores - Overall: {analysis.overall_score:.1f}, Clarity: {analysis.clarity_score:.1f}, Specificity: {analysis.specificity_score:.1f}")


def test_optimizer():
    """Test the prompt optimizer"""
    print("\nTesting Prompt Optimizer...")
    analyzer = PromptAnalyzer()
    optimizer = PromptOptimizer()
    
    test_prompt = "Write a story about a robot."
    print(f"Original: {test_prompt}")
    
    analysis = analyzer.analyze(test_prompt)
    optimization = optimizer.optimize(test_prompt, analysis)
    
    print(f"Optimized: {optimization.optimized_prompt[:100]}...")
    print(f"Strengths: {optimization.strengths}")
    print(f"Weaknesses: {optimization.weaknesses}")


def test_validation():
    """Test prompt validation"""
    print("\nTesting Prompt Validation...")
    
    test_cases = [
        ("", "Empty prompt"),
        ("hi", "Too short"),
        ("Write a comprehensive analysis of the economic impacts of artificial intelligence", "Valid prompt"),
        ("test", "Test input"),
        ("a" * 11000, "Too long")
    ]
    
    for prompt, description in test_cases:
        is_valid, error = validate_prompt(prompt)
        print(f"{description}: {'Valid' if is_valid else f'Invalid - {error}'}")


if __name__ == "__main__":
    test_analyzer()
    test_optimizer()
    test_validation()
    print("\nAll tests completed!")
