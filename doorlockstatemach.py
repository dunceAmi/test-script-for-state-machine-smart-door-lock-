class DoorLockFSM:
    def __init__(self):
        self.state = "LOCKED"   # initial state
        self.password = "1234"  # default password

    def on_event(self, event, input_password=None, new_password=None):
        """Handles events and transitions between states."""

        if self.state == "LOCKED":
            if event == "correct_password" and input_password == self.password:
                self.state = "UNLOCKED"
            elif event == "wrong_password" and input_password != self.password:
                self.state = "LOCKED"  # stays locked
            elif event == "reset_key":
                self.state = "RESETTING"

        elif self.state == "UNLOCKED":
            if event == "reset_key":
                self.state = "RESETTING"
            else:
                # any other action relocks
                self.state = "LOCKED"

        elif self.state == "RESETTING":
            if event == "new_password_set" and new_password:
                self.password = new_password
                self.state = "LOCKED"

        return self.state


# --------------------------
# Test Script
# --------------------------
if __name__ == "__main__":
    fsm = DoorLockFSM()

    # 1. Try wrong password
    print("Event: Wrong Password ->", fsm.on_event("wrong_password", input_password="0000"))

    # 2. Try correct password
    print("Event: Correct Password ->", fsm.on_event("correct_password", input_password="1234"))

    # 3. Reset password using security key
    print("Event: Reset Key ->", fsm.on_event("reset_key"))

    # 4. Set new password
    print("Event: New Password Set ->", fsm.on_event("new_password_set", new_password="5678"))

    # 5. Try old password (should fail)
    print("Event: Old Password ->", fsm.on_event("wrong_password", input_password="1234"))

    # 6. Try new password (should unlock)
    print("Event: Correct New Password ->", fsm.on_event("correct_password", input_password="5678"))
