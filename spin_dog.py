from ucl.common import byte_print, decode_version, decode_sn, getVoltage, pretty_print_obj, lib_version
from ucl.highCmd import highCmd
from ucl.highState import highState
from ucl.lowCmd import lowCmd
from ucl.unitreeConnection import unitreeConnection, HIGH_WIFI_DEFAULTS, HIGH_WIRED_DEFAULTS
from ucl.enums import MotorModeHigh, GaitType
from ucl.complex import motorCmd
import time

# You can use one of the 3 Presets WIFI_DEFAULTS, LOW_CMD_DEFAULTS or HIGH_CMD_DEFAULTS.
# IF NONE OF THEM ARE WORKING YOU CAN DEFINE A CUSTOM ONE LIKE THIS:
#
# MY_CONNECTION_SETTINGS = (listenPort, addr_wifi, sendPort_high, local_ip_wifi)
# conn = unitreeConnection(MY_CONNECTION_SETTINGS)
#

#This makes the robot spin right.
def spin_right():
    print(f'Running lib version: {lib_version()}')

    conn = unitreeConnection(HIGH_WIFI_DEFAULTS)
    conn.startRecv()
    hcmd = highCmd()
    hstate = highState()
    # Send empty command to tell the dog the receive port and initialize the connectin
    cmd_bytes = hcmd.buildCmd(debug=False)
    conn.send(cmd_bytes)
    time.sleep(0.5) # Some time to collect pakets ;)
    data = conn.getData()
    for paket in data:
        hstate.parseData(paket)
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print(f'SN [{byte_print(hstate.SN)}]:\t{decode_sn(hstate.SN)}')
        print(f'Ver [{byte_print(hstate.version)}]:\t{decode_version(hstate.version)}')
        print(f'SOC:\t\t\t{hstate.bms.SOC} %')
        print(f'Overall Voltage:\t{getVoltage(hstate.bms.cell_vol)} mv') #something is still wrong here ?!
        print(f'Current:\t\t{hstate.bms.current} mA')
        print(f'Cycles:\t\t\t{hstate.bms.cycle}')
        print(f'Temps BQ:\t\t{hstate.bms.BQ_NTC[0]} °C, {hstate.bms.BQ_NTC[1]}°C')
        print(f'Temps MCU:\t\t{hstate.bms.MCU_NTC[0]} °C, {hstate.bms.MCU_NTC[1]}°C')
        print(f'FootForce:\t\t{hstate.footForce}')
        print(f'FootForceEst:\t\t{hstate.footForceEst}')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

    motiontime = 0
    while True:
        motiontime += 1
        time.sleep(0.002)

        data = conn.getData()
        for paket in data:
            if motiontime % 100 == 0: #Print every 100 cycles
                hstate.parseData(paket)
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print(f'SN [{byte_print(hstate.SN)}]:\t{decode_sn(hstate.SN)}')
                print(f'Ver [{byte_print(hstate.version)}]:\t{decode_version(hstate.version)}')
                print(f'SOC:\t\t\t{hstate.bms.SOC} %')
                print(f'Overall Voltage:\t{getVoltage(hstate.bms.cell_vol)} mv') #something is still wrong here ?!
                print(f'Current:\t\t{hstate.bms.current} mA')
                print(f'Cycles:\t\t\t{hstate.bms.cycle}')
                print(f'Temps BQ:\t\t{hstate.bms.BQ_NTC[0]} °C, {hstate.bms.BQ_NTC[1]}°C')
                print(f'Temps MCU:\t\t{hstate.bms.MCU_NTC[0]} °C, {hstate.bms.MCU_NTC[1]}°C')
                print(f'FootForce:\t\t{hstate.footForce}')
                print(f'FootForceEst:\t\t{hstate.footForceEst}')
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

        if(motiontime > 0 and motiontime < 1000):
            hcmd.mode = MotorModeHigh.VEL_WALK
            hcmd.gaitType = GaitType.TROT
            hcmd.velocity = [0.0, 0.0]
            hcmd.yawSpeed = 2
            hcmd.footRaiseHeight = 0.1

        cmd_bytes = hcmd.buildCmd(debug=False)
        conn.send(cmd_bytes)

        if motiontime > 1000:
            break
    # time.sleep(0.1)

#This makes the robot spin left.
def spin_left():
    print(f'Running lib version: {lib_version()}')

    conn = unitreeConnection(HIGH_WIFI_DEFAULTS)
    conn.startRecv()
    hcmd = highCmd()
    hstate = highState()
    # Send empty command to tell the dog the receive port and initialize the connectin
    cmd_bytes = hcmd.buildCmd(debug=False)
    conn.send(cmd_bytes)
    time.sleep(0.5) # Some time to collect pakets ;)
    data = conn.getData()
    for paket in data:
        hstate.parseData(paket)
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
        print(f'SN [{byte_print(hstate.SN)}]:\t{decode_sn(hstate.SN)}')
        print(f'Ver [{byte_print(hstate.version)}]:\t{decode_version(hstate.version)}')
        print(f'SOC:\t\t\t{hstate.bms.SOC} %')
        print(f'Overall Voltage:\t{getVoltage(hstate.bms.cell_vol)} mv') #something is still wrong here ?!
        print(f'Current:\t\t{hstate.bms.current} mA')
        print(f'Cycles:\t\t\t{hstate.bms.cycle}')
        print(f'Temps BQ:\t\t{hstate.bms.BQ_NTC[0]} °C, {hstate.bms.BQ_NTC[1]}°C')
        print(f'Temps MCU:\t\t{hstate.bms.MCU_NTC[0]} °C, {hstate.bms.MCU_NTC[1]}°C')
        print(f'FootForce:\t\t{hstate.footForce}')
        print(f'FootForceEst:\t\t{hstate.footForceEst}')
        print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

    motiontime = 0
    while True:
        motiontime += 1
        time.sleep(0.002)

        data = conn.getData()
        for paket in data:
            if motiontime % 100 == 0: #Print every 100 cycles
                hstate.parseData(paket)
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')
                print(f'SN [{byte_print(hstate.SN)}]:\t{decode_sn(hstate.SN)}')
                print(f'Ver [{byte_print(hstate.version)}]:\t{decode_version(hstate.version)}')
                print(f'SOC:\t\t\t{hstate.bms.SOC} %')
                print(f'Overall Voltage:\t{getVoltage(hstate.bms.cell_vol)} mv') #something is still wrong here ?!
                print(f'Current:\t\t{hstate.bms.current} mA')
                print(f'Cycles:\t\t\t{hstate.bms.cycle}')
                print(f'Temps BQ:\t\t{hstate.bms.BQ_NTC[0]} °C, {hstate.bms.BQ_NTC[1]}°C')
                print(f'Temps MCU:\t\t{hstate.bms.MCU_NTC[0]} °C, {hstate.bms.MCU_NTC[1]}°C')
                print(f'FootForce:\t\t{hstate.footForce}')
                print(f'FootForceEst:\t\t{hstate.footForceEst}')
                print('+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=')

        if(motiontime > 0 and motiontime < 1000):
            hcmd.mode = MotorModeHigh.VEL_WALK
            hcmd.gaitType = GaitType.TROT
            hcmd.velocity = [0.0, 0.0]
            hcmd.yawSpeed = -2
            hcmd.footRaiseHeight = 0.1

        cmd_bytes = hcmd.buildCmd(debug=False)
        conn.send(cmd_bytes)

        if motiontime > 1000:
            break
    # time.sleep(0.1)