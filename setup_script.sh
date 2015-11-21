#!/bin/bash
# Setup your computer for python and the project

sudo bash <(curl -s https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda2-2.4.0-MacOSX-x86_64.sh)
sudo curl --silent --show-error --retry 5 https://bootstrap.pypa.io/get-pip.py | sudo python
sudo pip install -U scikit-image
ipython notebook
