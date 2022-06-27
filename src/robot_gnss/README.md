# GNSS module
A quick guide to connecting the GNSS module.

## Dependencies
* ROS Noetic
* [pySerial](https://pypi.org/project/pyserial)
* [nmea_navsat_driver](https://wiki.ros.org/nmea_navsat_driver)

## Publishing data
The nmea_navsat_driver package does not provide an API for programming languages and serves only for publishing data received from the GNSS module. To start publishing, use:
``` bash
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyACM0 _baud:=9600
```
!!! When monitoring the port from the container and from the host at the same time, problems arise. Avoid such situations, one port - one program that reads data from it !!!

The port may be different. The actual baud rate can be viewed via [u-center](https://www.u-blox.com/en/product/u-center): __Configuration View -> PRT (Ports) -> Baudrate__.
![u-center ports](./media/u-center_ports.png)

!!! For u-blox 7 chip, baud rate of USB port (not Serial2USB) is configured automatically !!!

___u-blox chipsets with built-in USB support (as used in the VK-172, RY835AI, and other boards) use a USB modem interface, and appear as /dev/ttyACM0.___

___In a manner of speaking, they autuobaud. More precisely, there is no baud setting, since these run as native USB devices. If you look at the u-blox protocol guide, you'll see that there literally is no way to set baud rate, start / stop bits, etc. for the ttyACM0 USB interface. The usual system commands for configuring tty devices will accept input (e.g. stty -F /devttyACM0 9600) but those are ignored.___

___This is distinct from devices that use a USB-UART bridge (BU-353) to create a real serial port on /dev/ttyUSB0. In those cases, both the port and the GPS receiver need to be set to the correct rate.___

## Topics
Visualize data: `rostopic echo [topic]`.

### List of topics
* __fix__ - position, [sensor_msgs/NavSatFix](http://docs.ros.org/en/api/sensor_msgs/html/msg/NavSatFix.html).  
The most necessary fields:
  * __latitude__
  * __longitude__
* __vel__ - velocity, [TwistStamped](http://docs.ros.org/en/api/geometry_msgs/html/msg/TwistStamped.html). Only published when the device outputs valid velocity information.
* __time_reference__ - time, [TimeReference](http://docs.ros.org/en/api/sensor_msgs/html/msg/TimeReference.html). Unix Time Stamp, you can translate it into an understandable form [here](https://www.epochconverter.com/).