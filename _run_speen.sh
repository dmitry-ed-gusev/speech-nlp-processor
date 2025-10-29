#!/usr/bin/env bash

###################################################################################################
#
#   Speech NLP Processor (SPEEN) execution main file.
#
#   Created:  Dmitrii Gusev, 28.10.2025
#   Modified:
#
###################################################################################################

# -- safe bash scripting
set -euf -o pipefail
# -- default encoding for scripts and utilities
export LANG='en_US.UTF-8'

# -- executing SPEEN main python file
python ./src/speen/speen.py
