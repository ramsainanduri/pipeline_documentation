import sys
import os
import yaml
import argparse

# Add arguments
parser = argparse.ArgumentParser(description='Description of your script')

parser.add_argument('-i', '--input_versions_yaml', type=str, help='Tool versions file in yaml format')
parser.add_argument('-td', '--tool_descriptons', type=str, help='Tool Description Mapping file')
parser.add_argument('-o', '--output', type=str, help='output file name')

args = parser.parse_args()


# Load the YAML data
def load_yaml(version_yaml):
    with open(version_yaml, 'r') as versions_data:
        versions_dict = yaml.load(versions_data, Loader=yaml.SafeLoader)

    return versions_dict

#prepare the mapping dict
def read_tool_descriptions(description_file):
    # Initialize an empty dictionary to store the column data
    data_dict = {}

    # Open the file in read mode
    with open(description_file, 'r') as file:
        # Read the first line of the file (the header)
        header = file.readline().strip()

        # Split the header into a list of column names
        columns = header.split('\t')

        # Initialize an empty list for each column in the header
        for column in columns:
            data_dict[column] = []

        # Loop over the remaining lines in the file
        for line in file:
            # Split the line into a list of values
            values = line.strip().split('\t')

            # Loop over each column in the header and append the corresponding value
            for i, column in enumerate(columns):
                data_dict[column].append(values[i])

    # Return the dictionary of column data
    return data_dict


versions_dict = load_yaml(args.input_versions_yaml)
descriptions_dict = read_tool_descriptions(args.tool_descriptons)


"""
{
    'bwa_umi': 
    {
        'Sentieon BWA': 
        {
            'version': 'v202010.01', 
            'container': 'SomaticPanelPipeline_2021-06-24.sif'
        }, 
        'Sentieon UMI': 
        {
            'version': 'v202010.01', 
            'container': 'SomaticPanelPipeline_2021-06-24.sif'
        }
    },
    'annotate_vep':
    {
        'VEP': 
        {
            'version': 'v103.1',
            'container': 'ensembl-vep_release_103.sif'
        },
    }
}

"""

if os.path.isfile(args.output):
    os.remove(args.output)

def map_tool_descriptions(version_dict,mapping_dict,output_file):

    with open(output_file, 'a+') as out_handle:
        out_handle.write(f"Process\tTool\tVersion\tType\tContainer_Name\tDescription\tContact_Person\n")

        for process in version_dict:
            out_var = process
            for tool in version_dict[process]:

                v = version_dict[process][tool]['version']
                if str(v).startswith('v') or str(v).startswith('V'):
                    version = v
                else:
                    version = f"v{v}"

                mapping_index = mapping_dict['Tool'].index(tool)
                out_var += f"\t<a href = \"{mapping_dict['URL'][mapping_index]}\" target=\"_blank\">{tool}</a>\t{version}\t{mapping_dict['Type'][mapping_index]}\t{version_dict[process][tool]['container']}\t{mapping_dict['Short_Description'][mapping_index]}\t{mapping_dict['External_Contact_Person'][mapping_index]}\n"

            out_handle.write(f"{out_var}")


map_tool_descriptions(versions_dict,descriptions_dict,args.output)
