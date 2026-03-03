# Author:Yi Sun(Tim) 2024-1-22


import pytest
import os

def perform_ui_login(browser,url,user,pwd,path,role):
    print(f"\n[Auth] Start UI login for {role}..")
    context = browser.new_context()
    page = context.new_page()
    try:
        from pages.login_admin import Admin_Portal
        login_p = Admin_Portal(page)
        page.goto(url)
        login_p.login(user,pwd)
        page.wait_for_load_state("networkidle")
        context.storage_state(path=path)
        print(f"[Auth] {role} login successful, state saved.")
    finally:
        context.close()

@pytest.fixture(scope="session")
def login_manager(browser,credentials,auth_files):
    def _ensuer_auth(role):
        path = auth_files.get(role)
        user = credentials.get(f"{role}_username")
        pwd = credentials.get(f"{role}_password")

        should_relogin = False
        if not os.path.exists(path):
            should_relogin = True
        elif time.time() - os.path.getmtime(path) > 86400: # 24 hours
            should_relogin = True

        if should_relogin:
            perform_ui_login(browser,credentials["egd_url"],user,pwd,path,role)
        return path
    return _ensuer_auth

@pytest.fixture(scope="class")
def page_in_class(browser, login_manager,request):
    """
        @pytest.mark.role("dealer")
    """
    # Default role is Admin
    marker = request.node.get_closest_marker("role")
    role = marker.args[0] if marker else "admin"
    storage_path = login_manager(role)

    context = browser.new_context(
        storage_state = storage_path,
        viewport={"width": 2560, "height": 1440}
    )
    page = context.new_page()
    yield page
    context.close()

AUTH_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../auth.json"))

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, credentials):
    if os.path.exists(AUTH_PATH):
        return {
            **browser_context_args,
            "storage_state": AUTH_PATH,
            "viewport": {"width": 2560, "height": 1440}
        }
    return {
        **browser_context_args,
        "viewport": {"width": 2560, "height": 1440}
    }

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        page = None

        for fixture_value in item.funcargs.values():
            if hasattr(fixture_value, "page"):
                page = fixture_value.page
                break
        if page:
            root_dir = item.config.rootdir
            screenshot_dir = os.path.join(root_dir, "report", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            safe_name = "".join([c for c in item.name if c.isalnum() or c in (' ', '.', '_')]).rstrip()
            page.screenshot(path=os.path.join(screenshot_dir, f"{safe_name}.png"), full_page=True)




