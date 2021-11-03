#!/bin/bash

LOGFILE=/tmp/navi.log
PIDFILE=/tmp/navi.pid
SEVERNAME=$(basename $0)

function fn_usage()
{
    echo ""
    echo "Syntax error!!"
    echo " .eg: ${SEVERNAME} <start|stop|query>"
    echo ""
}

function fn_start()
{
    echo -n "Starting ${SEVERNAME} ...         "
    uwsgi --http 0.0.0.0:9000 --wsgi-file webserver.py --master --processes 4 --threads 2 --py-autoreload 1 --pidfile ${PIDFILE} --daemonize ${LOGFILE}
    if [ $? -ne 0 ]; then
        echo "failed" && return 1
    else
        echo "ok" && return 0
    fi
}

function fn_stop()
{
    echo -n "Stopping ${SEVERNAME} ...         "
    ps -ef | grep uwsgi  | grep webserver.py | grep -v grep | awk -F" " '{print $2}' | xargs -I {} kill -9 {} &>/dev/null
    echo "ok" && return 0
}

function fn_query()
{
    echo "Query ${SEVERNAME}. "
    ps -ef | grep uwsgi  | grep webserver.py | grep -v grep
    return 0
}

function fn_main()
{
    [ $# -ne 1 ] && fn_usage && return 1
    [ "x$1" != "xstart" -a "x$1" != "xstop" -a "x$1" != "xquery" ] && fn_usage && return 1
 
    fn_$1
    return $?
}

fn_main "$@"
exit $?
