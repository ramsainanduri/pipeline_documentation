#!!/usr/bin/env python3

import os
import yaml
import shutil
import pandas as pd
from tabulate import tabulate

class FileParser:
    """
    A class that provides methods to parse different types of files and convert them to various formats.

    Attributes:
    - file_extension_map (dict): A dictionary that maps file extensions to corresponding file reading and formatting functions.
    - tool_desc_columns (list): A list of column names for tool descriptions.
    - tool_col_headers (list): A list of column names for tool versions.

    Methods:
    - parse(file_path, tool_descriptions=False): Parses the file at the given file path and returns a DataFrame or a subset of it based on the file extension.
    - yaml_file(file_path): Reads a YAML file and returns its contents as a dictionary.
    - read_file(file_path, sep='\t', tool_descriptions=False): Reads a CSV or TSV file and returns its contents as a DataFrame or a subset of it based on the tool_descriptions flag.
    - create_df_from_dict(dict_data, columns=None): Converts a dictionary to a DataFrame.
    - convert_df_to_markdown(df): Converts a DataFrame to a Markdown table.
    - convert_df_to_html(df): Converts a DataFrame to an HTML table.
    - read_image_file(file_path): Reads an image file and returns a Markdown image link.
    - markdown_table(header, body): Creates a Markdown table from a header and a body.
    - write_html_table_to_markdown(md_file, html_table, css_class='table table-striped table-bordered table-hover table-condensed table-responsive'): Writes an HTML table to a Markdown file with custom CSS styles.
    - map_tool_descriptions(versions_dict, mapping_df): Maps tool descriptions to tool versions and returns a DataFrame.
    """
    def __init__(self):
        self.file_extension_map = {
            '.txt': self.read_file,
            '.tsv': self.read_file,
            '.tab': self.read_file,
            '.csv': self.read_file,
            '.png': self.read_image_file,
            '.jpg': self.read_image_file,
            '.jpeg': self.read_image_file,
            '.gif': self.read_image_file,
            '.svg': self.read_image_file,
            '.yaml': self.yaml_file,
            '.yml': self.yaml_file
        }
        self.tool_desc_columns = ['Tool', 'URL', 'External_Contact_Person']
        self.tool_col_headers = ['Process', 'Tool', 'Version', 'External_Contact_Person']

    def parse(self, file_path, tool_descriptions=False):
        # Determine the file extension
        file_extension = os.path.splitext(file_path)[-1].lower()

        # Check if the file extension is supported
        if file_extension in self.file_extension_map:
            if file_extension == '.csv':
                # Call the corresponding file reading and formatting function
                return self.file_extension_map[file_extension](file_path, sep=',', tool_descriptions=tool_descriptions)
            elif file_extension in ['.yaml', '.yml']:
                # Call the corresponding file reading and formatting function
                return self.file_extension_map[file_extension](file_path)
            else:
                # Call the corresponding file reading and formatting function
                return self.file_extension_map[file_extension](file_path, tool_descriptions=tool_descriptions)
        else:
            # Handle unsupported file types or extensions
            return f"Unsupported file type: {file_extension}"

    def yaml_file(self, file_path):
        with open(file_path, 'r') as yaml_data:
            return yaml.load(yaml_data, Loader=yaml.SafeLoader)

    def read_file(self, file_path, sep='\t', tool_descriptions=False):
        # Read the file content
        df = pd.read_csv(file_path, sep=sep, header=0)

        if tool_descriptions:
            subset_df = df.loc[:, self.tool_desc_columns]
            return subset_df
        else:
            return df

    def create_df_from_dict(self, dict_data, columns=None):
        if not columns:
            columns = ['Key', 'Value']
        df = pd.DataFrame(dict_data.items(), columns=columns)
        return df

    def convert_df_to_markdown(self, df):
        # Convert the DataFrame to a Markdown table
        markdown_table = tabulate(df, tablefmt='pipe', headers='keys', showindex=False)
        return markdown_table
    
    def convert_df_to_html(self, df):
        # Convert the DataFrame to a Markdown table
        html_table = df.to_html(escape=False, index=False)
        return html_table

    def read_image_file(self, file_path):
        # Return a markdown image link for an image file
        base_name = os.path.basename(file_path)
        return f'![{base_name}]({file_path})\n\n'

    def markdown_table(self, header, body):
        table = f"| {' | '.join(header)} |\n"
        table += f"| {' | '.join(['---'] * len(header))} |\n"
        for row in body:
            table += f"| {' | '.join(row)} |\n"
        return table

    def write_html_table_to_markdown(self, md_file, html_table, css_class='table table-striped table-bordered table-hover table-condensed table-responsive'):
        # Write the HTML code with custom CSS styles
        md_file.write(f'<div class="{css_class}">\n')
        md_file.write(f"{html_table}\n")
        md_file.write('</div>\n')


    def map_tool_descriptions(self, versions_dict, mapping_df):
        # Convert the dictionary into a list of dictionaries
        versions_list = []
        for process, tools in versions_dict.items():
            for tool, version in tools.items():
                if str(version).startswith('v') or str(version).startswith('V'):
                    continue
                else:
                    version = f"v{version}"
                versions_list.append({'Process': process, 'Tool': tool, 'Version': version})
        df_versions = pd.DataFrame(versions_list)

        # Merge the two DataFrames based on the "Tool" column
        result_df = pd.merge(df_versions, mapping_df, on='Tool', how='left')

        # Fill any NaN values in the "Process" column with an empty string
        result_df['Process'].fillna('', inplace=True)

        # Format the "Tool" column as a link
        #result_df['Tool'] = result_df.apply(lambda row: f'[{row["Tool"]}]({row["URL"]})', axis=1)
        result_df['Tool'] = result_df.apply(lambda row: f'<a href="{row.URL}" target="_blank">{row.Tool}</a>', axis=1)

        # Remove duplicate names in the "Process" column and replace them with empty values
        result_df['Process'] = result_df['Process'].where(~result_df['Process'].duplicated(), '')

        # Replace NaN values with "-"
        result_df.fillna('-', inplace=True)

        # Reorder the columns as per your desired output
        result_df = result_df[self.tool_col_headers]

        return result_df


class MkDocsProfileGenerator(FileParser):
    """
    A class for generating a MkDocs project structure and configuration based on a YAML input file.

    Args:
        project_dir (str): The path to the directory where the MkDocs project will be created.
        input_yaml_file (str): The path to the YAML input file.
        tool_descriptions (str, optional): The path to a CSV file containing tool descriptions. Defaults to None.
        mkdocs_cfg (dict, optional): A dictionary containing additional configuration settings for the MkDocs project. Defaults to None.

    Attributes:
        project_dir (str): The path to the directory where the MkDocs project will be created.
        content_dir (str): The path to the directory where the MkDocs project content will be stored.
        input_yaml_file (str): The path to the YAML input file.
        tool_descriptions (str): The path to a CSV file containing tool descriptions.
        tools_df (pandas.DataFrame): A pandas DataFrame containing the tool descriptions.
        mkdocs_cfg (dict): A dictionary containing additional configuration settings for the MkDocs project.
        nav (list): A list containing the navigation structure for the MkDocs project.

    Methods:
        generate_section_files(section_type, section_data): Generates the markdown files for a given section type and section data.
        generate(): Generates the MkDocs project structure and configuration.
    """
    def __init__(self, project_dir, input_yaml_file, tool_descriptions=None, mkdocs_cfg=None):
        super().__init__() 
        self.project_dir = project_dir
        self.content_dir = os.path.join(project_dir, 'docs')
        self.input_yaml_file = input_yaml_file
        self.tool_descriptions = tool_descriptions
        self.tools_df = self.parse(tool_descriptions, tool_descriptions=True)
        self.mkdocs_cfg = mkdocs_cfg
        # Initialize the nav structure
        self.nav = [{'Home': 'index.md'}]

    def generate_section_files(self, section_type, section_data):

        section_nav = []
        # Create the markdown files for each section
        if section_type == 'profiles':
            self.content_dir = os.path.join(self.project_dir, 'docs/profiles')
            if not os.path.exists(self.content_dir):
                os.makedirs(self.content_dir)
            heading_level = 2
        else:
            self.content_dir = os.path.join(self.project_dir, 'docs')
            heading_level = 1
    
        for section in section_data:
            section_name = section.get('name')
            section_path = os.path.join(self.content_dir, f"{section_name}.md")
            if section_type == 'profiles':
                section_nav.append({section_name: f"profiles/{section_name}.md"})
            else:
                section_nav.append({section_name: f"{section_name}.md"})

            with open(section_path, 'w') as section_file:
                section_file.write(f"{'#' * heading_level} {section_name}\n\n")
                headings = section.get('headings', [])
                for heading in headings:
                    heading_name = heading.get('name')
                    heading_type = heading.get('type')
                    heading_content = heading.get('content')

                    if heading_name and heading_type:
                        section_file.write(f"\n{'#' * (heading_level + 1)} {heading_name}\n\n")

                        if heading_type == 'text':
                            section_file.write(f'{heading_content}\n\n')

                        elif heading_type == 'list':
                            for item in heading_content:
                                section_file.write(f'- {item}\n')
                            section_file.write('\n')

                        elif heading_type in ['dictionary', 'dict']:
                            for key, value in heading_content.items():
                                section_file.write(f'- **{key}:** {value}\n')
                            section_file.write('\n')

                        elif heading_type == 'table':
                            dict_df = self.create_df_from_dict(heading_content)
                            dict_table = self.convert_df_to_html(dict_df)
                            self.write_html_table_to_markdown(section_file, dict_table)

                        elif heading_type == 'image':
                            section_file.write(self.read_image_file(heading_content))

                        elif heading_type == 'file':
                            file_df = self.parse(heading_content)
                            file_table = self.convert_df_to_html(file_df)
                            self.write_html_table_to_markdown(section_file, file_table)

                        elif heading_type == 'versions':
                            versions_df = self.parse(heading_content)
                            if section_type == 'profiles':
                                versions_mapped_df = self.map_tool_descriptions(versions_df, self.tools_df)
                            else:
                                versions_mapped_df = versions_df
                            versions_table = self.convert_df_to_html(versions_mapped_df)
                            self.write_html_table_to_markdown(section_file, versions_table)

        if section_type == 'profiles':
            self.nav.append({'Profiles': section_nav})
        else:
            for elem in section_nav:
                self.nav.append(elem)
        
        print(f"Created {section_type} section files.")


    def generate(self):
        if not os.path.exists(self.project_dir):
            os.makedirs(self.project_dir)

        if os.path.exists(self.content_dir):
            shutil.rmtree(self.content_dir)

        os.makedirs(self.content_dir)


        pipeline_data = self.parse(self.input_yaml_file)
        
        for id in pipeline_data.keys():
            if id == 'pipeline':
                # Create the index.md file
                with open(os.path.join(self.content_dir, 'index.md'), 'w') as index_file:
                    index_file.write(f"## Pipeline Description\n\n")
                    info = pipeline_data.get('pipeline', {}).get('info', {})

                    if info:
                        info_df = self.create_df_from_dict(info, ['Info', 'Description'])
                        info_table = self.convert_df_to_html(info_df)
                        self.write_html_table_to_markdown(index_file, info_table)
                    else:
                        index_file.write(f"No description provided.\n\n")
            else:
                section_data = pipeline_data.get(id, [])
                self.generate_section_files(id, section_data)

        # Create the mkdocs.yml file and append the nav structure with the config settings

        mkdocs_final = {
            'site_name': pipeline_data.get('pipeline', {}).get('info', {}).get('name', 'Documentation Site'),
            'site_url': pipeline_data.get('pipeline', {}).get('info', {}).get('git_repo', ''),
            'github_url': pipeline_data.get('pipeline', {}).get('info', {}).get('git_repo', ''),
            'nav': self.nav
        }

        if self.mkdocs_cfg:
            mkdocs_final.update(self.mkdocs_cfg)

        mkdocs_yml_path = os.path.join(self.project_dir, 'mkdocs.yml')
        with open(mkdocs_yml_path, 'w') as mkdocs_yml_file:
            yaml.dump(mkdocs_final, mkdocs_yml_file, default_flow_style=False, sort_keys=False, indent=2)

        print("MkDocs project structure and configuration created.")

