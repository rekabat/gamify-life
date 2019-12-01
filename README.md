# gamify-life
A flask, mongodb, docker project

# Setup
Install:
- Python 3
  - Pip
  - Virtualenv
- Docker

## Install on Linux
### Python
Run the following commands:

```
sudo apt update
sudo apt install python3
sudo apt install python3-venv
sudo apt install python3-pip
```

### Docker
Follow [this guide](https://docs.docker.com/install/linux/docker-ce/ubuntu/).
And add yourself to a docker group, to circumvent the need of using `sudo`. See [this guide](https://docs.docker.com/install/linux/linux-postinstall/) on how to do so.

## Install on MacOS
### Homebrew
Run the following command in a terminal:

```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

### Python
Run the following command: 

```
brew install python3
```

### Docker
Run the following commands:
```
brew install docker docker-machine
brew cask install virtualbox
-> need password
-> possibly need to address System Preference setting
docker-machine create --driver virtualbox default
docker-machine env default
eval "$(docker-machine env default)" # Used to set up any new terminal to connect to Docker daemon (may want to alias)
```
[Reference guide](https://medium.com/@yutafujii_59175/a-complete-one-by-one-guide-to-install-docker-on-your-mac-os-using-homebrew-e818eb4cfc3)

# Running locally
Set up the virtual environment

```
python3 -m venv venv
```

Then install requirements

```
pip3 install -r requirements.txt
```

Then start up the local environment and run main

```
source venv/bin/activate
python3 src/index.py
```


# Running from a Docker container

Then install requirements

```
pip3 install docker-compose
```

Build the docker image

```
docker-compose up
```
