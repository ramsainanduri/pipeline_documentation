#!/usr/bin/env python3

import yaml

class Config:
    """
    A class for managing configuration settings for the pipeline documentation project.

    Attributes:
        MKDOCS_YAML (str): The file path for the default mkdocs.yaml configuration file.
        READTHEDOCS_YAML (str): The file path for the default readthedocs.yaml configuration file.
        TOOL_DESCRIPTIONS (str): The file path for the tool descriptions TSV file.
        PIPELINE_YAML (str): The file path for the pipeline YAML template file.
        GITHUB_URL (str): The URL for the GitHub repository for the pipeline documentation project.
        GITHUB_PAGES_YAML (str): The file path for the default GitHub Pages configuration file.
        PYTHON_REQUIREMENTS (str): The file path for the Python requirements file.
        EXTRA_CSS (str): The file path for the extra CSS file.

    Methods:
        __init__(self, mkdocs=None, readthedocs=None): Initializes a new Config instance with optional mkdocs and readthedocs file paths.
        load_mkdocs(self): Loads the mkdocs configuration file and returns its contents as a dictionary.
        load_readthedocs(self): Loads the readthedocs configuration file and returns its contents as a dictionary.
        load_yaml(self, file_path): Loads a YAML file at the specified file path and returns its contents as a dictionary.
    """

    MKDOCS_YAML = 'configs/default.mkdocs.yml'
    READTHEDOCS_YAML = 'configs/default.readthedocs.yaml'
    TOOL_DESCRIPTIONS = 'static/files/tool_descriptions.tsv'
    PIPELINE_YAML = 'static/templates/pipeline.yaml'
    GITHUB_URL = 'https://github.com/ramsainanduri/pipeline_documentation'
    GITHUB_PAGES_YAML = 'configs/default.github.pages.yaml'
    PYTHON_REQUIREMENTS = 'static/files/requirements.txt'
    EXTRA_CSS = 'static/css/extra.css'

    def __init__(self, mkdocs=None, readthedocs=None):
        """
        Initializes a new Config instance with optional mkdocs and readthedocs file paths.

        Args:
            mkdocs (str, optional): The file path for the mkdocs configuration file. Defaults to None.
            readthedocs (str, optional): The file path for the readthedocs configuration file. Defaults to None.
        """
        self.mkdocs = mkdocs
        self.readthedocs = readthedocs

    def load_mkdocs(self):
        """
        Loads the mkdocs configuration file and returns its contents as a dictionary.

        Returns:
            dict: The contents of the mkdocs configuration file as a dictionary.
        """
        if self.mkdocs:
            return self.load_yaml(self.mkdocs)
        else:
            return None
    
    def load_readthedocs(self):
        """
        Loads the readthedocs configuration file and returns its contents as a dictionary.

        Returns:
            dict: The contents of the readthedocs configuration file as a dictionary.
        """
        if self.readthedocs:
            return self.load_yaml(self.readthedocs)
        else:
            return None
    
    def load_yaml(self, file_path):
        """
        Loads a YAML file at the specified file path and returns its contents as a dictionary.

        Args:
            file_path (str): The file path for the YAML file to load.

        Returns:
            dict: The contents of the YAML file as a dictionary.
        """
        with open(file_path, 'r') as config_file:
            return yaml.load(config_file, Loader=yaml.FullLoader)

