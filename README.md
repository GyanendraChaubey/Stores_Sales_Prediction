# Stores_Sales_Prediction


### Software and account Requirement.

1. [Github Account](https://github.com)
2. [Heroku Account](https://dashboard.heroku.com/login)
3. [VS Code IDE](https://code.visualstudio.com/download)
4. [GIT cli](https://git-scm.com/downloads)
5. [GIT Documentation](https://git-scm.com/docs/gittutorial)

Creating conda environment

```
conda create -p venv python=3.7 -y

```
Activate activate environment
```
conda activate venv/

```

Install requirements

```
pip install -r requirements.txt

```

Add files to git

```
git add .

```

OR 

```
git add <file_name>

```

To check git status
```
git status
```

To check all version maintained by git
```
git log
```

To create version/commit all changes by git

```
git commit -m "message"
```

To send version/changes to github
```
git push origin main
```
To check remote url
```
git remote -v
```
To setup CI/CD pipeline in heroku we need 3 information:
1. HEROKU_EMAIL: gyanendrachaubey68@gmail.com
2. HEROKU_API_KEY: 
3. HEROKU_APP_NAME: stores-sales-prediction-gyan

Build Docker Image
```
docker build -t <image_name>:<tag_name>
```
```
Note: Image name of docker must be lowercase
```
To list docker image
```
docker images
```
Run docker images
```
docker run -p 5000:5000 -e PORT=5000 f8c749e73678
```
To check running contaainer in docker
```
docker ps
```
To stop docker container
```
docker stop <container_id>
```
