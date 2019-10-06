if [[ -z $1  ]]
then

uwsgi --http 0.0.0.0:5000 --plugin python  --module hello --callable app --stats 127.0.0.1:9191 --master --processes 10 --threads 5 -d /tmp/uwsg.log --pidfile /tmp/uwsgipid

else
uwsgi --stop /tmp/uwsgipid
#ps -ef|grep uwsgi|grep hello|awk '{print $2}'|xargs kill -9
fi
