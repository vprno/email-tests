from playwright.sync_api import expect

class InboxPage:
    
    def __init__(self, page):
        self.page = page
        self.write_email_link = page.get_by_role("link", name="Napísať správu")
        self.recipient_input = page.locator("#recipient_rightclick_to")
        self.subject_input = page.get_by_role("textbox", name="Predmet:")
        self.body_input = page.locator("#mail_composer_body")
        self.add_attachment_link = page.get_by_role("link", name="Pridať prílohu")
        self.attachment_list = page.locator(".composer-attachment-content")
        self.send_email_button = page.locator("#qa_email_send_bottom")
        self.logout_button = page.get_by_role("link", name="Odhlásiť")

    def click_write_email(self):
        self.write_email_link.click()

    def enter_recipient(self, recipient):
        self.recipient_input.fill(recipient)

    def fill_subject(self, subject):
        self.subject_input.fill(subject)

    def fill_body(self, body):
        self.body_input.fill(body)

    def attach_file(self, file_path):
        with self.page.expect_file_chooser() as fc_info:
            self.add_attachment_link.click()
        file_chooser = fc_info.value
        file_chooser.set_files(file_path)

    def send_email(self):
        self.send_email_button.click()
    
    def is_file_attached(self):
        expect(self.attachment_list).to_be_visible(timeout=5000)
    
    def check_email_send(self):
        # not ideal, because of time constraint, ideally you would check API POST requests and check the status, but this requires setup in Playwright and Python combo
        expect(self.recipient_input).not_to_be_visible(timeout=5000)
        expect(self.subject_input).not_to_be_visible(timeout=5000)
        expect(self.body_input).not_to_be_visible(timeout=5000)
                
    def logout(self):
        self.logout_button.click()