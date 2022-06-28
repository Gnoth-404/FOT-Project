# Goom (Google Meet + Zoom) - the video call application 

EEIT 2019 FoT: List of topics and softwares
An application where users can join or host a meeting with their name by using Stringee API with all other basic features of Zoom


<h1 align="center">Goom- the video call application</h1>
<h5 align="center">Goom where users can join or host a meeting with all basic features of Zoom</h5><br/>

![Image of Fakeflix Project](/static/Sources/homepage.png)

<br/>

## 🎯 About

We started this project with the purpose of learning ...<br/>


The Web App redirects you to an authentication page, where you can choose to sign up or to sign in: you can sign in with your custom account . Once you are logged in, you will land on the homepage, in which you can create a new meeting room by clicking create meeting or join an existing meeting <br/>




## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.
<br/>

## ▶️ Demo

Here you can find the demo link:

- [Demo](https://fakeflix.th3wall.codes)

## :sparkles: Features

:heavy_check_mark: &nbsp;&nbsp;User Sign In & User Sign Up<br />
:heavy_check_mark: &nbsp;&nbsp;Video call with Stringee API<br />
:heavy_check_mark: &nbsp;&nbsp;Responsive layout<br />

:heavy_check_mark: &nbsp;&nbsp;Chat room <br />
:heavy_check_mark: &nbsp;&nbsp;Share screen <br />
:heavy_check_mark: &nbsp;&nbsp;Mute microphone and disable video <br />
:heavy_check_mark: &nbsp;&nbsp;Device (Microphone + Camera) selection <br />

## :rocket: Technologies

- [Stringee API's](https://stringee.com/vi)
- [Vue](https://github.com/reduxjs/reselect)
- [Bootstrap](https://getbootstrap.com/)
- [Jquery](https://jquery.com/)
- [Django](https://www.djangoproject.com/)
- [Font Awesome](https://fontawesome.com/)
- [Digital Ocean](https://www.digitalocean.com/) for the deploy and CI.


## 📸 Screenshots

**Sign In**
![Screenshot of Goom Sign In](/static/Sources/login.png)
<br/>

**Sign Up**
![Screenshot of Goom Sign Up](/static/Sources/register.png)
<br/>

**Homepage**
![Screenshot of Goom Homepage](/static/Sources/homepage.png)
<br/>

**Meeting Room**
![Screenshot of Goot Meeting Room](/static/Sources/meeting_room.png)
<br/>


## 👨🏻‍💻 Run Locally

- Clone the project

```bash
  git clone https://github.com/Gnoth-404/FOT-Project.git
```

- Go to the project directory

```bash
  cd FOT-project
```

- Install dependencies

```bash
  pip install requirements.txt
```

- Create a .env file

- Request an API key from TMDB and them add it to the .env file

```
REACT_APP_API_KEY=REACT_APP_API_KEY
```

- Create a project inside Google Firebase and export the configuration

- Add the configuration inside the .env file created previously

```
REACT_APP_FIREBASE_API_KEY=REACT_APP_FIREBASE_API_KEY
REACT_APP_FIREBASE_AUTH_DOMAIN=REACT_APP_FIREBASE_AUTH_DOMAIN
REACT_APP_FIREBASE_PROJECT_ID=REACT_APP_FIREBASE_PROJECT_ID
REACT_APP_FIREBASE_STORAGE_BUCKET=REACT_APP_FIREBASE_STORAGE_BUCKET
REACT_APP_FIREBASE_MESSAGING_SENDER_ID=REACT_APP_FIREBASE_MESSAGING_SENDER_ID
REACT_APP_FIREBASE_APP_ID=REACT_APP_FIREBASE_APP_ID
REACT_APP_FIREBASE_MEASUREMEMT_ID=REACT_APP_FIREBASE_MEASUREMEMT_ID
```

- Start the server

```bash
  python manage.py runserver
```

