curl 'http://192.168.3.10:5000/getserv'
curl -d "champion=Renekton&power=96" -X POST 'http://192.168.3.10:5000/addtoserv'
curl -d "champion=Akali&power=121" -X PUT 'http://192.168.3.10:5000/putinfo'