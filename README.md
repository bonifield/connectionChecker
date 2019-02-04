# connectionChecker
check your ISP reliability with various scripts

### pinglog.py
- make a folder in /var/log and give the user permissions
```
sudo mkdir /var/log/pinglog
sudo chown username:groupname /var/log/pinglog
```
- add logrotate options:  keep for 30 days, rotate daily, compress old logs, set 0640 perms
```
sudo nano /etc/logrotate.conf
```
add the lines
```
/var/log/pinglog/pinglog.log {
	rotate 30
	daily
	missingok
	compress
 	create 0644 username groupname
}
```
- add a crontab entry
```
crontab -e
```
add the line
```
* * * * * /your/path/pinglog.py
```

### to check your logs
```
awk '{print $2,$3}' /var/log/pinglog/pinglog.log | sort | uniq -c | sort -nrk1 | sed -e 's/^ \+//g'
or just the up/down counts
awk '{print $3}' /var/log/pinglog/pinglog.log | sort | uniq -c | sort -nrk1 | sed -e 's/^ \+//g'
```
