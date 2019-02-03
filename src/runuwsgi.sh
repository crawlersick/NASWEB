#uwsgi -s /tmp/uwsgi.sock --plugin python --module hello --callable app
uwsgi --http 0.0.0.0:5001 --plugin python --module hello --callable app --stats 127.0.0.1:9191 --enable-threads -d /tmp/uwsgipid --logto2 /tmp/uwsgilog.log
