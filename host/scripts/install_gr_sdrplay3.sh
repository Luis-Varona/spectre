git clone https://github.com/fventuri/gr-sdrplay3.git
#cd into the cloned repo
cd gr-sdrplay3
# checkout a version stable with version 3.14.0 of the SDRPlay RSP API
git checkout v3.11.0.4
#built the OOT module
mkdir build && cd build && cmake .. && make
sudo make install

