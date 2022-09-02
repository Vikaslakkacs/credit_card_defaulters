
# Created on 28th Aug
# credit_card_defaulters
Machine learning project for Credit card defaulters

### Software and account Requirements:

1. [Git Hub Account]
2. [Heroku Account]
3. [Vs code IDE]
4. [Git Cli]


To setup CI/CD Pipeline in Heroku, we need below information
1. HEROKU_EMAIL= vikaslakkacs@gmail.com
2. HEROKU_API_KEY= c5aa42bf-dbc1-4959-91e0-fcb222cd463f
3. HEROKU_APP_NAME= credit-card-defaulters-vilakka

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tagname> .
<image_name>: name of the docker image-> ml-project
<tagname>: tag name mostly it is 'latest'
.: means create it in current directory
```
Note: Image name for docker must be lowercase

To list docker images
```
docker images
```

To run docker image
```
docker run -p 5000:5000 -e PORT= 5000 <docker image id>
<docker image id>: Can be found when 'docker images' command is ran
```