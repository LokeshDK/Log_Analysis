#!/usr/bin/env python3
#
# import postgresql library
import psycopg2

DBNAME = "news"


def execute_query(query, question):
    # Connect to Database
    try:
        db = psycopg2.connect(database=DBNAME)
    except psycopg2.Error as e:
        print(e)
    c = db.cursor()
    # Execute SQL Query
    try:
        c.execute(""" """ + query + """ """)
        # Get the table data in a variable
        all_data = c.fetchall()
    except psycopg2.Error as e:
        print(e)

    print(question)
    # print all the values in iteration
    for data in all_data:
        print("{:^10} | {:^3} Views"
              .format(data[0], data[1]))

    # Close DB COnnection
    db.close()    


def top_viewed_article():
    """  define new funtion for getting Query 1: Top Articles and total views """
    execute_query("""SELECT DISTINCT articles.title, t1.views FROM articles, log,
                    (SELECT SUBSTRING(path,10) AS path, COUNT(path) AS views
                    FROM log WHERE path != '/' GROUP BY log.path) AS t1
                    WHERE articles.slug = t1.path ORDER BY views DESC LIMIT 3;""",
                    "\nQuery 1 RESULT: What are the most popular three articles of all time?")

    
def top_authors():
    """ Define new method for getting Query 2: Top Author name and their total views """
    execute_query("""SELECT name, sum(views) AS views FROM author_n_view GROUP BY name ORDER BY views DESC;""",
                    "\nQuery 2 RESULT: Who are the most popular " +
                    "article authors of all time?")
    

def error_days():
    """ define new funtion for getting Query 3: Day where most error has occured """
    # Execute SQL Query
    execute_query("""select to_char(time, 'FMDD-FMMonth, YYYY') as day, 
                  round(count(*) * 100.0 / (select count(*) from log 
                  where path != '/') * 100,2) as percentage from log 
                  where path != '/' and status != '200 OK' group by day 
                  order by percentage desc LIMIT 1;""",
                  "\nQuery 3 RESULT: On which days did more than 1% of " +
                  "requests lead to errors?")


# Mail function to call all methods
if __name__ == '__main__':
    top_viewed_article()
    top_authors()
    error_days()
