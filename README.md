<p align="center">
  <h1>👨🏻‍💻🐍 server-client with sockets in python 🐍👨🏻‍💻</h1>
  <h6>by <i>FranciscoCharles</i></h6>
</p>

This project contains code example for a client-server using **Python** sockets. The codes are simple and very intuitive, the client simply sends messages to the server and the server returns a response. The client pings the server and at the end displays response time information such as mean, standard deviation, minimum and maximum.

<!--
<p align="center">
  <img src="./src/images/example_1.png" width="400">
  <img src="./src/images/example_2.png" width="400">
</p>
-->

# <a name=index>Table of contents 📚</a>

- [**Project organization**](#project_organization)
- [**How can i run?**](#run)
- [**Dependencies**](#dependencies)
- [**Version**](#version)
- [**License**](#license)


# **<a name=project_organization>👨🏻‍💻🐍 Project organization </a>**  <h6>[back to indice](#index)</h6>

this project splits the code into two folders, the first is the `client/` folder for the client codes and the second is the `server/` folder for the server codes. The codes are also divided by socket type, containing codes that use TCP and UDP. There is also TCP-type server code that uses threads. Below we have the organization of the folders:

- [**client/**](./code/client/)
  + [tcp_client.py](./code/client/tcp_client.py)
  + [udp_client.py](./code/client/udp_client.py)

- [**server/**](./code/server/)
  + [tcp_server.py](./code/server/tcp_server.py)
  + [tcp_server_with_thread.py](./code/server/tcp_server_with_thread.py)
  + [udp_server.py](./code/server/udp_server.py)

# **<a name=run>How can I run? 🧠💭</a>** <h6>[back to indice](#index)</h6>

Download the project and run the file from the desired server and its client of the same type.

# **<a name=dependencies>🧰 Dependencies ⚙️</a>**  <h6>[back to indice](#index)</h6>
- **Python** == **3.7** or higher.

# **<a name=version>Version</a>**  <h6>[back to indice](#index)</h6>
- current version of the project: 1.0.1.

# **<a name=license>License</a>**  <h6>[back to indice](#index)</h6>

For more information on the license for this project read the <a href="./LICENSE" title="go to license file">LICENSE</a> file.

---

<p align="center">
    Copyright © 2021 <b>FranciscoCharles</b>
</p>
