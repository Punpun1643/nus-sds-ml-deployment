# NUS SDS ML Deployment Workshop

> 📝 Resources: 
> - [GitHub repo](https://github.com/Punpun1643/nus-sds-ml-deployment) containing all codes and guides 
> - `modelDevelopment/Resume_Role_prediction.ipynb` contains the reference to how the model was developed. You can upload this to a notebook to interact with it
> - Alternatively, you can access the read-only version of the notebook [here](https://colab.research.google.com/drive/1UD4CwrGuFIYVA4l1ZvmagU6AzYQt43tU?usp=sharing)
> - `UpdatedResumeDataSet.csv` contains the dataset used to train the model
> - `app/model/resume_pipeline_0.2.pkl`contains the saved version of the model

## Table of content
- [Guide to uploading files]()
- [Prerequisite](#prerequisite)
    - [Install Docker](#install-docker)
        - [MacOS](#installing-docker-on-macos)
        - [Windows](#installing-docker-on-windows)
- [Docker](#docker)
    - [🏗️ Build Docker image](#build-docker-images)
    - [📦 Run image as container](#running-image-as-a-container)
    - [⚙️ Pushing & Pulling Images](#⚙️-pushing--pulling-images)
    - [🛑 Stop the running container](#🛑-stop-the-running-container)


## Guide to uploading files 

The workshop contains 3 parts. To follow along with each of the parts, you need to do the following:

### Part 1: saving model as pickle file

Note: remember to upload the `UpdatedResumeDataSet.csv` to your own Google Drive. You will need this dataset to run the notebook and train the model

You should also upload the `Resume_Role_prediction.ipynb` to Google Colab to follow along with the model saving part

However, if there's any difficulties or you don't wish to follow along with the saving portion of the workshop, you could also directly access the pickle file (i.e. the saved version of the model) at `app/model/resume_pipeline_0.2.pkl` 

### Part 2: building docker image and running image as container

We will be going through how we can write Dockerfile for our docker image. You could access the written Dockerfile at the root directory of the repo.


## Prerequisite

### 🚩 Install Docker

<details markdown="block">
<summary> <b>Install Docker on macOS</b> </summary>

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

5. 🎉 Verify Installation:
    - Open Terminal.

    - Run `docker --version` to check the installed version.

        If successful, you should be able to see (note that the exact version could be different):

        ```
        Docker version 24.0.2, build cb74dfc
        ```

    - Run `docker run hello-world` to ensure Docker can pull and run images.

        If successful, you should be able to see:

        ```
        Hello from Docker!
        This message shows that your installation appears to be working correctly.

        To generate this message, Docker took the following steps:
        1. The Docker client contacted the Docker daemon.
        2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
            (arm64v8)
        3. The Docker daemon created a new container from that image which runs the
            executable that produces the output you are currently reading.
        4. The Docker daemon streamed that output to the Docker client, which sent it
            to your terminal.

        To try something more ambitious, you can run an Ubuntu container with:
        $ docker run -it ubuntu bash

        Share images, automate workflows, and more with a free Docker ID:
        https://hub.docker.com/

        For more examples and ideas, visit:
        https://docs.docker.com/get-started/
        ```

### 🚩 Sign up for Docker Hub

If you don't have a Docker Hub account, create one [here](https://hub.docker.com/signup). This will be required for you to push and store your Docker image. 
</details>

<details markdown="block">
<summary> <b>Install Docker on Windows</b> </summary>

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

5. 🎉 Verify Installation:
    - Open Command Prompt or PowerShell.

    - Run `docker --version` to check the installed version.
        If successful, you should be able to see (note that the exact version could be different):

        ```
        Docker version 24.0.2, build cb74dfc
        ```

    - Run `docker run hello-world` to ensure Docker can pull and run images.

        If successful, you should be able to see:

        ```
        Hello from Docker!
        This message shows that your installation appears to be working correctly.

        To generate this message, Docker took the following steps:
        1. The Docker client contacted the Docker daemon.
        2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
            (arm64v8)
        3. The Docker daemon created a new container from that image which runs the
            executable that produces the output you are currently reading.
        4. The Docker daemon streamed that output to the Docker client, which sent it
            to your terminal.

        To try something more ambitious, you can run an Ubuntu container with:
        $ docker run -it ubuntu bash

        Share images, automate workflows, and more with a free Docker ID:
        https://hub.docker.com/

        For more examples and ideas, visit:
        https://docs.docker.com/get-started/
        ```

(Windows 10 Home Users Only):
- Install the WSL 2 Linux kernel update package.

- Set WSL 2 as your default version with `wsl --set-default-version 2`.

### 🚩 Sign up for Docker Hub

If you don't have a Docker Hub account, create one [here](https://hub.docker.com/signup). This will be required for you to push and store your Docker image. 
</details>

## Docker

### 🏗️ Build Docker images

To build docker image from `Dockerfile` run the following command in the directory with the `Dockerfile`:

```
docker build -t your_image_name:tag .
```

- `-t` allows you to tag your image with a name (and optionally a version).

- `.` at the end specifies the current directory as the context.

Example:

```
docker build -t punpun1643/resume-model-v2 .   
```

This builds a Docker image from Dockerfile with the image name `punpun1643/resume-model-v2` and the default `latest` image tag 

### 📦 Running image as a container

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

### ✅ Verify running containers

To view information of the currently running containers, you can use the following command:

```
docker ps
```

If you successfully run the container, you should be able to see:

```
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                  NAMES
e8e936d42494   punpun1643/resume-model-v2   "/start.sh"              13 seconds ago   Up 11 seconds   0.0.0.0:8080->80/tcp   unruffled_joliot
```

You should be able to access the running application at `localhost:8080/docs`

![F52E63AC-41F5-47B8-A463-4F3B3DCA78AE](https://github.com/Punpun1643/nus-sds-ml-deployment/assets/60144099/08c36f3c-450d-4197-95dd-a175fe4fd274)


### ⚙️ Pushing & Pulling Images

To push a created docker image to Docker Hub, run the following command: 

**⚠️ Important:** In order to push the image to your Docker Hub, you need to tag the image with your Docker Hub username and the desired repository name.

Example:

```
docker push punpun1643/resume-model-v2
```

This pushes the image to Docker Hub with the username `punpun1643` and the repository `resume-model-v2`, making it publicly accessible

If you push the image successfully, you should be able to see the repository:

![56E6CAA1-717C-4428-932B-6E9C026DD201_4_5005_c](https://github.com/Punpun1643/nus-sds-ml-deployment/assets/60144099/eafd65e2-c57e-41a2-9747-b5a750418736)


And the latest image:

![AB6A5B12-00C6-46F0-9A28-96CEE8A4F00A](https://github.com/Punpun1643/nus-sds-ml-deployment/assets/60144099/5f4240bd-ddcf-4ca4-a6f1-f30bd873f99e)


To pull a docker image from DockerHub, run the following command: 

```
docker pull [OPTIONS] IMAGE[:TAG]
```

Example:

```
docker pull punpun1643/resume-model-v2
```

This pulls the image from DockerHub and gives useful information to the user

### 🛑 Stop the running container 

To stop the running container, do the following:

1. Run `docker ps` to view the running container. Obtain the container ID of the container you want to stop.

Example: in this case, I want to stop the container from the image `punpun1643/resume-model-v2`. The container ID is therefore `e8e936d42494`
```
CONTAINER ID   IMAGE                        COMMAND                  CREATED          STATUS          PORTS                  NAMES
e8e936d42494   punpun1643/resume-model-v2   "/start.sh"              13 seconds ago   Up 11 seconds   0.0.0.0:8080->80/tcp   unruffled_joliot
```

2. Run the following command to stop the container:

```
docker stop [container_id]
```

Example:

```
docker stop e8e936d42494
```
