echo "Installing Dependencies"
sudo apt install git python3 python3-pip -y
pip3 install discord -U
echo "Installed git, python3, python3-pip with apt"
echo "Installed discord.py with pip3"
git clone "https://github.com/hirusha-adi/Discord-Channel-Attacthment-Save.git"
cd ./Discord-Channel-Attacthment-Save
echo "--> [Ctrl]+[Shift]+V to save the bot token"
echo "--> [Ctrl]+O to save the file"
sleep 4s
nano ./token.txt
python3 main.py