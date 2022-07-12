## Requirements:

1. Install PostgreSQL
2. Install Redis
3. Setup your .env file.

### Install PostgreSQL

```plaintext
# Create the file repository configuration:
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
# Import the repository signing key:
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
# Update the package lists:
sudo apt update
# Install PostgreSQL
sudo apt -y install postgresql-14 postgresql-contrib-14 postgresql-doc-14 libpq-dev
```

#### Setup PostgreSQL Server

Run the following commands:

1. `sudo su - postgres`
2. `psql`
   1. postgres-# \conninfo
   2. postgres-# \password postgres
   3. Enter New Passowrd new password is `postgres` & Confirm it
   4. Then type \q
   5. After that type exit
3. `sudo vim /etc/postgresql/14/main/postgresql.conf`
4. Uncomment listen_addresses = '*' and Change it to listen_addresses = 'localhost'
5. Uncomment port = 5432
6. `sudo systemctl restart postgresql`
7. `sudo systemctl enable postgresql`

### Create Project User & Database

Open new terminal and run the following commands:

1. Create the bookkeeper user for database:
   1. `createuser -e -s -P bookkeeper -U postgres -W -h localhost`
      1. Enter new password for new created user password is `BookPassword123456` and confirm it.
      2. Enter postgres password which is `postgres`.
2. Create the bookkeeper database:
   1. `createdb -e --encoding="UTF-8" --owner=bookkeeper bookkeeper_checklist -U bookkeeper -W -h localhost`
      1. Enter the password for user bookkeeper which is `BookPassword123456`

### Install Redis

```plaintext
sudo add-apt-repository ppa:redislabs/redis
sudo apt-get update
sudo apt-get install redis
sudo systemctl enable redis
sudo systemctl start redis
```
