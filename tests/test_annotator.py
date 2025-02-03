import os
import pytest
from iot_tools.annotator import IoTAnnotator

def test_annotator_init():
    annotator = IoTAnnotator("sample_images/")
    assert annotator.folder_path == "sample_images/"
    assert annotator.output_csv == "annotations.csv"

def test_annotator_invalid_folder():
    annotator = IoTAnnotator("invalid_path/")
    assert not os.path.exists(annotator.folder_path)
