CREATE VIEW article_views AS SELECT DISTINCT articles.title, t1.views FROM articles, log, (SELECT SUBSTRING(path,10) AS path, COUNT(path) AS views FROM log WHERE 
path != '/' GROUP BY log.path) AS t1 WHERE articles.slug = t1.path ORDER BY views DESC;

CREATE VIEW author_title AS SELECT DISTINCT article_views.title, articles.author FROM article_views INNER JOIN articles ON article_views.title = articles.title 
ORDER BY articles.author ASC;

CREATE VIEW author_n_view AS SELECT DISTINCT t1.name, article_views.views FROM (SELECT DISTINCT title, authors.name FROM authors, author_title WHERE authors.id = 
author_title.author ORDER BY authors.name ASC) AS t1, article_views WHERE article_views.title = t1.title ORDER BY article_views.views DESC;