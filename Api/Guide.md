API Concepts — Quick Reference
---

## What is an API?

**API** stands for **Application Programming Interface** — it's a defined way for two programs to talk to each other over the internet.

Think of it like a waiter at a restaurant:
- You (your code) tell the waiter (API) what you want
- The waiter goes to the kitchen (server/database)
- The kitchen prepares it and the waiter brings it back (response)

You never touch the kitchen directly — the API handles all the back-and-forth.

**In practice:** Instead of building your own weather station, you call a Weather API and it gives you the data instantly. APIs let you use other services without knowing how they work internally.

```
Your Code  →  Request (what you want)  →  API Server
Your Code  ←  Response (data/result)   ←  API Server
```

Every API interaction has two parts:
- **Request** — the URL + method + any data you send
- **Response** — status code + data the server sends back

---

## The 4 HTTP Methods

| Method | Purpose | When to use |
|--------|---------|-------------|
| `GET` | Read data | Fetch records from a server |
| `POST` | Create data | Send new data to a server |
| `PUT` | Replace data | Overwrite an entire record |
| `DELETE` | Remove data | Delete a record |

---

## Response Object — What You Get Back

When you call `requests.get(url)`, the response has 4 key parts:

| Attribute | What it gives you |
|-----------|------------------|
| `response.status_code` | Did it succeed? (200 = yes, 404 = not found) |
| `response.json()` | The actual data as a Python dict/list |
| `response.text` | Same data but as a raw string |
| `response.headers` | Metadata about the response (content type, server info, etc.) |

---

## POST: `json=` vs `data=`

Your notebook uses both — here's the difference:

| Parameter | Sends as | Use when |
|-----------|----------|----------|
| `json=data` | `application/json` | API expects JSON (most modern APIs) |
| `data=form_data` | `form-urlencoded` | API expects HTML form submission |

**Rule of thumb:** Use `json=` unless the API docs say otherwise.

---

## Query Parameters

Filters you attach to a GET request. Instead of building the URL manually:
```
/todos?userId=1&id=2
```
You pass them as a dict with `params=` and requests builds the URL for you. This keeps code clean and handles special characters automatically.

---

## Headers

Extra information sent along with every request — not the data itself, but metadata *about* the request.

**Common uses:**
- `User-Agent` — tells the server what kind of client is calling
- `Accept` — tells the server what format you want back (e.g., JSON)
- `Authorization` — proves who you are (see below)
- `content-type` — tells the server what format you're sending

---

## Authentication — 3 Types

**1. JWT Bearer Token** — most common in modern APIs
```
Authorization: Bearer <token>
```
You get the token after login. Pass it in headers on every request.

**2. API Key** — simpler, no login step
```
x-api-key: your_api_key_here
```
A static key the API provider gives you. Often passed in headers or as a query param.

**3. Basic Auth** — username + password
```python
auth=HTTPBasicAuth('username', 'password')
```
Older style. `requests` encodes it automatically.

---

## HTTP Status Codes (The Ones That Matter)

| Code | Meaning |
|------|---------|
| `200` | Success |
| `201` | Created (after POST) |
| `400` | Bad request — your data is wrong |
| `401` | Unauthorized — missing/bad auth |
| `403` | Forbidden — authenticated but no permission |
| `404` | Not found — wrong URL or ID |
| `429` | Too many requests — slow down |
| `500` | Server error — not your fault |

---

## JSON vs Text

APIs return data as a **string**. `.json()` parses that string into a Python dict so you can work with it like `data['title']`. Use `json.dumps(data, indent=4)` to pretty-print it in the terminal.

---

## PUT — Update / Replace a Record

**Concept:** PUT replaces an entire existing record with new data. You must send the full object — any field you leave out gets wiped.

- Targets a specific record via its ID in the URL: `/todos/1`
- If the record exists → replaces it. If not → some APIs create it.
- Use `PUT` when updating everything. Use `PATCH` when updating just one field.

**Syntax:**
```python
url = 'https://jsonplaceholder.typicode.com/todos/1'

updated_data = {
    "userId": 1,
    "id": 1,
    "title": "Updated title here",
    "completed": True
}

response = requests.put(url, json=updated_data)
print(response.status_code)          # 200 = updated successfully
print(response.json())               # returns the updated record
```

**PUT vs PATCH:**

| Method | Sends | Effect |
|--------|-------|--------|
| `PUT` | Full object | Replaces the entire record |
| `PATCH` | Only changed fields | Partially updates the record |

---

## DELETE — Remove a Record

**Concept:** DELETE removes a specific record from the server. You only need the record's ID in the URL — no request body required.

- After a successful delete, most APIs return `200` or `204` (No Content)
- The response body is usually empty — nothing to `.json()`
- Always verify with `status_code` since there's no data to confirm with

**Syntax:**
```python
url = 'https://jsonplaceholder.typicode.com/todos/1'

response = requests.delete(url)
print(response.status_code)    # 200 = deleted successfully

if response.status_code == 200:
    print("Record deleted successfully")
```

**With auth headers (real APIs):**
```python
headers = {"Authorization": "Bearer your_token_here"}

response = requests.delete(url, headers=headers)
print(response.status_code)
```

---

## Key Rules to Remember

- Always check `status_code` before using the response
- Use `json=` for POST, not `data=`, unless sending form data
- Use `params=` for query filters, never manually append to the URL
- Never hardcode API keys in your code — use environment variables
- `response.request.headers` shows you exactly what was sent (great for debugging)
