# AI Title Generation Feature

Status:
Paused

Reason:
The feature added too much complexity compared to its value.

Current problems:
- AI generation failures
- File rename edge cases
- Empty chat handling
- Duplicate titles
- Recovery flow

Future design:

AI titles should NOT create chats.

Correct flow:

Create chat
    |
    v
Save safely
    |
    v
Optional AI title suggestion
    |
    v
Rename existing chat


Possible future UI:

[ Suggest Title ]

If AI succeeds:
Rename automatically

If AI fails:
Keep current title


Requirements:
- Never break chat files
- Never create ghost chats
- Never block the user
- Always have manual rename fallback