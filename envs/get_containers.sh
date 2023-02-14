#!/bin/bash

# Run me in envs folder to get sinuglarities needed
# Please adjust paths of sif location in appropriate config_file
# requires sudo permissions

sudo singularity build pipeline_documentation_v1.0.sif docker://ramsainanduri/ubuntu_pipeline_documentation:v1.0
