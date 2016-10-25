<snippet>
  <content><![CDATA[
# ${1:DevOps Deployment}
Creating a virtual machine using Vagrant and virtual box. Deploying Nginx, Sqlite, Supervisord and Gunicorn via roles in Ansible on the VM. Creating a Flask application that runs on Gunicorn at http://0.0.0.0:5000.
## Installation
- Git clone the repository
- Install Virtual Box
- Install Ansible
- Install Vagrant
## Usage
Go to the repository SuperSnake/Vagrant and make sure that the role path for Ansible on your machine is configured to execute the roles in the directory SuperSnake/Ansible/roles.
## Commands
1. vagrant up --provision
2. open a browser
3. go to http://0.0.0.0:5000
4. See the result !
## Credits
Simon THOME ING3C
]]></content>
  <tabTrigger>readme</tabTrigger>
</snippet>
