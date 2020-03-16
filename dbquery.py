#!/usr/bin/env python3

import psycopg2

class txt:
    CYAN = '\033[96m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def top_articles():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = """
                select articles.title, count(*) as page_views
                from articles,log
                where log.path = '/article/' || articles.slug
                group by articles.title
                order by page_views desc
                limit 3;
                """
    c.execute(query)
    result = c.fetchall()
    
    title = '*** TOP ARTICLES ***'
    print('\n' + txt.CYAN + txt.BOLD + txt.UNDERLINE + title.center(55) + txt.END + '\n')
    for r in result:
        print (txt.BOLD + "  ", r[0], ":  " + txt.END, r[1],"views"  )
    db.close()

def top_authors():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = """
                select authors.name, count(path) as page_views
                from log, articles, authors
                where log.path like '%' || articles.slug and authors.id = articles.author
                group by name
                order by page_views desc;
                """
    c.execute(query)
    result = c.fetchall()
   
    title = '*** TOP AUTHORS ***'
    print('\n' + txt.GREEN + txt.BOLD + txt.UNDERLINE + title.center(55) + txt.END + '\n')
    for r in result:
        print (txt.BOLD + "  ", r[0], ":  " + txt.END, r[1],"views"  )
    db.close()

def error_log():
    db = psycopg2.connect(database="news")
    c = db.cursor()
    query = """
                select TO_CHAR(bad_req.dt,'Mon DD, YYYY') as date,
                    CONCAT(CAST (ROUND(bad_req.num::decimal*100/all_req.num,2) as VARCHAR)) as percent
                from (select DATE(time) as dt, COUNT(*) as num
                from log
                    where CAST(substring(status, 1,1) as NUMERIC) > 2
                        group by dt) as bad_req
                    join (select DATE(time) as dt, COUNT(*) as num
                    from log group by dt) as all_req
                on bad_req.dt = all_req.dt
                where (bad_req.num::decimal*100/all_req.num) >= 1;
                """
    c.execute(query)
    result = c.fetchall()

    title = '*** HIGH ERROR DAYS ***'
    print('\n' + txt.RED + txt.BOLD + txt.UNDERLINE + title.center(55) + txt.END + '\n')
    for r in result:
        print (txt.BOLD + "  ", r[0], ":  " + txt.END, r[1],"%"  )
    db.close()

if __name__ == '__main__':
    top_articles()
    top_authors()
    error_log()


