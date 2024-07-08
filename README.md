# Open-Cookie-Database

The [Open Cookie Database](open-cookie-database.csv) is an effort to describe and categorise all major cookies. All cookie descriptions are saved in a [downloadable CSV file](open-cookie-database.csv). All contributions to the CSV file are welcomed.

# How to contribute

All contributions are gratefully received. To contribute to the Open Cookie Database, please follow these steps:
1. Fork the repository
2. Add your cookie to the [open-cookie-database.csv](open-cookie-database.csv) file. Please make sure the information is as accurate and complete as possible.
3. For the ID column, we use randomly generated UUIDs. You can generate a random UUID using any library or online tool.
4. Commit your changes
5. Submit a pull request

# Category Descriptions

The definitions of the categories are as follows:

- Functional (also known as technical, essential or strictly necessary)
- Personalization (also known as preferences)
- Analytics (also known as performance or statistics)
- Marketing (also known as tracking or social media)
- Security

# Wildcard match
The last column in the database is called "Wildcard match". A `0` in this column means that the cookie name is not a wildcard, and a 1 means that the cookie name is a wildcard.

Where a cookie name is *not* a wildcard, it means that the cookie name is a fixed string.  For example, the cookie name `_ga` will always be `_ga` when set by Google Analytics.

However, if a cookie name is a wildcard, it means the exact cookie name may change from one website to another. Thankfully, the cookie name will always match a certain pattern. For example, the cookie `_gac_1234` is a wildcard cookie name, because the `1234` part of the cookie name can be any string.
