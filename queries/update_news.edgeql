UPDATE News
    FILTER .id = <uuid>$news_id
    SET {
        title := <str>$title,
        date_published := <cal::local_date>$date_published,
        author := <str>$author,
        section := <str>$section,
        country := <str>$country,
        news_content := <str>$news_content,
    }