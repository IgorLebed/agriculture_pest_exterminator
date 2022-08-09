#! /bin/bash
SCRIPT_PATH=$(dirname $(realpath $0))
sudo cp $SCRIPT_PATH/*.rules /etc/udev/rules.d/
echo "Setup completed"
