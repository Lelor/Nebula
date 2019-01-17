

# Migrations

For initialize, run migrations and create database tables, run:

```sh
py server db init
py server db migrate
py server db upgrade
```

🚧 SQLite does not support dropping, so if any column is removed you should remove `migrations` 
folder and the database file inside `/server`, and then, run the script above again.