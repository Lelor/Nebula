
<h1 align='center'>
    <img src='static/image/logo-32x32.png'><br>
    Nebula
    <br>
    <br>
    <a href='https://travis-ci.org/reebr/Nebula'>
        <img src='https://travis-ci.org/reebr/Nebula.svg?branch=development'>
    </a>
</h1>


# Migrations

For initialize, run migrations and create database tables, run:

```sh
py server db init
py server db migrate
py server db upgrade
```

🚧 SQLite does not support dropping, so if any column is removed you should remove `migrations` 
folder and the database file inside `/server`, and then, run the script above again.


[1]:https://travis-ci.org/reebr/Nebula.svg?branch=development
[2]:https://travis-ci.org/reebr/Nebula