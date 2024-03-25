# 0x09-web_infrastructure_design

Isaac Kumatse <ikumatse@st.ug.edu.gh>

This project is to research web infrastructure design. As we conducted research on different design principles, I whiteboarded diagrams of a developing web infrastructure. We started with a simple LAMP model and ended with a fully distributed, monitored, and secured system.

Files in this project contain links to each respective whiteboard diagram.


### Server
 A server is a robust computer system equipped with software to manage and process incoming requests from other computers, known as clients, over a specific network. Servers provide services, resources, and various functionalities, with numerous types available.

 Server Types

Web Server: Stores and handles HTTP requests, serving web pages. Notable examples include Apache and Nginx.

File Server: Manages files, offering the ability to upload, download, or access files over the network.

Database Server: Handles database management, with well-known examples like MySQL, PostgreSQL, and Microsoft SQL Server.

Mail Server: Manages sending, receiving, and storing emails. Notable options include Microsoft Exchange Server and Postfix.

DNS Server: Translates human-readable domains into IP addresses, enabling computers to locate each other over the internet.

Proxy Server: Acts as an intermediary between clients and servers, often used for request filtering and security purposes.

Media Server: Stores and delivers media content, such as videos, music, and images, and is commonly used for streaming.

Domain Name
A domain name is a user-friendly way of accessing and navigating the web, eliminating the need to memorize complex IP addresses.

DNS (Domain Name System) The DNS is responsible for translating the human-readable domain name entered by the user into the corresponding IP address of the website they want to visit.

Domain names are globally unique and are typically chosen to represent a brand or provide a meaningful association with the content or purpose of the website.

### Web Server
A web server is a remarkable piece of technology that plays a vital role in handling clients' requests, typically in the form of HTTP requests, and delivering the requested content.

### Application Server
Think of the application server as the cerebral cortex of a web application. Similar to the human brain's cerebral cortex, the application server is responsible for handling complex cognitive functions within the web application.

### Database
The database is arguably the most crucial component of any dynamic application. It serves as the repository for data, enabling a wide range of operations collectively referred to as CRUD. Creat. Read. Update. Delete.

## Task 0
### A SIMPLE WEB STACK INFRASTRUCTURE
In this web infrastructure with a single server, we provide hosting for a website accessible through www.foobar.com. The diagram demonstrates the server's components and the interaction between the server and a client making a request for foobar.com.

### EVENTS
USER REQUEST: The user inputs a memorable URL and submits it through their preferred browser.

DNS RESOLUTION: The computer initiates a DNS request to translate the human-readable URL into the website's actual IP address.

TCP CONNECTION: A Transmission Control Protocol (TCP) connection is established between the computer and the web server.

HTTP REQUEST: The computer is prepared to dispatch an HTTP request to the web server.

PROCESSING: The web server handles the HTTP request, generating the requested data. This data may be retrieved from the database by the application server or accessed from the codebase.

HTTP RESPONSE: The data is prepared for transmission back to the user.

RENDERING: The browser exhibits the information received from the server.

INTERACTION: The user engages with the content and initiates events within it.

### ISSUES
Single Point of Failure (SPOF)

A Single Point of Failure occurs when a system depends on a singular component, and if that component malfunctions, the entire system may fail. Within this framework, various SPOFs warrant attention

### Task 1
## A DISTRIBUTED WEB INFRASTRUCTURE

In this upgraded three-server web infrastructure, we continue to host the website www.foobar.com. This adjustment significantly boosts the reliability and resilience of our infrastructure. Let's delve into the enhancements:

Introducing Additional Servers: We've implemented an extra server for each component (Web server, Application server, and Database server). This setup effectively mitigates the risk of a Single Point of Failure (SPOF). Both servers operate concurrently, ensuring uninterrupted service even in the event of issues with one server.

Load Balancer: The Load Balancer functions as a traffic manager, evenly distributing incoming requests across multiple servers. Its primary purpose is to optimize resource allocation, enhance responsiveness, and elevate overall performance and availability.

LOAD BALANCER
The Load Balancer serves as the intermediary between clients and servers. It receives HTTP requests and redirects them to the appropriate server. Load balancers analyze incoming requests and determine distribution methods based on factors such as server load, health, or algorithms.

Load Balancer Algorithms:

Round Robin: Distributes traffic evenly in a circular fashion, ensuring relatively equal distribution.

Least Connections: Redirects HTTP requests to the server with the fewest connections.

PRIMARY-REPLICA DATABASES, also referred to as master-slave database clusters, are structured to prioritize high availability and fault tolerance within database systems.

In this setup, the primary database manages all operations, including Create, Read, Update, and Delete (CRUD), while the replica operates solely in a read-only capacity.

The primary server maintains a log of changes known as the Binary log, which it utilizes to communicate updates to the replica servers, ensuring they remain synchronized.

Replica servers receive updates from the primary server and implement these changes to achieve synchronization. They may be strategically positioned in different locations to optimize user experience and enhance system resilience.

### ISSUES
FIREWALLS: These are security mechanisms that monitor network traffic according to predefined security rules. In this infrastructure, two firewalls play critical roles: one positioned between the client and the Internet Service Provider (ISP), referred to as the client-side firewall, and another between the ISP and the server, known as the network firewall.

MONITORING: Continuous real-time monitoring of the system's health, performance, and security is indispensable for promptly addressing potential issues.

HTTPS: This stands for HyperText Transfer Protocol Secure, a protocol that employs encryption to safeguard the exchange of data between a user's browser and the web server, ensuring confidentiality and data integrity.

### Task 2
## SECURED AND MONITORED WEB INFRASTRUCTURE


Firewalls: These firewalls enhance security by subjecting a client's request for information from a server to thorough examination, ensuring comprehensive scrutiny of network traffic at multiple points.

SSL Certificate: To enable the serving of www.foobar.com over HTTPS, Secure Sockets Layer (SSL) technology ensures the encryption of data transmitted between users and the server, thereby guaranteeing data integrity and authenticating the server's identity.

Monitoring Clients: Monitoring is vital for overseeing resource performance, including servers, applications, and databases. It tracks metrics such as CPU and memory usage, response times, storage availability, hardware health, and system logs to detect security vulnerabilities and maintain a positive user experience.

 SSL is a protocol designed to enable secure communication over computer networks. It offers encryption, data integrity, and authentication, ensuring the protection of data transmitted between users and servers.

SERVING OVER HTTPS: Serving content over HTTPS is essential for various security reasons, including encryption of data in transit, maintaining data integrity, and safeguarding user privacy.

MONITORING: Monitoring entails the continuous tracking of resource performance, system health, and security. It ensures that resources remain available and operational, providing rapid alerts in the event of any issues. Additionally, monitoring helps to identify security threats by analyzing system logs and patterns.