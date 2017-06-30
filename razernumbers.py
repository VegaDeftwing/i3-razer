#Import all the things!
from razer.client import DeviceManager
from razer.client import constants as razer_constants
import i3

#Make a list of active workspace numbers
workspaces = i3.get_workspaces()
numlist = ['default']
for workspace in workspaces:
    if workspace['visible'] == True:
            num = workspace['num']
            numlist.append(num)


# Code I don't understand for the sake of setting up the razer device
device_manager = DeviceManager()
device_manager.sync_effects = False

###
# Make a load of funcions to make expanding this later much, much less painful
###

def one_on():
    device.fx.advanced.matrix[1, 2] = [255,255,255]

# def one_off():
#     device.fx.advanced.matrix[1, 2] = [0,0,0]
#
def two_on():
    device.fx.advanced.matrix[1, 3] = [255,255,255]

# def two_off():
#     device.fx.advanced.matrix[1, 3] = [0,0,0]
#
def three_on():
    device.fx.advanced.matrix[1, 4] = [255,255,255]

# def three_off():
#     device.fx.advanced.matrix[1, 4] = [0,0,0]
#
def four_on():
    device.fx.advanced.matrix[1, 5] = [255,255,255]

# def four_off():
#     device.fx.advanced.matrix[1, 5] = [0,0,0]
#
def five_on():
    device.fx.advanced.matrix[1, 6] = [255,255,255]

# def five_off():
#     device.fx.advanced.matrix[1, 6] = [0,0,0]
#
def six_on():
    device.fx.advanced.matrix[1, 7] = [255,255,255]

# def six_off():
#     device.fx.advanced.matrix[1, 7] = [0,0,0]
#
def seven_on():
    device.fx.advanced.matrix[1, 8] = [255,255,255]

# def seven_off():
#     device.fx.advanced.matrix[1, 8] = [0,0,0]
#
def eight_on():
    device.fx.advanced.matrix[1, 9] = [255,255,255]

# def eight_off():
#     device.fx.advanced.matrix[1, 9] = [0,0,0]
#
def nine_on():
    device.fx.advanced.matrix[1, 10] = [255,255,255]

# def nine_off():
#     device.fx.advanced.matrix[1, 10] = [0,0,0]
#
def zero_on():
    device.fx.advanced.matrix[1, 11] = [255,255,255]

# def zero_off():
#     device.fx.advanced.matrix[1, 11] = [0,0,0]
#
def wasd_on():
    device.fx.advanced.matrix[2, 3] = [255,255,255]
    device.fx.advanced.matrix[3, 2] = [255,255,255]
    device.fx.advanced.matrix[3, 3] = [255,255,255]
    device.fx.advanced.matrix[3, 4] = [255,255,255]

# def wasd_off():
#     device.fx.advanced.matrix[2, 3] = [0,0,0]
#     device.fx.advanced.matrix[3, 2] = [0,0,0]
#     device.fx.advanced.matrix[3, 3] = [0,0,0]
#     device.fx.advanced.matrix[3, 4] = [0,0,0]
#
def qwerty_on():
    device.fx.advanced.matrix[2, 2] = [255,255,255]
    device.fx.advanced.matrix[2, 3] = [255,255,255]
    device.fx.advanced.matrix[2, 4] = [255,255,255]
    device.fx.advanced.matrix[2, 5] = [255,255,255]
    device.fx.advanced.matrix[2, 6] = [255,255,255]
    device.fx.advanced.matrix[2, 7] = [255,255,255]

# def qwerty_off():
#     device.fx.advanced.matrix[2, 2] = [0,0,0]
#     device.fx.advanced.matrix[2, 3] = [0,0,0]
#     device.fx.advanced.matrix[2, 4] = [0,0,0]
#     device.fx.advanced.matrix[2, 5] = [0,0,0]
#     device.fx.advanced.matrix[2, 6] = [0,0,0]
#     device.fx.advanced.matrix[2, 7] = [0,0,0]
#

# I realize this loop is basically checking for a condition that no one will
# ever practically use, but, screw it, it works.

for device in device_manager.devices:

    if 1 in numlist:
        one_on()

    if 2 in numlist:
        two_on()

    if 3 in numlist:
        three_on()

    if 4 in numlist:
        four_on()

    if 5 in numlist:
        five_on()

    if 6 in numlist:
        six_on()

    if 7 in numlist:
        seven_on()

    if 8 in numlist:
        eight_on()

    if 9 in numlist:
        nine_on()

    if 0 in numlist:
        zero_on()

    if 10 in numlist:
        wasd_on()

    if 11 in numlist:
        qwerty_on()

#Do the thing Julie! Do. The. Thing!
    device.fx.advanced.draw()
