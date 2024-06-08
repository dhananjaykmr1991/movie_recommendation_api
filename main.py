from flask import Flask, request, jsonify
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the model and data
df_url = 'H:/Machine Learning Projects/django-aicenter/aicenter/artifacts/movie_recommendation_system/df_final_with_en.pkl'  # Local path for pickle file
similarity_path = 'H:/Machine Learning Projects/django-aicenter/aicenter/artifacts/movie_recommendation_system/similarity.npy'  # Local path for numpy file

# Ensure files exist
if not os.path.exists(df_url):
    raise FileNotFoundError(f"Pickle file not found: {df_url}")
if not os.path.exists(similarity_path):
    raise FileNotFoundError(f"Numpy file not found: {similarity_path}")

with open(df_url, 'rb') as file:
    df = pickle.load(file)

similarity = np.load(similarity_path)

@app.route('/recommend', methods=['GET'])
def recommend():
    movie = request.args.get('movie')
    if not movie:
        return jsonify({'error': 'No movie specified'}), 400

    try:
        movie_index = df[df['title'] == movie].index[0]
        distances = similarity[movie_index]
        movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:8]
        rec_movie = [df.iloc[i[0]].title for i in movie_list]
        return jsonify({'recommendations': rec_movie})
    except IndexError:
        return jsonify({'error': 'Movie not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)


