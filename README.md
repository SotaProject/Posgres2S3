# Posgres2S3
Backup Postgresql database to S3 daily via crontab 

## Restore
`gunzip < prefix_0000-00-00-00-00-00.sql.gz | PGPASSWORD=PASSWORD psql -h HOST -U USER DATABASE`
