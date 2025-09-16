# RAG + ElasticSearch Setup Guide

## 1. Create a `.gitignore` File

Add the following line to your `.gitignore` to prevent sensitive data from being tracked:

```
.env
```

---

## 2. Create a `.env` File

Add all your environment variables (such as API keys, document paths, etc.) to a `.env` file. Example:

```
OPENAI_API_KEY=your_openai_api_key
es_api_key=your_elasticsearch_api_key
es_cloud_id=your_elasticsearch_cloud_id
documentpath=/path/to/your/document.txt
```

---

## 3. Set Up a Virtual Environment

Create a virtual environment:

```bash
python -m venv <your_env_name>
```

Activate the virtual environment:

```bash
source <your_env_name>/bin/activate
```

---

## 4. Install Required Packages

Install all dependencies using pip:

```bash
pip install langchain langchain-openai langchain-elasticsearch langchain-community python-dotenv
```

---

## 5. Set Up ElasticSearch

- Create an ElasticSearch account if you do not have one.
- Create a new deployment (choose any cloud provider).
- Create an API key for the deployment.
- Find your **Cloud ID** by clicking on the deployment dropdown in the header and selecting "Manage Deployment".

---

## 6. Access ElasticSearch DevTools

- Click on **Kibana** in your ElasticSearch dashboard, then **DevTools**.
- To view indices, run:
  ```
  GET /_cat/indices
  ```
- After running your `main.py` successfully, your new index will appear here.
- You can also find your index in **Index Management**.

---

## 7. How Retrieval Works

- `vectordb` is an instance of the Elastic vector database.
- `.as_retriever(...)` turns the vector database into a retriever object for fetching relevant documents.
- `search_type="similarity"`: Fetches documents most similar to the query vector.
- `search_kwargs={"k": 3}`: Returns the top 3 most similar documents.

### Function Implementation

- **Purpose:** Returns a `VectorStoreRetriever` object, wrapping the vector store and providing search capabilities.
- **Arguments:**
  - `search_type`: Retrieval algorithm (`"similarity"`, `"mmr"`, or `"similarity_score_threshold"`).
  - `search_kwargs`: Fine-tunes the search (e.g., number of results, filtering, thresholds).
- **How it works:**
  - Optionally sets tags for tracking/logging.
  - Returns a `VectorStoreRetriever` with the specified settings.

#### Gotchas

- If you don’t specify `k`, the default is usually 4.
- `search_type` must be one of the supported types.
- `search_kwargs` can include options like `filter` or `score_threshold` for advanced queries.

---
