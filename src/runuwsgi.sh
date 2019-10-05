#uwsgi -s /tmp/uwsgi.sock --plugin python --module hello --callable app
#uwsgi --http 0.0.0.0:5000 --plugin python --module hello --callable app --stats 127.0.0.1:9191 --enable-threads -d /tmp/uwsg.log --pidfile /tmp/uwsgipid
uwsgi_python3 --http-socket 0.0.0.0:5000  --module hello --callable app --stats 127.0.0.1:9191 --enable-threads -d /tmp/uwsg.log --pidfile /tmp/uwsgipid
#stop with uwsgi command:
#uwsgi --stop /tmp/uwsgipid
#stop
#ps -ef|grep uwsgi|grep hello|awk '{print $2}'|xargs kill -9
