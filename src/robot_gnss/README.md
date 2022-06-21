# Поддержка модуля GNSS
Краткое руководство по подключению GNSS модуля.

## Зависимости
* ROS Noetic
* [pySerial](https://pypi.org/project/pyserial)
* [nmea_navsat_driver](https://wiki.ros.org/nmea_navsat_driver)

## Публикация данных
Пакет nmea_navsat_driver не предоставляет API для языков программирования и служит только для публикации данных, полученных с GNSS модуля. Для запуска публикации используйте следующую команду:
``` bash
rosrun nmea_navsat_driver nmea_serial_driver _port:=/dev/ttyACM0 _baud:=9600
```
!!! Замечены проблемы при одновременном мониторинге порта с контейнера и с хоста. Избегайте таких ситуаций, один порт - одна программа, считывающая с него данные !!!

Порт может быть другим. Реальную скорость передачи данных можно посмотреть через [u-center](https://www.u-blox.com/en/product/u-center): __Configuration View -> PRT (Ports) -> Baudrate__.
![u-center ports](./media/u-center_ports.png)

## Топики
Визуализировать данные из топиков можно командой `rostopic echo [topic]`.

### Список топиков
* __fix__ - положение, сообщения [sensor_msgs/NavSatFix](http://docs.ros.org/en/api/sensor_msgs/html/msg/NavSatFix.html).  
Самые необходимые поля:  
  * __latitude__ (Широта)
  * __longitude__ (Долгота)
* __vel__ - скорость, сообщения [TwistStamped](http://docs.ros.org/en/api/geometry_msgs/html/msg/TwistStamped.html). Сообщения публикуются только тогда, когда модуль GNSS выводит достоверную информацию о скорости.
* __time_reference__ - время, сообщения [TimeReference](http://docs.ros.org/en/api/sensor_msgs/html/msg/TimeReference.html). Это Unix-время, для примера перевести в человеческий вид можно [здесь](https://www.epochconverter.com/).