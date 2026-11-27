import json
from http.server import BaseHTTPRequestHandler, HTTPServer


def add_feedback(store, name, rating):
    if not name.strip():
        raise ValueError("name is required")
    if rating not in range(1, 6):
        raise ValueError("rating must be 1 to 5")
    store.append({"name": name.strip(), "rating": rating})
    return len(store)


def average_rating(store):
    if not store:
        return 0
    return round(sum(f["rating"] for f in store) / len(store), 2)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = json.dumps({"app": "Student Feedback", "status": "ok"})
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(body.encode())


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8000), Handler).serve_forever()

