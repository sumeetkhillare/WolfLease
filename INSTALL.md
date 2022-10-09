---
1. The project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled. 

2. Clone the github repository on your local system. Please make sure git is installed in the system. After cloning the repository move into it, with the help of cd command ,
```
git clone https://github.com/subodh30/WolfLease.git
cd WolfLease
```
3. It's a good practise to create a virtual environment to store your projects dependencies separately from the global ones. You can install virtualenv with
```
pip install virtualenv
```
4. Run the following command in the base directory of this project. This will create a new folder project_env in your project directory
```
python -m venv project_env
```
5. Now activate the virtual environment
```
source project_env/bin/activate
```
6. Use pip to install all requirements of the project listed in the requirements.txt file.
```
pip install -r requirements.txt
```
7. To run the server
```
python manage.py runserver
```
