from ibis.expr.types.relations import Table

from orlando.materialization import Materialization
from orlando.model import OrlandoModel

class SrcRecentlyPlayed(OrlandoModel):
    def __init__(self):
        self.materialization = Materialization.TABLE
        self.source_table_name = "recently_played"
        self.source_schema_name = "raw_music_matters_1"
        self.destination_table_name = "src_recently_played"
        self.destination_schema_name = "dev_music_matters_1"
        self.database = "dbttest"

    def select(self) -> Table:
        raw_recently_played: Table = self.source_table_obj
        return raw_recently_played
