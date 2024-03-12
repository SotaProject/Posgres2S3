# Posgres2S3
Backup Postgresql database to S3 daily via crontab 

## Restore
`gunzip < prefix_00000-00-00-00-00-00.sql.gz | psql DB`
