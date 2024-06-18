def test_should_main_return_welcome_message(app, client, logged_in):
    with app.app_context():
        client.post(
            "/login", data={"username": "test_user", "password": "test_password"}
        )
        expected_status_code = 200
        resp = client.get("/main")
        actual_status_code = resp.status_code
        actual_data = resp.data
        message = (
            "Hello! Choose a funny topic and I'll tell you a joke "
            "about it. You can have it in text or audio format!"
        )
        expected_message = f'"{message}"\n'
        assert actual_data == bytes(expected_message, "utf-8")
        assert actual_status_code == expected_status_code
