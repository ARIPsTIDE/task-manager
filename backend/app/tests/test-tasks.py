from app.main import API_KEY


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_debug(client):
    r = client.get("/debug")
    assert r.status_code == 200
    assert "env" in r.json()


def test_admin_stats_unauthorized(client):
    r = client.get("/admin/stats")
    assert r.status_code == 401


def test_admin_stats_authorized(client):
    r = client.get(
        "/admin/stats",
        headers={"x-api-key": API_KEY},
    )
    assert r.status_code == 200


def test_create_task(client):
    payload = {
        "title": "  My task  ",
        "description": "Test description"
    }
    r = client.post("/tasks", json=payload)
    assert r.status_code == 201

    data = r.json()
    assert data["title"] == "My task"  # strip couvert 🎯
    assert data["status"] == "TODO"


def test_list_tasks(client):
    r = client.get("/tasks")
    assert r.status_code == 200
    assert isinstance(r.json(), list)


def test_get_task_not_found(client):
    r = client.get("/tasks/999")
    assert r.status_code == 404


def test_update_task(client):
    # create
    r = client.post("/tasks", json={"title": "Old", "description": "desc"})
    task_id = r.json()["id"]

    # update
    r = client.put(
        f"/tasks/{task_id}",
        json={"title": " New title ", "status": "DONE"},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["title"] == "New title"
    assert data["status"] == "DONE"
    assert data["updated_at"] is not None


def test_delete_task(client):
    r = client.post("/tasks", json={"title": "To delete"})
    task_id = r.json()["id"]

    r = client.delete(f"/tasks/{task_id}")
    assert r.status_code == 204

    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 404
