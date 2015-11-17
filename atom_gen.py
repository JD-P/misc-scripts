from bs4 import BeautifulSoup
import time

def gen_iso_8601():
    """Generate an ISO 8601 date+time stamp for the current time in UTC."""
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())

entry_soup = BeautifulSoup("<entry>", "xml")
title = input("What is the title of the entry?:")
title_tag = entry_soup.new_tag("title")
title_tag.string = title
url = input("What is the URL of the entry?:")
link_tag = entry_soup.new_tag("link", href=url)
pound_url = url.replace("#", "/")
date_of_publish = input("What is the date of publish for the linked item?" +
                        " (YYYY-MM-DD format):")
website = "".join(url.split("/")[2].split("www."))
_id_tag = entry_soup.new_tag("id")
_id_tag.string = "tag:" + website + "," + date_of_publish + ":" + pound_url.split(website)[1]
updated_tag = entry_soup.new_tag("updated")
updated_tag.string = gen_iso_8601()
entry_tag = entry_soup.entry
entry_tag.append(title_tag)
entry_tag.append(link_tag)
entry_tag.append(_id_tag)
entry_tag.append(updated_tag)
print(entry_soup.prettify())
