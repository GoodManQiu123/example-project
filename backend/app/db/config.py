"""
Overview:
This configuration file sets up the connection details for MongoDB, specifying the URIs for both the main and test
databases. It supports switching between a testing mode and a production mode based on an environment variable,
allowing for flexibility in development, testing, and deployment phases.

Details:
- MONGO_URI: The connection string for the main MongoDB database, which includes authentication details, the cluster
  address, and additional connection options tailored for this specific database instance.
- MONGO_TEST_URI: Similar to MONGO_URI but intended for a separate testing database, ensuring that tests do not
  interfere with production data.
- TEST_MODE: A boolean flag determined by the "TEST_MODE" environment variable. When set to True, the application
  is considered to be in testing mode, and operations will be directed towards the test database. Otherwise, the
  application will interact with the main database.

Usage:
- In development or testing environments, ensure that the "TEST_MODE" environment variable is set to "True" to
  prevent accidental modifications to production data.
- In production, either unset the "TEST_MODE" environment variable or set it to "False" to switch to using the
  main database.
- The configured URIs include necessary authentication details and are ready to be used with MongoDB clients or
  ORM libraries like MongoEngine for database operations.

Security Note:
- The URIs contain sensitive information, including credentials for database access. In a real-world application,
  it is recommended to use more secure methods for managing such credentials, like environment variables, secret
  management services, or configuration files that are not included in version control.
"""

import os

MONGO_URI = "mongodb+srv://s2606445:Carlson@cluster0.lckhdjd.mongodb.net/psd?retryWrites=true&w=majority&appName" \
            "=Cluster0"
MONGO_TEST_URI = "mongodb+srv://s2606445:Carlson@cluster0.lckhdjd.mongodb.net/test?retryWrites=true&w=majority" \
                 "&appName=Cluster0"

TEST_MODE = os.environ.get("TEST_MODE", "True") == "True"

print("Test Mode: ", TEST_MODE)
