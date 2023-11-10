# Steps
1. Clone repository
2. Type in the terminal: docker build -t proiectulmeu . 
   **docker build-> This command is used to build a Docker image.**

   **-t proiectulmeu-> This flag is used to tag the resulting image with a name. In this case, the name is set to "proiectulmeu." The -t flag stands for "tag."**

   **.-> The dot at the end represents the build context. It specifies the location of the Dockerfile and any files that are used during the build process. In this case, it assumes that the Dockerfile is in the current directory.**
 
3. Type in the terminal: docker run --rm -it --name <my-running-app> proiectulmeu

 **docker run-> This command is used to run a Docker container.**

  **--rm-> This flag automatically removes the container when it exits. It's often used for short-lived containers to avoid cluttering your system with stopped     containers.**

  **-it-> These flags combine two options:**
  **-i or --interactive-> Keeps STDIN open even if not attached, allowing you to interact with the container.**
  **-t or --tty-> Allocates a pseudo-TTY, which is useful for an interactive shell.**
  **--name <my-running-app>-> This option allows you to assign a name to your container, in this case, <my-running-app>. Naming containers can make it easier to manage them.**

  **proiectulmeu: This is the name or ID of the Docker image you want to run. Replace it with the actual name or ID of your Docker image.**
