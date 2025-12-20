# 🛠️ BFMC: Embedded Platform Setup Guide
[![Platform: Mbed OS](https://img.shields.io/badge/Platform-Mbed--OS-blue.svg)](https://os.mbed.com/)
[![Board: Nucleo-F401RE](https://img.shields.io/badge/Board-Nucleo--F401RE-red.svg)](https://www.st.com/en/evaluation-tools/nucleo-f401re.html)

This document provides a step-by-step guide to configuring your environment for the **Bosch Future Mobility Challenge** embedded platform.

---

## 📋 1. Preliminary Setup
Before you initiate the building process, ensure your environment is correctly configured. 

> [!IMPORTANT]
> All installations should use **Python 3.6+**. 
> Administrative privileges may be required for some steps.

### 🔧 Required Tools

| Tool | Purpose | Link |
| :--- | :--- | :--- |
| **Python 3.6+** | Scripting & Package Management | [Download](https://www.python.org/downloads/) |
| **CMake** | Build Process Management | [Download](https://cmake.org/download/) |
| **GNU Arm Toolchain** | Cross-compiler for Nucleo-F401RE | [Download](https://developer.arm.com/tools-and-software/open-source-software/developer-tools/gnu-toolchain/gnu-rm/downloads) |

---

## 💻 2. Installation Steps

### 🔹 Ninja & Mbed-tools
Ninja focuses on build speed, while `mbed-tools` is essential for managing the project structure. Run the following in your terminal:


# Install Ninja build system
pip install ninja

# Install Mbed-tools
pip install mbed-tools

# Install formatting tools for build output
pip install prettytable intelhex

## 🏗️ Building and Flashing

This module focuses on the transition from source code to hardware execution. It is a critical part of the **Embedded Platform** development workflow for the BFMC competition.

---

# 🧠 The Engineering Logic
Our build system is designed to be **cross-platform**. We use `mbed-tools` to compile high-level C++ code into a machine-readable `.bin` (binary) file specifically optimized for the **ARM Cortex-M4** architecture of the **Nucleo-F401RE**.

---

# 🛠️ Step 1: Building the Project
Based on the **MBED CLI 2** documentation, the `mbed-tools` command manages the build lifecycle. This ensures all dependencies are linked and the code is optimized for the microcontroller.

# Build Command
Run the following in your terminal to compile the code:

mbed-tools compile -m NUCLEO_F401RE -t GCC_ARM
## 🧩 Adding New Components

To maintain a scalable and professional codebase, our project follows a strict architectural structure. This section guides you through adding new features while keeping the repository clean and organized.

---

## 🏗️ Project Structure Logic
We separate interface from implementation to ensure modularity. You will notice that the `include` and `source` directories mirror each other:
* **`.hpp` files** (Headers/Interfaces) reside under the `include/` directory.
* **`.cpp` files** (Implementation) reside under the `source/` directory.



---

## 🛠️ Using the `newComponent.py` Script
To simplify development and avoid manual folder creation, we use an automation script. This ensures every new feature follows the existing project structure and naming conventions.

### 🚀 Execution Steps
1.  **Navigate** to the directory containing the script:
    `Embedded_Platform\newComponent\`
2.  **Run** the script using your terminal or IDE:
    ```bash
    python newComponent.py
    ```
3.  **Enter Category:** Select the functional area for your component:
    * `brain`: Decision-making logic.
    * `driver`: Low-level hardware interaction.
    * `periodics`: Tasks that run at specific time intervals.
    * `utils`: Helper functions and general utilities.
4.  **Enter Name:** Provide a clear, descriptive name for your new component.
5.  **Serial Callback:** Choose whether to automatically register a serial callback command for this component (used for real-time debugging).

---

## ⚠️ Compatibility Note
> [!WARNING]
> The `newComponent.py` script and the flashing tools are optimized for **Windows environment**. Correct functionality on **Linux** is not guaranteed. If using Linux, please verify the created file paths manually.

---

## 💡 Why use this script?
* **Consistency:** Every team member creates files in the exact same way.
* **Speed:** Automatically generates boilerplate code so you can focus on the logic.
* **Safety:** Reduces human error in linking headers and sources.

# 🔍 Debugging and Communication

This section explains how to interact with the vehicle in real-time and details the safety protocols governing the hardware.

---

## 🛠️ 1. Serial Debugging (PuTTY)
Direct communication with the Nucleo board is essential for real-time telemetry and manual testing.

### Configuration Steps
1. **Identify Port:** Connect the Nucleo to your PC and check the **COM Port** in the Windows *Device Manager*.
2. **Setup PuTTY:** Configure the connection with these parameters:
   * **Connection type:** Serial
   * **Serial line:** `COMxx`
   * **Speed:** `115200`
3. **Terminal Configuration:** * Set **Local echo** to `Force on`.
   * Set **Local line editing** to `Force on`.
4. **Connection:** Click **Open**. A successful connection is confirmed by the message: `I'm alive`.

> [!IMPORTANT]
> When sending commands manually via PuTTY, you must press **Ctrl+M**, then **Ctrl+J**, and then **Enter** to signal the end of a message.

---

## ⚡ 2. Power States (Safety Logic)
To protect the vehicle’s hardware and the user, we implemented three distinct power states (KL - *Klemmenbezeichnung*):

| State | Name | Description |
| :--- | :--- | :--- |
| **KL0** | Standby | No functionality. All incoming commands are discarded. |
| **KL15** | Sensor Mode | Only interactions with sensors are active (IMU, Voltage, Consumption). |
| **KL30** | Operational | Full control enabled. Vehicle can now steer and drive. |

### 🔋 PowerManager & Battery Protection
Our `PowerManager` system monitors the LiPo battery in real-time:
* **Warning Level (7.2V):** A periodic warning is sent via serial to alert the operator.
* **Critical Level (7.0V):** The Nucleo sends an error message and enters **Sleep Mode** to prevent cell damage.
* **Hot-Swap:** Battery capacity can be updated via serial after a replacement without needing to rebuild the firmware.

---

## 💬 3. Message Structure & Protocol
The Nucleo utilizes a specific string-based protocol for high-reliability communication.



### Standard Formats
* **Request (PC to Nucleo):** `#command:val1;val2;valx;;\r\n`
* **Response (Nucleo to PC):** `@command:response1;response2;responsex;;\r\n`

### Command Reference Table
| Command | Description | Range | Example Request |
| :--- | :--- | :--- | :--- |
| `speed` | Sets target speed | -500 to +500 [mm/s] | `#speed:60;;\r\n` |
| `steer` | Sets steering angle | -230 to +230 [deg*10] | `#steer:180;;\r\n` |
| `vcd` | Controlled Move | Speed; Steer; Time | `#vcd:80;-130;121;;\r\n` |
| `kl` | Set Power State | 0, 15, or 30 | `#kl:15;;\r\n` |
| `imu` | Enable IMU | bool (0 or 1) | `#imu:1;;\r\n` |

### System Limits
To ensure hardware longevity, the following hard limits are enforced:
* **Max Speed:** `500 mm/s`
* **Max Steering:** `25°`
* **Max Move Duration:** `25.5 seconds` (255 deciseconds)
* **IMU Frequency:** `6.67 Hz` (150 ms)

---

> [!TIP]
> If the vehicle behavior is inconsistent, always verify the **Power State** first. Motor commands will not execute unless the system is in **KL30**.
# 🔄 Main Software Flow

This section provides a deep dive into the functional operation and architectural hierarchy of the embedded platform’s software.

---

## 🌐 Overview
The following architecture outlines how the different software layers interact to provide a stable and responsive autonomous platform. By separating the system into distinct layers, we ensure that high-level decision-making (Planning) is decoupled from low-level hardware control (Actuation).



---

## 🏗️ System Hierarchy
Our software structure is designed to showcase the interaction between the **Main Loop** and various specialized subsystems. This hierarchical approach allows for:

* **Modular Interaction:** Components communicate through defined interfaces.
* **Synchronous Execution:** The main loop manages time-critical tasks (like motor control) while handling asynchronous events (like serial commands).
* **Predictability:** Each layer has a specific responsibility, making debugging more efficient during track testing.

---

## 🔍 Deep Dive: Component Interaction
The software flow is generally divided into three primary stages:

1.  **Sensing Layer (Input):**
    * Reads raw data from the IMU, encoders, and battery sensors.
    * Filters raw signals to provide stable values for the logic layers.

2.  **Processing Layer (Logic):**
    * Parses incoming serial messages from the Raspberry Pi or PC.
    * Manages the **Power State Machine** (KL0, KL15, KL30).
    * Calculates the required PWM values using calibration polynomials.

3.  **Actuation Layer (Output):**
    * Converts processed logic into physical movement via the Steering and Motor drivers.
    * Sends feedback responses back via serial to confirm command execution.



---

## 🔄 The Main Loop Logic
The core of the system is a non-blocking main loop that ensures high-frequency updates for critical vehicle functions. 

* **Priority 1:** Safety checks (Battery levels and Power States).
* **Priority 2:** Motor and Steering PWM updates.
* **Priority 3:** Serial message parsing and telemetry reporting.

---

> [!TIP]
> Understanding this flow is essential when implementing new features via the `newComponent.py` script. Always consider which layer your new feature belongs to (e.g., a new sensor goes into the Sensing Layer, while a new maneuver goes into the Processing Layer).
> # 🎯 Calibration Integration

This section explains how to integrate calibration results from the BFMC Dashboard into the Embedded Platform and the internal logic that enables high-precision control.

---

## 🌐 Overview
To achieve accurate movement, the vehicle requires more than generic commands. The dashboard generates C++ source files containing **polynomial coefficients**, **steering offsets**, and **spline data**. These parameters ensure:
* Steering commands translate to exact wheel angles.
* Motor speeds are adjusted via precise polynomial mapping.
* Mechanical zero-offsets are corrected automatically.

---

## 🧠 Internal Behavior & Logic
When calibration files are added, the system shifts from "Legacy" mode to "Calibrated" mode.

### 1. Calibration Flags
Within the generated `speedingmotor.cpp` and `steeringmotor.cpp`, the following macros are updated:
* **Default Firmware:** `#define calibrated 0` (Uses basic interpolation).
* **Calibrated Firmware:** `#define calibrated 1` (Enables polynomial logic and custom safety limits).

### 2. Polynomial-Based Control
Instead of a lookup table, the system uses a mathematical expression to map speed/angle to a PWM value. The script fills the following placeholder with track-specific data:


int CSpeedingMotor::computePWMPolynomial(int speed){
    int64_t y = zero_default;
    // The Dashboard inserts the calculated polynomial expression here
    return (int)y;
}
