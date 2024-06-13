This repository contains a robust and scalable FastAPI application designed to manage a Configuration Management system for onboarding organizations from each country. The API provides functionalities for CRUD (Create, Read, Update, Delete) operations for managing configurations.

**Overview**
As an international logistics company dealing with international transactions, we require a robust system to handle onboarding requirements for each country. Different countries have different onboarding requirements. For example:

Onboarding a company in India requires Business Name, PAN, and GSTIN numbers.
Onboarding a company in the USA may require Business Name, a different type of registration number, and other additional details.
This system is designed to manage these varied requirements efficiently.

**Features**
Create Configuration: API to create a configuration of a country's onboarding requirements.
Get Configuration: API to provide the configuration requirements of a country.
Update Configuration: API to update the configuration requirements of a country.
Delete Configuration: API to delete the configuration requirements of a country.
Technology Stack
Framework: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
Data Validation: Pydantic
