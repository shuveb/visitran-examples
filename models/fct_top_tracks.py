from ibis.expr.types.relations import Table

from src_tracks import SrcTracks
from src_artists import SrcArtists
from src_recently_played import SrcRecentlyPlayed

from orlando.materialization import Materialization

class FctTopTracks(SrcTracks, SrcArtists, SrcRecentlyPlayed):
    def __init__(self):
        self.materialization = Materialization.TABLE
        self.destination_table_name = "fct_top_tracks"
        self.destination_schema_name = "dev_music_matters_1"
        self.database = "dbttest"

    def select(self) -> Table:
        tbl_tracks = SrcTracks().select()
        tbl_artists = SrcArtists().select()
        tbl_recently_played = SrcRecentlyPlayed().select()

        fct_top_tracks = tbl_recently_played \
            .join(
                tbl_tracks, tbl_recently_played.track_id == tbl_tracks.track_id
            )
        fct_top_tracks = fct_top_tracks \
            .join(
                tbl_artists, fct_top_tracks.artist_id == tbl_artists.artist_id
            )

        fct_top_tracks = fct_top_tracks.group_by(
            [fct_top_tracks.track_id,
                fct_top_tracks.track_name,
                fct_top_tracks.artist_name]
        ).aggregate(
            fct_top_tracks.track_id.count().name("track_listen_count")
        )

        return fct_top_tracks
