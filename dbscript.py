#!/usr/bin/env python3

import psycopg2

# Database queries

# Database query 1: What are the most popular three articles of all time?
pop_articles = """
                select articles.title, count(*) as page_views
                from log, articles
                where log.status='200 OK' and articles.slug = substr(log.path, 10)
                group by articles.title
                order by page_views desc
                limit 3;
                """

# Database query 2: Who are the most popular article authors of all time?
pop_authors = """
                select authors.name, count(*) as page_views
                from articles, authors, log
                where articles.slug = substr(log.path, 10) and authors.id = articles.author and log.status='200 OK' 
                group by authors.name
                order by page_views desc;
                """

# Database query 3: On which day did more than 1% of requests lead to errors?
error_percent = """
                select TO_CHAR(bad_req.dt,'Mon DD, YYYY') as date,
                    CONCAT(CAST (ROUND(bad_req.num::decimal*100/all_req.num,2) as VARCHAR), '%') as percent
                from (select DATE(time) as dt, COUNT(*) as num
                from log
                    where CAST(substr(status, 1,1) as NUMERIC) > 2
                        group by dt) as bad_req
                    join (select DATE(time) as dt, COUNT(*) as num
                    from log group by dt) as all_req
                on bad_req.dt = all_req.dt
                where (bad_req.num::decimal*100/all_req.num) >= 1;
                """


# Query data from the database, open and close the connection
def query_db(query_request):
    conn = psycopg2.connect(database="news")
    cursor = conn.cursor()
    cursor.execute(query_request)
    output = cursor.fetchall()
    conn.close()
    return output


# Writing the report

# Print a title of the report
def print_title(title):
    print ("\n\t\t" + title + "\n")

# Print report's output  
def print_output(output, append):
    [print(str(r[0])+' -- '+str(r[1])+append) for r in output]
    print()


# Print the three most popular articles of all time
def most_pop_articles():
    most_pop_articles = query_db(pop_articles)
    print_title("Most popular articles of all time")
    print_output(query_db(pop_articles), " views")


# Print the most popular authors of all time
def most_pop_authors():
    most_pop_authors = query_db(pop_authors)
    print_title("Most popular authors of all time")
    print_output(query_db(pop_authors), " views")


# Print which day(s) had more than 1% of requests lead to errors
def error_request_days():
    error_request_days = query_db(error_percent)
    print_title("Days with more than 1 percent of requests leading to errors")
    print_output(query_db(error_percent), " error rate")


if __name__ == '__main__':
    most_pop_articles()
    most_pop_authors()
    error_request_days()