import os
import pytest
from iot_tools.simulator import IoTSimulator

def test_simulator_init():
    simulator = IoTSimulator("annotations.csv", "sample_images/")
    assert os.path.exists(simulator.csv_file)
    assert os.path.exists(simulator.image_folder)

def test_simulator_update_status():
    simulator = IoTSimulator("annotations.csv", "sample_images/")
    simulator.annotations = {
        "image1.jpg": [{"appliance": "Light", "status": "Off", "coords": (10, 10, 50, 50)}]
    }
    simulator.update_status("Light On")
    assert simulator.annotations["image1.jpg"][0]["status"] == "On"
