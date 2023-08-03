
select (
insert News {
    title := <str>$title,
    date_published := <cal::local_date>$date_published,
    author:= (
        select User
        filter .id = <uuid>$author
    ),
    section := <str>$section,
    country := <str>$country,
    news_content := <str>$news_content
}
) {id, author, news_content};
