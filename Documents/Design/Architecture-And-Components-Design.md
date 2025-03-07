# Architecture and Components Design
This document provides a comprehensive overview of the architecture and design of various components within a specified technology stack. It outlines the structure and interrelations between frontend, backend, testing, and deployment elements, along with the rationale behind technology selection. Furthermore, it delves into alternative technological frameworks, offering insights into potential variations in the system's architecture. The document also details the design and functionalities of individual components, contributing to a holistic understanding of the system's operation and potential scalability.

## Table of Content
- [**Technology Stack Architecture**](#technology-stack-architecture)
    - [**Description**](#description)
    - [**Frontend Components**](#frontend-components)
    - [**Backend Components**](#backend-components)
    - [**Test Components**](#test-components)
    - [**Deployment Components**](#deployment-components)
    - [**Decision-Making for Technology Selection**](#decision-making-for-technology-selection)
    - [**Horizontal comparison of each component**](#horizontal-comparison-of-each-component)
    - [**Alternative Technology Stack**](#alternative-technology-stack)
- [**Software Architecture**](#software-architecture)
    - [**Overview**](#overview)
    - [**Alternative Software Architecture**](#alternative-software-architecture)
- [**Components Design**](#components-design)
    - [`ClientUI`](#clientui)
    - [`CoAuthors`](#coauthors)
    - [`CitedTree`](#citedtree)
    - [`SameTopic`](#sametopic)
    - [`TopicConnections`](#topicconnections)
    - [`PaperDashboard`](#paperdashboard)
    - [`CatalogAPI`](#catalogapi)
    - [`AnalysisAPI`](#analysisapi)
    - [`Models`](#models)
    - [`Schema`](#schema)
    - [`Catalog`](#catalog)
    - [`Analysis`](#analysis)
    - [`Extractor`](#extractor)
    - [`GrobidClient`](#grobidclient)
    - [`Client`](#client)
    - [`Parser`](#parser)
    - [`Types`](#types)
    - [`CatalogAccess`](#catalogaccess)
    - [`MongoengineModels`](#mongoenginemodels)
    - [`Config`](#config)


## **Technology Stack Architecture**
![Technology Stack Architecture](../Image/tech-stack.jpg)
*Figure 1: Technology stack architecture.*

### **Description**
The proposed architecture employs Vue coupled with Axios for front-end development, FastAPI for backend API services, Python for backend data processing, and MongoDB as the data storage solution. The defined dependencies ensure a fluid exchange of data and operations between the front-end and back-end components, promoting a cohesive and efficient workflow.

#### *Why Front-End*?
The architectural choice of a separated front-end in our system architecture is essential for several strategic reasons:
1. **Specialized Focus:** Front-end separation allows for a focused approach to user experience design, tailored specifically to the varied needs of our users. By decoupling the user interface from the server-side logic, we can tailor the front-end to support scenarios such as data-driven academic research, policy analysis, and comprehensive literature reviews without being constrained by back-end processes.
2. **Agility and Scalability:** A separated front-end facilitates agile development and deployment. As the needs of students, academics, and professionals evolve, the front-end can be updated and scaled independently of the back-end services, ensuring the system remains responsive to the changing demands of evidence-based decision-making.
3. **Performance and Optimization:** This separation allows for the optimization of front-end resources for speed and efficiency, critical for tasks such as rendering complex data visualizations or managing extensive literature databases, ensuring that the system is both powerful and responsive.
4. **Enhanced User Interaction:** By focusing on the front-end, we can ensure that features such as citation tracking, note-taking, and customizable searches are implemented in a way that is intuitive and efficient, enhancing the overall user experience and facilitating the academic writing process.
5. **Flexibility in Technology Stack:** The separation allows us to choose the most appropriate technologies for the front-end, ensuring that the system's interface is built using tools best suited for creating a dynamic and user-friendly environment. It also means that as new front-end technologies emerge, the system can adapt without the need for extensive back-end overhauls.
6. **Streamlined Development Workflow:** A separate front-end enables a streamlined workflow for developers, where front-end and back-end teams can work in parallel on different aspects of the system. This approach reduces bottlenecks and accelerates the development process, which is essential for a complex system designed to handle a vast array of academic research functions.
7. **Ease of Testing and Maintenance:** Testing the user interface becomes more manageable when it is decoupled from the back-end logic. The front-end can be tested for usability and performance independently, ensuring that the system remains reliable and effective for user-driven exploration and analysis.

In essence, the decision to architect a distinct front-end directly supports the system's ambition to be a comprehensive research and analysis platform that remains user-centric, agile, and technologically robust. This separation is vital for ensuring that the system not only meets but exceeds the expectations of its diverse user base.

### **Frontend Components**
#### *Components List:*
- **`Vue`**
    - A progressive JavaScript framework used for crafting modern, interactive user interfaces. Vue is known for its declarative rendering, component-based structure, and its ability to smoothly blend with other libraries and tools. 
    - [Vue Official Documentation](https://vuejs.org/v2/guide/)
- **`Vuex`**
    - This state management pattern library is tailored for Vue.js. It serves as a centralized store for all the components in an application, with rules ensuring the state can only be mutated in a predictable fashion. 
    - [Vuex Official Documentation](https://vuex.vuejs.org/)
- **`VuesticUI`**
    - A Vue.js UI toolkit for web development, VuesticUI offers a collection of high-quality components and tools for building rich, responsive interfaces. 
    - [VuesticUI Official Documentation](https://ui.vuestic.dev/)
- **`Webpack`** 
    - As a static module bundler for modern JavaScript applications, Webpack processes your application's modules and efficiently bundles them into static assets. 
    - [Webpack Official Documentation](https://webpack.js.org/concepts/)
- **`Axios`**
    - A promise-based HTTP client for making HTTP requests from the browser or Node.js applications, Axios integrates easily with Vue.js and provides a straightforward API for interaction. 
    - [Axios Official Documentation](https://axios-http.com/docs/intro)
- **`vis.js`** 
    - A powerful, interactive charting and data visualization library for the browser. It offers a variety of chart types and can be easily integrated into Vue applications. 
    - [vis.js Official Documentation](https://visjs.org/)

#### *Component Dependencies:*
- **`Vue → Vuex`**
    - Vuex serves as the state management pattern for applications using Vue. It is essential for maintaining a centralized and coherent state across the application.
- **`Vue → VuesticUI`** 
    - Vue utilizes VuesticUI for rich UI components, which are integral to crafting an engaging user interface.
- **`Vue → Axios`** 
    - Axios is crucial for Vue applications to handle HTTP requests, allowing seamless communication with back-end services.
- **`Vue → vis.js`**
    - integration of vis.js with Vue enables the creation of interactive data visualizations within the user interface.
- **`Webpack → Vue`** 
    - Webpack is leveraged to bundle Vue components efficiently, enhancing application performance and asset management.
- **`Webpack → VuesticUI`** 
    - VuesticUI components are managed and bundled within the Webpack ecosystem, ensuring correct integration and styling.
- **`Webpack → Axios`**
    - Axios is configured within Webpack to handle asynchronous HTTP requests as part of the build process.

### **Backend Components**
#### *Component List*:
- **`FastAPI`**
    - A contemporary, high-performance web framework for building APIs with Python, based on standard Python type hints. 
    - [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- **`Python`**
    - As a programming language, Python is used extensively for data processing and analysis in the backend due to its powerful libraries and versatility. 
    - [Python Official Documentation](https://docs.python.org/3/)
- **`MongoDB`**
    - A document-based NoSQL database known for its scalability and flexibility, MongoDB serves as the storage engine for handling large volumes of data. 
    - [MongoDB Official Documentation](https://docs.mongodb.com/)
- **`Grobid`**
    - An open-source software library for document conversion and the extraction of bibliographical data in PDF files. It is typically used for processing academic documents and transforming them into structured TEI encoded documents. 
    - [Grobid Official Documentation](https://grobid.readthedocs.io/)
#### *Component Dependencies:*
- **`Vue + Axios → FastAPI`**
    - The front-end framework Vue, in combination with Axios, depends on FastAPI for processing API requests, enabling robust communication between the client and server.
- **`FastAPI → Python`**
    - FastAPI harnesses Python's capabilities to execute complex backend logic and data processing routines.
- **`Python → MongoDB`**
    - Python uses libraries such as PyMongo to interact with MongoDB, allowing data manipulation and retrieval for back-end processing.
- **`Python → Grobid`** 
    - Python may call upon Grobid services for the extraction of information from PDF documents, further processed within the business logic.

### **Test Components**
#### *Component List:*
- **`Vitest:`** 
    - A unit testing framework for Vue.js applications, designed to provide fast and reliable test execution. 
    - [Vitest Official Documentation](https://vitest.dev/)
- **`Pytest`** 
    - A mature full-featured Python testing tool that helps you write better programs. It is used for writing and executing tests on the back-end side, ensuring the reliability of Python code. 
    - [Pytest Official Documentation](https://docs.pytest.org/en/stable/)
#### *Component Dependencies:*
- **`Vitest → Vue`**
    - Vitest is utilized for testing Vue components, ensuring the front-end logic behaves as expected.
- **`Pytest → Python`**
    - Pytest is employed to test Python code, including data processing and business logic in the back-end, guaranteeing code quality and performance.
- **`Pytest → FastAPI`**
    - Pytest is also used to test FastAPI endpoints, verifying the correct behavior of API calls and responses.

### **Deployment Components**
#### *Component List:*
- **`Docker`**
    - A containerization platform that encapsulates applications and their environments for consistent deployment across different systems. Docker ensures that applications run the same, regardless of where they are deployed. It provides a way to package the application with its environment and dependencies into a container, which can be transported and run anywhere Docker is supported.
    - [Docker Official Documentation](https://www.docker.com/)

#### *Component Dependencies:*
- **`Frontend Container -> All Frontend Components`**
    - The frontend container bundles all frontend components including Vue, Vuex, VuesticUI, Webpack, Axios, and vis.js. This container is responsible for the presentation layer of the application, providing the user interface and handling interactions with the user.
  
- **`Backend Container -> All Backend Components (Except Grobid Component)`**
    - The backend container encompasses the components required for the application's server-side operations, such as FastAPI, Python, and MongoDB. This container handles API requests, business logic, data processing, and analysis. It interacts with the frontend container to serve processed data and accept user inputs.
  
- **`Grobid Container -> Grobid`**
    - This container is dedicated to running Grobid, a tool for extracting information from PDF documents. It acts as a standalone service that can be utilized by the backend for processing academic documents and transforming them into structured data.

### **Decision-Making for Technology Selection**
The architecture and choice of technologies for the this system were methodically planned to align with the project's objectives, the proficiency of the development team, and the specific needs of our target users.
1. **Development Team Background**
    - Our team comprises skilled developers with a strong background in modern JavaScript frameworks, experience in Python for data processing, and proficiency with NoSQL databases. This existing expertise strongly influenced the selection of Vue.js, FastAPI, and MongoDB to capitalize on our team's strengths and ensure a smooth development process.
2. **Project and User Requirements Fit**
    - Through in-depth discussions and iterative feedback sessions with stakeholders, we mapped out the crucial features and performance expectations for the system. The client emphasized the need for a responsive UI, robust data processing capabilities, and a flexible data storage approach that can accommodate complex queries, leading to our technology choices.
    - The technology stack was designed to strike a balance between development efficiency and product scalability. Vue.js, along with its associated libraries, was chosen for its reactive nature and ease of integration, which aligns with our aim to deliver a responsive user experience. FastAPI, paired with Python's rapid development and rich library ecosystem, addresses our backend data processing requirements. MongoDB's schema-less design is particularly suited to our needs, offering the flexibility necessary for the varied and evolving datasets encountered in academic research. Additionally, most PDF article extractors, including plugins and libraries, output data in formats like Python dictionaries, XML, or JSON. For instance, the format used by Grobid, the tool we employ for article extraction, is XML. These formats are inherently compatible with MongoDB's storage mechanism, which uses BSON objects. This compatibility is a considerable advantage for storing and managing the data efficiently within our system.
3. **Security and Data Integrity**
    - In an academic research platform like ours, where the integrity of scholarly work and the privacy of personal and institutional data are of utmost importance, the selection of backend technologies that prioritize security and data integrity is crucial. **FastAPI** and **MongoDB** have been chosen with these priorities in mind, offering advanced security features tailored to the needs of our diverse user base, from students to government agencies.
        - **FastAPI:** This framework is designed with security as a core feature, offering easy integration with secure authentication and authorization systems like OAuth2 and JWT tokens. This is particularly important for our system, which caters to a wide range of users, each requiring controlled access to different levels of data and functionality. For example, students may need access to public academic resources, while academics and government officials may require access to sensitive or proprietary data.
        - **MongoDB:** Known for its robust security mechanisms, MongoDB offers encryption at rest and in transit, ensuring that all data, from student notes to confidential research findings, is securely stored and transferred. Access control, auditing features, and regular security patches further enhance data integrity, providing peace of mind for users reliant on the system for their research and decision-making processes.
    - The integration of these technologies ensures that all user interactions with the system, from data entry to complex queries, are conducted in a secure environment, safeguarding against unauthorized access and data breaches. This adherence to high security and data integrity standards is essential for maintaining the trust and reliability expected by our users in their scholarly and professional endeavors.

4. **Data Volume Considerations**
    - Given the system's aim to serve as a comprehensive platform for academic research, it will initially handle approximately 10,000 records, encompassing a wide range of data types from simple bibliographic information to complex analysis results. **MongoDB** has been selected as our database solution for its exceptional ability to manage such diverse data volumes efficiently.
        - **Scalability:** MongoDB's document-oriented structure and schema-less design provide significant flexibility, allowing us to easily accommodate the evolving nature of academic data. This is particularly important as the system grows to include more records and more complex types of data analysis, ensuring that we can scale our database infrastructure without extensive re-engineering.
        - **Performance:** MongoDB's indexing capabilities, sharding, and replication features are designed to maintain high performance even as data volume grows. This is crucial for our system, which must deliver quick and accurate search results across vast datasets to users conducting time-sensitive research.
        - **Data Management:** The system's features, such as advanced research functionality, data management tools, and analysis and visualisation capabilities, require a database that can handle complex queries and aggregate functions efficiently. MongoDB's rich query language and aggregation framework enable us to provide these sophisticated features without compromising on performance.
    - The choice of MongoDB, with its emphasis on performance, scalability, and flexibility, aligns with our project's goals and the varied requirements of our users. Whether it's a student compiling a literature review or a government agency conducting policy analysis, our database infrastructure is equipped to support their diverse needs effectively.
5. **Concurrency and Scalability**
    - In the context of the diverse and dynamic needs outlined in the system's purpose and intended user base, the system's architecture must be inherently scalable and capable of handling concurrent access across varied use cases. From in-depth literature reviews by students to complex data analysis for government policy formulation, the system's workload can be highly variable and unpredictable. This necessitates a backend infrastructure that can effortlessly adapt to changing demands without degradation in performance.

    - The choice to build the backend with **FastAPI** and deploy it within **Docker containers** is strategic, ensuring lightweight, isolated environments that are both efficient and portable. This containerization serves multiple purposes:
        - **Isolation:** Each Docker container provides an isolated environment for a segment of the system's functionality, ensuring that any changes or issues within one container do not affect others, which is crucial for maintaining the system's stability across its varied user base.
        - **Portability:** Docker containers can be easily moved, copied, and deployed across different environments, enhancing the development lifecycle and ensuring consistency between development, testing, and production environments. This is particularly beneficial given the system's broad scope, which might require deployment across different institutions with varying infrastructure setups.
        - **Resource Efficiency:** Containers require less overhead than traditional virtual machines, allowing more efficient use of system resources. This is key for a system expected to handle complex data processing tasks such as extracting paper details, analyzing topic connections, and visualizing author relationships.

    - Looking forward, the integration of **Kubernetes (k8s)** for container orchestration will enable the system to dynamically scale resources across containers in response to real-time demand. Kubernetes facilitates:
        - **Horizontal Scaling:** Automatically increasing or decreasing the number of container instances based on the system's current load. This ensures that the system can handle peak loads efficiently, such as during exam periods for students or end-of-quarter analysis for companies, without permanent allocation of excessive resources.
        - **Load Balancing:** Distributing user requests intelligently across multiple container instances to ensure optimal resource utilization and response times. This is crucial for maintaining a seamless user experience, whether it's a student rapidly searching for literature or a company conducting extensive market analysis.
        - **Self-healing:** Automatically restarting failed containers, replacing them, and rebalancing loads without downtime. This resilience is vital for a system that supports critical research and decision-making processes across different sectors.
    - In summary, the system's backend architecture, built on FastAPI and deployed in Docker containers with future Kubernetes integration, is designed to meet the scalability and concurrency requirements inherent in serving a diverse and demanding user base. This approach ensures that the system remains responsive, efficient, and adaptable, catering to the dynamic needs of students, academics, government agencies, and companies engaged in various forms of academic and industry-specific research.

The selection of Vue.js, FastAPI, and MongoDB was a strategic decision grounded in a comprehensive understanding of our team's strengths, project requirements, and user needs. This thoughtful alignment is poised to yield a platform that is not only effective in fulfilling the diverse requirements of its users but is also fortified with the robustness, security, and scalability needed for future growth. The integration of these technologies underscores our commitment to delivering a high-quality, user-centric academic research platform.

### **Horizontal comparison of each component**
The selection of each technology component within our stack was the result of a deliberate evaluation of its strategic advantages, suitability for meeting both the project goals and the client's specific needs, and its comparison to other potential alternatives. Below we detail the rationale for our choices:

#### **`Vue.js`**
- **Chosen Over:** Angular, React  
- **Advantages:** Provides a simplified and adaptable structure for rapid UI development. Its component-driven architecture is ideal for dynamic user interfaces.  
- **Justification:** The selection was based on Vue.js's gentle learning curve, thorough documentation, and vibrant community. For a platform intended to serve a diverse user base, from students to government officials, a smooth and interactive user experience is paramount, which Vue.js offers with its reactive system.

#### **`Vuex`**
- **Chosen Over:** Redux, MobX  
- **Advantages:** Offers a streamlined state management system, essential for maintaining cohesive state throughout the application.  
- **Justification:** Vuex's native integration with Vue.js significantly simplifies state management. For a system that includes complex features like user-defined filters and search, this simplicity is invaluable.

#### **`VuesticUI`**
- **Chosen Over:** Ant Design, BootstrapVue  
- **Advantages:** Offers an extensive collection of pre-designed components that are seamlessly integrated with Vue.js, enhancing the speed of UI development.
- **Justification:** The cohesive design system of VuesticUI aligns with our goal for a user-friendly interface that supports diverse features, from data visualization to literature management, enhancing user experience and engagement.

#### **`Webpack`**
- **Chosen Over:** Rollup, Parcel  
- **Advantages:** Optimizes loading time and ensures high performance, essential for a seamless user experience.  
- **Justification:** Its wide range of plugins and community support offers a more customizable setup, which is vital for handling the complex asset management our system requires.

#### **`Axios`**
- **Chosen Over:** Fetch API, SuperAgent  
- **Advantages:** Presents a robust solution for HTTP requests with a promise-based API, simplifying server communication.  
- **Justification:** Axios's widespread adoption and ease of use make it the best choice for our project, especially considering the need for efficient communication between the system's front end and the back end.

#### **`vis.js`**
- **Chosen Over:** ECharts, Chart.js  
- **Advantages:** Provides extensive charting and dynamic visualization features essential for detailed academic data presentation.
- **Justification:** vis.js offers an optimal mix of customizability and user-friendliness, catering to our user base's sophisticated data analysis and visualization needs, ranging from students performing literature reviews to businesses conducting market research.

#### **`FastAPI`**
- **Chosen Over:** Flask, Django REST framework  
- **Advantages:** Known for its fast performance and asynchronous nature, ideal for high-performance APIs.  
- **Justification:** The modern approach to API development and automatic Swagger documentation generation aligns with our goal to provide a powerful yet user-friendly platform for academic research.

#### **`MongoDB`**
- **Chosen Over:** MySQL, PostgreSQL  
- **Advantages:** The schema-less design offers unparalleled flexibility in managing diverse datasets.  
- **Justification:** MongoDB's ability to handle unstructured data efficiently is crucial for the academic articles and related metadata, ensuring the system remains adaptive and scalable.

#### **`Grobid`**
- **Chosen Over:** Tika, PDFBox  
- **Advantages:** Specializes in extracting information from PDF documents, essential for processing academic papers.  
- **Justification:** Given the system's focus on academic literature analysis, Grobid is ideally suited for converting articles into a structured format for further processing and analysis.

#### **`Vitest`**
- **Chosen Over:** Jest, Mocha  
- **Advantages:** Provides an efficient and reliable framework for Vue.js front-end testing.  
- **Justification:** The system requires robust front-end testing to maintain a high-quality user experience, and Vitest offers superior integration with Vue.js compared to other frameworks.

#### **`Pytest`**
- **Chosen Over:** unittest, Nose2  
- **Advantages:** Enables comprehensive backend testing, indispensable for data processing integrity.  
- **Justification:** Pytest's extensive plugin system and simplicity ensure a streamlined testing process, which is vital for the complex data handling our system performs.

#### **`Docker and Kubernetes`**
- **Chosen Over:** Traditional VMs, Heroku  
- **Advantages:** Provide the flexibility to manage and scale applications seamlessly, necessary for modern application deployment.
- **Justification:** The agility afforded by Docker and Kubernetes in deployment and infrastructure management will enable the system to adapt to user growth and changing requirements effectively.

#### ***Conclusion***
In conclusion, the selected technology stack not only fulfills the individual requirements of performance, scalability, and usability but also integrates into a cohesive architecture that aligns with the overall purpose of the system. Each technology component has been chosen with a strategic perspective, ensuring that the system is well-equipped to support the intricate tasks of academic literature research and analysis, catering to the diverse needs of students, researchers.

### **Alternative Technology Stack**
Here is an alternative technology stack that could have been chosen for the system, along with a comparative analysis of its advantages and limitations compared to the selected stack.

#### **`React + Redux`**
- **Instead Of:** Vue.js + Vuex  
- **Advantages:** Offers a robust ecosystem and is highly performant in large-scale applications.
- **Limitations:** React and Redux introduce a steeper learning curve and added complexity, which might not align with the ease of use required for our academic-focused platform.

#### **`Tailwind CSS`**
- **Instead Of:** VuesticUI  
- **Advantages:** Tailwind CSS offers a utility-first approach that grants detailed control over styling and responsive design, allowing for more custom and finely-tuned UI elements.
- **Limitations:** Unlike VuesticUI, Tailwind CSS does not come with a wide range of ready-made components. This might require additional time for component development and design customization, potentially extending the overall development timeline.

#### **`Vite`**
- **Instead Of:** Webpack  
- **Advantages:** Promises faster rebuilds and simpler configuration.
- **Limitations:** The relative newness means a smaller plugin ecosystem and less community support compared to Webpack.

#### **`Fetch API`**
- **Instead Of:** Axios  
- **Advantages:** Built-in within browsers, removing the need for external libraries.
- **Limitations:** Does not provide features like automatic JSON data transformation that Axios offers.

#### **`Chart.js`**
- **Instead Of:** vis.js  
- **Advantages:** Provides a lightweight solution with a simple API, perfect for fundamental charting needs.
- **Limitations:** Falls short in offering the advanced and interactive visualization features essential for the detailed academic data analysis our platform necessitates.

#### **`Django + Django REST Framework`**
- **Instead Of:** FastAPI  
- **Advantages:** A full-stack framework with a mature ecosystem, complemented by a RESTful API-building toolkit.
- **Limitations:** Lacks the performance and modern API development features of FastAPI, such as automatic Swagger documentation.

#### **`PostgreSQL`**
- **Instead Of:** MongoDB  
- **Advantages:** Powerful SQL database with strong compliance to standards.
- **Limitations:** Not as adept as MongoDB at handling unstructured data, which is critical for our evolving academic datasets.

#### **`Cypress`**
- **Instead Of:** Vitest  
- **Advantages:** Offers an excellent setup for end-to-end testing with a rich feature set.
- **Limitations:** More focused on end-to-end testing and could be less efficient for unit testing specific to Vue.js.

#### **`Flask + Flask RESTPlus`**
- **Instead Of:** FastAPI  
- **Advantages:** Simple and easy to learn, with Flask RESTPlus for building RESTful APIs.
- **Limitations:** Does not provide the same level of performance and built-in data validation features as FastAPI.

#### **`Heroku`**
- **Instead Of:** Docker + Kubernetes  
- **Advantages:** Simplifies application deployment directly in the cloud.
- **Limitations:** Does not offer the containerization and orchestration capabilities necessary for scalable and complex deployments.

#### ***Comparative Analysis***
The alternative stack provides certain benefits; however, it poses significant limitations in terms of the complexity of learning and managing the technologies, the development speed, performance, and flexibility in handling unstructured data, as well as in scalability and deployment management. These limitations underscore the reasons for our selected technology stack, which provides a more user-friendly, efficient, and scalable solution tailored to the needs of a diverse academic audience.

## **Software Architecture**
![Component Architecture](../Image/component-graph.png)
*Figure 2: Component architecture for the application.*

### **Overview**
The system adopts a 5-tier architecture, strategically designed to modularize the functional aspects of academic literature research and analysis. This tiered approach enables effective separation of concerns, fostering enhanced scalability, improved maintainability, and secure operation. It ensures that the client interface, presentation logic, business processes, integration services, and resource management remain distinct yet seamlessly interact. This design not only streamlines development and maintenance but also optimizes the system’s security by layering access controls and operational permissions.

#### **`Client Tier`**
- **Description:** The Client Tier is the system's front-facing layer, hosting the ClientUI that users interact with. This tier is dedicated to delivering the user interface through which all user inputs and interactions occur, designed for accessibility and usability.
- **Relation:** It directly interacts with the Presentation Tier, sending user requests down the tier hierarchy and presenting processed data back to the user.
- **Components:**
    - [`ClientUI`](#clientui)
- **Advantages:** Provides a centralized interface for all user interactions, simplifying the user experience and offering a gateway to the underlying functionalities.
- **Potential Downsides:** As the most exposed layer, it's vulnerable to attacks; hence, it requires robust security measures.

#### **`Presentation Tier`**
- **Description:** The Presentation Tier manages the application's logic for presenting data to the user. It interprets commands from the Client Tier and decides how to represent information to users effectively.
- **Relation:** It acts as an intermediary, transforming data from the Business Tier into a user-friendly format and vice versa.
- **Corresponding Directories:**
    - [frontend/src/views/](../../frontend/src/views)
    - [backend/app/routers/](../../backend/app/routers)
- **Components:**
    - [`CoAuthors`](#coauthors)
    - [`CitedTree`](#citedtree)
    - [`SameTopic`](#sametopic)
    - [`TopicConnections`](#topicconnections)
    - [`PaperDashboard`](#paperdashboard)
    - [`CatalogAPI`](#catalogapi)
    - [`AnalysisAPI`](#analysisapi)
- **Advantages:** Separates the logic of how data is displayed from the core business logic, allowing designers and developers to work independently.
- **Potential Downsides:** Increased complexity in data handling and potential performance bottlenecks if not well-optimized.

#### **`Business Tier`**
- **Description:** This tier contains the core business logic of the system, processing user requests, performing operations, and making logical decisions.
- **Relation:** It interfaces with the Presentation Tier to receive processed user inputs and interacts with the Integration Tier to fetch and manipulate data.
- **Corresponding Directories:**
    - [backend/app/services](../../backend/app/services)
- **Components:**
    - [`Models`](#models)
    - [`Schema`](#schema)
    - [`Catalog`](#catalog)
    - [`Analysis`](#analysis)
    - [`Extractor`](#extractor)
    - [`GrobidClient`](#grobidclient)
    - [`Client`](#client)
    - [`Parser`](#parser)
    - [`Types`](#types)
- **Advantages:** Centralizes business logic, promoting reusability and consistency across the system.
- **Potential Downsides:** Complex logic can be difficult to manage and may become a bottleneck for performance if not carefully architected.

#### **`Integration Tier`**
- **Description:** This tier orchestrates the communication between the Business Tier and the Resource Tier, facilitating the integration of different data sources and external services.
- **Relation:** It serves as a conduit for data, ensuring that requests and responses flow between the front-end and back-end systems correctly and efficiently.
- **Corresponding Directories:**
    - [backend/app/integration/](../../backend/app/integration)
- **Components:**
    - [`CatalogAccess`](#catalogaccess)
- **Advantages:** Allows for a decoupled architecture where the core business logic is insulated from changes in data sources and external services.
- **Potential Downsides:** Adds another layer of complexity and can be a point of failure if not robustly designed.

#### **`Resource Tier`**
- **Description:** The Resource Tier is responsible for managing all data storage and retrieval operations, ensuring data integrity and security.
- **Relation:** It interacts directly with the Integration Tier to provide the necessary data to fulfill business operations.
- **Corresponding Directories:**
    - [backend/app/db/](../../backend/app/db)
- **Components:**
    - [`MongoengineModels`](#mongoenginemodels)
    - [`Config`](#config)
- **Advantages:** Provides a dedicated layer for data operations, allowing for optimized data management and scalability.
- **Potential Downsides:** Requires careful management to prevent data bottlenecks and maintain performance, especially under high load conditions.

Each tier’s design considers the project’s goals and user needs, ensuring that students, academics, and professionals can effectively conduct literature research, analysis, and visualization without facing the complexities of the underlying system. The architecture provides the framework to support the advanced research functionality, data management tools, citation tracking, and analysis and visualization capabilities that are key to meeting the diverse requirements of the system's users. However, the layered approach, while beneficial for organization and scalability, introduces additional complexity and may necessitate careful consideration of performance and security implications at each level.

### **Alternative Software Architecture**
While the 5-tier architecture described provides a robust and scalable framework for the system, an alternative architecture could be considered to address specific needs or constraints. One such alternative might be a microservices-based architecture. In this approach, the system is decomposed into a set of small, autonomous services, each implementing a specific business capability.

#### Microservices-based Architecture
- **Description:** A microservices architecture structures an application as a collection of loosely coupled services, each designed to execute a unique business function. Each service is self-contained and can be developed, deployed, and scaled independently.
- **Components:**
    - `Search Service`: Manages literature search functionalities.
    - `User Management Service`: Handles authentication and user profiles.
    - `Data Processing Service`: Executes extraction, analysis, and parsing of academic papers.
    - `Data Storage Service`: Manages data persistence and retrieval.
    - `API Gateway`: Provides a single entry point for all client requests.

#### Limitations and Misalignments with Business and Project Goals
- **Tight Coupling with Components**: While microservices offer independence, they may require more coordination when changes occur that span multiple services. This could lead to a tightly coupled system if not managed correctly, which contradicts the goal of having a modular system that simplifies updates and maintenance.

- **Complex Service Interactions**: The system aims to create dynamic networks of connections between articles, authors, and topics. Microservices communicating over a network can introduce complexity and latency in these interactions, potentially reducing the system's responsiveness and user experience.

- **Data Consistency**: The Resource Tier in the 5-tier architecture ensures consistent and centralized data management. In a microservices architecture, each service may have its own database, leading to challenges in maintaining data consistency across services, which is critical for the system's intended use in academia and policy analysis.

- **Deployment Overhead**: The intended users include students and academics who may not have extensive technical expertise. A microservices architecture could introduce overhead in deployment and management, potentially complicating the operational aspect for such users.

- **Security**: Each microservice might expose its own API, which could increase the attack surface of the system. The 5-tier architecture's layering of access controls might be more straightforward to secure compared to the numerous endpoints that microservices would introduce.

- **Resource Utilization**: Microservices can be more resource-intensive, as each service may require its own runtime environment. For smaller user groups like individual researchers or small companies, this might not align with the project goal of providing a user-friendly and cost-effective system.

- **User Experience Consistency**: Given the system’s diverse user base, consistent user experience is crucial. The 5-tier architecture facilitates a unified user interface, whereas a microservices approach might lead to fragmentation, affecting usability for students and academics who are the primary users.

In conclusion, while a microservices architecture offers certain advantages such as independence and scalability, it may not align well with the system's current goals and user requirements. The complexity, potential for tight coupling, challenges in maintaining data consistency, deployment overhead, and security considerations present significant limitations for the project. The original 5-tier architecture is better suited to the system’s need for a coherent, secure, and user-friendly platform for academic literature research and analysis.

## **Components Design**
### `ClientUI`
#### *Description*
The `ClientUI` serves as the user interface layer of the system, providing an interactive web-based front end for users to access and interact with the system's features. It handles user input, displays data, and provides a seamless user experience by integrating with the backend services.

### `CoAuthors`
#### *Description*
The `CoAuthors` component is a Vue.js single-file component responsible for visualizing the co-authorship network within academic research. It leverages the `vis-network` library to display interactive graphs that represent the connections between authors and papers. This component provides users with insights into collaborative relationships and scholarly article connections.

#### *Related Requirement IDs*
- 3A

#### *Corresponding File*
[frontend/src/views/author/CoAuthors.vue](../../frontend/src/views/author/CoAuthors.vue)

#### *Provided Interfaces*
This component provides several interfaces for:
- Initiating a search for papers and displaying search results.
- Selecting a paper from the search results to generate a co-authorship network.
- Visualizing and interacting with the co-authorship network graph.
- Highlighting and navigating to specific nodes within the network.

#### *Functionalities*
User Interaction
- `handleSearch()`
    - Initiates a search and processes the results for user interaction.
- `handleResultSelect()`
    - Handles user selection of a paper from the search results and triggers the network generation process.

Network Visualization
- `initializeNetwork()`
    - Initializes the network graph with nodes and edges representing authors and papers.
- `highlightNode()`
    - Highlights the corresponding node and list item when an author or paper is selected.

#### *Dependencies*
The `CoAuthors` component relies on several internal modules and libraries to perform its functions:
- `vis-network/standalone` for generating interactive network graphs.
- `vue-router` for routing and navigation.
- Utility functions from `@/utils/network.js` for network-related operations.
- The `req` module from `@/utils/req.js` for making API requests to the backend.
- Sub-components like `SearchResult` and `PaperList` for structuring the user interface.

#### *Usage*
The `CoAuthors` component is used in the system's user interface for real-time user interactions, specifically within the academic research network visualization functionality. It is not designed for batch processing but rather for providing interactive, on-demand visualizations of academic collaborations. This component fits into a component-based architectural pattern and is designed to work within the larger Vue.js ecosystem, reflecting a modular and reactive design approach.

### `CitedTree`
#### *Description*
The `CitedTree` component is designed to visualize citation networks, depicting how academic papers reference one another. It is a Vue.js single-file component that creates a visual representation of a citation tree using the `vis-network` library, enabling users to understand the impact and relationship between various scholarly works.

#### *Related Requirement IDs*
- 4A

#### *Corresponding File*
[frontend/src/views/reference/CitedTree.vue](../../frontend/src/views/reference/CitedTree.vue)

#### *Provided Interfaces*
This component provides several interfaces for:
- Conducting searches for academic papers to include in the citation network.
- Selecting a paper to serve as the root of the citation tree.
- Visualizing the citation network with options to navigate and explore different papers and their citation links.

#### *Functionalities*
User Interface
- `handleSearch()`
    - Initiates a search for papers based on user input and displays the results in a modal.
- `handleResultSelect()`
    - Selects a paper and generates a citation network based on that paper.

Network Visualization
- `initializeNetwork()`
    - Sets up and renders the network visualization with hierarchical layouts and arrowed edges to represent citation directions.
- `highlightNode()`
    - Highlights a node on the network graph and the corresponding list item in the paper list when selected.

#### *Dependencies*
The `CitedTree` component relies on several internal modules and libraries to perform its functions:
- `vis-network/standalone` for the creation and manipulation of network graphs.
- `vue-router` to handle routing and query parameters.
- Utility functions from `@/utils/network.js` for formatting and options generation.
- The `req` service from `@/utils/req.js` for HTTP requests to the backend server.
- Components like `SearchResult` and `PaperList` are used to present search results and lists of papers respectively.

#### *Usage*
The `CitedTree` component is typically used by researchers or students who wish to explore the citation relationships between various academic articles. It is meant for real-time interaction where users can dynamically search for and select papers to visualize their citation network. The component supports interactive use rather than batch processing and is part of a larger Vue.js frontend application, indicative of a modern, modular web architecture.

### `SameTopic`
#### *Description*
The `SameTopic` component is a dynamic Vue.js interface for visualizing the network of academic papers related by common topics. It functions by creating an interactive network graph that connects papers sharing similar themes, using `vis-network` to enable users to explore the relationships between different scholarly works based on shared topics.

#### *Related Requirement IDs*
- 2A

#### *Corresponding File*
[frontend/src/views/topic/SameTopic.vue](../../frontend/src/views/topic/SameTopic.vue)

#### *Provided Interfaces*
This component provides several interfaces for:
- Executing search queries to find papers related to a specific topic.
- Selecting a paper from the search results to visualize other papers related to the same topic.
- Generating and interacting with a visual network graph to explore connections between papers.

#### *Functionalities*
Search and Data Retrieval
- `handleSearch()`
    - Initiates a query to search for papers and handles the display of results.
- `handleResultSelect()`
    - Manages the selection of a paper from the search results and initiates the network visualization based on the selected topic.

Network Visualization
- `initializeNetwork()`
    - Initializes the network visualization with nodes representing topics and papers, and edges representing their relationships.
- `highlightNode()`
    - Highlights a node within the network graph corresponding to user interaction.

#### *Dependencies*
The `SameTopic` component relies on:
- `vis-network/standalone` for creating and managing the network graph.
- `vue-router` for accessing route parameters.
- Helper functions from `@/utils/network.js` for network graph customization.
- `req.js` utility for backend communication to fetch required data.
- Sub-components such as `SearchResult` and `PaperList` for modal and list presentations, respectively.

#### *Usage*
The `SameTopic` component is used for real-time user interaction on the front end of the system, specifically tailored for researchers or any user interested in exploring thematic connections between papers. It is not intended for batch processing but for interactive, on-demand visualizations, fitting into a component-based frontend architecture designed for modularity and reactivity.


### `TopicConnections`
#### *Description*
The `TopicConnections` component is envisioned as a part of the system's user interface to visualize and explore the interconnections between various academic papers based on shared topics. Currently under development, this component aims to provide a comprehensive view of how different research papers are interlinked through common subjects, facilitating a deeper understanding of research landscapes.

#### *Related Requirement IDs*
- 2B

#### *Corresponding File*
[frontend/src/views/topic/TopicConnections.vue](../../frontend/src/views/topic/TopicConnections.vue)

#### *Provided Interfaces*
Once completed, this component is expected to provide interfaces for:
- Displaying a network or list view of papers connected by common research topics.
- Allowing users to select and delve into specific papers for more detailed information.
- Facilitating the exploration of topic-based research clusters and their contributing papers.

#### *Functionalities*
The component's planned functionalities include:
- Network Visualization
    - Placeholder for future network visualization functionality.
- Interactive List Display
    - Placeholder for an interactive list that highlights topic connections between papers.

#### *Dependencies*
Upon its completion, the `TopicConnections` component might depend on:
- `vis-network/standalone` or a similar library for rendering interactive network graphs.
- Backend services for fetching papers and their topic connections.
- Utility functions for processing and displaying network data.

#### *Usage*
`TopicConnections` is intended for use in scenarios where users—such as researchers, students, and academicians—wish to explore the thematic relationships between various scholarly articles. It will support interactive exploration to aid in literature reviews and research discovery. While still under development, it is designed for real-time interaction within the system's user interface, contributing to a rich, explorative research tool.

### `PaperDashboard`
#### *Description*
The `PaperDashboard` component serves as a central hub in the user interface for presenting detailed information about an uploaded academic paper, including its metadata, authors, references, and related analytical insights. It enables users to interactively explore various dimensions of the paper, such as topics, author networks, and citation trees, through a series of dynamically loaded dashboard cards.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 4A, 4B, 4C, 4D, 4E

#### *Corresponding File*
[frontend/src/views/PaperDashboard.vue](../../frontend/src/views/PaperDashboard.vue)

#### *Provided Interfaces*
This component provides interfaces for:
- Uploading and analyzing academic papers to extract metadata and related insights.
- Displaying detailed information about the paper, including title, authors, abstract, and more.
- Navigating to different analytical views based on the paper's data, such as topic analysis, co-author networks, and citation trees.

#### *Functionalities*
File Upload and Analysis
- `onFileAdded()`
    - Handles the upload of a paper file, triggers its analysis, and updates the dashboard with extracted information.

Information Display
- Presents a detailed view of the paper's metadata and analysis results, such as topics, co-authors, and citations.

Dashboard Navigation
- Provides links to various analytical views related to the paper, allowing users to delve deeper into specific areas of interest.

#### *Dependencies*
The `PaperDashboard` component depends on:
- `req.js` for backend communication to upload files and retrieve analysis results.
- `DashboardCard` and `UserChip` sub-components for rendering parts of the UI, such as analytical cards and author chips.
- Vue.js compositional utilities for reactive state management and component lifecycle handling.

#### *Usage*
`PaperDashboard` is primarily used by researchers, academics, and students who seek an integrated platform to upload, analyze, and explore academic papers. It is designed for real-time interaction, providing immediate feedback and insights upon file upload. This component is part of a larger web application aimed at enhancing academic research through advanced data visualization and analysis tools.

### `CatalogAPI`
#### *Description*
The `CatalogAPI` module serves as the backbone for the catalog endpoints in a scholarly communication platform, utilizing FastAPI for routing. It is designed to facilitate searches and retrievals of academic papers, authors, topics, and citation relationships through a variety of filters. The API endpoints enable users to access detailed information and establish connections between different entities within the academic domain, supporting functionalities like search results generation, citation tree construction, and exploration of co-authorship and topic-related articles.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 2A, 2B
- 3A, 3B, 3C,
- 4A, 4B, 4C, 4D, 4E
- 5A, 5B, 5C, 5D, 5E, 5F, 5G

#### *Corresponding File*
[backend/app/routers/catalog_api.py](../../backend/app/routers/catalog_api.py)

#### *Provided Interfaces*
This module provides RESTful API endpoints for:
- Searching academic papers with detailed filters such as title, DOI, publication date, and more.
- Retrieving lists of topics and authors based on specific search criteria.
- Constructing citation trees to visualize how papers cite each other.
- Exploring co-authorship networks and articles related to similar topics.

#### *Functionalities*
API Endpoints
- `root()`
    - Returns the root URI for the Catalog API, confirming the API's operational status.
- `search_papers()`
    - Searches for papers based on various filters and returns a `PaperResponse`.
- `search_topics()`
    - Retrieves topics based on ID or name, returning a `TopicResponse`.
- `search_authors()`
    - Finds authors using filters like name, email, or affiliation, providing an `AuthorResponse`.
- `get_same_topic()`
    - Identifies articles related to the same topic, resulting in a `SameTopicResponseSchema`.
- `get_co_author_by_filter()`
    - Fetches co-authorship information, yielding a `CoAuthorResponseSchema`.
- `get_cited_tree_by_filter()`
    - Generates a citation tree for a given article, returning a `CitedTreeResponseSchema`.

#### *Dependencies*
The `CatalogAPI` depends on:
- FastAPI for creating the web API routes and handling HTTP requests.
- Dependency injection patterns provided by FastAPI to incorporate filter objects like `ArticleFilter`, `TopicFilter`, and `AuthorFilter`.
- Internal services defined in `..services.catalog` for performing the actual search and retrieval logic based on the incoming API requests.
- Schema models from `..services.schema` to structure the API responses.

#### *Usage*
The `CatalogAPI` is used to power the backend of a scholarly communication platform, providing a RESTful interface for frontend applications and external systems to query academic data. It is designed for real-time interaction, allowing users to dynamically search for and explore academic content. The API is structured to support a microservices architecture, where it can act as a standalone service that interfaces with other parts of the system or external applications.

### `AnalysisAPI`
#### *Description*
The `AnalysisAPI` module is dedicated to handling the upload and analysis of academic documents within a scholarly communication platform. It facilitates the ingestion of new documents by allowing users to upload files, which are then saved, parsed, and analyzed to extract essential metadata like title, authors, abstract, and keywords. This process is crucial for automating the addition of scholarly content to the platform's database, thereby enhancing its value and utility for users.

#### *Related Requirement IDs*
- 1A, 1B

#### *Corresponding File*
[backend/app/routers/analysis_api.py](../../backend/app/routers/analysis_api.py)

#### *Provided Interfaces*
This module provides interfaces for:
- Checking the operational status of the Analysis API through a root endpoint.
- Uploading academic documents for processing, including the extraction and storage of valuable metadata and content.

#### *Functionalities*
API Endpoints
- `root()`
    - Provides a simple endpoint to verify the API's availability and to discover the base URI for analysis routes.
- `upload_document()`
    - Accepts document files for upload, processes the content to extract scholarly information, and returns a summary of the extracted data.

#### *Dependencies*
The `AnalysisAPI` depends on:
- FastAPI for creating API routes and handling HTTP requests.
- The `analysis` service for the actual parsing and extraction of content from uploaded documents.
- The `catalog` service's `save_parse_article` function to save the extracted information into the system's database.

#### *Usage*
`AnalysisAPI` is integral to the scholarly platform's functionality, particularly for users wishing to contribute new content to the database. It is designed for real-time interaction, where documents are uploaded and processed on-demand, providing immediate feedback to the user. This API supports a microservices architecture, functioning as a distinct service that could be scaled independently from the rest of the platform's components.


### `Models`
#### *Description*
The `Models` module in a scholarly communication platform defines the structure and relationships of entities within the academic database system. It encompasses a variety of Pydantic models and data classes to represent articles, topics, authors, institutions, departments, and their interrelations, such as author-institution, author-department, article-author, article-topic, and article-citation connections. These models are crucial for validating, managing, and ensuring the integrity of data related to academic articles, including metadata, authorship, affiliations, and references. Utilizing Pydantic, the module enforces type hints, validates data, and provides detailed error messages for incorrect data inputs, facilitating smooth data operations in an ORM context.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 3A, 3B, 3C

#### *Corresponding File*
[backend/app/services/models.py](../../backend/app/services/models.py)

#### *Provided Interfaces*
This module provides data models for:
- Defining the schema and validation rules for articles, authors, topics, and other entities in the academic domain.
- Establishing relationships between different entities, such as the connection between an article and its authors or topics.

#### *Functionalities*
Data Structure and Validation
- Models like `ArticleVO`, `TopicVO`, `AuthorVO`, etc., define the properties and validation rules for their respective entities.
- Relationship models like `ArticleAuthorVO`, `ArticleTopicVO`, etc., define the associations between different entities.

Custom Validators
- Implement custom validators for fields such as publication dates and DOIs to ensure they conform to required formats.

ORM Integration
- Models are designed with ORM mode enabled, allowing them to work seamlessly with ORM objects and database operations.

#### *Dependencies*
The `Models` module relies on:
- Pydantic for data validation and schema definition.
- Python's `re` module for regular expression operations, particularly for custom validators like DOI validation.
- Python's `warnings` module to issue warnings for data that does not conform to expected formats.

#### *Usage*
The `Models` module is integral to the platform's backend, especially in services that interact with the database, such as the catalog and analysis services. It ensures that data flowing into and out of the system is correctly structured and validated, providing a robust foundation for data integrity and reliability. This module is utilized across the system for data operations, making it a critical component of the platform's data management architecture, suitable for both real-time interactions and batch processing tasks.

### `Schema`
#### *Description*
The `Schema` module is designed to define the structure of API responses within a scholarly communication platform. It utilizes Pydantic models to describe entities like papers, authors, topics, and their collections, ensuring consistency and clarity in API communication. This module plays a pivotal role in shaping the data exchange between the backend and frontend or external systems, providing well-defined schemas for individual items, response structures, and specialized formats for representing complex relationships such as co-authorship networks and citation trees.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 2A, 2B
- 3A, 3B, 3C
- 4A, 4B, 4C, 4D, 4E
- 5A, 5B, 5C, 5D, 5E, 5F, 5G

#### *Corresponding File*
[backend/app/schema/schema.py](../../backend/app/services/schema.py)

#### *Provided Interfaces*
This module offers schemas for:
- Structuring responses for API endpoints that deal with papers, authors, and topics.
- Representing complex data structures like citation networks and co-authorship graphs in a digestible format for frontend consumption.

#### *Functionalities*
Response and Entity Schemas
- `ResponseSchema` provides a generic response structure for API endpoints, including status codes, messages, and data payloads.
- Entity schemas like `AuthorSchema`, `TopicSchema`, and `PaperItemSchema` define the data format for authors, topics, and papers, respectively.

Relationship and Network Schemas
- `SameTopicConnectionItemSchema` and `CoAuthorConnectionItemSchema` describe the connections between topics and papers or authors and their co-authored papers.
- `CitedConnectionItemSchema` models the citation relationships between papers, forming the basis for constructing citation trees.

#### *Dependencies*
The `Schema` module relies on:
- Pydantic for data validation and schema definition, ensuring that all data exchanged through the API endpoints adheres to the specified formats.
- Python's built-in typing system to specify types for fields in the models, enhancing code readability and reliability.

#### *Usage*
The `Schema` module is used across the API layer of the platform to ensure that data returned from various endpoints is consistently structured and conforms to predefined formats. It is crucial for API documentation, client-side data handling, and ensuring interoperability between different components of the system. This module supports the platform's architectural design, be it microservices, monolithic, or any other pattern, by providing a clear contract for data exchange.

### `Catalog`
#### *Description*
The Catalog component is crucial for the system’s ability to import and manage academic articles within the database. It includes a series of interfaces and functions that work together to parse article data from various formats, save articles and their related information (authors, citations, topics), and generate structured responses for user queries.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 2A, 2B
- 3A, 3B, 3C
- 4A, 4B, 4C, 4D, 4E 

#### *Corresponding File*
[backend/app/services/catalog.py](../../backend/app/services/catalog.py)

#### *Provided Interfaces*
This component provides several interfaces for:
- Importing and parsing article metadata, content, and references from input data structures or JSON files.
- Creating and managing relationships between articles, authors, and topics within the database.
- Searching for articles, authors, and topics based on a set of criteria or filters.
- Constructing citation trees to analyze the interconnections between academic works.
- Generating structured response objects in accordance with the defined schemas to facilitate the consumption of data by client applications or other system components.

#### *Functionalities*
- Article Management
    - `save_parse_article()`
        - Processes and saves article metadata to the database.
    - `save_parse_article_with_filepath()`
        - Parses a JSON file containing article metadata and saves it to the database.
    - `save_parse_articles_within_dir()`: 
        - Recursively processes and saves articles from JSON files within a directory.

- Query and Response Generation
    - `search_papers_by_filter_as_response()`
        - Retrieves a list of papers based on filters and returns a `PaperResponse`.
    - `search_topics_by_filter_as_response()`: 
        - Fetches topics based on filters and returns a `TopicResponse`.
    - `search_authors_by_filter_as_response()`: 
        - Gathers a list of authors based on filters and returns an `AuthorResponse`.
    - `search_same_topic_by_filter_as_response()`: 
        - Identifies articles sharing the same topic and returns a `SameTopicResponseSchema`.
    - `search_co_author_by_filter_as_response()`: 
        - Identifies co-author relationships and returns a `CoAuthorResponseSchema`.
    - `search_cited_tree_by_filter_as_response()`: 
        - Maps citation relationships up to a specified citation depth and returns a `CitedTreeResponseSchema`.

#### *Dependencies*
The Catalog component relies on several internal modules to perform its functions:
- CRUD operation classes from the `integration.catalog_access` module for interaction with the database.
- Types from `services.Parser.types` and `services.models` for data structure definitions.
- Schemas from `services.schema` for response object formatting.

#### *Usage*
This component is designed for use within a service-oriented architecture and can be invoked by other system components or services that require access to academic data. It can also be used in batch operations, such as importing a large dataset of articles into the system, or for real-time querying in response to user inputs.

### `Analysis`
#### *Description*
The `Analysis` module is central to processing academic documents within the scholarly communication platform. It integrates functionalities for parsing documents, extracting metadata, and analyzing content to identify topics and keywords. This module uses natural language processing (NLP) techniques and Latent Dirichlet Allocation (LDA) for topic modeling, enhancing the platform's capability to automate the ingestion, categorization, and analysis of scholarly articles.

#### *Related Requirement IDs*
- 1A, 1B

#### *Corresponding File*
[backend/app/services/analysis.py](../../backend/app/services/analysis.py)

#### *Provided Interfaces*
This component provides interfaces for:
- Cleaning and preprocessing document text to remove noise and standardize the content.
- Extracting and cleaning abstracts from documents to improve the quality of metadata.
- Performing topic modeling on articles to identify and extract significant topics and keywords.
- Parsing XML representations of articles to construct structured ArticleObjects, including metadata and content.
- Extracting XML content from PDF documents using external services like GROBID.

#### *Functionalities*
Document Processing and Analysis
- `_clean_doc()`: Cleans document text by removing stopwords, punctuation, and applying lemmatization.
- `_clean_abstract()`: Processes abstracts to remove unwanted characters and formats the text.
- `get_topics_from_article()`: Analyzes an article to extract significant topics using LDA topic modeling.
- `get_article_object()`: Parses an XML file into an ArticleObject, incorporating topic analysis.

External Integration and File Handling
- `get_extracted_xml()`: Interfaces with external services like GROBID to convert PDFs to XML format for further processing.

#### *Dependencies*
The `Analysis` module relies on:
- NLTK for natural language processing tasks, such as stopwords removal and lemmatization.
- Gensim for topic modeling and keyword extraction from texts.
- Custom modules like `Extractor` and `Parser` for handling the extraction and parsing of document content.

#### *Usage*
The `Analysis` module is invoked during the document upload and processing workflow, where it analyzes uploaded academic papers to extract metadata, topics, and keywords. This automated processing enriches the platform's database with structured, searchable scholarly content. It supports batch processing of documents for database enrichment and real-time analysis during document uploads, adaptable to various architectural patterns like microservices or monolithic architectures, depending on the system's design.

### `Extractor`
#### *Description*
The `Extractor` component is essential for converting academic documents from PDF format to structured XML. It utilizes GROBID, an open-source tool, to perform this transformation, enabling further processing and analysis of the document's content. This module serves as an intermediary step in the document ingestion pipeline, preparing the documents for detailed parsing and metadata extraction.

#### *Related Requirement IDs*
- 1a, 1b, 1c, 1d

#### *Corresponding File*
[backend/app/services/Extractor/extractor.py](../../backend/app/services/Extractor/extractor.py)

#### *Provided Interfaces*
This component provides interfaces for:
- Converting PDF documents to XML format using the GROBID service.
- Generating file paths for the resulting XML documents based on the original PDF file paths.

#### *Functionalities*
File Conversion and Path Handling
- `_generate_xml_path()`: Generates the file path for the XML document based on the original PDF file path.
- `pdf_to_xml()`: Converts a PDF document to XML format by interacting with a GROBID server.
- `_check_grobid_running()`: Checks if the GROBID service is accessible and running, ensuring the conversion process can proceed.

#### *Dependencies*
The `Extractor` component relies on:
- The GROBID service for document conversion, which must be running and accessible from the system where the extractor is executed.
- The `subprocess` module for checking the availability of the GROBID service.

#### *Usage*
The `Extractor` component is used during the initial stages of document processing, specifically when new academic documents are uploaded to the platform for inclusion in the database. It is designed for real-time interaction during the document upload process, ensuring that documents are immediately converted and ready for further processing. This component can be adapted to various architectural patterns, but it is particularly suited for microservices architectures where separate services handle different aspects of document processing and analysis.

### `GrobidClient`
#### *Description*
The `GrobidClient` serves as a Python interface to interact with the GROBID service, a machine learning library for extracting, parsing, and restructuring raw documents (like PDFs) into structured XML and TEI encoded documents. It handles the concurrent processing of documents, utilizing ThreadPoolExecutor for parallelizing calls to the GROBID services. The client manages batches of documents to optimize memory usage and processing time, making it an efficient tool for large-scale document analysis.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D

#### *Corresponding File*
[backend/app/services/Extractor/Grobid/grobid_client.py](../../backend/app/services/Extractor/Grobid/grobid_client.py)

#### *Provided Interfaces*
This component offers interfaces for:
- Configuring and initiating connections to the GROBID server.
- Processing batches of documents with customizable parameters (batch size, timeout, etc.).
- Handling the conversion of documents from PDF or text format to structured XML using various GROBID services.

#### *Functionalities*
Server and Process Management
- `_load_config()`: Loads configuration settings from a JSON file.
- `_test_server_connection()`: Checks if the GROBID server is running and accessible.
- `_output_file_name()`: Generates the output file name based on the input file and specified output directory.

Document Processing
- `process()`: Processes a directory of documents in batches, converting them to TEI XML.
- `process_batch()`: Processes a batch of documents concurrently, applying a specified GROBID service.
- `process_pdf()`: Converts a single PDF document to TEI XML format.
- `process_txt()`: Processes a plain text file containing citations, converting them to TEI XML format.

#### *Dependencies*
The `GrobidClient` component depends on:
- The GROBID service, which must be operational and accessible via a network.
- The `requests` library for HTTP communication with the GROBID server.
- The `concurrent.futures` module for parallel processing of document batches.

#### *Usage*
The `GrobidClient` is typically used in the context of document ingestion and preprocessing pipelines, where a large number of academic documents need to be converted from PDF or plain text to structured XML format for further analysis. It is suitable for both real-time and batch processing scenarios and fits well within microservices architectures where it can serve as a dedicated service for document conversion and preprocessing.

### `Client`
#### *Description*
The `Client` serves as a foundational class for building clients that interact with RESTful APIs. It provides generic methods to send HTTP requests like GET, POST, PUT, and DELETE, making it versatile for various API interactions. The class includes mechanisms for encoding requests, decoding responses, handling authentication, and managing connection timeouts, making it a robust tool for API communication.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D

#### *Corresponding File*
[backend/app/services/Extractor/Grobid/client.py](../../backend/app/services/Extractor/Grobid/client.py)

#### *Provided Interfaces*
This component offers interfaces for:
- Sending HTTP requests (GET, POST, PUT, DELETE) to APIs.
- Encoding data into request bodies and setting appropriate content-type headers.
- Decoding responses from APIs, typically expecting JSON responses.
- Handling authentication with APIs using credentials like username and API key.

#### *Functionalities*
Configuration and Connection
- `__init__()`: Initializes the client with API base URL, authentication credentials, and timeout settings.
- `get_credentials()`: Retrieves authentication credentials for API requests.

HTTP Request Methods
- `get()`: Sends a GET request to the specified API endpoint.
- `delete()`: Sends a DELETE request to the specified API endpoint.
- `put()`: Sends a PUT request with data to the specified API endpoint.
- `post()`: Sends a POST request with data to the specified API endpoint.

Utility Functions
- `encode()`: Encodes the data into the request body, setting the content-type to JSON.
- `decode()`: Decodes the response body from JSON to a dictionary or returns an error message.
- `service_status()`: Checks the status of the service by calling a predefined status endpoint.

#### *Dependencies*
The `Client` component relies on the `requests` library for handling HTTP requests and responses, making it a crucial dependency for the component's operation.

#### *Usage*
The `Client` is designed to be a base class for specific API clients. It can be extended and customized to interact with particular RESTful APIs by providing the base URL and any necessary authentication credentials. It is suitable for applications that require integration with external services, data ingestion from APIs, or any scenario where RESTful API communication is needed. The `Client` fits well within both microservices and monolithic architectures, serving as a modular piece for handling external API interactions.

### `Parser`
#### *Description*
The `Parser` is a crucial component responsible for parsing XML documents related to academic articles. It converts XML data into structured objects representing articles, including metadata like titles and DOIs, content such as abstracts and keywords, and relationships like references and authorships. The parser leverages the ElementTree XML API for navigating and querying the XML structure, extracting relevant information through XPath expressions, and transforming it into Python objects.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D

#### *Corresponding File*
[backend/app/services/Parser/parser.py](../../backend/app/services/Parser/parser.py)

#### *Provided Interfaces*
This component offers interfaces for extracting various elements from XML documents, including:
- Metadata extraction: Parses the article's title, DOI, publisher, publication date, and journal.
- Content extraction: Retrieves the abstract and keywords from the article.
- Author extraction: Identifies authors, their affiliations, and emails from the article.
- Reference extraction: Gathers cited references, parsing their authors, titles, publication types, and other bibliographic details.

#### *Functionalities*
XML Parsing
- `_string_to_tree()`: Converts XML string content into an ElementTree object for parsing.
- `_parse_metadata()`: Extracts and structures the article's metadata.
- `_parse_content()`: Retrieves the article's abstract and keywords.
- `_parse_author()`: Identifies and lists the article's authors and their details.
- `_find_raw_reference()`: Finds raw reference strings within the XML document.
- `_store_references()`: Processes raw references using external tools like Anystyle to parse bibliographic information.
- `_parse_reference()`: Constructs structured reference objects from parsed bibliographic data.

Utility Functions
- `_find_text_single()`, `_find_text_paragraph()`, `_find_words_list()`: Utility functions for extracting text from specific XML nodes or attributes following given XPath expressions.

#### *Dependencies*
The `Parser` relies on:
- `xml.etree.ElementTree` for XML parsing and manipulation.
- External tools like Anystyle CLI for advanced parsing of bibliographic references.
- Standard libraries such as `io`, `json`, `subprocess`, and `tempfile` for file operations and subprocess management.

#### *Usage*
The `Parser` is utilized in scenarios requiring detailed analysis and extraction of academic article information from XML documents, such as metadata indexing, content analysis, and citation network construction. It serves as a backend utility in scholarly communication platforms, digital libraries, or research databases, facilitating content ingestion, metadata enrichment, and bibliometric analysis. The component aligns with both microservices-oriented and monolithic architectures, acting as a specialized service or module within larger information processing pipelines.

### `Types`
#### *Description*
The `Types` component defines a series of data classes used to structure and represent the parsed data from academic articles within the parsing system. It encapsulates the metadata, content, authors, and references of articles in a structured format, enabling easy manipulation and access to specific pieces of information extracted from XML documents or other sources. These data classes serve as the foundational building blocks for the system, allowing for standardized communication and storage of article-related data across different modules or services.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D

#### *Corresponding File*
[backend/app/services/Parser/types.py](../../backend/app/services/Parser/types.py)

#### *Provided Interfaces*
This component offers data structures for:
- `Metadata`: Contains article metadata like title, DOI, publisher, journal, and publication date.
- `Content`: Holds the abstract and a list of keywords from the article.
- `Author`: Represents an author's name, affiliation, and optional email address.
- `Reference`: Details a cited reference, including the list of authors, title, type, container title, DOI, and publication date.
- `ArticleObject`: Aggregates metadata, content, authors, and references into a single object representing an entire article.

#### *Functionalities*
Data Modeling
- The component defines the structure of data for articles, enabling standardized processing and handling across the system.

Serialization
- Provides methods (`to_json`, `to_dict`) for converting the data classes into dictionary or JSON formats for storage or transmission.

#### *Dependencies*
Relies on the Python standard library:
- `dataclasses` for defining simple data-holding classes.
- `typing` for specifying types of data each class holds, enhancing code clarity and type-checking.

#### *Usage*
These data classes are used throughout the parsing system and potentially in other parts of a larger application that deals with scholarly articles. They are crucial for tasks like:
- Parsing XML documents to extract article information.
- Structuring parsed data for further processing or analysis.
- Serializing article data for storage in databases or transmission over APIs.
- Facilitating the exchange of structured article data between different system components or external services.

The design aligns well with a variety of software architectures, including microservices, where each service could use these data classes to communicate article data, or monolithic architectures, where they serve as the common data format across different modules.

### `CatalogAccess`
#### *Description*
The `CatalogAccess` module provides a structured and type-safe way to interact with the MongoDB database, specifically tailored for handling scholarly communication data. It employs the MongoEngine ODM to map Python classes to MongoDB documents and offers CRUD operations for entities such as articles, topics, authors, and institutions. Each entity is associated with a specialized CRUD class that extends from a base class, ensuring uniformity and type safety across different database operations. This module serves as the backbone for data persistence and retrieval within the system, enabling efficient and structured access to stored academic data.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 2A, 2B
- 3A, 3B, 3C
- 4A, 4B, 4C, 4D, 4E

#### *Corresponding File*
[backend/app/integration/catalog_access.py](../../backend/app/integration/catalog_access.py)

#### *Provided Interfaces*
This module provides CRUD operations for various entities, encapsulated in classes like:
- `ArticleCRUD`
- `TopicCRUD`
- `AuthorCRUD`
- `InstitutionCRUD`
- `DepartmentCRUD`
- `AuthorInstitutionCRUD`
- `AuthorDepartmentCRUD`
- `ArticleAuthorCRUD`
- `ArticleCitationCRUD`
- `TopicRelationshipCRUD`
- `ArticleTopicCRUD`

Each class offers methods for creating, reading (retrieving by filter), updating, and deleting entities, along with specialized search functionalities tailored to the specific needs of each entity type.

#### *Functionalities*
Data Persistence and Retrieval
- Facilitates the creation, update, retrieval, and deletion of various entities in the database in a structured manner.

Search and Querying
- Provides capabilities to search and filter entities based on specific criteria, enhancing the application's ability to access and manipulate academic data.

Type Safety and Validation
- Ensures type safety and validation for data being persisted or retrieved from the database, minimizing errors and improving data integrity.

#### *Dependencies*
This component depends on several internal and external modules:
- `MongoEngine` for object-document mapping and database interaction.
- `MongoDB` as the underlying database system.
- Entity and Filter classes from `services.models` for data validation and transfer objects.

#### *Usage*
This module is integral to the system's data layer, interacting directly with the database to perform various operations related to scholarly communication entities. It is used across the application wherever database interaction is required, including but not limited to:
- Storing parsed article data extracted from documents.
- Retrieving articles, authors, or topics based on specific search criteria.
- Updating records as new information becomes available or corrections are made.
- Deleting records that are no longer needed or are incorrect.

The `CatalogAccess` module is compatible with various architectural patterns, especially service-oriented or microservices architectures, where it can serve as the data access layer for different services managing scholarly data.


### `MongoengineModels`
#### *Description*
The `MongoengineModels` module defines the data schemas and relationships for a scholarly communication system using MongoEngine, a Document-Object Mapper (ODM) for working with MongoDB from Python. It sets up models for various entities such as articles, authors, topics, institutions, departments, and various relationships among them, such as author-institution and article-author. This module is crucial for structuring and manipulating data in the MongoDB database, providing a foundation for storing and querying academic paper-related information efficiently.

#### *Related Requirement IDs*
- 1A, 1B, 1C, 1D
- 2A, 2B
- 3A, 3B, 3C
- 4A, 4B, 4C, 4D, 4E

#### *Corresponding File*
[backend/app/db/mongoengine_models.py](../../backend/app/db/mongoengine_models.py)

#### *Provided Interfaces*
This module provides data models for entities such as:
- `Article`: Represents academic articles, with fields for title, abstract, publication date, DOI, and more.
- `Topic`: Defines topics or subjects associated with articles.
- `Author`: Contains information about authors of articles, including name, email, and affiliation.
- `Institution`: Represents institutions to which authors may belong, like universities or research centers.
- `Department`: Defines departments within institutions.
- `AuthorInstitution`: Models the many-to-many relationship between authors and institutions.
- `AuthorDepartment`: Models the many-to-many relationship between authors and departments.
- `ArticleAuthor`: Represents the relationship between articles and their authors.
- `ArticleCitation`: Models citation relationships between articles.
- `ArticleTopic`: Links articles with their topics.
- `TopicRelationship`: Models hierarchical relationships between topics.
- `Sequence`: Provides a mechanism for generating sequential IDs.

#### *Functionalities*
Database Schema Definition
- Defines the structure of the database collections and their fields, ensuring data consistency and validation.

Relationship Management
- Manages complex relationships between entities, such as the many-to-many relationships between authors and institutions.

Index Management
- Ensures efficient querying by defining indexes on frequently queried and unique fields.

Sequence Management
- Provides sequential numbering for entities that require unique identifiers, aiding in data integrity and reference.

#### *Dependencies*
This component relies on:
- `MongoEngine`: For defining data models and managing interactions with MongoDB.
- MongoDB: As the underlying NoSQL database to store and manage the data models defined by this module.
- `config`: A configuration module that provides database connection settings and toggles between test and production environments.

#### *Usage*
This module is fundamental to the data layer of the system, providing the necessary structure for storing and retrieving academic paper-related data. It is used across the application to:
- Store new articles, authors, topics, etc., as they are added to the system.
- Retrieve and update existing records based on user interactions or automated processes.
- Delete records as necessary, maintaining data integrity and relevance.

The `MongoengineModels` module is compatible with various software architectures, particularly those that separate data access from business logic, such as MVC or clean architecture. It serves as the model layer in such patterns, encapsulating the data and its behavior.

### `Config`
#### *Description*
The `Config` module provides the MongoDB connection settings for the scholarly communication platform. It contains the URI strings for both the main and test databases hosted on MongoDB Atlas. The module also includes a `TEST_MODE` flag, determined by an environment variable, to toggle between production and test environments, allowing for isolated testing without affecting production data.

#### *Corresponding File*
[backend/app/db/config.py](../../backend/app/db/config.py)

#### *Provided Interfaces*
This component offers configuration settings for:
- MongoDB connection URIs for production and testing databases.
- A flag to toggle between test and production modes based on environment variables.

#### *Functionalities*
Database Configuration
- Sets up the connection strings for MongoDB, facilitating connections to the appropriate database based on the mode of operation (test or production).

Environment Mode Determination
- Determines the operational mode (test or production) by checking an environment variable, which can be useful for automated testing or development purposes.

#### *Dependencies*
The `Config` module relies on:
- `os`: To access environment variables for determining the test mode.
- MongoDB Atlas: As the cloud database service where the production and test databases are hosted.

#### *Usage*
This module is used across the application to:
- Initialize database connections with the correct URI based on the operational mode.
- Enable separation of test data from production data by toggling the `TEST_MODE` flag, ensuring that tests do not interfere with live data.

The `Config` module is essential for both development and deployment phases of the application, providing flexibility in switching between different operational modes and databases. It is particularly useful in scenarios that require a clear separation between production and testing environments, such as continuous integration/continuous deployment (CI/CD) pipelines, automated testing, and staging environments.
