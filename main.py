#!/usr/bin/env python3

import argparse
import os
from src.classes import MkDocsProfileGenerator
from src.config import Config
import shutil

import argparse
import os

class ArgumentParser:
    """
    A command line argument parser for a pipeline documentation tool.

    Args:
        config (object): An object containing configuration values for the pipeline documentation tool.

    Attributes:
        config (object): An object containing configuration values for the pipeline documentation tool.
        parser (argparse.ArgumentParser): An instance of the argparse.ArgumentParser class.

    Methods:
        setup_arguments(): Adds command line arguments to the parser.
        parse_args(): Parses command line arguments and returns the result.
    """

    def __init__(self, config=None):
        self.config = config
        self.parser = argparse.ArgumentParser(description="Your script description")
        self.setup_arguments()

    def setup_arguments(self):
        self.parser.add_argument("-e", "--example", action="store_true", help="Create example_command.sh")
        self.parser.add_argument("-g", "--github", default=self.config.GITHUB_URL, help="GitHub URL to your project/pipeline")
        self.parser.add_argument("-m", "--mkdocs_config", default=self.config.MKDOCS_YAML, help="project directory")
        self.parser.add_argument("-p", "--project_dir", default=os.getcwd(), help="project directory")
        self.parser.add_argument("-r", "--readthedocs_config", default=self.config.READTHEDOCS_YAML, help="project directory")
        self.parser.add_argument("-t", "--tool_descriptions", default=self.config.TOOL_DESCRIPTIONS, help="Tool Description Mapping file")
        self.parser.add_argument("-y", "--yaml", default=self.config.PIPELINE_YAML, help="Full path to the pipeline YAML file")
        self.parser.add_argument("-v", "--version", action="store_true", help="Print version")

    def parse_args(self):
        return self.parser.parse_args()

def main():
    """
    Entry point of the script. Parses command line arguments and generates documentation or other tasks based on the arguments.

    Args:
        None

    Returns:
        None
    """
    cfg = Config()
    arg_parser = ArgumentParser(cfg)
    args = arg_parser.parse_args()

    # Update the config with the arguments
    cfg.mkdocs = args.mkdocs_config
    cfg.readthedocs = args.readthedocs_config
    mkdocs_config = cfg.load_mkdocs()
    # readthedocs_config = cfg.load_readthedocs()

    if args.example:
        # Create example_command.sh
        example_command = f"python {__file__} -g {args.github} -y {args.yaml}"
        with open("example_command.sh", "w") as example_file:
            example_file.write(f"{example_command}\n")
        print(f"Created example_command.sh: {example_command}")
    elif args.version:
        print("Your script version")
    else:
        # Implement the logic for generating documentation or other tasks based on the arguments
        # Create the MkDocs profile
        mkdocs_profile = MkDocsProfileGenerator(args.project_dir, args.yaml, args.tool_descriptions, mkdocs_config)
        mkdocs_profile.generate()
    
        shutil.copyfile(cfg.readthedocs, os.path.join(args.project_dir, ".readthedocs.yaml"))
        shutil.copyfile(cfg.PYTHON_REQUIREMENTS, os.path.join(args.project_dir, "docs/requirements.txt"))


if __name__ == "__main__":
    main()
