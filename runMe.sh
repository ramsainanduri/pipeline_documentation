#!/usr/bin/bash

########### HOW TO RUN ###################
#bash runMe.sh /home/ramsainanduri/Pipelines/Validation_Documents/mkdocs_test/params.yaml https://github.com/ramsainanduri/mkdocs_test.git /home/ramsainanduri/Pipelines/Validation_Documents/mkdocs_test/report.html No_Singularity_at_the_moment
###########################################

#please provide full paths for all the files

yaml_file=${1}
github_project_URL=${2}
output_file=${3}
singularity_image=${4}

github_project_name=$(basename ${github_project_URL} | sed 's/.git//g')
script_file="/home/ramsainanduri/Pipelines/Validation_Documents/mkdocs_test/template.Rmd"
local_project_location=$(grep 'location:' ${yaml_file} | sed 's/location:.* //g' | sed 's/ //g')
tmp_dir=${local_project_location}"/tmp"
mkdir -p ${tmp_dir}
output_file_name_md=$(echo ${output_file} |sed 's/.html$/.md/g')


#ignore tmp dir from the local repo
gitignore_tmp=$(grep ^tmp ${local_project_location}'/.gitignore')
if [ $gitignore_tmp != '' ]
then
    echo -e "\ntmp\n" >> ${local_project_location}'/.gitignore'
    git add ${local_project_location}'/.gitignore'
fi

#Running the main Rmd
R -e "library(yaml);params=yaml::read_yaml('${yaml_file}');params;rmarkdown::render('$script_file', output_file='${output_file}', intermediates_dir='${tmp_dir}', knit_root_dir='${tmp_dir}', clean=F)"


#Copying the markdown file to the projects docs folder
mkdocs new ${local_project_location}


echo -e "site_name: ${github_project_name}\nsite_url: ${github_project_URL}\nmarkdown_extensions: \n\t- tables" > ${local_project_location}'/mkdocs.yml'


md_destination=${local_project_location}'/docs/index.md'
date=$(date '+%Y%m%d')

#########
#${md_destination} ]
#then
#    mv ${md_destination} ${md_destination}'.'${date}'.backup'
#fi 
cp ${output_file_name_md} ${md_destination}

