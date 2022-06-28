# Goom (Google Meet + Zoom) - the video call application 

EEIT 2019 FoT: List of topics and softwares
An application where users can join or host a meeting with their name by using Stringee API with all other basic features of Zoom


<h1 align="center">Goom- the video call application</h1>
<h5 align="center">Goom where users can join or host a meeting with all basic features of Zoom</h5><br/>

<br/>

## 🎯 About

I have started this project with the purpose of learning how to structure a Web App of a mid-level complexity integrating the Redux logic.<br/>
I've tried to replicate the original layout as much as possible and I've also made some improvements in some sections inserting route animations and micro-interactions. I've also inserted a really close clone of Netflix's original splash animation (forked from a famous [codepen from Claudio Bonfati](https://codepen.io/claudio_bonfati/pen/mdryxPv)), made entirely with CSS, as well as the play animation. I have then sampled the original Netflix "ta-duummm" sound and I made it play along with the two animations.<br/>
I put a lot of effort into it and I hope that you could like it.<br/><br/>
The Web App redirects you to an authentication page, in which you can choose to sign up or to sign in: you can sign in with your custom account or with your Google account. Once you are logged in and after the splash animation, you will land on the homepage, in which you can find a mix of movies and series divided into rows.<br/>
Each row represents a movie/series category: you can click on it and you will be redirected to the selected category, a page that loads thousands of movies with an infinite scroll. You can also navigate to the movies page, series page, new & popular page (that contains the upcoming movies/series and the most popular ones) or you can navigate to your favorites page.<br/>
You can add/remove movies/series through the plus and minus buttons that you can find hovering each poster or opening a single movie's detail modal. If you click on the play button you can enjoy a custom CSS-only play animation with Fakeflix's brand name.<br/>
You have also the option to search through TMDB's catalogue using the search functionality inside the fixed navbar: you can search by movie name, actor or movie director.<br/><br/>
Go try it and please let me know if you enjoyed it with a ⭐️, I would appreciate it a lot.
<br/>

## ▶️ Demo

Here you can find the demo link:

- [Demo](https://fakeflix.th3wall.codes)

## :sparkles: Features

:heavy_check_mark: &nbsp;&nbsp;Display movies and series, old and upcoming, also from the real Netflix<br />
:heavy_check_mark: &nbsp;&nbsp;Category related page with infinite scroll<br />
:heavy_check_mark: &nbsp;&nbsp;Search by title, actor, movie director<br />
:heavy_check_mark: &nbsp;&nbsp;Add/Remove to/from "My list" functionality<br />
:heavy_check_mark: &nbsp;&nbsp;Detail modal with extra informations about the selected movie/series<br />
:heavy_check_mark: &nbsp;&nbsp;Customized splash animation (credits: [Claudio Bonfati's pen](https://codepen.io/claudio_bonfati/pen/mdryxPv)) with characteristic Netflix sound<br />
:heavy_check_mark: &nbsp;&nbsp;Play animation with characteristic Netflix sound<br />
:heavy_check_mark: &nbsp;&nbsp;Google login<br />
:heavy_check_mark: &nbsp;&nbsp;User Sign In & User Sign Up<br />
:heavy_check_mark: &nbsp;&nbsp;Use of React hooks and custom hooks<br />
:heavy_check_mark: &nbsp;&nbsp;Favourites list persistence (session storage)<br />
:heavy_check_mark: &nbsp;&nbsp;Responsive layout<br />
:heavy_check_mark: &nbsp;&nbsp;Swipeable movies list<br />
:heavy_check_mark: &nbsp;&nbsp;Loading skeletons<br />
:heavy_check_mark: &nbsp;&nbsp;Route animations and micro-interactions (handled with Framer Motion)<br />

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
  pip install requirements
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

## :white_check_mark: Requirements

Before starting :checkered_flag:, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.
<br/>
