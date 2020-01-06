#!/bin/bash
echo " nama program: "
read n
kill -9 $(ps -ef | grep $n | awk {'print $2" "$8'})
