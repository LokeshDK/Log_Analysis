# import postgresql library
import psycopg2

DBNAME = "news"


# define new funtion for getting Query 1: Top Articles and total views
def top_viewed_article():
    # Connect to Database
    db = psycopg2.connect(database=DBNAME)
    print("connected to db")
    c = db.cursor()
    # Execute SQL Query
    c.execute("SELECT DISTINCT articles.title, views FROM articles, " +
              "(SELECT REPLACE(SUBSTRING(path,10), '-', ' ') AS title, " +
              "COUNT(path) AS views " +
              "FROM log WHERE path != '/' GROUP BY path " +
              "ORDER BY views DESC LIMIT 3) " +
              "top_views WHERE LOWER(articles.title) LIKE '%' || " +
              "top_views.title || '%' " +
              "ORDER BY top_views.views DESC;")

    # Get the table data in a variable
    article_list = c.fetchall()
    print("\nQuery 1 RESULT: What are the most popular " +
          "three articles of all time?")
    # print all the values in iteration
    for top_article in article_list:
        print("{:^10} | {:^3}"
              .format(top_article[0], top_article[1]) +
              " Views")

    # Close DB COnnection
    db.close()
    print("\n Connection to db has been closed")


# Define new method for getting Query 2: Top Author name and their total views
def top_authors():
    # Connect to Dtabase
    db = psycopg2.connect(database=DBNAME)
    print("connected to db")
    c = db.cursor()
    # Execute SQL Query o cretae view to get list of top viwed article
    c.execute("CREATE VIEW top_views AS SELECT DISTINCT articles.title, " +
              "SUM(views) as total_views FROM articles, " +
              "(SELECT REPLACE(SUBSTRING(path,10), '-', ' ') AS title, " +
              "COUNT(path) AS views FROM log WHERE path != '/' " +
              "GROUP BY path " +
              "ORDER BY views DESC) top_views " +
              "WHERE LOWER(articles.title) LIKE '%' " +
              "|| top_views.title || '%' GROUP BY articles.title ORDER BY " +
              "total_views DESC;")

    # Execute SQL Query to get result of top article authors.
    c.execute("select distinct name as author_name, " +
              "sum(total_views) as total_views " +
              "from (select distinct articles.title, authors.name, " +
              "top_views.total_views from authors inner join articles on " +
              "authors.id = articles.author inner join top_views " +
              "on top_views.title = articles.title " +
              "order by total_views desc) as temp " +
              "group by name order by total_views desc;")

    # Get the table data in a variable
    article_list = c.fetchall()
    print("\n Query 2 RESULT: Who are the most popular " +
          "article authors of all time?")
    # print all the values in iteration
    for top_view in article_list:
        print("{:^10} | {:^3}"
              .format(top_view[0], top_view[1]) +
              " Views")

    c.execute("DROP VIEW top_views")
    # Close DB COnnection
    db.close()
    print("\n VIEW DROPPED!!!! ")
    print("connection to db has been closed")


# define new funtion for getting Query 3: Day where most error has occured
def error_days():
    # Connect to Dtabase
    db = psycopg2.connect(database=DBNAME)
    print("connected to db")
    c = db.cursor()
    # Execute SQL Query
    c.execute("select to_char(time, 'FMDD-FMMonth, YYYY') as day, " +
              "round(count(*) * 100.0 / (select count(*) from log " +
              "where path != '/') * 100,2) as percentage from log " +
              "where path != '/' and status != '200 OK' group by day " +
              "order by percentage desc LIMIT 1;")

    # Get the table data in a variable
    article_list = c.fetchall()
    print("\n Query 3 RESULT: On which days did more than 1% of " +
          "requests lead to errors?")
    # print all the values in iteration
    for top_article in article_list:
        print("{:^10} | {:^3}"
              .format(top_article[0], top_article[1]) +
              "% Error")

    # Close DB COnnection
    db.close()
    print("\n connection to db has been closed")

# Mail function to call all methods
if __name__ == '__main__':
    top_viewed_article()
    top_authors()
    error_days()
