# Payload with Attachement
```json
{
    "content_html": "<h1>test</h1>",
    "subject": "this is subject",
    "to_recipients": "email@example.com",
    "attach_files": [
        {
            "file_bytes": "SGVsbG8gV29ybGQh",
            "name": "file1.txt",
            "isInline": true,
            "content_id": "cid:sdfsfsdf"
        },
        {
            "file_bytes": "SGVsbG8gV29ybGQh",
            "name": "file2.txt",
            "isInline": false,
            "content_id": "cid:asdfsfd"
        }
    ]
}
```

# Payload no Attachement
```json
{
    "content_html": "<h1>test</h1>",
    "subject": "Subject no Attachement",
    "to_recipients": "email@example.com",
    "attach_files": []
}
```