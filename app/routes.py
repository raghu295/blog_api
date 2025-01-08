from flask import Blueprint, request, jsonify
from .models import User, Post
from . import db, bcrypt
from flask_login import login_user, current_user, logout_user, login_required

main = Blueprint('main', __name__)

@main.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], email=data['email'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully'}), 201

@main.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'User Credentials does not match!'}), 401

@main.route('/logout', methods=['POST'])
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'}), 200

@main.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.paginate(page=page, per_page=2, error_out=False)
    if not posts.items:
        return jsonify({'message': 'No posts found'}), 404
    return jsonify([post.to_dict() for post in posts.items]), 200

@main.route('/post/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = Post.query.get(post_id)
    if post is None:
        return jsonify({'message': 'Post has been already deleted'}), 404
    return jsonify(post.to_dict()), 200

@main.route('/post', methods=['POST'])
@login_required
def create_post():
    data = request.get_json()
    post = Post(title=data['title'], content=data['content'], author=current_user)
    db.session.add(post)
    db.session.commit()
    return jsonify({'message': 'Post created successfully'}), 201

@main.route('/post/<int:post_id>', methods=['PUT'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        return jsonify({'message': 'Permission denied'}), 403
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'}), 200

@main.route('/post/<int:post_id>', methods=['DELETE'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        return jsonify({'message': 'Permission denied'}), 403
    db.session.delete(post)
    db.session.commit()
    return jsonify({'message': 'Post deleted successfully'}), 200