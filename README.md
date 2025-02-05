# 🚀 IoTVision: Open-Source IoT Device Annotation & Simulation!

## 🔹 What is IoTVision?

IoTVision is a Python-based open-source package designed to help researchers, developers, and engineers annotate IoT devices in images and simulate their status dynamically.

- **IoT Annotator**: Easily label IoT devices in images with bounding boxes and store metadata in a CSV file.
- **IoT Simulator**: Toggle IoT device states using simple commands and visualize the updates in real time.

## 🎯 Who is it for?

- **Smart Home & Industrial IoT Developers** 🏠🏭
- **Computer Vision & AI Researchers** 📸🤖
- **Simulation & Digital Twin Enthusiasts** 🌍💡

If you're working with smart environments, IoT-based automation, or digital twins, this tool will make your workflow smoother!

## ⚡ Why Should You Use It?

✅ **Automates IoT Device Annotation** – No more manual tracking!
✅ **Enables Real-Time IoT Device Simulation** – Easily control and monitor states.
✅ **Lightweight & Easy to Use** – Simple command-line interface.
✅ **Open Source & Extensible** – Contribute and expand its capabilities.

---

## 🔧 Installation

Install IoTVision using pip:

```sh
pip install iotvision
```

---

## 🚀 Usage

### 1️⃣ Using IoTVision in a Python Script

```python
from iotvision import IoTAnnotator, IoTSimulator

# Annotate IoT devices
folder_path = "path/to/image_folder"
annotator = IoTAnnotator(folder_path)
annotator.annotate_images()

# Simulate IoT devices
# Make sure that you have an empty annotations.csv file in the project directory.
csv_path = "annotations.csv"
simulator = IoTSimulator(csv_path, folder_path)
simulator.start()
```

---

### 2️⃣ Using IoTVision from the Command Line

#### Annotating Images

Run the following command to annotate IoT devices in images:

```sh
iot-annotate
```

You will be prompted to enter the folder path containing images. The annotation process involves:

- Clicking on images to draw bounding boxes
- Pressing **o** for "On", **f** for "Off", **t** to set an appliance type, and **s** to save
- Annotations are saved to `annotations.csv`

#### Simulating IoT Devices

Run the following command to start the IoT simulator:

```sh
iot-simulate
```

The simulator will:

- Load the images and overlay annotations
- Allow users to update device states dynamically using text commands
- Example command format: `fan1 On`
- Type `exit` to quit the simulation

---

## 📌 Example

```sh
# Annotate IoT devices
iot-annotate

# Simulate IoT devices
iot-simulate
```

---

## 📦 Dependencies

- OpenCV (`opencv-python`)
- NumPy

---

## 📝 License

This project is licensed under the **MIT License**.
