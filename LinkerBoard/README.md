#Installing libsoc library

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install automake
sudo apt-get install autoconf
sudo apt-get install libtool
sudo apt-get install libtool-bin
sudo apt-get install python-dev


git clone https://github.com/mvartani76/iot-detroit-jan2017

cd iot-detroit-jan2017

git clone https://github.com/jackmitch/libsoc

cd libsoc

autoreconf -i

./configure --enable-board=dragonboard410c --enable-python=2

make
sudo make install

sudo ldconfig -v -N

sudo apt-get install python-pip
pip install libsoc_zero
