# NUS SDS ML Deployment Workshop

## Table of content

- [Prerequisite](#prerequisite)
    - [Install Docker](#install-docker)
        - [MacOS](#installing-docker-on-macos)
        - [Windows](#installing-docker-on-windows)
- [Docker: running docker image as container](#docker)
    - [Build Docker image](#build-docker-images)
    - [Run image as container](#running-image-as-a-container)

## Prerequisite

### Install Docker

#### Installing Docker on macOS

1. Prerequisites:
    - macOS must be version `10.14` or newer.

    - Virtualization must be enabled on your system (it usually is by default on modern Macs).

2. Download Docker Desktop for Mac:
    - Go to the official Docker website: [Docker Hub](https://hub.docker.com/)

    - Navigate to "Get Docker" or "Docker Desktop".

    - Download the Docker Desktop for Mac installer.

3. Install Docker:
    - Locate the downloaded `.dmg` file and double-click to open it.

    - Drag the Docker icon to the Applications folder.

4. Run Docker:
    - Open your Applications folder and click on the Docker app.

    - You'll see a Docker icon in the top status bar indicating that Docker is running.

    - The first time you run Docker, it might ask for privileged access. Grant the necessary permissions.

5. Verify Installation:
    - Open Terminal.

    - Run `docker --version` to check the installed version.

    - Run `docker run hello-world` to ensure Docker can pull and run images.

#### Installing Docker on Windows

1. Prerequisites:
    - Windows 10 64-bit: Pro, Enterprise, or Education (Build 16299 or later). For Windows 10 Home, ensure you're updated to at least version 2004 and follow additional steps during setup.

    - Hyper-V and Containers Windows features must be enabled. Docker will enable these for you, but if you're using a virtual machine, ensure that it's configured for virtualization.

2. Download Docker Desktop for Windows:
    - Go to the official Docker website: [Docker Hub](https://hub.docker.com/)

    - Navigate to "Get Docker" or "Docker Desktop".

    - Download the Docker Desktop for Windows installer.

3. Install Docker:
    - Locate the downloaded .exe file and double-click to run the installer.

    - Follow the installation wizard instructions. It may require a restart.

4. Run Docker:
    - Once installed, launch Docker from the Start menu or desktop icon.

    - Docker will start as a tray application.

    - The first time you start Docker, it might take some time to initialize and enable required features.

5. Verify Installation:
    - Open Command Prompt or PowerShell.

    - Run `docker --version` to check the installed version.

    - Run `docker run hello-world` to ensure Docker can pull and run images.

(Windows 10 Home Users Only):
- Install the WSL 2 Linux kernel update package.

- Set WSL 2 as your default version with `wsl --set-default-version 2`.

## Docker

### Build Docker images

To build docker image from `Dockerfile` run the following command in the directory with the `Dockerfile`:

```
docker build -t your_image_name:tag .
```

- `t` allows you to tag your image with a name (and optionally a version).

- `.` at the end specifies the current directory as the context.

Example:

```
docker build -t punpun1643/resume-model-v2 .   
```

This builds a Docker image from Dockerfile with the image name `punpun1643/resume-model-v2` and the default `latest` image tag 

### Running image as a container

To run the docker image from the previous step as container, run the following command: 

```
docker run [OPTIONS] IMAGE[:TAG]
```

Some common `OPTIONS` include:
- p: Publish a container's port to the host. Format: `<host_port>:<container_port>`

Example:

```
docker run -p 8080:80 punpun1643/resume-model-v2
```
This runs `punpun1643/resume-model-v2` and maps port `80` in the container to port `8080` on the host.