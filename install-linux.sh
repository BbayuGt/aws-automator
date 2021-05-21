
#install needed tools
sudo apt update
sudo apt install curl wget unzip python3 python-is-python3 python3-pip
pip3 install selenium

#install chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt -f install

curl https://chromedriver.storage.googleapis.com/90.0.4430.24/chromedriver_linux64.zip >chromedriver.zip
unzip chromedriver.zip
chmod +x ./chromedriver

echo "it should ready now!"
