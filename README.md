# RAG-components

## Overview

RAG-components is a modular set of components designed to facilitate the integration and utilization of Retrieval-Augmented Generation (RAG) techniques in machine learning workflows. This repository contains reusable components to enable fast, scalable, and efficient RAG-based applications, including but not limited to document retrieval, embedding management, and text generation.

## Features

- **Document Retrieval**: Efficiently retrieve relevant documents from various data sources (e.g., text files, databases, APIs).
- **Embeddings**: Supports multiple embedding models to represent documents and queries in vector space.
- **Text Generation**: Leverage advanced language models for generating responses based on retrieved information.
- **Database Integration**: Integrates with relational and non-relational databases for storing and retrieving documents, embeddings, and other data.
- **Integration with LLMs**: Seamlessly integrate with large language models (LLMs) for context-rich answers and generation tasks.

## Architecture

The repository is structured as follows:
- `components/`: Contains individual RAG components (retrievers, generators, etc.).
- `models/`: Pre-trained models or interfaces for custom model loading.
- `database/`: Contains scripts for database setup, interaction, and management (e.g., PostgreSQL).
- `utils/`: Utility functions to assist with tasks like embedding, data preprocessing, etc.
- `config.py`: Configuration file for setting up model paths, database connections, etc.
- `tests/`: Unit and integration tests for all components.

## Database Integration

The `RAG-components` repository includes functionality to interact with various databases, including relational and non-relational databases. The database layer allows you to store, retrieve, and manage documents, embeddings, and other data for efficient RAG workflows.

### Supported Databases

- **PostgreSQL**: For relational storage of documents, queries, and embeddings.
technologies.

### Configuration

Database connection configurations are set up in the `config.py` file. Example configuration for PostgreSQL:

```python
DATABASE_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'user': 'your_user',
    'password': 'your_password',
    'dbname': 'rag_db'
}
