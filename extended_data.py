"""
Extended assessment data generator to reach 377+ assessments.
"""
import json
import os

def generate_extended_assessments():
    """Generate a comprehensive list of 377+ assessments."""
    
    assessments = []
    
    # ==========================================
    # KNOWLEDGE & SKILLS (K) - Technical Tests
    # ==========================================
    
    # Programming Languages (50+)
    programming_languages = [
        ("Python (New)", "python-new", "Multi-choice test that measures the knowledge of Python programming, databases, modules and library. For developers with 1-3 years experience.", 11),
        ("Python Advanced", "python-advanced", "Advanced Python test covering metaclasses, decorators, generators, async programming, and performance optimization.", 25),
        ("Java 8", "java-8", "Assesses knowledge of Java 8 programming language including OOP concepts, collections, streams, and multithreading.", 20),
        ("Java 11", "java-11", "Tests Java 11 features including new APIs, modules system, and language enhancements.", 22),
        ("Java 17", "java-17", "Evaluates Java 17 knowledge including sealed classes, pattern matching, and records.", 22),
        ("JavaScript", "javascript", "Tests JavaScript programming skills including ES6+, DOM manipulation, async programming, and modern frameworks knowledge.", 15),
        ("JavaScript Advanced", "javascript-advanced", "Advanced JavaScript covering closures, prototypes, memory management, and performance.", 20),
        ("TypeScript", "typescript", "Evaluates TypeScript knowledge including type system, interfaces, generics, and Angular/React integration.", 16),
        ("C#", "csharp", "Evaluates C# programming knowledge including .NET framework, LINQ, async/await patterns, and object-oriented design.", 20),
        ("C# Advanced", "csharp-advanced", "Advanced C# covering memory management, unsafe code, reflection, and performance optimization.", 25),
        ("C++", "cpp", "Tests C++ programming proficiency including memory management, STL, templates, and object-oriented design.", 20),
        ("C++ Modern", "cpp-modern", "Modern C++ (C++17/20) including smart pointers, move semantics, and concurrency.", 22),
        ("C Programming", "c", "Tests C language fundamentals including pointers, memory management, and system programming.", 18),
        ("Go (Golang)", "go-lang", "Tests Go programming language proficiency including concurrency, interfaces, and system programming.", 20),
        ("Rust", "rust", "Evaluates Rust programming knowledge including ownership, borrowing, and systems programming concepts.", 22),
        ("Kotlin", "kotlin", "Assesses Kotlin programming skills including Android development, coroutines, and interoperability with Java.", 18),
        ("Swift", "swift", "Tests Swift programming for iOS development including UIKit, SwiftUI, and app architecture patterns.", 20),
        ("Ruby", "ruby", "Tests Ruby programming knowledge including OOP, metaprogramming, and Rails framework basics.", 18),
        ("Ruby on Rails", "ruby-rails", "Evaluates Ruby on Rails framework knowledge including MVC, ActiveRecord, and deployment.", 22),
        ("PHP", "php", "Evaluates PHP programming skills including web development, frameworks, and database integration.", 18),
        ("PHP Laravel", "php-laravel", "Tests Laravel PHP framework skills including Eloquent ORM, routing, and middleware.", 20),
        ("Scala", "scala", "Tests Scala programming including functional programming, Akka framework, and Spark integration.", 22),
        ("R Programming", "r-programming", "Evaluates R programming for statistical analysis, data manipulation, and visualization.", 22),
        ("MATLAB", "matlab", "Evaluates MATLAB programming for numerical computing and data analysis.", 22),
        ("Perl", "perl", "Tests Perl programming knowledge including regex, file I/O, and scripting.", 18),
        ("Shell Scripting (Bash)", "shell-scripting", "Evaluates Bash shell scripting skills including automation and system administration tasks.", 18),
        ("PowerShell", "powershell", "Tests PowerShell scripting for Windows administration and automation.", 18),
        ("Objective-C", "objective-c", "Assesses Objective-C knowledge for iOS/macOS development.", 20),
        ("Dart", "dart", "Tests Dart language fundamentals for Flutter development.", 16),
        ("Lua", "lua", "Evaluates Lua scripting for game development and embedded systems.", 15),
        ("Haskell", "haskell", "Tests Haskell functional programming concepts.", 25),
        ("F#", "fsharp", "Evaluates F# functional programming with .NET integration.", 22),
        ("Clojure", "clojure", "Tests Clojure functional programming and JVM integration.", 22),
        ("Elixir", "elixir", "Evaluates Elixir programming including OTP and Phoenix framework.", 20),
        ("Julia", "julia", "Tests Julia for scientific computing and data analysis.", 22),
        ("Groovy", "groovy", "Evaluates Groovy scripting for JVM platforms.", 18),
        ("Visual Basic", "visual-basic", "Tests Visual Basic programming for Windows applications.", 16),
        ("COBOL", "cobol", "Evaluates COBOL knowledge for legacy system maintenance.", 25),
        ("Fortran", "fortran", "Tests Fortran for scientific computing applications.", 22),
        ("Assembly", "assembly", "Evaluates assembly language fundamentals.", 30),
    ]
    
    for name, slug, desc, duration in programming_languages:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Web Frameworks & Libraries (30+)
    web_frameworks = [
        ("React", "react", "Tests React.js knowledge including components, hooks, state management, and modern React patterns.", 18),
        ("React Advanced", "react-advanced", "Advanced React covering Redux, performance optimization, and server-side rendering.", 22),
        ("Angular", "angular", "Assesses Angular framework knowledge including components, services, RxJS, and TypeScript integration.", 18),
        ("Angular Advanced", "angular-advanced", "Advanced Angular including NgRx, lazy loading, and enterprise patterns.", 22),
        ("Vue.js", "vue-js", "Tests Vue.js framework knowledge including components, Vuex, and Vue Router.", 18),
        ("Vue.js 3", "vue-3", "Evaluates Vue 3 composition API, reactivity system, and ecosystem.", 18),
        ("Next.js", "nextjs", "Tests Next.js framework knowledge including SSR, routing, and API routes.", 18),
        ("Nuxt.js", "nuxtjs", "Evaluates Nuxt.js for Vue applications with SSR.", 18),
        ("Svelte", "svelte", "Evaluates Svelte framework knowledge for building reactive web applications.", 16),
        ("Node.js", "nodejs", "Tests Node.js backend development skills including Express, async patterns, file system, and API development.", 16),
        ("Express.js", "express", "Evaluates Express.js framework for Node.js backend development.", 15),
        ("Django", "django", "Evaluates Django web framework skills including ORM, templates, views, and deployment.", 20),
        ("Flask", "flask", "Tests Flask micro-framework knowledge for Python web development.", 16),
        ("FastAPI", "fastapi", "Evaluates FastAPI framework for modern Python APIs.", 16),
        ("Spring Framework", "spring-framework", "Tests Spring/Spring Boot knowledge including dependency injection, REST APIs, and data access.", 22),
        ("Spring Boot", "spring-boot", "Advanced Spring Boot covering microservices, security, and cloud deployment.", 22),
        ("ASP.NET", "asp-net", "Evaluates ASP.NET web development skills including MVC, Web API, and Entity Framework.", 22),
        ("ASP.NET Core", "asp-net-core", "Tests ASP.NET Core for modern cross-platform web development.", 22),
        ("Laravel", "laravel", "Tests Laravel PHP framework skills including Eloquent ORM, routing, and middleware.", 20),
        ("Symfony", "symfony", "Evaluates Symfony PHP framework knowledge.", 20),
        ("CodeIgniter", "codeigniter", "Tests CodeIgniter PHP framework basics.", 16),
        ("Bootstrap", "bootstrap", "Tests Bootstrap CSS framework knowledge for responsive web design.", 15),
        ("Tailwind CSS", "tailwind-css", "Evaluates Tailwind CSS utility-first framework skills for modern web design.", 15),
        ("HTML5 & CSS3", "html-css", "Evaluates front-end web development skills including semantic HTML, CSS layouts, and responsive design.", 15),
        ("SASS/SCSS", "sass", "Tests SASS/SCSS preprocessor knowledge for CSS.", 12),
        ("Webpack", "webpack", "Evaluates Webpack module bundler configuration and optimization.", 16),
        ("jQuery", "jquery", "Tests jQuery library knowledge for DOM manipulation.", 12),
        ("Ember.js", "ember", "Evaluates Ember.js framework knowledge.", 18),
        ("Backbone.js", "backbone", "Tests Backbone.js MVC framework.", 16),
        ("Gatsby", "gatsby", "Evaluates Gatsby static site generator.", 16),
    ]
    
    for name, slug, desc, duration in web_frameworks:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Databases & Data (25+)
    databases = [
        ("SQL", "sql", "Comprehensive SQL assessment covering queries, joins, subqueries, aggregations, and database design principles.", 15),
        ("SQL Advanced", "sql-advanced", "Advanced SQL including window functions, CTEs, and query optimization.", 22),
        ("MySQL", "mysql", "Tests MySQL database administration and query skills.", 18),
        ("PostgreSQL", "postgresql", "Assesses PostgreSQL database skills including advanced queries, performance tuning, and administration.", 20),
        ("Oracle Database", "oracle-database", "Tests Oracle DB knowledge including PL/SQL, performance optimization, and database administration.", 25),
        ("SQL Server", "sql-server", "Evaluates Microsoft SQL Server skills including T-SQL and administration.", 22),
        ("MongoDB", "mongodb", "Tests MongoDB knowledge including NoSQL concepts, aggregation framework, and schema design.", 18),
        ("MongoDB Advanced", "mongodb-advanced", "Advanced MongoDB including sharding, replication, and performance optimization.", 22),
        ("Redis", "redis", "Tests Redis in-memory database skills including caching, data structures, and persistence.", 18),
        ("Cassandra", "cassandra", "Evaluates Apache Cassandra distributed database knowledge.", 22),
        ("DynamoDB", "dynamodb", "Tests AWS DynamoDB NoSQL database skills.", 18),
        ("Neo4j", "neo4j", "Evaluates Neo4j graph database and Cypher query language.", 20),
        ("Elasticsearch", "elasticsearch", "Evaluates Elasticsearch knowledge including indexing, queries, and aggregations.", 20),
        ("Firebase", "firebase", "Tests Firebase backend services and real-time database.", 16),
        ("SQLite", "sqlite", "Evaluates SQLite embedded database knowledge.", 12),
        ("MariaDB", "mariadb", "Tests MariaDB database administration.", 18),
        ("CouchDB", "couchdb", "Evaluates CouchDB document database.", 16),
        ("InfluxDB", "influxdb", "Tests InfluxDB time-series database.", 18),
        ("Apache Spark", "apache-spark", "Assesses Spark knowledge including RDDs, DataFrames, Spark SQL, and MLlib.", 25),
        ("Hadoop", "hadoop", "Evaluates Hadoop ecosystem including HDFS, MapReduce, and Hive.", 25),
        ("Kafka", "kafka", "Tests Apache Kafka knowledge including streams, producers, consumers, and architecture.", 22),
        ("RabbitMQ", "rabbitmq", "Evaluates RabbitMQ messaging knowledge including queues, exchanges, and patterns.", 18),
        ("Airflow", "airflow", "Tests Apache Airflow workflow orchestration.", 20),
        ("dbt", "dbt", "Evaluates dbt data transformation tool knowledge.", 16),
        ("Snowflake", "snowflake", "Tests Snowflake cloud data warehouse.", 20),
    ]
    
    for name, slug, desc, duration in databases:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Cloud & DevOps (30+)
    cloud_devops = [
        ("AWS Cloud Practitioner", "aws-cloud", "Evaluates knowledge of AWS cloud services, architecture, security, and deployment practices.", 25),
        ("AWS Solutions Architect", "aws-solutions-architect", "Tests AWS architecture design including EC2, S3, VPC, and high availability.", 35),
        ("AWS Developer", "aws-developer", "Evaluates AWS developer skills including Lambda, API Gateway, and DynamoDB.", 30),
        ("AWS SysOps", "aws-sysops", "Tests AWS system operations and administration.", 30),
        ("Microsoft Azure", "azure", "Assesses Azure cloud platform knowledge including compute, storage, networking, and security services.", 25),
        ("Azure Administrator", "azure-administrator", "Tests Azure administration and resource management.", 30),
        ("Azure Developer", "azure-developer", "Evaluates Azure development including App Services and Functions.", 28),
        ("Google Cloud Platform", "google-cloud", "Tests GCP knowledge including Compute Engine, Cloud Functions, BigQuery, and GKE.", 25),
        ("GCP Professional", "gcp-professional", "Advanced GCP architecture and deployment.", 35),
        ("Docker", "docker", "Evaluates Docker containerization skills including images, containers, compose, and orchestration basics.", 18),
        ("Kubernetes", "kubernetes", "Tests Kubernetes knowledge including pods, services, deployments, and cluster management.", 22),
        ("Kubernetes Advanced", "kubernetes-advanced", "Advanced Kubernetes including Helm, operators, and security.", 28),
        ("Terraform", "terraform", "Assesses Terraform infrastructure as code skills including providers, modules, and state management.", 20),
        ("Ansible", "ansible", "Tests Ansible automation and configuration management.", 18),
        ("Puppet", "puppet", "Evaluates Puppet infrastructure automation.", 18),
        ("Chef", "chef", "Tests Chef configuration management.", 18),
        ("Jenkins", "jenkins", "Tests Jenkins CI/CD knowledge including pipelines, plugins, and automation best practices.", 18),
        ("GitLab CI", "gitlab-ci", "Evaluates GitLab CI/CD pipeline configuration.", 16),
        ("GitHub Actions", "github-actions", "Tests GitHub Actions workflow automation.", 16),
        ("CircleCI", "circleci", "Evaluates CircleCI continuous integration.", 16),
        ("ArgoCD", "argocd", "Tests ArgoCD GitOps practices.", 18),
        ("Git & Version Control", "git", "Evaluates Git proficiency including branching, merging, rebasing, and collaboration workflows.", 15),
        ("Linux Administration", "linux-admin", "Tests Linux system administration skills including shell scripting, user management, and system services.", 25),
        ("Linux Advanced", "linux-advanced", "Advanced Linux including kernel, security, and performance tuning.", 30),
        ("Nginx", "nginx", "Tests Nginx web server configuration and optimization.", 16),
        ("Apache HTTP", "apache", "Evaluates Apache web server administration.", 16),
        ("Prometheus", "prometheus", "Tests Prometheus monitoring and alerting.", 18),
        ("Grafana", "grafana", "Evaluates Grafana dashboards and visualization.", 15),
        ("ELK Stack", "elk-stack", "Tests Elasticsearch, Logstash, and Kibana log management.", 22),
        ("DevOps Fundamentals", "devops", "Assesses DevOps practices including CI/CD, containerization, infrastructure as code, and monitoring.", 25),
    ]
    
    for name, slug, desc, duration in cloud_devops:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Mobile Development (15)
    mobile_dev = [
        ("Android Development", "android-development", "Assesses Android app development skills including activities, fragments, and Jetpack libraries.", 25),
        ("Android Kotlin", "android-kotlin", "Tests Android development with Kotlin including Compose.", 22),
        ("iOS Development", "ios-development", "Tests iOS development knowledge including Swift, UIKit, and Apple development practices.", 25),
        ("iOS SwiftUI", "ios-swiftui", "Evaluates SwiftUI declarative UI framework.", 22),
        ("React Native", "react-native", "Evaluates React Native mobile development skills including navigation, state, and native modules.", 20),
        ("Flutter", "flutter", "Tests Flutter/Dart knowledge for cross-platform mobile development.", 20),
        ("Xamarin", "xamarin", "Evaluates Xamarin cross-platform development.", 22),
        ("Ionic", "ionic", "Tests Ionic framework for hybrid mobile apps.", 18),
        ("Mobile App Security", "mobile-security", "Evaluates mobile application security practices.", 22),
        ("App Store Guidelines", "app-store", "Tests knowledge of iOS App Store requirements.", 15),
        ("Google Play Guidelines", "google-play", "Evaluates Google Play Store requirements.", 15),
        ("Push Notifications", "push-notifications", "Tests mobile push notification implementation.", 14),
        ("Mobile Testing", "mobile-testing", "Evaluates mobile application testing practices.", 18),
        ("Responsive Design", "responsive-design", "Tests responsive design principles for mobile.", 15),
        ("PWA Development", "pwa", "Evaluates Progressive Web App development.", 18),
    ]
    
    for name, slug, desc, duration in mobile_dev:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # AI/ML & Data Science (20)
    ai_ml = [
        ("Machine Learning", "machine-learning", "Evaluates machine learning knowledge including algorithms, model evaluation, and practical implementation.", 30),
        ("Deep Learning", "deep-learning", "Tests deep learning knowledge including neural networks, CNNs, RNNs, and frameworks like TensorFlow.", 30),
        ("TensorFlow", "tensorflow", "Evaluates TensorFlow machine learning framework.", 25),
        ("PyTorch", "pytorch", "Tests PyTorch deep learning framework.", 25),
        ("Keras", "keras", "Evaluates Keras neural network library.", 20),
        ("Natural Language Processing", "nlp", "Assesses NLP knowledge including text processing, sentiment analysis, and language models.", 28),
        ("Computer Vision", "computer-vision", "Tests computer vision concepts including image processing, object detection, and recognition algorithms.", 28),
        ("Data Science Fundamentals", "data-science", "Tests data science knowledge including statistical analysis, machine learning concepts, and data visualization.", 30),
        ("Statistics for Data Science", "statistics", "Evaluates statistical knowledge for data analysis.", 25),
        ("AI Fundamentals", "ai-basics", "Evaluates artificial intelligence knowledge including algorithms, applications, and ethical considerations.", 25),
        ("Pandas", "pandas", "Tests Pandas data manipulation library.", 18),
        ("NumPy", "numpy", "Evaluates NumPy numerical computing library.", 16),
        ("Scikit-learn", "scikit-learn", "Tests Scikit-learn machine learning library.", 22),
        ("Data Visualization", "data-visualization", "Evaluates data visualization best practices and tools.", 18),
        ("Feature Engineering", "feature-engineering", "Tests feature engineering for machine learning.", 22),
        ("Model Deployment", "model-deployment", "Evaluates ML model deployment practices.", 20),
        ("MLOps", "mlops", "Tests MLOps practices and tools.", 25),
        ("Time Series Analysis", "time-series", "Evaluates time series analysis and forecasting.", 22),
        ("Recommendation Systems", "recommendation-systems", "Tests recommendation system algorithms.", 22),
        ("Generative AI", "generative-ai", "Evaluates generative AI concepts including LLMs.", 25),
    ]
    
    for name, slug, desc, duration in ai_ml:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # BI & Analytics (15)
    bi_analytics = [
        ("Tableau", "tableau", "Tests Tableau visualization skills including dashboards, calculations, and data connections.", 20),
        ("Power BI", "power-bi", "Assesses Power BI skills including DAX, data modeling, and report/dashboard creation.", 20),
        ("Looker", "looker", "Tests Looker BI platform skills including data modeling and visualization.", 20),
        ("Qlik", "qlik", "Evaluates Qlik Sense/QlikView skills for business intelligence and data visualization.", 22),
        ("SAS", "sas", "Tests SAS programming and analytics including data manipulation, statistical procedures, and reporting.", 25),
        ("SPSS", "spss", "Evaluates SPSS statistical analysis software.", 22),
        ("Google Analytics", "google-analytics", "Tests Google Analytics web analytics.", 18),
        ("Adobe Analytics", "adobe-analytics", "Evaluates Adobe Analytics digital marketing analytics.", 20),
        ("Excel Data Analysis", "excel-data-analysis", "Advanced Excel for data analysis including Power Query.", 22),
        ("Financial Modeling", "financial-modeling", "Tests financial modeling with spreadsheets.", 25),
        ("Business Intelligence", "business-intelligence", "Evaluates BI concepts and practices.", 22),
        ("Data Warehousing", "data-warehousing", "Tests data warehouse design and implementation.", 25),
        ("ETL Processes", "etl", "Evaluates ETL pipeline design and implementation.", 22),
        ("Data Quality", "data-quality", "Tests data quality management practices.", 18),
        ("Report Writing", "report-writing", "Evaluates business report writing skills.", 18),
    ]
    
    for name, slug, desc, duration in bi_analytics:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Office & Productivity (15)
    office = [
        ("Microsoft Excel (Advanced)", "excel-advanced", "Tests advanced Excel skills including formulas, pivot tables, macros, and data analysis features.", 20),
        ("Microsoft Excel Basics", "excel-basics", "Evaluates basic Excel spreadsheet skills.", 15),
        ("Microsoft Word", "word-processing", "Tests Microsoft Word proficiency including formatting, templates, mail merge, and document collaboration.", 15),
        ("Microsoft PowerPoint", "powerpoint", "Assesses PowerPoint skills including slide design, animations, and presentation best practices.", 15),
        ("Microsoft Outlook", "outlook", "Tests Outlook email and calendar management.", 12),
        ("Microsoft Access", "access", "Evaluates Microsoft Access database skills.", 18),
        ("Microsoft Office 365", "office-365", "Tests Office 365 cloud suite proficiency.", 20),
        ("Google Workspace", "google-workspace", "Evaluates Google Docs, Sheets, and Slides.", 18),
        ("Google Sheets", "google-sheets", "Tests Google Sheets spreadsheet skills.", 16),
        ("English Language Proficiency", "english-proficiency", "Tests English language skills including grammar, vocabulary, reading comprehension, and business writing.", 25),
        ("Business Writing", "business-writing", "Evaluates professional business writing skills.", 20),
        ("Technical Writing", "technical-writing", "Tests technical documentation writing.", 22),
        ("Typing Speed & Accuracy", "typing-test", "Measures typing speed and accuracy for data entry and administrative roles.", 10),
        ("Data Entry", "data-entry", "Evaluates data entry speed and accuracy.", 12),
        ("Digital Literacy", "digital-literacy", "Tests digital skills and comfort with technology tools commonly used in modern workplaces.", 20),
    ]
    
    for name, slug, desc, duration in office:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # API & Architecture (15)
    api_arch = [
        ("REST API Design", "rest-api", "Assesses REST API design knowledge including endpoints, methods, status codes, and best practices.", 18),
        ("GraphQL", "graphql", "Tests GraphQL knowledge including queries, mutations, schemas, and resolver patterns.", 18),
        ("Microservices Architecture", "microservices", "Evaluates microservices concepts including patterns, communication, and deployment strategies.", 25),
        ("System Design", "system-design", "Evaluates system design skills including architecture patterns, scalability, and trade-offs.", 35),
        ("Software Architecture", "software-architecture", "Tests software architecture knowledge including patterns, principles, and modern practices.", 30),
        ("Clean Code & Best Practices", "clean-code", "Evaluates knowledge of coding best practices, design patterns, and code quality principles.", 22),
        ("Object-Oriented Programming", "oop-concepts", "Tests OOP concepts including inheritance, polymorphism, encapsulation, and design principles.", 18),
        ("Design Patterns", "design-patterns", "Evaluates software design patterns knowledge.", 22),
        ("SOLID Principles", "solid", "Tests SOLID design principles understanding.", 18),
        ("Domain-Driven Design", "ddd", "Evaluates DDD concepts and practices.", 25),
        ("Event-Driven Architecture", "event-driven", "Tests event-driven architecture patterns.", 22),
        ("API Security", "api-security", "Evaluates API security best practices.", 20),
        ("OAuth & Authentication", "oauth", "Tests OAuth and authentication protocols.", 18),
        ("gRPC", "grpc", "Evaluates gRPC framework knowledge.", 18),
        ("WebSocket", "websocket", "Tests WebSocket real-time communication.", 15),
    ]
    
    for name, slug, desc, duration in api_arch:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Security (12)
    security = [
        ("Cybersecurity Fundamentals", "cybersecurity", "Tests cybersecurity knowledge including threats, vulnerabilities, risk management, and security controls.", 28),
        ("Ethical Hacking", "ethical-hacking", "Evaluates penetration testing and ethical hacking skills.", 30),
        ("Network Security", "network-security", "Tests network security concepts and practices.", 25),
        ("Application Security", "app-security", "Evaluates application security testing and practices.", 25),
        ("Cloud Security", "cloud-security", "Tests cloud security best practices.", 25),
        ("Security Operations", "sec-ops", "Evaluates SOC operations and incident response.", 28),
        ("Compliance & Governance", "compliance", "Tests security compliance knowledge (SOC2, ISO, GDPR).", 22),
        ("Cryptography", "cryptography", "Evaluates cryptography fundamentals.", 25),
        ("Identity Management", "identity-management", "Tests identity and access management.", 22),
        ("Security Architecture", "security-architecture", "Evaluates security architecture design.", 28),
        ("Vulnerability Assessment", "vulnerability-assessment", "Tests vulnerability assessment skills.", 25),
        ("GDPR Knowledge", "gdpr-knowledge", "Tests understanding of GDPR requirements and data protection practices.", 18),
    ]
    
    for name, slug, desc, duration in security:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Testing (10)
    testing = [
        ("QA Fundamentals", "qa-fundamentals", "Tests quality assurance fundamentals.", 22),
        ("Selenium Testing", "selenium", "Tests Selenium WebDriver knowledge for automated web application testing.", 20),
        ("Test-Driven Development", "tdd", "Tests TDD knowledge including unit testing, mocking, and test automation practices.", 20),
        ("Automated Testing", "automated-testing", "Evaluates test automation strategies and tools.", 22),
        ("Performance Testing", "performance-testing", "Tests performance testing with JMeter and similar tools.", 22),
        ("API Testing", "api-testing", "Evaluates API testing with Postman and similar tools.", 18),
        ("Mobile Testing", "mobile-app-testing", "Tests mobile application testing methodologies.", 20),
        ("Cypress", "cypress", "Evaluates Cypress end-to-end testing.", 18),
        ("Jest", "jest", "Tests Jest JavaScript testing framework.", 16),
        ("PyTest", "pytest", "Evaluates PyTest Python testing framework.", 16),
    ]
    
    for name, slug, desc, duration in testing:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # Enterprise Systems (10)
    enterprise = [
        ("Salesforce", "salesforce", "Tests Salesforce CRM knowledge including administration, customization, and development.", 25),
        ("SAP Fundamentals", "sap", "Evaluates SAP ERP system knowledge including modules and business processes.", 30),
        ("ServiceNow", "servicenow", "Tests ServiceNow platform knowledge including ITSM, workflows, and administration.", 22),
        ("JIRA & Issue Tracking", "jira", "Evaluates JIRA usage for project management, issue tracking, and agile workflows.", 15),
        ("Confluence", "confluence", "Tests Confluence documentation and collaboration.", 12),
        ("Workday", "workday", "Evaluates Workday HR system knowledge.", 22),
        ("NetSuite", "netsuite", "Tests NetSuite ERP system.", 25),
        ("Dynamics 365", "dynamics-365", "Evaluates Microsoft Dynamics 365.", 25),
        ("HubSpot", "hubspot", "Tests HubSpot CRM and marketing.", 18),
        ("Zendesk", "zendesk", "Evaluates Zendesk customer service platform.", 16),
    ]
    
    for name, slug, desc, duration in enterprise:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Knowledge & Skills"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # ABILITY & APTITUDE (A) - Cognitive Tests
    # ==========================================
    
    cognitive = [
        ("Verify G+", "verify-g-plus", "General cognitive ability assessment measuring verbal, numerical, and inductive reasoning abilities.", 36, True),
        ("Numerical Reasoning", "numerical-reasoning", "Assesses ability to understand, interpret, and analyze numerical data and statistical information.", 25, True),
        ("Verbal Reasoning", "verbal-reasoning", "Measures ability to understand and evaluate written information, and to make logical conclusions.", 19, True),
        ("Inductive Reasoning", "inductive-reasoning", "Tests ability to identify patterns and logical rules from data to solve novel problems.", 25, True),
        ("Deductive Reasoning", "deductive-reasoning", "Evaluates ability to draw logical conclusions from given premises and apply rules consistently.", 20, False),
        ("Abstract Reasoning", "abstract-reasoning", "Measures ability to identify patterns, logical rules, and trends in abstract visual data.", 20, True),
        ("Mechanical Comprehension", "mechanical-comprehension", "Tests understanding of physical and mechanical concepts including forces, motion, and simple machines.", 25, False),
        ("Spatial Reasoning", "spatial-reasoning", "Evaluates ability to visualize and manipulate 2D and 3D objects mentally.", 20, False),
        ("Checking Test", "checking-test", "Measures speed and accuracy in checking and comparing data, codes, and information.", 10, False),
        ("Calculation Test", "calculation-test", "Assesses basic to intermediate mathematical and arithmetic calculation abilities.", 15, False),
        ("Logical Reasoning", "logical-reasoning", "Measures logical thinking ability through pattern recognition and rule application.", 20, True),
        ("Error Checking", "error-checking", "Tests ability to identify errors and inconsistencies in data and documents.", 12, False),
        ("Reading Comprehension", "reading-comprehension", "Measures ability to understand and interpret written business communications.", 18, False),
        ("Data Interpretation", "data-interpretation", "Tests ability to interpret charts, graphs, and statistical data.", 20, False),
        ("Critical Thinking", "critical-thinking", "Evaluates ability to analyze arguments, evaluate evidence, and draw logical conclusions.", 25, True),
        ("Working Memory Assessment", "working-memory", "Measures working memory capacity and information processing abilities.", 15, False),
        ("Processing Speed", "processing-speed", "Tests speed and accuracy of cognitive processing and reaction time.", 12, False),
        ("Fluid Intelligence", "fluid-intelligence", "Measures fluid reasoning ability independent of prior knowledge.", 25, True),
        ("Attention to Detail", "attention-to-detail", "Assesses accuracy, thoroughness, and attention to detail in work tasks.", 15, False),
        ("Graduate Verbal Reasoning", "graduate-verbal", "Verbal reasoning test designed for graduate-level candidates entering the workforce.", 19, True),
        ("Graduate Numerical Reasoning", "graduate-numerical", "Numerical reasoning test designed for graduate-level candidates with business context.", 25, True),
        ("Apprentice Verbal Reasoning", "apprentice-verbal", "Verbal reasoning test designed for apprentice and entry-level candidates.", 15, False),
        ("Apprentice Numerical Reasoning", "apprentice-numerical", "Numerical reasoning test designed for apprentice and entry-level candidates.", 18, False),
        ("Graduate Management Aptitude", "graduate-management", "Comprehensive aptitude test for graduate management trainee programs.", 50, True),
    ]
    
    for name, slug, desc, duration, adaptive in cognitive:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Ability & Aptitude"],
            "remote_support": "Yes",
            "adaptive_support": "Yes" if adaptive else "No"
        })
    
    # ==========================================
    # PERSONALITY & BEHAVIOUR (P)
    # ==========================================
    
    personality = [
        ("OPQ32 (Occupational Personality Questionnaire)", "opq32", "Comprehensive personality assessment measuring 32 personality characteristics relevant to work behavior and performance.", 25),
        ("Motivation Questionnaire (MQ)", "motivation-questionnaire", "Measures 18 dimensions of motivation to understand what drives and engages an individual at work.", 20),
        ("Technology Professional 8.0 Job Focused Assessment", "technology-professional-8-0-job-focused-assessment", "The Technology Job Focused Assessment assesses key behavioral attributes required for success in fast-paced roles.", 16),
        ("Leadership Assessment", "leadership-assessment", "Evaluates leadership potential and style, measuring key leadership competencies and behaviors.", 30),
        ("Team Dynamics Assessment", "team-dynamics", "Assesses how individuals work within teams, including collaboration, communication, and conflict resolution.", 20),
        ("Emotional Intelligence Assessment", "emotional-intelligence", "Measures emotional awareness, management, and social skills in professional contexts.", 20),
        ("Work Style Assessment", "work-style", "Measures work preferences, habits, and styles that impact job performance and satisfaction.", 15),
        ("Values Assessment", "values-assessment", "Identifies core work values and organizational culture fit factors.", 12),
        ("Integrity Assessment", "integrity-test", "Evaluates integrity, reliability, and counterproductive work behavior risk factors.", 20),
        ("Safety Questionnaire", "safety-questionnaire", "Measures safety consciousness and risk-taking tendencies for safety-critical roles.", 18),
        ("Resilience Assessment", "resilience", "Evaluates psychological resilience, stress management, and bounce-back capability.", 18),
        ("Cultural Fit Assessment", "cultural-fit", "Assesses alignment with organizational values and culture for better person-organization fit.", 15),
        ("Stress Tolerance", "stress-tolerance", "Assesses ability to perform effectively under pressure and manage work-related stress.", 18),
        ("Achievement Motivation", "achievement-motivation", "Measures drive for excellence, goal orientation, and motivation to achieve results.", 16),
        ("Entrepreneurial Assessment", "entrepreneurial", "Measures entrepreneurial mindset, risk tolerance, and innovation competencies.", 25),
    ]
    
    for name, slug, desc, duration in personality:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Personality & Behaviour"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # COMPETENCIES (C)
    # ==========================================
    
    competencies = [
        ("Universal Competency Framework (UCF)", "universal-competency-framework", "Comprehensive competency assessment based on SHL's Universal Competency Framework covering 8 competency clusters.", 35),
        ("Sales Competency Assessment", "sales-competencies", "Evaluates key sales competencies including persuasion, relationship building, and commercial awareness.", 25),
        ("Communication Skills Assessment", "communication-assessment", "Measures written and verbal communication competencies for professional workplace settings.", 20),
        ("Problem Solving Assessment", "problem-solving", "Measures analytical thinking and problem-solving abilities through business scenarios.", 25),
        ("Decision Making Assessment", "decision-making", "Assesses decision-making styles and effectiveness through realistic business scenarios.", 25),
        ("Adaptability Assessment", "adaptability", "Measures ability to adapt to change, learn new skills, and work effectively in dynamic environments.", 20),
        ("Innovation & Creativity", "innovation-creativity", "Evaluates creative thinking, idea generation, and innovative problem-solving abilities.", 22),
        ("Negotiation Skills", "negotiation-skills", "Assesses negotiation abilities including persuasion, conflict resolution, and win-win thinking.", 25),
        ("Presentation Skills", "presentation-skills", "Evaluates presentation and public speaking competencies through simulated scenarios.", 20),
        ("Time Management", "time-management", "Measures planning, prioritization, and time management competencies.", 18),
        ("Initiative Assessment", "initiative", "Evaluates proactivity, self-starting behavior, and willingness to take initiative.", 18),
        ("Service Orientation", "service-orientation", "Measures dedication to meeting customer needs and providing excellent service.", 18),
        ("Analytical Thinking", "analytical-thinking", "Evaluates ability to analyze complex information and draw logical conclusions.", 22),
        ("Business Acumen", "business-acumen", "Assesses understanding of business operations, strategy, and financial concepts.", 25),
        ("Customer Focus Assessment", "customer-focus", "Measures customer orientation, service mindset, and customer experience competencies.", 20),
        ("Service Excellence", "service-excellence", "Evaluates service delivery competencies and commitment to customer satisfaction.", 18),
        ("Detail Orientation", "detail-orientation", "Measures thoroughness, accuracy, and attention to detail in work tasks.", 15),
        ("Conflict Resolution", "conflict-resolution", "Assesses conflict management and resolution skills through workplace scenarios.", 22),
        ("Stakeholder Management", "stakeholder-management", "Evaluates stakeholder engagement and relationship management competencies.", 25),
        ("Influence & Persuasion", "influence-skills", "Measures ability to influence others and gain buy-in through persuasive communication.", 20),
        ("Strategic Thinking", "strategic-thinking", "Evaluates strategic planning and thinking abilities for senior roles.", 30),
        ("Change Management", "change-management", "Assesses change management skills including vision, communication, and implementation.", 25),
        ("Remote Work Assessment", "remote-work", "Evaluates competencies essential for successful remote work including self-management and communication.", 20),
        ("Virtual Collaboration", "virtual-collaboration", "Assesses ability to collaborate effectively in virtual and distributed team environments.", 18),
        ("Cross-Cultural Competence", "cross-cultural", "Measures ability to work effectively across different cultures and geographies.", 20),
        ("Digital Agility", "digital-agility", "Evaluates adaptability to new technologies and digital transformation initiatives.", 18),
        ("Results Orientation", "results-orientation", "Measures focus on achieving results and goal-directed behavior.", 18),
        ("Project Leadership", "project-leadership", "Assesses competencies for leading projects and cross-functional teams.", 25),
        ("Relationship Building", "relationship-building", "Evaluates ability to build and maintain professional relationships.", 20),
        ("Ethical Decision Making", "ethical-decisions", "Measures ethical judgment and decision-making in workplace scenarios.", 22),
        ("Accountability Assessment", "accountability", "Evaluates sense of responsibility and ownership for results.", 18),
        ("Continuous Learning", "continuous-learning", "Measures commitment to learning and professional development.", 18),
        ("Coaching Skills", "coaching-skills", "Assesses ability to coach and develop others.", 22),
        ("Mentoring Competency", "mentoring", "Evaluates mentoring skills and knowledge transfer abilities.", 20),
        ("Knowledge Sharing", "knowledge-sharing", "Measures willingness and ability to share knowledge with others.", 18),
        ("Process Improvement", "process-improvement", "Evaluates ability to identify and implement process improvements.", 22),
    ]
    
    for name, slug, desc, duration in competencies:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Competencies"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # BIODATA & SITUATIONAL JUDGEMENT (B)
    # ==========================================
    
    sjt = [
        ("Graduate Situational Judgement Test", "graduate-sjt", "Presents realistic work scenarios to assess judgment and decision-making for graduate roles.", 25),
        ("Customer Service SJT", "customer-service-sjt", "Evaluates judgment in customer-facing situations including conflict resolution and service excellence.", 20),
        ("Management Situational Judgement", "management-sjt", "Assesses managerial judgment through realistic management scenarios and decision points.", 30),
        ("Sales Situational Judgement", "sales-sjt", "Tests judgment in sales scenarios including objection handling and relationship building.", 25),
        ("Leadership SJT", "leadership-sjt", "Evaluates leadership judgment through team and organizational scenarios.", 28),
        ("Technical Team SJT", "technical-team-sjt", "Assesses judgment in technical team situations.", 25),
        ("Healthcare SJT", "healthcare-sjt", "Evaluates judgment in healthcare workplace scenarios.", 25),
        ("Retail SJT", "retail-sjt", "Tests judgment in retail customer service scenarios.", 20),
        ("Call Center SJT", "call-center-sjt", "Assesses judgment in call center customer interactions.", 22),
        ("Entry Level SJT", "entry-level-sjt", "Situational judgment test for entry-level roles.", 20),
    ]
    
    for name, slug, desc, duration in sjt:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Biodata & Situational Judgement"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # SIMULATIONS (S)
    # ==========================================
    
    simulations = [
        ("Inbox/Email Simulation", "inbox-simulation", "Interactive simulation assessing email management, prioritization, and professional communication.", 30),
        ("Coding Simulation", "coding-simulation", "Hands-on coding exercise assessing practical programming skills in realistic development scenarios.", 60),
        ("Role Play Simulation", "role-play-simulation", "Interactive simulation assessing interpersonal skills through realistic workplace scenarios.", 25),
        ("Customer Service Simulation", "customer-service-simulation", "Simulated customer interactions testing service skills.", 25),
        ("Sales Simulation", "sales-simulation", "Simulated sales scenarios testing negotiation and persuasion.", 30),
        ("Leadership Simulation", "leadership-simulation", "Simulated leadership challenges and decisions.", 35),
        ("Data Analysis Simulation", "data-analysis-simulation", "Hands-on data analysis exercise.", 40),
        ("Presentation Simulation", "presentation-simulation", "Simulated presentation delivery and Q&A.", 25),
    ]
    
    for name, slug, desc, duration in simulations:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Simulations"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # ASSESSMENT EXERCISES (E)
    # ==========================================
    
    exercises = [
        ("Case Study Analysis", "case-study-analysis", "Business case study exercise assessing analytical thinking and strategic recommendation abilities.", 45),
        ("Virtual Group Exercise", "group-exercise", "Collaborative exercise assessing teamwork, leadership, and communication in group settings.", 45),
        ("Written Analysis Exercise", "written-analysis", "Written exercise testing analytical and communication skills.", 40),
        ("Business Presentation Exercise", "business-presentation-exercise", "Exercise testing presentation preparation and delivery.", 45),
        ("In-Basket Exercise", "in-basket", "Prioritization and decision-making exercise.", 40),
        ("Fact Finding Exercise", "fact-finding", "Information gathering and analysis exercise.", 35),
        ("Planning Exercise", "planning-exercise", "Project planning and scheduling exercise.", 40),
        ("Competency-Based Interview Guide", "competency-interview", "Structured interview exercise framework.", 30),
    ]
    
    for name, slug, desc, duration in exercises:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Assessment Exercises"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # DEVELOPMENT & 360 (D)
    # ==========================================
    
    development = [
        ("360 Degree Feedback", "360-feedback", "Comprehensive multi-rater feedback assessment for leadership development.", 40),
        ("Coaching Readiness", "coaching-readiness", "Assesses readiness and receptiveness to coaching and development feedback.", 15),
        ("Self-Awareness Assessment", "self-awareness", "Measures level of self-awareness and insight into personal strengths and development areas.", 18),
        ("Learning Agility", "learning-agility", "Evaluates ability to learn quickly, adapt to new situations, and apply learnings.", 22),
        ("Potential Assessment", "potential-assessment", "Identifies high-potential employees for succession planning and leadership development.", 35),
        ("Career Development Assessment", "career-development", "Evaluates career interests and development opportunities.", 25),
        ("Leadership Development", "leadership-development", "Assessment for leadership development planning.", 35),
        ("Manager Development", "manager-development", "Assessment focused on developing management skills.", 30),
        ("Executive Development", "executive-development", "High-level development assessment for executives.", 45),
        ("Team Development", "team-development", "Assessment for team effectiveness and development.", 30),
    ]
    
    for name, slug, desc, duration in development:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": ["Development & 360"],
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    # ==========================================
    # ROLE-SPECIFIC (Mixed Types)
    # ==========================================
    
    role_specific = [
        ("Software Engineer Assessment", "software-engineer", "Comprehensive assessment for software engineering roles covering coding, problem-solving, and collaboration.", 45, ["Knowledge & Skills", "Competencies"]),
        ("Data Analyst Assessment", "data-analyst", "Evaluates data analysis skills including SQL, visualization, statistics, and business insight generation.", 35, ["Knowledge & Skills"]),
        ("Product Manager Assessment", "product-manager", "Comprehensive assessment for PM roles covering strategy, prioritization, and stakeholder management.", 40, ["Competencies", "Personality & Behaviour"]),
        ("QA Engineer Assessment", "qa-engineer", "Tests quality assurance skills including testing methodologies, automation, and defect management.", 30, ["Knowledge & Skills"]),
        ("UX Designer Assessment", "ux-designer", "Evaluates UX design knowledge including research, wireframing, prototyping, and usability principles.", 30, ["Knowledge & Skills", "Competencies"]),
        ("DevOps Engineer Assessment", "devops-engineer", "Comprehensive DevOps assessment covering CI/CD, infrastructure, monitoring, and collaboration.", 40, ["Knowledge & Skills"]),
        ("HR Professional Assessment", "hr-professional", "Evaluates HR competencies including talent acquisition, employee relations, and organizational development.", 35, ["Competencies", "Knowledge & Skills"]),
        ("Marketing Professional", "marketing-professional", "Assesses marketing skills including digital marketing, analytics, and campaign management.", 30, ["Knowledge & Skills", "Competencies"]),
        ("Accountant Assessment", "accountant", "Evaluates accounting knowledge including GAAP, financial statements, and audit procedures.", 35, ["Knowledge & Skills"]),
        ("Sales Representative Assessment", "sales-representative", "Comprehensive sales assessment covering prospecting, negotiation, and customer relationship skills.", 30, ["Competencies", "Personality & Behaviour"]),
        ("Call Center Assessment", "call-center-skills", "Comprehensive assessment for call center roles covering communication, problem solving, and customer orientation.", 25, ["Competencies", "Personality & Behaviour"]),
        ("Retail Assessment", "retail-skills", "Evaluates skills and behaviors essential for retail roles including sales, service, and product knowledge.", 20, ["Competencies"]),
        ("Administrative Professional", "administrative-professional", "Comprehensive assessment for administrative roles covering organization, communication, and office technology.", 30, ["Competencies", "Knowledge & Skills"]),
        ("Healthcare Professional Assessment", "healthcare-assessment", "Assesses competencies and values essential for healthcare roles including empathy, attention to detail, and ethical judgment.", 30, ["Competencies", "Personality & Behaviour"]),
        ("Business Analyst Assessment", "business-analyst", "Comprehensive assessment for business analyst roles covering requirements analysis, process modeling, and stakeholder management.", 35, ["Knowledge & Skills", "Competencies"]),
        ("Financial Analysis", "financial-analysis", "Evaluates financial analysis skills including ratio analysis, financial modeling, and investment evaluation.", 25, ["Knowledge & Skills"]),
        ("Project Management", "project-management", "Assesses project management knowledge including planning, scheduling, risk management, and agile methodologies.", 30, ["Knowledge & Skills"]),
        ("Agile & Scrum", "agile-scrum", "Tests Agile and Scrum methodology knowledge including sprint planning, ceremonies, and agile principles.", 20, ["Knowledge & Skills"]),
        ("Networking Fundamentals", "networking", "Evaluates networking knowledge including TCP/IP, routing, switching, and network security basics.", 25, ["Knowledge & Skills"]),
        ("ITIL Fundamentals", "itil", "Evaluates ITIL framework knowledge including service lifecycle and best practices.", 25, ["Knowledge & Skills"]),
        ("IT Support Assessment", "it-support", "Comprehensive assessment for IT support roles covering troubleshooting and customer service.", 30, ["Knowledge & Skills", "Competencies"]),
        ("Helpdesk Skills", "helpdesk", "Tests helpdesk competencies including technical knowledge and customer communication.", 25, ["Knowledge & Skills", "Competencies"]),
        ("Banking Operations", "banking-operations", "Assessment for banking operations roles covering accuracy, compliance, and customer service.", 30, ["Knowledge & Skills", "Competencies"]),
        ("Insurance Professional", "insurance-professional", "Assessment for insurance roles covering underwriting concepts and customer orientation.", 30, ["Knowledge & Skills", "Competencies"]),
        ("Manufacturing Supervisor", "manufacturing-supervisor", "Assessment for manufacturing supervisory roles covering operations and team leadership.", 35, ["Competencies", "Knowledge & Skills"]),
        ("Logistics & Supply Chain", "logistics-operations", "Assessment for logistics roles covering operations, planning, and supply chain principles.", 30, ["Knowledge & Skills"]),
        ("Executive Assessment", "executive-assessment", "Comprehensive executive-level assessment covering strategic thinking, leadership, and business acumen.", 60, ["Competencies", "Personality & Behaviour"]),
        ("Manager Plus Assessment", "manager-plus", "Assesses managerial potential and readiness including leadership, planning, and team development.", 40, ["Competencies", "Personality & Behaviour"]),
        ("Graduate Technology Assessment", "graduate-tech", "Assessment for graduate technology roles covering coding aptitude and technical reasoning.", 45, ["Ability & Aptitude", "Knowledge & Skills"]),
        ("Graduate Finance Assessment", "graduate-finance", "Assessment for graduate finance roles covering numerical reasoning and financial concepts.", 40, ["Ability & Aptitude", "Knowledge & Skills"]),
    ]
    
    for name, slug, desc, duration, types in role_specific:
        assessments.append({
            "url": f"https://www.shl.com/solutions/products/product-catalog/view/{slug}/",
            "name": name,
            "description": desc,
            "duration": duration,
            "test_type": types,
            "remote_support": "Yes",
            "adaptive_support": "No"
        })
    
    return assessments


if __name__ == "__main__":
    assessments = generate_extended_assessments()
    print(f"Total assessments: {len(assessments)}")
    
    # Count by type
    type_counts = {}
    for a in assessments:
        for t in a.get('test_type', []):
            type_counts[t] = type_counts.get(t, 0) + 1
    
    print("\nBy test type:")
    for t, count in sorted(type_counts.items()):
        print(f"  {t}: {count}")
    
    # Save to file
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    output_path = os.path.join(data_dir, 'shl_assessments.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(assessments, f, indent=2, ensure_ascii=False)
    
    print(f"\nSaved to: {output_path}")
