import time
from playwright.sync_api import sync_playwright
import os

def take_screenshots():
    os.makedirs("docs/screenshots", exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(viewport={"width": 1440, "height": 900})
        page = context.new_page()
        
        base_url = "http://localhost:8000"
        
        page.goto(f"{base_url}/index.php")
        time.sleep(2)
        page.screenshot(path="docs/screenshots/landing.png", full_page=False)
        print("Captured landing")
        
        page.goto(f"{base_url}/auth/login.php")
        time.sleep(1)
        page.screenshot(path="docs/screenshots/login.png")
        print("Captured login")
        
        # Login as student
        page.fill("input[name='email']", "karthik65@nova.edu")
        page.fill("input[name='password']", "karthik123")
        page.click("button[type='submit']")
        time.sleep(3)
        page.screenshot(path="docs/screenshots/dashboard.png")
        print("Captured dashboard")
        
        page.goto(f"{base_url}/student/attendance.php")
        time.sleep(2)
        page.screenshot(path="docs/screenshots/qr-attendance.png")
        print("Captured qr-attendance")
        
        page.goto(f"{base_url}/student/performance.php")
        time.sleep(2)
        page.screenshot(path="docs/screenshots/performance.png")
        print("Captured performance")
        
        page.goto(f"{base_url}/auth/logout.php")
        time.sleep(1)
        
        # Login as admin
        page.goto(f"{base_url}/auth/login.php")
        time.sleep(1)
        # Select admin role
        page.evaluate("document.getElementById('roleInput').value = 'admin';")
        page.fill("input[name='email']", "admin@nova.edu")
        page.fill("input[name='password']", "password123")
        page.click("button[type='submit']")
        time.sleep(3)
        
        page.goto(f"{base_url}/admin/dashboard.php")
        time.sleep(2)
        page.screenshot(path="docs/screenshots/admin.png")
        print("Captured admin")
            
        browser.close()

if __name__ == "__main__":
    take_screenshots()
