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

# Running locally
Set up the virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Then install requirements

```
pip install docker-compose
pip install -r requirements.txt
```

Build the docker image

```
docker-compose up
```