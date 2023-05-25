import os
import tempfile

from maven_artifact import Downloader
from maven_artifact.utils import Utils


def test_downloader_of_existing_artifact():
    artifact = Utils.create_artifact_from_mvn_coordinates("org.apache.solr:solr:war:3.5.0")

    dl = Downloader()

    tmpdirname = tempfile.TemporaryDirectory()

    tmpfile = os.path.join(tmpdirname.name, "example.war")

    dl.download(artifact, filename=tmpfile)

    assert os.path.exists(tmpfile)

    tmpdirname.cleanup()
