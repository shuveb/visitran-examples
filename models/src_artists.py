from ibis.expr.types.relations import Table

from orlando.materialization import Materialization
from orlando.model import OrlandoModel

class SrcArtists(OrlandoModel):
    def __init__(self):
        self.materialization = Materialization.TABLE
        self.source_table_name = "artists"
        self.source_schema_name = "raw_music_matters_1"
        self.destination_table_name = "src_artists"
        self.destination_schema_name = "dev_music_matters_1"
        self.database = "dbttest"

    def select(self) -> Table:
        raw_recently_played: Table = self.source_table_obj
        return raw_recently_played[
            raw_recently_played["id"].name("artist_id"),
            raw_recently_played["name"].name("artist_name"),
            "popularity",
            "followers",
            "genres"
        ]
