# Discord-Channel-Attacthment-Save

Save all messages and attachments sent in a channel

# Available Commands

## `help`

- Display help/command usage for this discord bot

## `save [limit=9999]`

- Save all messages and attachments sent in the channel with the given limit. `limit` will default to 9999

# Installing and Running

## Arch Linux

run the commands below, line by line

```bash
sudo pacman -Syy install git nano python python-pip --noconfirm
pip install discord -U
git clone "https://github.com/hirusha-adi/Discord-Channel-Attacthment-Save.git"
cd ./Discord-Channel-Attacthment-Save
nano ./token.txt
# [Ctrl]+[Shift]+V to save the bot token
# [Ctrl]+O to save the file"
python main.py
```

## Ubuntu/Debian

run the commands below, line by line

```bash
sudo apt install git python3 python3-pip nano -y
pip3 install discord -U
git clone "https://github.com/hirusha-adi/Discord-Channel-Attacthment-Save.git"
cd ./Discord-Channel-Attacthment-Save
nano ./token.txt
# [Ctrl]+[Shift]+V to save the bot token
# [Ctrl]+O to save the file
python3 main.py
```

## Windows

1. Download and install Python3. Make sure to 'Add to PATH' when install python3

![imagew1](https://www.tutorials24x7.com/uploads/2019-12-26/files/3-tutorials24x7-python-windows-install.png)

2. Download the code as a .zip file from [this Github Reposotory](https://github.com/hirusha-adi/Discord-Channel-Attacthment-Save)

![imagew2](https://cdn.discordapp.com/attachments/935515175073763398/937186561299197952/unknown.png)

(this above image might not be the same)

3. Extract the downloaded `.zip` file

4. open `cmd` or `powershell` in that folder

5. run the command below to install requirements

```
python -m pip install -U discord
```

6. run the command below to start the prorgam

```
python main.py
```
