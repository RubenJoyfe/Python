from flask import Flask, jsonify, request
import json

application = Flask(__name__)

@application.route('/')
def root():
    return 'API Levantada'

@application.route('/posts', methods=['GET'])
def get_posts():
    try:
        posts = []
        with open('data/posts.json', 'r') as json_file:
            posts = json.load(json_file)
        return jsonify(posts), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/posts/<int:id>', methods=['GET'])
def get_post(id):
    try:
        posts = []
        with open('data/posts.json', 'r') as json_file:
            posts = json.load(json_file)
        for post in posts:
            if post['id'] == id:
                return jsonify(post)
        return jsonify({}), 404
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/posts/<int:id>', methods=['PUT'])
def update_post(id):
    try:
        posts = []
        post = None
        with open('data/posts.json', 'r') as json_file:
            posts = json.load(json_file)
        for p in posts:
            if p['id'] == id:
                post = p
        if post is None:
            return jsonify({'ERROR': 'El Post no existe'}), 404
        
        update_post = request.get_json()

        data = ['userId', 'title', 'body']
        for d in data:
            if d in update_post:
                post[d] = update_post[d]

        with open('data/posts.json', 'w') as f:
            f.write(json.dumps(posts, indent=4))
        return jsonify(post), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    try:
        posts = []
        post = None
        with open('data/posts.json', 'r') as json_file:
            posts = json.load(json_file)
        for p in posts:
            if p['id'] == id:
                post = p
        if post is None:
            return jsonify({'ERROR': 'El Post no existe'}), 404
        
        posts.remove(post)

        with open('data/posts.json', 'w') as f:
            f.write(json.dumps(posts, indent=4))
        return ('', 200)
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/posts', methods=['POST'])
def create_post():
    try:
        posts = []
        with open('data/posts.json', 'r') as json_file:
            posts = json.load(json_file)
        last_id = 0
        for post in posts:
            if post['id'] > last_id:
                last_id = post['id']
        
        new_post_data = request.get_json()
        new_post = {
            'id': last_id + 1,
            'body': new_post_data['body'],
            'title': new_post_data['title'],
            'userId': new_post_data['userId']
        }
        posts.append(new_post)

        with open('data/posts.json', 'w') as f:
            f.write(json.dumps(posts, indent=4))

        return jsonify(new_post), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/comments', methods=['GET'])
def get_comments():
    try:
        comments = []
        with open('data/comments.json', 'r') as json_file:
            comments = json.load(json_file)
        return jsonify(comments), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    try:
        comments = []
        with open('data/comments.json', 'r') as json_file:
            comments = json.load(json_file)
        for comment in comments:
            if comment['id'] == id:
                return jsonify(comment)
        return jsonify({}), 404
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    try:
        comments = []
        comment = None
        with open('data/comments.json', 'r') as json_file:
            comments = json.load(json_file)
        for c in comments:
            if c['id'] == id:
                comment = c
        if comment is None:
            return jsonify({'ERROR': 'El Comentario no existe'}), 404
        
        update_comment = request.get_json()

        data = ['postId', 'name', 'email', 'body']
        for d in data:
            if d in update_comment:
                comment[d] = update_comment[d]

        with open('data/comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4))
        return jsonify(comment), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    try:
        comments = []
        comment = None
        with open('data/comments.json', 'r') as json_file:
            comments = json.load(json_file)
        for c in comments:
            if c['id'] == id:
                comment = c
        if comment is None:
            return jsonify({'ERROR': 'El Comentario no existe'}), 404
        
        comments.remove(comment)

        with open('data/comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4))
        return ('', 200)
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400

@application.route('/comments', methods=['POST'])
def create_comment():
    try:
        comments = []
        with open('data/comments.json', 'r') as json_file:
            comments = json.load(json_file)
        last_id = 0
        for c in comments:
            if c['id'] > last_id:
                last_id = c['id']
        
        new_comment_data = request.get_json()
        new_comment = {
            'id': last_id + 1,
            'body': new_comment_data['body'],
            'postId': new_comment_data['postId'],
            'name': new_comment_data['name'],
            'email': new_comment_data['email']
        }
        comments.append(new_comment)

        with open('data/comments.json', 'w') as f:
            f.write(json.dumps(comments, indent=4))

        return jsonify(new_comment), 200
    except Exception:
        return jsonify({'ERROR': 'Error desconocido'}), 400


if __name__ == '__main__':
    application.run(debug=True)