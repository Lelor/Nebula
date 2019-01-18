<h1 align='center'>
    <img src='static/image/logo-64x64.png'><br>
    Nebula
</h1>
<h4 align='center'>A simple wiki client</h4>
<br>
<div align='center'>
    <a href='https://travis-ci.org/reebr/Nebula'>
        <img src='https://travis-ci.org/reebr/Nebula.svg?branch=development'>
    </a>
    <a href="https://codecov.io/gh/reebr/Nebula">
        <img src="https://codecov.io/gh/reebr/Nebula/branch/development/graph/badge.svg" />
    </a>
    <a href='https://github.com/reebr/Nebula/commits/development'>
        <img src='https://img.shields.io/github/last-commit/reebr/nebula.svg'>
    </a>
    <a href='https://github.com/reebr/nebula/issues'>
        <img src='https://img.shields.io/github/issues/reebr/nebula.svg'>
    </a>
</div>

# Nebula

. . . 

## Migrations

For initialize, run migrations and create database tables:

```sh
py server db init
py server db migrate
py server db upgrade
```

🚧 SQLite does not support dropping, so if any column is removed you should remove `migrations` 
folder and the database file inside `/server`, and then, run the script above again.
