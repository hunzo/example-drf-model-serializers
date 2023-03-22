#!bin/bash


# Section 1- Bash options
# set -o errexit  
# set -o pipefail  
# set -o nounset

python3 manage.py collectstatic --noinput  
python3 manage.py makemigrations  
python3 manage.py migrate