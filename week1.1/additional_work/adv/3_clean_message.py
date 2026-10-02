"""Advanced Task 3: Clean Message Toolkit
- Collect a message that might contain extra spaces or mixed casing.
- Use at least three different string methods (e.g. strip, title, replace, upper) to tidy the message.
- Print the original and cleaned versions so the difference is obvious.
- Extension: show the message length before and after cleaning.
"""

raw_message = str(input("Type a message to tidy: "))

raw_message_length = len(raw_message)

clean_message = raw_message.lower()
clean_message = clean_message.strip()
clean_message = clean_message.title()

clean_message_length = len(clean_message)

print(f"""
Your message length has been shrunk from {raw_message_length} to {clean_message_length} characters.

Your clean message:

{clean_message}
""")

# TODO: apply a sequence of string methods to produce a cleaned_message
# Example methods: strip, title, replace, lower, upper
# TODO: display the original and cleaned messages
# Extension: display the character counts for each version
