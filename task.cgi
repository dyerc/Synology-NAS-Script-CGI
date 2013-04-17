#!/bin/sh

echo "Content-type: text/html"
echo ""

if [ -z "$QUERY_STRING" ]; then
  nohup ./myscript.sh > log 2>&1 &
fi

echo "<!DOCTYPE html>"
echo "<html>"
echo " <head>"
echo "  <title>My Task</title>"
echo "  <meta http-equiv=\"refresh\" content=\"3;URL='?done=f'\">"
echo " </head>"
echo "<body>"
echo "  <pre>"
tail -n 20 log
echo "  </pre>"
echo "</body>"
echo "</html>"

exit 0
