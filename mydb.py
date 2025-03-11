# Install MySQL on your computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install pymysql

import pymysql

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='My1s$SQlr0Ot@',
    database='dbcid'
)
print("Connected successfully!")

"""

1. python manage.py dumpdata > datadump.json
2. Change settings.py to your mysql
3. Make sure you can connect on your mysql (permissions,etc)
4. python manage.py migrate --run-syncdb
5. Exclude contentype data with this snippet in shell
    python manage.py shell
    from django.contrib.contenttypes.models import ContentType
    ContentType.objects.all().delete()
    quit()
6. python manage.py loaddata datadump.json

"""