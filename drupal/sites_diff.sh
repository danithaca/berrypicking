echo "Usage: ./site_diff.sh @site1 @site2"

drush $1 pm-list --status=enabled --format=csv | sort > /tmp/1.list
drush $2 pm-list --status=enabled --format=csv | sort > /tmp/2.list
meld /tmp/1.list /tmp/2.list
#diff /tmp/1.list /tmp/2.list
