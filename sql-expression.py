from sqlalchemy import(
    create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#executing the instructions from our localhost "chinook" database

db = create_engine("postgresql:///chinook")

meta = MetaData(db)

# Creates variable for artist table 
artist_table = Table(
    "Artist", meta, 
    Column("AtistId", Integer, primary_key=True),
    Column("Name", String)
    )

#Creates variable for album table 
album_table = Table(
    "Album", meta,
    Column("AlbumId", Integer, primary_key=True ),
    Column("Title", String),
    Column("ArtistId", Integer, ForeignKey("artist_table.ArtistId"))

)

#creates variable for track table
track_table = Table(
    "Track", meta,
    Column("TrackId", Integer, primary_key=True),
    Column("Name", String),
    Column("AlbumId", Integer, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Integer, primary_key=False ),
    Column("GenreId", Integer, primary_key=False ),
    Column("Composer", String),
    Column("Milliseconds", Integer),
    Column("Bytes", Integer),
    Column("UnitPrice", Float)
)


#connection to database
with db.connect() as connection:

 #Query- select all records from the "Artist" table

 select_query = artist_table.select()

 results= connection.execute(select_query)
 for result in results:
    print(result)