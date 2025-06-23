#!/usr/bin/env python3
"""
AI Prompt Analyzer and Optimizer

A Python application that analyzes user-provided prompts for AI models
and provides optimized versions with detailed feedback.
"""

import re
import argparse
from typing import Dict, List, Tuple
from dataclasses import dataclass
from prompt_analyzer import PromptAnalyzer
from prompt_optimizer import PromptOptimizer
from utils import load_config, save_analysis_report


@dataclass
class AnalysisResult:
    """Data structure to hold analysis results"""
    original_prompt: str
    optimized_prompt: str
    clarity_score: float
    specificity_score: float
    structure_score: float
    context_score: float
    creativity_score: float
    overall_score: float
    strengths: List[str]
    weaknesses: List[str]
    suggestions: List[str]


def main():
    """Main entry point for the application"""
    parser = argparse.ArgumentParser(
        description="AI Prompt Analyzer and Optimizer",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --interactive
  python main.py --file prompts.txt
  python main.py --prompt "Write a story about a robot"
        """
    )
    
    parser.add_argument(
        '--interactive', '-i',
        action='store_true',
        help='Run in interactive mode'
    )
    
    parser.add_argument(
        '--file', '-f',
        type=str,
        help='Path to file containing prompt(s) to analyze'
    )
    
    parser.add_argument(
        '--prompt', '-p',
        type=str,
        help='Direct prompt to analyze'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        help='Output file path for analysis report'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Enable verbose output'
    )
    
    args = parser.parse_args()
    
    # Initialize analyzer and optimizer
    analyzer = PromptAnalyzer()
    optimizer = PromptOptimizer()
    
    if args.interactive:
        run_interactive_mode(analyzer, optimizer, args.verbose)
    elif args.file:
        analyze_from_file(analyzer, optimizer, args.file, args.output, args.verbose)
    elif args.prompt:
        analyze_single_prompt(analyzer, optimizer, args.prompt, args.output, args.verbose)
    else:
        print("No input provided. Use --help for usage information.")
        print("Quick start: python main.py --interactive")


def run_interactive_mode(analyzer: PromptAnalyzer, optimizer: PromptOptimizer, verbose: bool = False):
    """Run the application in interactive mode"""
    print("=== AI Prompt Analyzer and Optimizer ===")
    print("Enter your prompt for analysis (press Enter twice to finish):")
    print("Type 'quit' to exit.\n")
    
    while True:
        lines = []
        print("Prompt: ", end="")
        
        while True:
            try:
                line = input()
                if line.lower().strip() == 'quit':
                    print("Goodbye!")
                    return
                if line == "" and lines:
                    break
                lines.append(line)
            except KeyboardInterrupt:
                print("\nGoodbye!")
                return
        
        if not lines:
            continue
            
        prompt = "\n".join(lines)
        result = analyze_and_optimize_prompt(analyzer, optimizer, prompt)
        display_analysis_result(result, verbose)
        print("\n" + "="*60 + "\n")


def analyze_from_file(analyzer: PromptAnalyzer, optimizer: PromptOptimizer, 
                     **kwargs):
    """Analyze prompts from a file"""
    file_path = kwargs.get('file_path')
    output_path = kwargs.get('output_path')
    verbose = kwargs.get('verbose', False)

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        
        # Split by double newlines to handle multiple prompts
        prompts = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        results = []
        for i, prompt in enumerate(prompts, 1):
            print(f"Analyzing prompt {i}/{len(prompts)}...")
            result = analyze_and_optimize_prompt(analyzer, optimizer, prompt)
            results.append(result)
            
            if len(prompts) == 1 or verbose:
                display_analysis_result(result, verbose)
        
        if output_path:
            save_analysis_report(results, output_path)
            print(f"Analysis report saved to: {output_path}")
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error reading file: {e}")


def analyze_single_prompt(analyzer: PromptAnalyzer, optimizer: PromptOptimizer,
                         **kwargs):
    """Analyze a single prompt provided via command line"""
    prompt = kwargs.get('prompt')
    output_path = kwargs.get('output_path')
    verbose = kwargs.get('verbose', False)

    result = analyze_and_optimize_prompt(analyzer, optimizer, prompt)
    display_analysis_result(result, verbose)
    
    if output_path:
        save_analysis_report([result], output_path)
        print(f"Analysis report saved to: {output_path}")


def analyze_and_optimize_prompt(analyzer: PromptAnalyzer, optimizer: PromptOptimizer, 
                               prompt: str) -> AnalysisResult:
    """Analyze and optimize a prompt"""
    # Analyze the prompt
    analysis = analyzer.analyze(prompt)
    
    # Optimize the prompt
    optimized = optimizer.optimize(prompt, analysis)
    
    # Create result object
    result = AnalysisResult(
        original_prompt=prompt,
        optimized_prompt=optimized.optimized_prompt,
        clarity_score=analysis.clarity_score,
        specificity_score=analysis.specificity_score,
        structure_score=analysis.structure_score,
        context_score=analysis.context_score,
        creativity_score=analysis.creativity_score,
        overall_score=analysis.overall_score,
        strengths=optimized.strengths,
        weaknesses=optimized.weaknesses,
        suggestions=optimized.suggestions
    )
    
    return result


def display_analysis_result(result: AnalysisResult, verbose: bool = False):
    """Display the analysis result in a formatted way"""
    print("="*60)
    print("PROMPT ANALYSIS RESULTS")
    print("="*60)
    
    if verbose:
        print(f"\nORIGINAL PROMPT:")
        print("-" * 20)
        print(f"{result.original_prompt}\n")
    
    print(f"OPTIMIZED PROMPT:")
    print("-" * 20)
    print(f"{result.optimized_prompt}\n")
    
    print(f"ANALYSIS SCORES:")
    print("-" * 20)
    print(f"Overall Score:     {result.overall_score:.1f}/10")
    print(f"Clarity:          {result.clarity_score:.1f}/10")
    print(f"Specificity:      {result.specificity_score:.1f}/10")
    print(f"Structure:        {result.structure_score:.1f}/10")
    print(f"Context:          {result.context_score:.1f}/10")
    print(f"Creativity:       {result.creativity_score:.1f}/10")
    
    print(f"\nSTRENGTHS:")
    print("-" * 20)
    for strength in result.strengths:
        print(f"• {strength}")
    
    print(f"\nWEAKNESSES:")
    print("-" * 20)
    for weakness in result.weaknesses:
        print(f"• {weakness}")
    
    print(f"\nSUGGESTIONS FOR IMPROVEMENT:")
    print("-" * 20)
    for suggestion in result.suggestions:
        print(f"• {suggestion}")


if __name__ == "__main__":
    main()
