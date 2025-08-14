# API Specification

## Overview

The AI Graph Generation and Insight Tool provides a RESTful API for programmatic 
access to data visualization and insight generation capabilities. All endpoints 
return JSON responses and follow standard HTTP conventions.

---

## Base Configuration

### URLs

| Environment           | Base URL                             |
|-----------------------|--------------------------------------|
| **Local Development** | `http://localhost:5000/api/v1`       |
| **Production**        | `https://your-app.render.com/api/v1` |

### Authentication

> **Note**: Currently, the API does not require authentication. Future versions 
> may implement API key-based authentication for rate limiting and usage tracking.

### Content Types

- **File uploads**: `Content-Type: multipart/form-data`

- **JSON payloads**: `Content-Type: application/json`

## API Endpoints

| Purpose                  | Method | Route              |
|--------------------------|--------|--------------------|
| **Health Check**         | `GET`  | `/health`          |
| **Status Check**         | `GET`  | `/status`          |
| **Upload File**          | `POST` | `/upload`          |
| **Preprocess**           | `POST` | `/preprocess`      |
| **Profile**              | `POST` | `/profile`         |
| **Feature Extraction**   | `POST` | `/features`        |
| **Graph Recommendation** | `POST` | `/recommendations` |
| **Graph Generation**     | `POST` | `/graph`           |
| **Generate Insights**    | `GET`  | `/insights`        |
| **Full Pipeline**        | `POST` | `/advi-pipeline`   |


### Common Error Codes

| Error Code            | Description                               |
|-----------------------|-------------------------------------------|
| `INVALID_FILE_TYPE`   | Unsupported file format                   |
| `FILE_TOO_LARGE`      | File exceeds size limit                   |
| `MALFORMED_DATA`      | File structure is invalid                 |
| `PROCESSING_FAILED`   | Internal processing error                 |
| `UPLOAD_NOT_FOUND`    | Invalid or expired upload ID              |
| `RATE_LIMIT_EXCEEDED` | Too many requests (future implementation) |
| `INTERNAL_ERROR`      | Unexpected server error                   |

---

## Rate Limiting

> **Future implementation** will include rate limiting with the following headers:

```http
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 87
X-RateLimit-Reset: 1692014400
```

---

## Data Retention Policy

- **Uploaded files**: Automatically deleted after 24 hours
- **Processing results**: Cached for 1 hour
- **PII data**: No personally identifiable information stored permanently



