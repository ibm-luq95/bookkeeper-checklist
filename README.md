
# Installing Instructions #

1. Clone the project.
2. Create .env file in src/bookkeeper_checklist_project directory.
3. Put the important environment variables in the .env file.
    `

STAGE_ENVIRONMENT="DEV"
ALLOWED_HOSTS="127.0.0.1, "
DEBUG=True
SECRET_KEY='django-insecure-6kcnz6_pv-%j&yv2)2#*n_$nu#0u+1*m(e#vm5w*1@3znjh7(+'
DB_HOST="{{PUT_YOUR_LOCAL_IP_ADDRESS}}"
DB_NAME="bookkeeper-checklist-user"
DB_USERNAME="bookkeeper-user"
DB_PASSWORD="BookPassword$123456"
DB_PORT=5432
REDIS_HOST="{{PUT_YOUR_LOCAL_IP_ADDRESS}}"
REDIS_PORT=6379
    `
