echo "Installing Dependencies"
sudo pacman -Syy install git nano python python-pip --noconfirm
pip install discord -U
echo "Installed git, nano, python, python-pip with apt"
echo "Installed discord.py with pip"
git clone "https://github.com/hirusha-adi/Discord-Channel-Attacthment-Save.git"
cd ./Discord-Channel-Attacthment-Save
echo "--> [Ctrl]+[Shift]+V to save the bot token"
echo "--> [Ctrl]+O to save the file"
sleep 4s
nano ./token.txt
python main.py
