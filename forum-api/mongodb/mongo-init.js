db.auth('root', 'rootpass')

db = db.getSiblingDB('forum-dev')

db.createUser({
    user: 'monguser',
    pwd: 'mongpass',
    roles: [
        {
            role: 'readWrite',
            db: 'forum-dev',
        }
    ]
});