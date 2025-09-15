Create a .gitignore file and add .env
Create a .env file and add all environment variables such as api key etc...
Set up a virtual environment using python -m venv <name of your virtual environment>
Activate virtual environment using source <virtual environment name>/bin/activate
Install the following packages
langchain
langchain_openai
langchain_elasticsearch
langchain_community
python-dotenv by using pip install pip install langchain langchain-openai langchain-elasticsearch langchain-community python-dotenv
Create an ElasticSearch account if you do not have one. Create a new deployment by choosing any cloud provider and create an api key for the deployment. Click on the deployment dropdown from the header and click on manage deployment, you will find the cloud id on that screen.
Next, to access DevTools in ElasticSearch, Click on Kibana then devTools.
Clear console and add GET /\_cat/indices then run it, you should see a bunch of indices. Your new indice will be added when you run main.py successfully. Go to elastic and run GET /\_cat/indices again. If you search through indices, you should find one with the name you assigned to "index_name". If you go to Index management, you'll see your indice there.
