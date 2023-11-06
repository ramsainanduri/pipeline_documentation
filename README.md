# Pipeline Documentation

This automatic documentation generation is a time-saving tool for developers and teams, as it eliminates the need to manually create and maintain documentation. It also helps ensure that documentation is up-to-date and consistent, as changes made to the pipeline.yaml file used for the document updation in a simple and easy way.  

The pipeline.yaml file contains all the relevant information about the pipeline or tool, including the description, inputs, outputs, parameters, and usage. This information is used to generate the HTML and MD documents, which provide clear and detailed information about the pipeline or tool.  

The HTML document is visually appealing and easy to navigate, with links to different sections and a search bar for quickly finding specific information. The MD document is plain text, but can be formatted with Markdown syntax for a more readable and structured format. The MD document can be uploaded to a readthedocs server for online documentation. It uses the mkdocs format, with the required "docs" folder and related files in the project root folder.  

Additionally, the generated documentation also includes a table of contents for easy navigation, and sections for examples.  

Overall, this repo helps improve the documentation process for pipelines and tools, making it easier for others to understand and use them.  

## Requirements

Python 3.11.0 or higher is required to run this program.

## Installation

To install the required packages, run the following command:

`pip install -r env/requirements.txt`

## Usage

The pipeline documentation can be generated using the following command:

`python main.py -h`

To create an example command, use the following command:

`python main.py -e`

## Pipeline YAML Structure

The pipeline.yaml file contains all the relevant information about the pipeline or tool, including the description, inputs, outputs, parameters, and usage. This information is used to generate the MD documents, which provide clear and detailed information about the pipeline or tool.

The pipeline.yaml file has the following structure:

```
sections: # list of sections
  - name: <Name of the element that can be used for name of the makdown.md and in NAV bar>
    headings: # list of headings (currently only two levels of headings are supported)
      - name: <HEADING NAME> # name of the heading
        type: text # data tyoe
        content: | # content of the heading
          The program aims to simplify the process of creating and maintaining documentation for software projects using MkDocs and Read the Docs.
```

Each section has a name and a list of headings. Each heading has a name, type, and content. The name is the name of the heading, the type is the data type, and the content is the content of the heading. The content can be plain text or a list of items.

The following data types are supported:

- text: printed as is
- list: printed as a list
- dictionary: printed as a key value pair
- dict: printed as a key value pair
- image: printed as an image
- table: printed as a table (can be used to display dict as a table)
- file: printed as a table (can be used for text files)
- versions: printed as a table (can be used for versions.yaml file)

## Examples

Example pipeline.yaml can be found at 

```
static/templates/pipeline.yaml
```
