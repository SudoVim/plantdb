# plantdb

Database for storing and retrieving information about plants. This project
represents the main organization point for the entire plantdb series of
projects.

## MongoDB

I'm using MongoDB for the project because it allows me to be less strict with
the schema. I'd use a relational database for speed and the ability to link
multiple tables together, but I don't really need the underlying speed.

## categories collection

The `categories` collection contains all of the categories that plants can fall into:

```
{
  "name": "<name>"
}
```

## plants collection

The `plants` collection contains information about specific plants. It looks like:

```
{
  "name": "<plant_name>",
  "latin": "<latin_name>",
  "category": "<category>",
  "description": "<plant_description>",
  "tags": [
    "tag_1",
    "tag_2"
  ]
}
```
