#!/usr/bin/env bash

echo "---------------------------------------------------"
echo "This script will install virtual environment,"
echo "Set it up and install packages to run this project"
echo "One key note:"
echo "It will not install python neither postgresql"
echo "---------------------------------------------------"
read -p "Click ""ENTER"" continue."
echo "Installing virtual environment..."
sudo apt install virtualenv
echo "---------------------------------------------------"
echo "Creating virtual environment in current directory"
echo "---------------------------------------------------"
virtualenv -p python3 sky-venv
# pip install -r requirements.txt
sky-venv/bin/pip install -r requirements.txt
source ./sky-venv/bin/activate
echo "---------------------------------------------------"
echo "Installation completed"
echo "---------------------------------------------------"
echo "Make sure 'local_settings.py' is configured!"
echo "---------------------------------------------------"
read -r -p "Do you want to start server? [Y/n] " response
echo
response=${response,,} # tolower
if [[ $response =~ ^(yes|y| ) ]] || [[ -z $response ]]; then
echo "---------------------------------------------------"
echo "Making migrations"
echo "---------------------------------------------------"
python manage.py migrate
echo "---------------------------------------------------"
echo "Running Tests"
echo "---------------------------------------------------"
python manage.py test
echo "---------------------------------------------------"
echo "Populating database"
echo "---------------------------------------------------"
python manage.py loaddata task-exam.json
echo "---------------------------------------------------"
echo "Running Server"
echo "By default there are three users:"
echo "'super-user' with password 'mkonjibhu'"
echo "'another-super' with password 'mkonjibhu'"
echo "'user' with password 'mkonjibhu'"
echo "---------------------------------------------------"
echo "https://www.youtube.com/watch?v=zl_ITK2rm9g"
echo "---------------------------------------------------"
python manage.py runserver
fi
if [[ $response =~ ^(no|n| ) ]] || [[ -z $response ]]; then
exit
fi
