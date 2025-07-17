import sys
from awsglue.utils import getResolvedOptions

args = getResolvedOptions(sys.argv, ['startDate', 'endDate'])

start_date = args['startDate']
end_date = args['endDate']

print(f"Glue job started for date range: {start_date} to {end_date}")
