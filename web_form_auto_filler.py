import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Launch Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Open the form
driver.get("https://forms.office.com/pages/responsepage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAANAAooclc1UREtaTzNSU09PUEFVRkg3VTNCUkdDQ05KUC4u&route=shorturl")

# Give form time to load
time.sleep(5)

try:
    # Find all text boxes
    text_inputs = driver.find_elements(By.CSS_SELECTOR, "input[data-automation-id='textInput']")
    print(f"Found {len(text_inputs)} text boxes.")

    # Answers for each question
    answers = [
        "Ronak Jat",                   # Q1
        "19",                          # Q2
        "Amity University Rajasthan",  # Q3
        "Computer Science",            # Q4
        "AI",                          # Q5
        "Python",                      # Q6
        "Unemployed"                   # Q7
    ]

    # Fill all text fields
    for i, ans in enumerate(answers):
        if i < len(text_inputs):
            text_inputs[i].send_keys(ans)
            time.sleep(2)

    # Select gender = Woman
    gender_option = driver.find_element(By.XPATH, "//div[contains(@role,'radio')]//span[normalize-space()='Woman']")
    gender_option.click()
    print("Selected gender: Woman")
    time.sleep(2)

    # Click the Submit button
    submit_btn = driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='submitButton']")
    submit_btn.click()
    print("✅ Form filled and submitted successfully!")

    time.sleep(3)

except Exception as e:
    print("❌ Error:", e)

finally:
    driver.quit()
