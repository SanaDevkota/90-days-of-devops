# Virtual Machine
-   it allows multiple operating systems to run on the same physical machine, by creating a virtual environment for each operating system


# Container vs Virtualization
- **Containerization** is a method of packaging software so that it can run consistently across different environments. Containers provide a way to package an application and its dependencies into a single unit, called a container image, that can be run on any system with a compatible container runtime.

- **Virtualization**, on the other hand, is a technology that allows multiple virtual versions of a single physical machine to run on the same hardware. Virtual machines (VMs) provide a way to run multiple operating systems on one physical machine, which can be useful for isolating different applications or for testing and development.

In summary, containerization is focused on packaging and running applications, while virtualization is focused on creating virtual versions of hardware. Both technologies can be used together to achieve different goals such as scaling, isolation, and cost savings.



# Docker vs Virtual Machine
Virtual machine has its guest operating system above the host operating system, which makes virtual machines heavy, While on the other hand, Docker containers share the host operating system, and that is why they are lightweight.

The virtual machine does no share operating system, and there is strong isolation in the host kernel. Hence, they are more secure as compared to Containers. A container have a lot of security risks, and vulnerabilities as the containers have shared host kernel.

Docker containers are easily portable because they do not have separate operating systems. A container can be ported to a different OS, and it can start immediately. On the other hand, virtual machines have separate OS, so porting a virtual machine is difficult as compared to containers.

![Image](https://user-images.githubusercontent.com/69889600/211190070-2d0e6b26-2506-424d-b28a-5d1412619ce1.jpg)



# Containers
Container is just a process running from directory and all the data is coming from image.



# Docker Engine
Docker Engine is an open source containerization technology for building and containerizing your applications. Docker Engine acts as a client-server application.



# Docker Engine vs Docker Deamon
The Docker Engine is the layer between the Docker command-line interface (CLI) and the Docker daemon. The Docker CLI uses the Docker Engine API to communicate with the Docker daemon, which performs the requested actions. In short, the Docker Engine is the software that allows the host machine to run and manage Docker containers, while the Docker daemon is the background process that actually runs and manages the containers.



# Docker Architecture
Docker uses a client-server architecture. The Docker client talks to the Docker daemon, which does the heavy lifting of building, running, and distributing your Docker containers. The Docker client and daemon can run on the same system, or you can connect a Docker client to a remote Docker daemon. The Docker client and daemon communicate using a REST API, over UNIX sockets or a network interface.

!(Architecture)[https://user-images.githubusercontent.com/69889600/211189964-520ae32a-30c7-4aa1-ad9d-418911c087c5.jpg]




# Docker Hub
Docker Hub is a cloud-based registry service which allows you to link to code repositories, build your images and test them, store and distribute them as Docker images. Docker Hub is the world’s largest library and community for container images. It allows you to find and use millions of container images published by Docker users and organizations. Docker Hub is the default registry for Docker. You can use it to store and distribute your images publicly or privately. You can also use Docker Hub to create an automated build, which builds and publishes your image whenever you push a change to your code repository.

# Docker Image
- it's simply like a class in OOP. it includes all the dependencies and libraries required to run the application.

- Docker image is a read-only template with instructions for creating a Docker container. An image includes everything needed to run an application - the code or binary, runtimes, dependencies, and any other filesystem objects required.

# Docker-commands

- List running container :
    `docker ps`
- List all container even exited one :
    `docker ps -a`

- List all images :
    - `docker images -a`
- 