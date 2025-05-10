# Creating a Hello World Template

Hello World is the most basic example SAM Template. To start creatiing it run this command: <br>
```sh
sam init
```
<br>

Then press 1 for AWs Quick Start Template, then 1 again for zip package, then select your runtime, usually you would go for 1 for the latest supported nodejs or 2 for the latest supported python (this might change in the future). Now name your stack application name. Finally select 1 for Hello World template. Now you will have a new directory with the name of your stack app. 

# Deploying an application

To deploy an application you need to start with: <br>
```sh
sam build
```
<br>

This will build your sam app. Then you must deploy it. If you are deploying this app for the first time you must use: <br>
```sh
sam deploy --guided
```
<br>

This will allow you to name your application, then it will ask for your region which is eu-west-2 (although it should already be the default option). Then just press enter for the rest of the question.

The next time you deploy your app you can just run `sam deploy`.