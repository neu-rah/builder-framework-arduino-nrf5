# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.
"""

from os import listdir
from os.path import isdir, join

from SCons.Script import DefaultEnvironment

print("r-site.net changed nRF5 pio script!")
print("===================================")

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinonordicnrf5")
assert isdir(FRAMEWORK_DIR)

env.Append(
    ASFLAGS=[],
    # ASFLAGS=["-x", "assembler-with-cpp"],

    CFLAGS=["-std=gnu11"],

    CCFLAGS=[
        "-Os",  # optimize for size
        "-ffunction-sections",  # place each function in its own section
        "-fdata-sections",
        "-Wall",
        "-mthumb",
        "-nostdlib",
        "--param", "max-inline-insns-single=500"
    ],

    CXXFLAGS=[
        "-fno-rtti",
        "-fno-exceptions",
        "-std=gnu++11",
        "-fno-threadsafe-statics"
    ],

    CPPDEFINES=[
        ("ARDUINO", 10805),
        # For compatibility with sketches designed for AVR@16 MHz (see SPI lib)
        ("F_CPU", "16000000L"),
        "ARDUINO_ARCH_NRF5",
        "NRF5",
        # ("DM_GATT_CCCD_COUNT",4),
        ("IS_SRVC_CHANGED_CHARACT_PRESENT",1),
        "%s" % board.get("build.mcu", "")[0:5].upper()
    ],

    LIBPATH=[
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "toolchain", "gcc")
    ],

    CPPPATH=[
        join(FRAMEWORK_DIR, "cores", board.get("build.core")),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "external", "rtx", "include"),

        # DONT USE THIS FROM EXAMPLES.. LET USER DO ITS OWN BSP, ITS SIMPLER
        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "examples", "bsp"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "bsp"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "config"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "softdevice", "common", "softdevice_handler"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "softdevice", "s110", "headers"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "crc16"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "util"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "bootloader_dfu"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "bootloader_dfu","ble_transport"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "bootloader_dfu","hci_transport"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "scheduler"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "timer"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "trace"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "hci"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "uart"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "fifo"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "sensorsim"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "button"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "fds"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "fstorage"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "experimental_section_vars"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "pwm"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "low_power_pwm"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "libraries", "twi"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","common"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","device_manager"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","device_manager","config"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_services","ble_dfu"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_services","ble_gls"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_services","ble_bas"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_services","ble_hrs"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_services","ble_dis"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_advertising"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_error_log"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_db_discovery"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "ble","ble_racp"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "config"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "hal"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "delay"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "gpiote"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "pstorage"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "pstorage", "config"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "ble_flash"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "hal"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "uart"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "config"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "common"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "twi_master"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "sdio"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "timer"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "ppi"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "drivers_nrf", "twi_master"),
        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "components", "drivers_nrf", "twi_master","deprecated","config"),

        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "components", "serialization", "common"),
        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "components", "serialization", "common","transport"),
        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "components", "serialization", "application","transport"),
        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "components", "serialization", "application","codecs","s110","serializers"),
        # join(FRAMEWORK_DIR, "cores", board.get("build.core"),
        #      "SDK", "components", "serialization", "application","codecs","s110","mddleware"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "properitary_rf","gzll"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "properitary_rf","gzll","config"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "device"),

        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "toolchain"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "toolchain","gcc"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"),
             "SDK", "components", "toolchain", "CMSIS", "Include"),

        join(FRAMEWORK_DIR, "variants", board.get("build.variant"))
    ],

    LINKFLAGS=[
        "-Os",
        "-Wl,--gc-sections",
        "-mthumb",
        "--specs=nano.specs",
        "--specs=nosys.specs",
        "-Wl,--check-sections",
        "-Wl,--unresolved-symbols=report-all",
        "-Wl,--warn-common",
        "-Wl,--warn-section-align"
    ],

    LIBSOURCE_DIRS=[join(FRAMEWORK_DIR, "libraries")],

    LIBS=["m"]
)

if "BOARD" in env:
    env.Append(
        CCFLAGS=[
            "-mcpu=%s" % env.BoardConfig().get("build.cpu")
        ],
        LINKFLAGS=[
            "-mcpu=%s" % env.BoardConfig().get("build.cpu")
        ]
    )

env.Append(
    CCFLAGS=[
        "-mcpu=%s" % env.BoardConfig().get("build.cpu")
    ])

# Process softdevice options
softdevice_ver = None
cpp_defines = env.Flatten(env.get("CPPDEFINES", []))
if "NRF52_S132" in cpp_defines:
    softdevice_ver = "s132"
elif "NRF51_S130" in cpp_defines:
    softdevice_ver = "s130"
elif "NRF51_S110" in cpp_defines:
    softdevice_ver = "s110"

print("checking softdevice...");
if softdevice_ver:

    #dfu=""
    dfu=("_ble_dfu" if "BLE_DFU_APP_SUPPORT" in cpp_defines else "")

    env.Append(
        CPPPATH=[
            join(FRAMEWORK_DIR, "cores", board.get("build.core"),
                 "SDK", "components", "softdevice", softdevice_ver+dfu , "headers")
        ],

        CPPDEFINES=["%s" % softdevice_ver.upper()]
    )

    hex_path = join(FRAMEWORK_DIR, "cores", board.get("build.core"),
                    "SDK", "components", "softdevice", softdevice_ver+dfu, "hex")

    for f in listdir(hex_path):
        if f.endswith(".hex") and f.lower().startswith(softdevice_ver):
            env.Append(SOFTDEVICEHEX=join(hex_path, f))

    if "SOFTDEVICEHEX" not in env:
        print("------------------------------------------------------")
        print("Warning! Cannot find an appropriate softdevice binary!")
        print("from: ",hex_path)
        print("------------------------------------------------------")

    # Update linker script:
    ldscript_dir = join(FRAMEWORK_DIR, "cores",
                        board.get("build.core"), "SDK",
                        "components", "softdevice", softdevice_ver+dfu,
                        "toolchain", "armgcc")
    mcu_family = board.get("build.ldscript", "").split("_")[1]
    ldscript_path = ""
    for f in listdir(ldscript_dir):
        if f.endswith(mcu_family) and softdevice_ver in f.lower():
            ldscript_path = join(ldscript_dir, f)

    if ldscript_path:
        env.Replace(LDSCRIPT_PATH=ldscript_path)
        print("linker script path:",ldscript_path)
    else:
        print("------------------------------------------------------------------------------")
        print("Warning! Cannot find an appropriate linker script for the required softdevice!")
        print("------------------------------------------------------------------------------")

# Select crystal oscillator as the low frequency source by default
clock_options = ("USE_LFXO", "USE_LFRC", "USE_LFSYNT")
if not any(d in clock_options for d in cpp_defines):
    env.Append(CPPDEFINES=["USE_LFXO"])

#
# Target: Build Core Library
#

libs = []

if "build.variant" in board:
    env.Append(CPPPATH=[
        join(FRAMEWORK_DIR, "variants", board.get("build.variant"))
    ])

    libs.append(
        env.BuildLibrary(
            join("$BUILD_DIR", "FrameworkArduinoVariant"),
            join(FRAMEWORK_DIR, "variants",
                 board.get("build.variant"))))

libs.append(
    env.BuildLibrary(
        join("$BUILD_DIR", "FrameworkArduino"),
        join(FRAMEWORK_DIR, "cores", board.get("build.core"))))

env.Prepend(LIBS=libs)
