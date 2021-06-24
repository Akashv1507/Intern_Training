'''
Using psycopg2 module to interface with a postgreSQL database
pip install psycopg2
'''
import psycopg2
from src.appConfig import loadAppConfig, getAppConfigDict

# get these variables from some config mechanism so that connection is not exposed and hardcoded

configDict = loadAppConfig()
hostStr = configDict["hostStr"]
dbStr = configDict["dbStr"]
uNameStr = configDict["uNameStr"]
dbPassStr = configDict["dbPassStr"]

try:
    # get the connection object
    conn = psycopg2.connect(host=hostStr, dbname=dbStr,
                            user=uNameStr, password=dbPassStr)
    # get the cursor from connection
    cur = conn.cursor()
    print("PostgreSQL server information")
    print(conn.get_dsn_parameters(), "\n")
    # create the query
    # postgreSQL_select_Query = "select sch_date + (15 * (sch_block-1) * interval '1 minute') as sch_time, \
    #     sch_val from public.schedules where sch_utility=%s and sch_type=%s \
    #         and sch_date between %s and %s order by sch_date, sch_block"

    # # execute the query
    # cur.execute(postgreSQL_select_Query,
    #             ('util1', 'urs', dt.datetime(2020, 7, 1), dt.datetime(2020, 7, 1)))
    # # fetch all the records from cursor
    # records = cur.fetchall()

    # # get the column names returned from the query
    # colNames = [row[0] for row in cur.description]

    # # create a dataframe from the fetched records
    # records = pd.DataFrame.from_records(records, columns=colNames)

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
    records = 0
finally:
    # closing database connection and cursor
    if(conn):
        # close the cursor object to avoid memory leaks
        cur.close()
        # close the connection object also
        conn.close()