#!/usr/bin/bash

################################################################################
version='v1.0'
author='Ram Sai Nanduri'
git_repo='https://github.com/ramsainanduri/pipeline_documentation.git'
pd_path=$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )
example_command="bash $(realpath $0) -g ${git_repo} -o ${pd_path}/../pipeline_documentation.html -y ${pd_path}/../templates/pipeline.yaml -s ${pd_path}/../envs/pipeline_documentation_v1.0.sif"
################################################################################

################################################################################
# Help                                                                         #
################################################################################
Help()
{
    # Display Help
    echo -e "Description:\n\tThis script produces documentation in HTML format and creates a \"docs\" folder containing the necessary files to display the \"readme\" in the ReadTheDocs format.\n"
    echo -e "This script is developed and maintained by:\n\tAuthor:\t\t${author}\n\tVersion:\t${version}\n"
    echo -e "USAGE:\n\t${example_command}"
    echo
    echo "parameters: $(basename $0) [-e|h|g|o|s|v|y]"
    echo " -e     create example_command.sh"
    echo " -h     print this help."
    echo " -g     github url to your project/pipeline"
    echo " -o     full path to the output file"
    echo " -s     full path to the singularity container"
    echo " -v     print version"
    echo " -y     full path to the pipeline yaml file"
    echo
}

# Get the flags
while getopts ':g:o:s:y:evh' flag
do
    case "${flag}" in
        g) github_project_URL=${OPTARG};;
        o) output_file=${OPTARG};;
        s) singularity_container=${OPTARG};;
        y) yaml_file=${OPTARG};;
        e) #create example_command.sh
            echo -e "${example_command}\n" > ${pd_path}/../example_command.sh
            exit;;
        v) #print version
            echo -e "${version}"
            exit;;
        h) # display Help
            Help
            exit;;

        \?) # incorrect flag
            echo -e "Error: Invalid flag\n"
            Help
            exit;;
   esac
done


#pipeline documentation repo path and files
date=$(date '+%Y%m%d')
rmd_file=${pd_path}"/../templates/template.Rmd"
template_mkdocs_yaml=${pd_path}"/../templates/template.mkdocs.yaml"
local_project_location=$(grep 'location:' ${yaml_file} | sed 's/location:.* //g' | sed 's/ //g')
github_project_name=$(basename ${github_project_URL} | sed 's/.git//g')
tmp_dir=${local_project_location}"/tmp"
md_output=$(echo ${output_file} |sed 's/.html$/.md/g')
md_destination=${local_project_location}'/docs/index.md'

#singularity specific
binds=${pd_path}'/../,'${local_project_location}
singularity_cmd='singularity run --bind'

#main Rmd cmd
rmd_cmd='R -e "library(yaml);params=yaml::read_yaml('\'${yaml_file}\'');params;rmarkdown::render('\'$rmd_file\'', output_file='\'${output_file}\'', intermediates_dir='\'${tmp_dir}\'', knit_root_dir='\'${tmp_dir}\'', clean=F)"'

#Generate script file
rm ${local_project_location}/run.sh
echo -e "mkdir -p ${tmp_dir}" >> ${local_project_location}/run.sh
echo -e "\n${rmd_cmd}\n" >> ${local_project_location}/run.sh

#Copying the markdown file to the projects docs folder
echo -e "rm -rf ${local_project_location}/docs" >> ${local_project_location}/run.sh
echo -e "rm ${local_project_location}/mkdocs.yml" >> ${local_project_location}/run.sh
echo -e "mkdocs new ${local_project_location}" >> ${local_project_location}/run.sh

echo -e "echo -e \"site_name: ${github_project_name}\\\nsite_url: ${github_project_URL}\\\n\" > ${local_project_location}/mkdocs.yml " >> ${local_project_location}/run.sh

echo -e "grep -v \"site_name\|site_url\" ${template_mkdocs_yaml} >> ${local_project_location}/mkdocs.yml" >> ${local_project_location}/run.sh

echo -e "cp ${pd_path}/../templates/requirements.txt ${local_project_location}/docs/" >> ${local_project_location}/run.sh
echo -e "cp ${pd_path}/../templates/readthedocs.yaml ${local_project_location}/.readthedocs.yaml" >> ${local_project_location}/run.sh

echo -e "cp ${md_output} ${md_destination}" >> ${local_project_location}/run.sh

echo -e "cp ${pd_path}/../templates/github_pages.template.yaml ${local_project_location}/docs/_config.yaml" >> ${local_project_location}/run.sh
#echo -e "mv ${local_project_location}/mkdocs.yml ${local_project_location}/docs/mkdocs.yaml" >> ${local_project_location}/run.sh

echo -e "rm -rf ${tmp_dir}" >> ${local_project_location}/run.sh
echo -e "rm ${md_output}" >> ${local_project_location}/run.sh

#eval ${i}='something'

#Running the script in a container
main_cmd=${singularity_cmd}' '${binds}' '${singularity_container}' bash '${local_project_location}'/run.sh'
echo -e "\n${main_cmd}\n"
$main_cmd
rm ${local_project_location}/run.sh