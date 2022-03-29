#!/bin/sh
# wait-for-postgres.sh

set -e

host="$1"
shift
cmd="$@"

until pg_isready -U postgres -d postgres -h "$host" ; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"
exec $cmd
